# github-actions-study
GithubActions学習用リポジトリ。  
学習目的のため、コードにコメント付けまくりです。  


  
## study00: 公式が用意したクイックスタートのワークフロー
公式ドキュメントの[クイックスタート](https://docs.github.com/ja/actions/learn-github-actions/understanding-github-actions)をやってみる

  
## study01: echoするだけのワークフロー
[ここ](https://github.com/izumiikezaki/github-actions-study/actions/workflows/study01.yml)から「run workflow」のボタン押すとただhogeをechoするだけ。

## study02:PR作成でコメントを追加するbashが走るワークフロー
PRまたはissueでコメントを残すとbotが返事（？）してくる。
PRへの返信はbash、issueへの返事はpythonのスクリプトをで書いた。


コード上ではわからないが、これらのようにワークフロー内でスクリプトを動かすには`git update-index --add --chmod=+x (スクリプトのパス)`を行って権限を許可しなければいけない。
 

> **Warning**  
> issue_commentのトリガーはmasterにマージされていないと動かないらしい。（つまりこのワークフローを作るPR内で検証できない）  
> ちょっとした罠じゃん。
  
## study03: マーケットプレイスのアクションが動くワークフロー
毎日wakatimeの履歴がgistに更新されるワークフロー（のはずだったがうまく動かない）。  
マーケットプレイスの[waka-box](https://github.com/marketplace/actions/waka-box)というアクションを利用した例として出す予定だった。<br/>
<img src="https://user-images.githubusercontent.com/39111330/172936254-f0114021-0aff-4285-af67-ba3631ff7656.png" width="320px">
  
APIキーとかの値はActions secretsとして隠せるから安心
![image](https://user-images.githubusercontent.com/39111330/172970674-c0786c24-1ee2-43e7-a192-fa4ccdfdeff8.png)


## study04: カスタムのアクションが動くワークフロー
