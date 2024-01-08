import random
import math

data = [['見','貝'],['土','士'],['眠','眼']]
str_data =['A','B','C','D','E','F','G']

level = 1
col = 5
row = 4

def start_message():
    print('違う漢字の番号(例:A１)を入力してください')

def section_message():
    print('レベル：'+str(level))

def view_question():
    question = random.randint(0,2)
    mistake_number = random.randint(0,col * row -1)
    question_view = data[question]
    print('デバック：mistake_number = '+str(mistake_number))
    print(question_view)
    i = 0
    j = 0
    k = 1
    l = 0
    str_pr =''
    str_bar = '--'
    while l < col:
        str_pr += str_data[l]+' '
        str_bar += '--'
        l += 1
    print('/|'+str_pr)
    print(str_bar)
    while i < row:
        print(str(k)+'|',end = '')
        while j < col:
            if (i * col + j) == mistake_number:
                print(question_view[1],end = '')
            else:
                print(question_view[0],end = '')
            j += 1
        print("")
        i += 1
        k += 1
        j = 0
    return mistake_number

def change_input_number(input_str):
    change_str = {"A":0,"B":1,"C":2,"D":3,"E":4,"G":5,"H":6}
    ch = list(input_str)
    ch_number1 = change_str[ch[0]]
    ch_number2 = int(ch[1]) - 1
    view_number = (int(ch_number2) * col )+ int(ch_number1)
    print('デバック：input_number = '+str(view_number))
    return view_number

def is_correct_number(mistake_number,input_number):
    if mistake_number == input_number:
        return True
    else:
        return False

def view_result(is_correct,mis_number):
    if is_correct == True:
        print('正解！')
    else:
        print('不正解、、、')
        change_string(mis_number)

def change_string(number):
    #先頭の英文字の表示方法
    ch_str1 = number % col
    #二文字目の数字の表示方法
    ch_str2 = math.floor(number // col +1)
    print('正解は'+str_data[ch_str1]+str(ch_str2))

def play():
    section_message()
    mis_nm = view_question()
    choice = input('(例：A1)')
    print('デバック：choice = '+choice)
    ch_nm = change_input_number(choice)
    judge = is_correct_number(mis_nm,ch_nm)
    view_result(judge,mis_nm)
   
start_message()
play()