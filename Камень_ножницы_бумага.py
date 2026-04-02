import random
games=['камень','ножницы','бумага']
hello=["""Добро пожаловать в игру "Камень, Ножницы, Бумага"
       ,"чтобы выйти наберите больше очков чем робот, когда надоест скажите - Выйти"""]
x=random.choice(games)
b=0
n=0
g=0
while True:
    x=random.choice(games)
    p=input('Введите значение:  ')
    if p=='выйти':
        print('End')
        break
    elif p==x:
        print('ничья')
        n+=1
    elif p!=x:
        if x=='камень' and p=='бумага':
            print('win')
            g+=1
        elif p=='камень' and x=='бумага':
            print('game over')
            b+=1
        elif x=='бумага' and p=='ножницы':
            print('win')
            g+=1
        elif p=='бумага' and x=='ножницы':
            print('game over')
            b+=1
        elif x=='камень' and p=='ножницы':
            print('win')
            g+=1
        elif p=='камень' and x=='ножницы':
            print('game over')
            b+=1
print(g,'|',n,'|',b)
print('человек|ничья|бот')
