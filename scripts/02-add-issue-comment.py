from github import Github
import sys

args = sys.argv

ISSUE_NUM = args[1]

token = os.getenv("GH_TOKEN")
repo_name = os.getenv("GH_REPO")
gh = Github(token)
repo = g.get_repo(repo_name)
issue = gh.get_issue(number=ISSUE_NUM)
issue.create_comment("Test")


# gh issue comment $ISSUE_NUM --body "prコメント"
