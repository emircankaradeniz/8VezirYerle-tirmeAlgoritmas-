import random
import os
def main():
    Matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    def function(a,b):
        for i in Matrix[a]:
            if i == 1:
                return False
        count =0
        while count<8:
            if Matrix[count][b] ==1:
                return False
            count=count+1
        a2 = a
        b2 = b
        k =0
        while k==0:
            if a2==0 or b2==0:
                a3 = a2
                b3 = b2
                while True:
                    if Matrix[a3][b3]==1:
                        return False
                    elif a3!=7 and b3!=7:
                        a3=a3+1
                        b3=b3+1
                    else:
                        k=1
                        break
            else:
                a2=a2-1
                b2=b2-1
        a3=a
        b3=b
        k2=0
        while k2==0:
            if a3==7 or b3==0:
                a4 = a3
                b4 = b3
                while True:
                    if Matrix[a4][b4] ==1:
                        return False
                    elif a4!=0 and b4!=7:
                        a4=a4-1
                        b4=b4+1
                    else:
                        k2=1
                        break
            else:
                a3=a3+1
                b3=b3-1
        return True

    while True:
        Matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        Matrix[random.randint(0,7)][random.randint(0,7)] = 1
        vezirSayisi = 7
        count = 0
        count2 = 0
        while vezirSayisi > 0:
            c = 0
            d = 0
            e = 0
            while True:
                if e == 1 or count > 9:
                    break
                for i in Matrix:
                    if e == 1 or c > 8:
                        break
                    for j in i:
                        if e == 1 or d > 8:
                            break
                        if j == 0 and function(c, d) == True:
                            Matrix[c][d] = 1
                            vezirSayisi -= 1
                            e = 1
                            break
                        d += 1
                    d = 0
                    c += 1
                c = 0
                count+=1
            count2+=1
            if(count2>9):
                break
        if(vezirSayisi==0):
            break
    for r in Matrix:
        print(r)
    os.system("pause")
if __name__ == '__main__':
    main()
