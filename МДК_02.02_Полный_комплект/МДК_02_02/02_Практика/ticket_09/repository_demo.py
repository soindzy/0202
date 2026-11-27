from git_support import init_repository, git_run


def demonstrate(directory):
    repo = init_repository(directory)
    source = repo / "hello.py"
    source.write_text('print("Hello, world!")\n', encoding="utf-8")
    git_run(repo, "add", "hello.py")
    git_run(repo, "commit", "-m", "Add hello program")
    return {"files": git_run(repo, "ls-files").stdout.strip().splitlines(),
            "commits": int(git_run(repo, "rev-list", "--count", "HEAD").stdout),
            "clean": not git_run(repo, "status", "--porcelain").stdout.strip()}
