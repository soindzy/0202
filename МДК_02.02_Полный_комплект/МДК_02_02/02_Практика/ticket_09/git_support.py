"""Команды Git выполняются только в переданном учебном каталоге."""
import os
from pathlib import Path
import shutil
import subprocess


def git_run(directory, *args, check=True):
    executable = os.environ.get("GIT_EXECUTABLE") or shutil.which("git")
    if not executable:
        raise RuntimeError("Установите Git и добавьте его в PATH либо задайте GIT_EXECUTABLE")
    env = os.environ.copy()
    # Не используем пользовательские настройки, подпись и внешние хуки.
    env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull,
               GIT_CONFIG_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0")
    hooks = str(Path(directory).resolve() / ".empty_hooks")
    command = [executable, "-c", "user.name=Student", "-c", "user.email=student@example.invalid",
               "-c", "commit.gpgsign=false", "-c", "core.autocrlf=false",
               "-c", f"core.hooksPath={hooks}", *args]
    result = subprocess.run(command, cwd=directory, env=env, text=True,
                            encoding="utf-8", errors="replace", capture_output=True, timeout=30)
    if check and result.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {result.stdout} {result.stderr}")
    return result


def init_repository(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    if any(directory.iterdir()):
        raise ValueError("Учебный репозиторий создаётся только в пустом каталоге")
    git_run(directory, "init", "-b", "main")
    return directory
