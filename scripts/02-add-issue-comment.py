from github import Github
import sys
import os

args = sys.argv

ISSUE_NUM = int(args[1])

token = os.getenv("GH_TOKEN")
repo_name = os.getenv("GH_REPO")
sender_name = os.getenv("COMMNENT_SENDER")

gh = Github(token)
repo = gh.get_repo(repo_name)
issue = repo.get_issue(number=ISSUE_NUM)
issue.create_comment("@"+sender_name+" も見ています")
