#!/bin/bash

PR_NUM=$1
MSG="@${COMMNENT_SENDER} も見ています"
echo $MSG
gh pr comment $PR_NUM --body $MSG