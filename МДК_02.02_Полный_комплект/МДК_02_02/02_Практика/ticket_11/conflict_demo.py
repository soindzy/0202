from git_support import init_repository, git_run


def demonstrate(directory):
    repo = init_repository(directory)
    config = repo / "config.ini"
    config.write_text("timeout = 10\n", encoding="utf-8")
    git_run(repo, "add", "config.ini")
    git_run(repo, "commit", "-m", "Initial timeout")
    git_run(repo, "checkout", "-b", "feature")
    config.write_text("timeout = 30\n", encoding="utf-8")
    git_run(repo, "add", "config.ini")
    git_run(repo, "commit", "-m", "Feature timeout")
    git_run(repo, "checkout", "main")
    config.write_text("timeout = 20\n", encoding="utf-8")
    git_run(repo, "add", "config.ini")
    git_run(repo, "commit", "-m", "Main timeout")
    merge = git_run(repo, "merge", "feature", check=False)
    unmerged = git_run(repo, "diff", "--name-only", "--diff-filter=U").stdout.splitlines()
    if merge.returncode != 1 or "config.ini" not in unmerged:
        raise RuntimeError("Ожидался настоящий конфликт config.ini")
    conflict_text = config.read_text(encoding="utf-8")
    # Учебное согласованное решение: принять timeout = 30.
    config.write_text("timeout = 30\n", encoding="utf-8")
    git_run(repo, "add", "config.ini")
    git_run(repo, "commit", "-m", "Resolve timeout conflict: use 30")
    return {"conflict": conflict_text, "result": config.read_text(encoding="utf-8"),
            "unmerged": git_run(repo, "ls-files", "-u").stdout,
            "clean": not git_run(repo, "status", "--porcelain").stdout.strip(),
            "parents": len(git_run(repo, "show", "-s", "--format=%P", "HEAD").stdout.split())}
