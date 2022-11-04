import schedule
import time 
def main():
    print("時間になりました")
    time.sleep(10)
    print("さようなら")
    
schedule.every().day.at("02:25").do(main) #スケジュールの登録する

while True:
    schedule.run_pending() #現在時刻が02:22なら一回だけ発火する(2回目以降は無効、実行するとわかるが並列処理ではない)
    print("b")
    time.sleep(1)
