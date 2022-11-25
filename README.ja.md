# Eagle-pnginfo

![](misc/sss_top.png)

[English README](README.md)

- [AUTOMATIC1111's Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 用の Extension です
- WebUIで生成した画像を、生成情報(プロンプト・Generation Info)を含めて、お手元の PC で動いている [Eagle](https://jp.eagle.cool/) (画像管理ソフト) へ転送・登録します

## インストール方法

- `Extensions` タブを開く

- `Install from URL` にこのレポジトリの URL を入力

- `Install` を実行

- 別途、PCへ [Eagle]([https://jp.eagle.cool/](https://jp.eagle.cool/) をインストールしておく

## 使い方 / How to use

- "設定" タブで、この Extension を有効にする

- 別途、"Eagle" アプリを立ち上げておく

- "AUTO1111" の Web UI を開き、いつも通り画像を生成する
  
   - 生成された画像は、自動的に Eagle アプリに登録されます

## 設定項目について

| In "Setting" tab                      | ![](misc/sss08.png)                                                                                                             |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| "Send all image to Eagle"             | この Extension を有効にします                                                                                                            |
| FolderID on Eagle                     | (option: 必須ではありません)<br/>画像を登録する Eagle 側のフォルダID を指定できます                                                                          |
| Save Generation info as Annotation    | PNGinfo に表示されるような、3行からなる生成情報を、Eagle の メモ欄に登録します                                                                                 |
| Save positive prompt to Eagle as tags | プロンプトを Eagle の tag として登録します                                                                                                     |
| Save negative prompt to Eagle as      | ネガティブプロンプトを Eagle の tag として登録します<br/>None: 登録しません<br/>tag: 登録します<br/>n:tag 登録します。登録時、タグ名の頭に "n:" をつけ、通常のプロンプトの tag と判別できるようにします |

## 設定サンプル

| Settings              | Result                | Comment                                                                                             |
| --------------------- | --------------------- | --------------------------------------------------------------------------------------------------- |
| ![](misc/sss00.png)   | No output to Eagle    |                                                                                                     |
| ![](misc/sss01-1.png) | ![](misc/sss01-2.png) | 画像を Eagle へ送ります                                                                                     |
| ![](misc/sss02-1.png) | ![](misc/sss02-2.png) | 画像を Eagle へ送ります<br/>Generation info 付き                                                              |
| ![](misc/sss03-1.png) | ![](misc/sss03-2.png) | 画像を Eagle へ送ります<br/>Generation info, tag, positive prompt 付き                                        |
| ![](misc/sss04-1.png) | ![](misc/sss04-2.png) | 画像を Eagle へ送ります<br/>Generation info, tag, negative　prompt 付き                                        |
| ![](misc/sss05-1.png) | ![](misc/sss05-2.png) | 画像を Eagle へ送ります<br/>Generation info, tag, negative　prompt 付き。< i.e.) n:bad anatomy                  |
| ![](misc/sss06-1.png) | ![](misc/sss06-2.png) | 画像を Eagle へ送ります<br/>Generation info, tag, positive prompt, negative prompt 付き。< i.e.) n:bad anatomy |
| ![](misc/sss07-1.png) | FolderID              | "Eagle forlderID" を取得するには、Eagle UI で対象のフォルダを右クリックし、"copy link" を選択                                  |
| ![](misc/sss07-4.png) | ![](misc/sss07-3.png) | folderID を入れておくと、対象のフォルダに画像が格納されます                                                                  |
| ![](misc/sss07-2.png) |                       | folderID の悪い例<br/>コピーしたものをそのまま入力すると左画像のように長いパス名が入っていますが、必要になるのは右端の文字列のみです                           |
