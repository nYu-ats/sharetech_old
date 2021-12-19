# ShareTech

### 環境構築手順
##### 確認環境
- OS : macOS Big Sur 11.6
- docker : 20.10.8
- docker-compose : 1.29.2
- python : 3.8.2
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
4. コマンドパレットで”Reopen in Container”を実行
5. ".devcontainer"フォルダが作成されるので、環境に合わせて編集する。以下サンプル。
```
$ view devcontainer.json
{
        "name": "Django",
        "dockerComposeFile": [
                "../docker-compose.yml",
                "docker-compose.extend.yml"
        ],

        "service": "django",
        "runServices": [
                "django",
                "mysql"
                        ],

        "workspaceFolder": "/usr/src/sharetech",

        "settings": {},

        "extensions": []
}

$ view docker-compose.extend.yml
version: '3.8'
services:
  django:
    init: true

    volumes:
      - .:/workspace:cached
      - /var/run/docker.sock:/var/run/docker.sock

    command: /bin/sh -c "while sleep 1000; do :; done"

```
6. コマンドパレットで"Rebuild Container"を実行

### アプリケーション実行手順
1. メール送信用の環境変数を設定
```
$ EMAIL_HOST=<メールアドレス>
$ EMAIL_APP_PASS=<アプリケーションパスワード>
```
3. Visual Studio Codeでターミナルを開き、下記コマンド実行
```
$ pipenv shell
$ python3 manage.py migrate
$ python3 manage.py runserver 0.0.0.0:8000
```
3. ブラウザで http://127.0.0.1:8000 にアクセス

### AWS Elastic Beanstalk デプロイ手順
1. EB CLI インストール  
新しいターミナルウィンドウで下記を実行

``` sh
pipenv shell
mkdir /var/lib/ebcli
cd /var/lib/ebcli

# Install
git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git
./aws-elastic-beanstalk-cli-setup/scripts/bundled_installer

# Path
echo 'export PATH="/root/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
echo 'export PATH=/root/.pyenv/versions/3.7.2/bin:$PATH' >> /root/.bash_profile && source /root/.bash_profile

# Setup
cd /usr/src/sharetec
eb init

# >>
# Select a default region
# 1) us-east-1 : US East (N. Virginia)
# 2) us-west-1 : US West (N. California)
# 3) us-west-2 : US West (Oregon)
# 4) eu-west-1 : EU (Ireland)
# 5) eu-central-1 : EU (Frankfurt)
# 6) ap-south-1 : Asia Pacific (Mumbai)
# 7) ap-southeast-1 : Asia Pacific (Singapore)
# 8) ap-southeast-2 : Asia Pacific (Sydney)
# 9) ap-northeast-1 : Asia Pacific (Tokyo)
# 10) ap-northeast-2 : Asia Pacific (Seoul)
# 11) sa-east-1 : South America (Sao Paulo)
# 12) cn-north-1 : China (Beijing)
# 13) cn-northwest-1 : China (Ningxia)
# 14) us-east-2 : US East (Ohio)
# 15) ca-central-1 : Canada (Central)
# 16) eu-west-2 : EU (London)
# 17) eu-west-3 : EU (Paris)
# 18) eu-north-1 : EU (Stockholm)
# 19) eu-south-1 : EU (Milano)
# 20) ap-east-1 : Asia Pacific (Hong Kong)
# 21) me-south-1 : Middle East (Bahrain)
# 22) af-south-1 : Africa (Cape Town)
(default is 3): 9

# You have not yet set up your credentials or your credentials are incorrect 
# You must provide your credentials.
(aws-access-id): {your access-key}
(aws-secret-key): {your secret-key}

# Select an application to use
# 1) sharetec
# 2) [ Create new Application ]
(default is 2): 1

```

2. デプロイ

``` sh
pwd
# >>
# /usr/src/sharetech

eb deploy
```
