# github-actions-study
GithubActions学習用リポジトリ。
学習目的のため、コードにコメント付けまくりです。



## ワークフローを設定する
公式ドキュメントの[クイックスタート](https://docs.github.com/ja/actions/learn-github-actions/understanding-github-actions)をやってみる


## study01:echoするワークフロー
[ここ](https://github.com/izumiikezaki/github-actions-study/actions/workflows/study01.yml)から「run workflow」のボタン押すとただhogeをechoするだけ。

## study02:PR作成でコメントを追加するbashが走るワークフロー
[![echoするだけ](https://github.com/izumiikezaki/github-actions-study/actions/workflows/study01.yml/badge.svg)](https://github.com/izumiikezaki/github-actions-study/actions/workflows/study01.yml)
このリポジトリのPRまたはissueでコメントを残すとbotが返事（？）してくる。
PRへの返信はbash、issueへの返事はpythonのスクリプトを使っている。


コード上ではわからないが、これらのようにワークフロー内でスクリプトを動かすには`git update-index --add --chmod=+x (スクリプトのパス)`を行って権限を許可しなければいけない。
 

> **Warning**  
> issue_commentのトリガーはmasterにマージされていないと動かないらしい。（つまりこのワークフローを作るPR内で検証できない）  
> ちょっとした罠じゃん。

## study03:マーケットプレイスのアクションが動くワークフロー
毎日wakatimeの履歴がgistに更新されるワークフロー（のはずだったがうまく動かない）。  
マーケットプレイスの[waka-box](https://github.com/marketplace/actions/waka-box)というアクションを利用した例として出す予定だった。<br/>
<img src="https://user-images.githubusercontent.com/39111330/172936254-f0114021-0aff-4285-af67-ba3631ff7656.png" width="320px">

## 4:カスタムのアクションが動くワークフロー
