#!/bin/bash

PR_NUM=$1
echo $1
gh pr comment $PR_NUM -F ./comments "prコメント"