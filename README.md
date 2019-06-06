# DAICO_ENGINE

## sshキーの作成

1. ホームディレクトリでcd .sshをし、存在を確認する
2. .sshフォルダを削除し、mkdir .sshで新たにフォルダを作る
3. cd .sshをし、ssh-keygen -t rsaでsshの作成をする
4. pbcopy < ~/.ssh/id_rsa.pubでsshをコピーする
5. githubのsettingsにてsshを追加する
6. vim ~/.bashrcにssh-add -K ~/.ssh/id_rsaを記入
7. exec $SHELL -lで反映させる
8. 完了次第、git clone sshでok

## Nuxt環境構築

* Project name

  * admin,client,customerの3つを作成した。

* Project description

  * engine,company,user

* Use a custom server framework

  * express

* Choose features to install (Press space to select, a to toggle all, i to invert selection)

* Use a custom UI framework

  * element-ui

* Use a custom test framework

  * jest

* Choose rendering mode

  * Universal

* Author name

  * Takaaki Takada

* Choose a package manager
  
  * npm

1. npx create-nuxt-app projectnameでプロジェクトを作成（これは既にやってあるのでやらないでください）
2. npm install(できない場合はnodeをインストールからやりましょう)
3. npm run dev

## Djang環境構築

1. cd DAICO_ENGINE/api
2. pyenv virtualenv 3.6.5 daico
3. pyenv local daico
4. pip install django==2.1
5. pip install django-rest-framework
6. pip install django-cors-headers
7. pip install sqlalchemy
8. pip install mysqlclient
9. python manage.py runserver

## mysql反映

1. mysql -uroot -pでrootで入る
2. grant all on アスタリスク.アスタリスク to neekey@'%' identified by '#nky%2T0A1K9A0D6A0T1' with grant option;ですべての管理をできるmysqlアカウントを作成する
3. vim ~/.bashrcにてユーザ名とパスワードを書き換える
4. exec $SHELL -lで反映させる
5. mysqlで入り、create database daicodb;でデータベースを作る
