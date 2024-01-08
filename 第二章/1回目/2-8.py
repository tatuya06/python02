import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1
change_str = {'A':0,'B':1,'C':2}
change_num = {'1':0,'2':1,'3':2}

def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル:' + str(level))

def view_question():
    choice_data = random.randint(0, 2)
    mistake_number = random.randint(0, 8)
    question = data[choice_data]
    print('デバッグ:mistake_number = '+ str(mistake_number))
    print(question)
    print('/|A B C')
    print('--------')
    i = 0
    j = 0
    k = 0
    while i < 3:
        k_number = k + 1
        print(str(k_number) + '|',end="")
        while j < 3: 
            if i * 3 + j == mistake_number:
               print(question[1],end="")
            else:
                print(question[0], end="")
            j = j + 1
        print(end='\n')
        i = i + 1
        k = k + 1
        j = 0  # 内部ループ終了時に j をリセット
    return mistake_number

def change_input_number(input_str):
    cm = list(input_str)
    # 先頭の英文字を変換する
    na = change_str[cm[0]]
    nb = change_num[cm[1]]
    if nb == 0:
        nb = nb * 1
    elif nb == 1:
        nb = nb + 2
    elif nb == 2:
        nb = nb * 3
    view_nm = na + nb
    return view_nm

def is_correct_number(mistake_number, input_number):
    return input_number == mistake_number

def view_result(is_correct):
    if is_correct == True:
        print('正解！')
    else:
        print('不正解')

def play():
    section_message()
    mis = view_question()
    choice = input('(例:A1)')
    print('デバッグ:choice = ' + choice)
    cin = change_input_number(choice)
    print('デバック:input_number = '+ str(cin))
    is_correct = is_correct_number(mis,cin)
    view_result(is_correct)

start_message()
play()