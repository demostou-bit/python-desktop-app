import time

count = 10

#while True:で無限ループを作り、その中で
#time.sleep(1)を実行しながら、変数countの値を表示している
#sleep関数で引数に指定した1秒だけプログラムを停止できる
while True:
  print(count)
  count = count - 1
  time.sleep(1)
  if count < 0: break
  