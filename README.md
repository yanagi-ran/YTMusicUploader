# YTMusicUploader
## これはなんですか？
[YouTube Music](https://music.youtube.com) へローカルにある音楽ファイルをアップロードするためのソフトです。  
ベースは [ytmusicapi](https://ytmusicapi.readthedocs.io/en/stable/index.html) を使用しています。  
GUIで簡単にファイル選択できるようにしただけってことです。  
## 使い方
### 必要なもの
Python  

### インストール
リリースページからzipファイルをダウンロード・展開してください。  
中にある `setup.bat` を実行してください。  
```
Please paste the request headers from Firefox and press 'Enter, Ctrl-Z, Enter' to continue:
```

になったら、できればFireFoxでYouTubeMusicを開き、開発者モードを表示します。  
ネットワークタブに移動して検索欄に `/browse` と入力します。  

![image](https://github.com/yanagi-ran/YTMusicUploader/assets/163057636/a5cfecd9-d215-44ed-864d-f347a2fad890)

↑のようなものが出たらそれをクリック。  

![image](https://github.com/yanagi-ran/YTMusicUploader/assets/163057636/298efb4b-c0b8-4db1-ae5c-c20948dc94c8)

Request HeadersのRawをONにして、内容をコピーしてコンソールに貼り付けて  
**Enter→Ctrl+Z→Enter**の順でキーを入力。  
```
done
```

って出たらOK。カレントディレクトリ内に `browser.json` ができます。  
### 使い方

![見た目](https://github.com/yanagi-ran/YTMusicUploader/assets/163057636/4a738d20-1e28-4bfa-8bc2-63f0219fc191)

↑こんな見た目だよ。  
まず「ファイルを選択」をクリック。アップロードしたい音声ファイルを選択してください。  
選べるフォーマットは、、、"mp3","flac","m4a","ogg","wma" です。  

![image](https://github.com/yanagi-ran/YTMusicUploader/assets/163057636/c14e7d98-21f8-433d-b27d-6e4adf2dc7e6)

あとはアップロードボタンを押すだけです。  

![image](https://github.com/yanagi-ran/YTMusicUploader/assets/163057636/6fc11074-03b9-45a5-9c71-d52d35721f02)

アップロード中はプログレスが表示されるよ。  
## データが心配？
ソースコードを見ていただければわかる通り、このソフト自体に怪しい関数はないです。  
ですが使っている ytmusicapi がその通りである保証はありません。  
もし怖いのであれば普通にブラウザからアップロードしてください。  
ていうかセットアップが若干初心者には厳しい感じがしますけど。  
## 著作権表示
Copyright (C) 2024 yanagi-ran  
MIT License

## 更新履歴
```
v1.1 - プチアップデート
概要:
  ファイルを追加できるように
  一度に複数ディレクトリからアップロードできるようになったはずです。
  削除については難航しています(全部書き直す必要があるかも)
  応急処置で全クリアボタンを追加。

======================

v1.0 - 初回リリース
概要:
  基本的な機能の追加
```
