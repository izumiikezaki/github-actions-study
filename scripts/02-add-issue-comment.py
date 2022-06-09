from github import Github
import sys
import os

args = sys.argv

ISSUE_NUM = args[1]
print(args)
print(ISSUE_NUM)

token = os.getenv("GH_TOKEN")
repo_name = os.getenv("GH_REPO")
gh = Github(token)
repo = gh.get_repo(repo_name)
issue = repo.get_issue(number=ISSUE_NUM)
issue.create_comment("Test")


# gh issue comment $ISSUE_NUM --body "prコメント"

