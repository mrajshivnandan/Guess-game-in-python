run = True

def call1():
    r = input("\nFor next press y and to continue press any other key.\n")
    if r == "y":
        global run
        run = False
    else:
        run = True

while run== True:
    print('-------------Welcome To Age Master-------------')
    age = int(input('To know when you will become 100year old Enter your Age or Year of Birth.\n'))

    if age<100 and age>0:
        print(f'You will be 100 years old after {100-age} Years in the Year {2020+(100-age)}')
        call1()
    elif age>=1900 and age<=2020:
        print(f'You are now {2020-age} years old and will be 100 years old in the Year {age+100}')
        call1()
    elif age>100 and age<150:
        print("You have already completed 100 years of life")
        call1()
    elif age>149 and age<1000:
        print("This Program is only for normal humans you are too much old")
        call1()
    elif age>999 and age<1900:
        print("You are way too old")
        call1()
    elif age>2020:
        print("You are not yet born")
        call1()
    else:
        print("you are not a human")
        call1()
while True:
    i= input("Do You want to know your age in any year if yes press y and to exit press n\n")
    if i== 'y':
        break
    elif i== 'n':
        print("Thanks for visiting and taking your valuable time with us")
        exit()
    else:
        print("Type only y or n")
end= True
def call():
    t = input("\nFor exit press q and to continue press any other key.\n")
    if t == "q":
        global end
        exit("Thanks for visiting and taking your valuable time with us")
    else:
        end = True
while end== True:

    y1= int(input('Enter your "Year of birth" or your "age"\n'))
    y2= int(input('Enter the "year" in which you want to know your age\n'))

    if y2-y1<=150 or (y2-2020)+y1<=150 or y1-(2020-y2)>=150:
        if y1<1000 and y1>=0:
            print("Type= age\nValue=", y1)
            print(f'Want to know the age in the year {y2}')
        if y1>=1000:
            print("Type= Year of birth\n Value=" ,y1)
    else: pass

    if y2>= 1900 and y2<= 2150 and y1>=1900 and y2>=y1 and y2>=2020:
        print(f'Your age will be {y2-y1} years old in the Year {y2}')
        call()
    elif y2>= 1900 and y2<= 2150 and y1>=1900 and y2>=y1 and y2<2020:
        print(f'Your age was {y2-y1} years old in the Year {y2}')
        call()
    elif y1>= 1900 and y1<= 2020 and y2> 2150 and y2<y1:
        print(f'It it nearly impossible to live so long but your age will be {y2-y1} years old')
        call()
    elif y1>= 0 and y1<= 150 and y2>= 2020 and y2<=2150:
        print(f'Your age will be {(y2-2020)+y1} years old in the Year {y2}')
        call()
    elif y1>150 and y1<1000 and y2>= 2020:
        print(f'You are too much old or trying random values but still your age will be {(y2-2020)+y1} years old at {y2}')
        call()
    elif y1<150 and y1>=0 and y2<= 2020 and y2>= 1900 and y1-(2020-y2)>=0:
        print(f'Your age was {y1-(2020-y2)} years old at {y2}')
        call()
    elif y1<150 and y1>=0 and y2<= 2020 and y2>= 1900 and y1-(2020-y2)<0:
        print(f'You were not present that time')
        call()
    elif y1<1900 and y1>=1000 and y2>= 2020 and y2>y1:
        print(f'You are too much old or trying random values but still your age will be {y2-y1} years old at {y2}')
        call()
    elif y2<y1:
        print('The year should be greater than your year of birth')
        call()
    elif y2>= 1900 and y2<= 2150 and y1<y2 and y2-y1<=150:
        print(f'Your age will be {y2-y1} years old at {y2}')
        call()
    elif y2>=2150 and y2<=5000 and y1>=1900 and y1<=2020 and y2>=y1:
        print(f'If you will be alive then Your age would be {y2-y1} years old at {y2}')
        call()
    elif y2>=2150 and y2<=5000 and y1<=150 and y1>=0 and y2>=y1:
        print(f'If you will be alive then Your age would be {y1+(y2-2020)} years old at {y2}')
        call()
    elif y1>2020:
        print("You are not yet born")
    else:
        print("Enter proper values")
        call()

