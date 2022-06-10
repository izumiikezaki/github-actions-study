#!/bin/bash

PR_NUM=$1
gh pr comment $PR_NUM --body "@${COMMNENT_SENDER} も見ています"