## 📁 フォルダ構成とファイル概要

練習用フォルダ（`python_c1`, `python_c2`, `python_c3`）と、成果物用のアプリフォルダ（`app`）に分けて管理しています。

### python_c1（基礎ウィジェット・基本操作）
* **window.py**: 1枚のウィンドウを表示
* **pack_01.py**: 画面中央に文字列を表示
* **pack_02.py, grid_01〜05.py, place_01〜02.py**: ウィジェットの配置（レイアウト）
* **event_01〜03.py**: ボタンの配置
* **event_04〜09.py**: bind関数（イベント処理）
* **label_01〜05.py**: Labelウィジェット
* **font.py**: フォントテスト
* **entry.py**: テキストフィールド
* **messagebox.py**: メッセージボックス
* **name_app.py, name_app_class.py**: 入力した名前を表示するミニアプリ
* **option_01〜04.py**: ウィジェットの属性設定
* **widget_variable.py**: ウィジェット変数

### python_c2（応用操作・イベント処理）
* **timer.py**: カウントダウン
* **timer_desktop.py**: カウントダウン（GUIが固まる例）
* **timer_threading.py**: カウントダウン（Timer関数を利用）
* **timer_A.py**: after関数
* **scale.py**: スライダー
* **spinbox.py**: スピンボタン
* **progressbar_01〜02.py**: プログレスバー
* **csv_read.py**: quiz.csvを読み込んでリストに変換
* **radio.py**: ラジオボタンテスト
* **switch.py**: 画面の切り替え
* **combobox.py**: コンボボックス
* **canvas_01.py**: Canvasウィジェット表示
* **canvas_02.py**: さまざまな図形や画像ファイル（nsw.png）を描画
* **canvas_03.py**: 特定の図形を消去する
* **color.py**: カラー選択ダイアログを使用
* **photoimage.py**: png画像を読み込む

### python_c3（データベース・発展機能）
* **create_db.py**: sample.dbを作成
* **create_table.py**: personalテーブルを作成
* **insert_data.py**: personalテーブルに3件のデータを追加
* **select_01.py**: idとname列のすべての行のデータを取得し、表示
* **select_02.py**: 抽出した全データを表示
* **select_03.py**: 抽出したデータを1個ずつ取り出す
* **select_04.py**: すべての列のデータを取得
* **select_05.py**: 条件に合致したデータを抽出し表示
* **select_06.py**: 結果を並べ替え
* **update.py**: データを更新
* **delete.py**: データを削除
* **replece.py**: データの追加、または更新
* **placeholder.py**: データの部分を後から追加
* **drop.py**: テーブルを削除
* **create_db1.py**: memo.dbを作成
* **text_01.py**: Textウィジェットに文字列を挿入
* **text_02.py**: 入力した文字列を表示
* **text_03.py**: 文字列を削除
* **scrollbar.py**: スクロールバーとTextウィジェットを連動
* **calender_01.py**: カレンダーを表示
* **calender_02.py**: カレンダーをGUI化
* **create_db2.py**: collection.dbを作成し、booksテーブルを作成
* **treeview_01.py**: 階層列を使ったTreeviewウィジェット
* **treeview_02.py**: 階層列を使わないTreeviewウィジェット
* **menu.py**: メニューコマンドを表示

### app（完成アプリケーション）
* **countdown_app.py**: カウントダウンタイマー
* **quiz_app.py**: 4択クイズ
* **warikan_app.py**: 割り勘計算
* **drawing_app.py**: お絵描きアプリ
* **memory_app.py**: 神経衰弱アプリ
* **memo_app.py**: カレンダー型メモアプリ
* **collection_app.py**: 蔵書管理アプリ