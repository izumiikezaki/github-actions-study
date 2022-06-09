# github-actions-study
test用
GithubActions学習用リポジトリ。
学習目的のため、コードにコメント付けまくりです。



## ワークフローを設定する
公式ドキュメントの[クイックスタート](https://docs.github.com/ja/actions/learn-github-actions/understanding-github-actions)をやってみる


## 1:echoするワークフロー

## 2:PR作成でコメントを追加するbashが走るワークフロー
ワークフロー内でシェルスクリプトを動かすために：
 - `- uses: actions/checkout@v2`　をアクションに追加
 - `git update-index --add --chmod=+x ./scripts/02-add-issue-comment.sh`をローカルで行って実行
 

> **Warning**
> issue_commentのトリガーはmasterにマージされていないと動かないらしい。

## 3:マーケットプレイスのアクションが動くワークフロー

## 4:カスタムのアクションが動くワークフロー
