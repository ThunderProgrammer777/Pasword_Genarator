import time
import random
import string
print("In this program you will learn how to type very fast.")
print("Wait while we make a word </>")
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
time_taken = []
semi = []
final = []
choice=str(input("Should we start?[Y/n]:"))
while choice != 'n':
    for _ in range(3):
        n=random.randint(0,25)
        if n in semi:
            pass
        else :
            semi.append(lower[n])


    for _ in range(3):
        n=random.randint(0,25)
        if n in semi:
            pass
        else:
            semi.append(upper[n])

    while len(final)!=6:
        n=random.randint(0,5)
        if  semi[n] in final:
            pass
        else:
            final.append(semi[n])
    oh = "".join(final)
    print(oh)
    x=3
    while x!=0:
        print(x)
        time.sleep(1)
        x=x-1
    start = time.time()
    ans = input()
    end = time.time()
    t = end-start
    print(t)
    print(time_taken)
    time_taken.append(t)
    check = list(ans)
    if ans[0]==final[0] and ans[1]==final[1] and ans[2]==final[2] and ans[3]==final[3] and ans[4]==final[4] and ans[5]==final[5]:
        if len(time_taken)==1:
            print(f"Great, You type 6 word in {t} seconds.")
        elif len(time_taken)!=1:
            for o in time_taken:
                to=bool(o>=t)
                if o==t:
                    pass
                elif to==True:
                    print("Good,You type faster than previous."
                          f"You type 6 word in {t} seconds{o}.")
                    time_taken.remove(o)
                elif to==False:
                    print("Good,But not better than previous.:)")

    else :
        print("NO! Wrong Answer")
    semi.clear()
    check.clear()
    final.clear()
    choice=str(input("Do you want to do again?[Y/n]"))
