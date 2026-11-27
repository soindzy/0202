from git_support import init_repository, git_run


def demonstrate(directory):
    repo = init_repository(directory)
    (repo / "main.txt").write_text("Основная версия\n", encoding="utf-8")
    git_run(repo, "add", "main.txt")
    git_run(repo, "commit", "-m", "Initial version")
    git_run(repo, "checkout", "-b", "feature")
    (repo / "feature.txt").write_text("Новая функция\n", encoding="utf-8")
    git_run(repo, "add", "feature.txt")
    git_run(repo, "commit", "-m", "Add feature")
    git_run(repo, "checkout", "main")
    git_run(repo, "merge", "--no-ff", "feature", "-m", "Merge feature")
    return {"branch": git_run(repo, "branch", "--show-current").stdout.strip(),
            "feature": (repo / "feature.txt").read_text(encoding="utf-8").strip(),
            "parents": len(git_run(repo, "show", "-s", "--format=%P", "HEAD").stdout.split()),
            "clean": not git_run(repo, "status", "--porcelain").stdout.strip()}
