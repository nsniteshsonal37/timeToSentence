from num2words import num2words
def num2string(num):
    return((num2words(num)).replace('-',' '))
def out(x):
    list1=x.split(':')
    s1=int(list1[0])
    s2=int(list1[1])
    if(s1<0):
        return("A day can't have negative hours!")
    if(s1==0):
        s1=12
    if(s1>12 and s1<25):
        s1=int(s1-12)
    if(s1>24):
        s1=int(s1%24)
    if(s2>60):
        s1+=int(s2/60)
        s2=int(s2%60)

    if(s2<0):
        return("An hour can't have negative minutes!")
    elif(s2==0):
        return (f"{num2string(s1)} o{{}}clock".format("'"))
    elif(s2==1):
        return (f"one minute past {num2string(s1)}")
    elif(s2==15):
        return (f"quarter past {num2string(s1)}")
    elif(s2==30):
        return (f"half past {num2string(s1)}")
    elif(s2==45):
        if(s1==12):
            return (f"quarter to {num2string(1)}")
        return (f"quarter to {num2string(s1+1)}")
    elif(s2==59):
        if(s1==12):
            return (f"one minute to {num2string(1)}")
        return (f"one minute to {num2string(s1+1)}")
    elif(s2==60):
        if(s1==12):
            return (f"{num2string(1)} o{{}}clock".format("'"))
        return (f"{num2string(s1+1)} o{{}}clock".format("'"))
    elif(s2>30):
        if(s1==12):
            return (f"{num2string(60-s2)} minutes to {num2string(1)}")
        return (f"{num2string(60-s2)} minutes to {num2string(s1+1)}")
    elif(s2<30):
        return (f"{num2string(s2)} minutes past {num2string(s1)}")

print(out("15:00"))