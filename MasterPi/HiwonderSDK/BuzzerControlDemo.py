import time
import Board

Board.setBuzzer(0) # Off

Board.setBuzzer(1) # On
time.sleep(0.1) # 0.1 s time delay
Board.setBuzzer(0) #Off

time.sleep(1) # time delay

Board.setBuzzer(1)
time.sleep(0.5)
Board.setBuzzer(0)