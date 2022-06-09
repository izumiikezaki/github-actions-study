#!/bin/bash

PR_NUM=$1
MSG="@"$COMMNENT_SENDER" も見ています"
gh pr comment $PR_NUM --body "prコメント"