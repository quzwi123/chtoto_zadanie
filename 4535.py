from random import *

x=int(input("введите количество вопросов: "))
key=0
slovar={
            }
for i in range(0,x):
    print(key)
    key=key+1
    question=input("введите вопрос: ")
    slovar[key]=question
print(slovar)
random.shuffle(slovar)
print(slovar)
    
