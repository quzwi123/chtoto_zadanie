import random
x=int(input("введите количество вопросов "))
y=int(input("введите количество вариантов "))
voprosi=list()
for i in range(0,x):
    vopros=input("введите вопрос ")
    voprosi.append(vopros)
    
print(voprosi)
random.shuffle(voprosi)
z=x/y
for i in range(0,y):
print(voprosi)
    
