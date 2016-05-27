#calc_txtmatch.py
	-テキストマッチの実行時間計測スクリプト
	-引数としてこれから実行するクライアントを指定
	-python calc_txtmatch.py client
	-(client : execution file)
	-input :execution file
	-output:result_txtmachi.txt(write execution time)

calc_label.py 
-ラベリングのの実行時間計測スクリプト
-引数としてこれから実行するクライアントを指定
-python calc_label.py client
-(client : execution file)
-input :execution file
-output:result_label.txt(write execution time)

calc_detect.py 
-顔認識の実行時間計測スクリプト
-引数としてこれから実行するクライアントを指定
-python calc_detect.py client
-(client : execution file)
-input :execution file
-output:result_detect.txt(write execution time)

result.py
-実行時間の平均を出す
-input :result_txtmatch.txt
-input :result_label.txt
-input :result_detect.txt

	-output:team_result.txt(write average execution time)