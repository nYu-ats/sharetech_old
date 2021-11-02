# ShareTech

### 環境構築手順
##### 確認環境
- OS : macOS Big Sur 11.6
- docker : 20.10.8
- docker-compose : 1.29.2
- Visual Studio Code : 1.6.12(Universal)

##### 事前準備
1. dockerインストール
2. docker-composeインストール
3. Visual Studio Codeインストール
4. Visual Studio Codeにremote containersをインストール

##### 手順
1. ローカルでプロジェクトフォルダ作成
2. リモートリポジトリの取り込み
```
$ git init
$ git remote add origin <リモートURL>
$ git checkout -b <ブランチ名>
$ git pull origin <ブランチ名>
```
3. Visual Studio Codeで"手順1"で作成したフォルダを開く
4. 
```
$ docker-compose up -d --build
```

### アプリケーション実行手順
1. Visual Studio Codeでターミナルを開き、下記コマンド実行
```
$ pipenv shell
$ python3 manage.py runserver 0.0.0.0:8000
```
2. ブラウザで http://127.0.0.1:8000 にアクセス
