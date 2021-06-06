# circle-finder
URL: https://circle-finder.com  
概要:慶應大学の新入生のための慶應テニスサークル情報収集＆比較Webサービス  
解決したい課題:
1. 慶應大学の新入生は数多くある慶應のテニスサークルの情報収集が大変(色々なテニサーのTwitterやInstagramを探す等)だからその手助けをしたい。特にテニスサークルは他のサークルと違って入サーの締切りがあることが多いので、あまり他のサークルとじっくり比較する時間がないままに入サーを決めざるを得ない状況になっている。特に、コロナ禍でオンラインで手軽にテニサーの情報を得られることが新入生の助けになると思う。
2. 慶應大学硬式テニスサークル側も新歓でTwitter, Instagram, LINEなどで情報発信に力を入れているものの新入生に認知してもらうのが大変だからその負担を軽減。

[Youtube 参考動画](https://youtu.be/gqMYXy_T6iw)

# 技術スタック
フロントエンド HTML, CSS, JS  
使用フレームワーク Bootstrap, jQuery  
バックエンド Python  
使用フレームワーク Django  
データベース PostgreSQL  
インフラ AWS(EC2, S3, RDS(PostgreSQL), Route53)  
Webサーバ Nginx
アプリケーションサーバ Gunicorn


# 機能一覧
- サークル一覧表示機能
- サークル詳細表示機能
- サークル編集者によるサークル情報編集機能(画像ファイルアップロードも可能)
- 認証機能(サインアップ、ログイン、ログアウト)
- ページネーション機能
- Like機能(jQueryのAjaxで実装)
- 管理画面でのDBテーブル操作(Django標準)
- 最適サークル診断機能(練習本気度、テニス経験者率、飲み会頻度の3軸を5段階評価し、最もマッチしているサークルを最小二乗法で算出)
