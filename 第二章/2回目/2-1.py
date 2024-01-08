import random

level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def viwe_level():
    print ('レベル：'+str(level))


def play():
    start_message()
    viwe_level()
    choice =  input('(例:A1)')
    print('デバック：choice = '+choice)

play()