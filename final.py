import random
def zanovo():
    x=int(input("введите количество вопросов "))
    kol_variantov=int(input("введите количество вариантов от 1 до 4"))
    voprosi=list()
    u=1
    for i in range(0,x):
        vopros=input(f"введите вопрос {u}:")
        voprosi.append(vopros)
        u=u+1
    random.shuffle(voprosi)
    len1=len(voprosi)
    if kol_variantov == 1:
        print(voprosi)
    elif kol_variantov == 2:
        if x%2==0:
            var1=voprosi[0:len1:2]
            var2=voprosi[1:len1:2]
            print("вариант 1: ",var1)
            print("вариант 2: ",var2)
        else:
            print("количесвто вопросов не раздедить поровну между 2 вариантами")
            zanovo()
    elif kol_variantov == 3:
        if x%3==0:
            var1=voprosi[0:len1:3]
            var2=voprosi[1:len1:3]
            var3=voprosi[2:len1:3]
            print("вариант 1: ",var1)
            print("вариант 2: ",var2)
            print("вариант 3: ",var3)
        else:
            print("количесвто вопросов не раздедить поровну между 3 вариантами")
            zanovo()
    elif kol_variantov == 4:
        if x%4==0:
            var1=voprosi[0:len1:4]
            var2=voprosi[1:len1:4]
            var3=voprosi[2:len1:4]
            var4=voprosi[3:len1:4]
            print("вариант 1: ",var1)
            print("вариант 2: ",var2)
            print("вариант 3: ",var3)
            print("вариант 4: ",var4)
        else:
            print("количесвто вопросов не раздедить поровну между 4 вариантами")
            zanovo()
    else:
        print("вариантов должно быть 1, 2, 3 или 4")
        zanovo()

zanovo()

