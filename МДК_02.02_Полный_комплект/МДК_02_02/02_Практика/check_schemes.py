"""Проверка схем draw.io, интерфейсов в исходниках и общего альбома."""
import ast
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parent
EXPECTED={
 1:[('addition','add')],2:[('geometry','rectangle_area')],
 3:[('temperature','celsius_to_fahrenheit')],
 4:[('input_data','parse_request'),('calculator','calculate'),('output_data','format_result')],
 5:[('maximum','find_maximum')],6:[('positive','count_positive')],
 7:[('price_source','get_prices'),('price_total','total_prices'),('price_output','format_total')],
 16:[('text_validation','is_nonempty')],
 22:[('discount','discounted_price'),('formatting','format_price')],
 24:[('text_length','string_length')],25:[('user_data','create_user'),('user_message','format_user')]}


def graph(path):
 root=ET.parse(path).getroot()
 assert root.tag=='mxfile'
 diagrams=root.findall('diagram')
 for diagram in diagrams:
  model=diagram.find('mxGraphModel'); assert model is not None
  width,height=float(model.get('pageWidth')),float(model.get('pageHeight'))
  cells=model.findall('./root/mxCell');ids=[c.get('id') for c in cells]
  assert len(ids)==len(set(ids)) and '0' in ids and '1' in ids
  for cell in cells:
   assert 'image=' not in cell.get('style','')
   if cell.get('parent'):assert cell.get('parent') in ids
   if cell.get('vertex')=='1':
    geo=cell.find('mxGeometry'); assert geo is not None
    x,y,w,h=[float(geo.get(k,'0')) for k in ('x','y','width','height')]
    assert x>=0 and y>=0 and w>0 and h>0 and x+w<=width and y+h<=height
    assert 'fontFamily=Times New Roman;' in cell.get('style','')
   elif cell.get('edge')=='1':
    geo=cell.find('mxGeometry'); assert geo is not None
    for side in ('source','target'):
     if cell.get(side):assert cell.get(side) in ids
     else:assert geo.find(f"mxPoint[@as='{side}Point']") is not None
 return diagrams


def main():
 album=graph(ROOT/'Схемы_МДК_02_02.drawio')
 assert len(album)==11
 for index,(number,interfaces) in enumerate(EXPECTED.items()):
  folder=ROOT/f'ticket_{number:02d}'
  pages=graph(folder/'SCHEME.drawio');assert len(pages)==1
  model=pages[0].find('mxGraphModel')
  assert ET.tostring(model)==ET.tostring(album[index].find('mxGraphModel'))
  text=' '.join(c.get('value','') for c in model.findall('./root/mxCell'))
  assert 'main.py' in text
  source_tree=ast.parse((folder/'main.py').read_text(encoding='utf-8'))
  imported={(n.module,a.name) for n in ast.walk(source_tree) if isinstance(n,ast.ImportFrom) for a in n.names}
  for module,function in interfaces:
   assert module+'.py' in text and function in text
   module_tree=ast.parse((folder/(module+'.py')).read_text(encoding='utf-8'))
   assert any(isinstance(n,ast.FunctionDef) and n.name==function for n in module_tree.body)
   assert (module,function) in imported
  png=(folder/'SCHEME.png').read_bytes();assert png[:8]==bytes([137,80,78,71,13,10,26,10])
  print(f'Билет {number:02d}: PASS — XML, интерфейсы, исходники, PNG')
 print('PASS: 11 схем; обязательные задания 04 и 07 покрыты; общий альбом совпадает с отдельными схемами.')


if __name__=='__main__':main()
