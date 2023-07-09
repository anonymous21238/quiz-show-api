''' This project was made by:-
 Aakash Agarwal (2021222)
 Aryesh Shakya (2021238) 
 Siddharth Rajput (2021102)'''

import requests, json, html   
def func1(data1, n):
    c=0
    for i in range(n):
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        if data1["results"][i]['type']=='multiple':
            l=[]
            l.append(html.unescape(data1["results"][i]["correct_answer"]))
            l.extend(html.unescape(data1["results"][i]["incorrect_answers"]))
            l2=set(l)
            l1=list(l2)
            print(f'Q{i+1}) {html.unescape(data1["results"][i]["question"])}        (Press "e" to exit here)')
            for j in range(len(l1)):
                print(f'{chr(j+97)}. {l1[j]}')
            for k in l1:
                if l[0]==k:
                    if l1.index(k)==0:
                        ch='a'
                    elif l1.index(k)==1:
                        ch='b'
                    elif l1.index(k)==2:
                        ch='c'
                    elif l1.index(k)==3:
                        ch='d'
                    else:
                        print("Wrong input!!")
            ans=input("Enter your choice: ")
            if ans=='e':
                print("Your final score: ",c,"out of",n)
                print('''"Knowledge has a beginning but no end," so let's keep ourselves going.
Attempt this anytime you want.
We will miss you till then.''')
                exit()
                
            print("Correct answer is :", html.unescape(data1["results"][i]["correct_answer"]) )
            if ans==ch:
                c+=1
        else:
            print(f'Q{i+1}) {html.unescape(data1["results"][i]["question"])}        (Press "e" to exit here)')
            print("a) True\nb) False")
            ans=input("Enter your choice: ")
            if ans=='e':
                print("Your final score: ",c,"out of",n)
                print('''"Knowledge has a beginning but no end," so let's keep ourselves going.
Attempt this anytime you want.
We will miss you till then.''')

                exit()
            print("Correct answer is :", html.unescape(data1["results"][i]["correct_answer"]) )
            if ans=='a':
                ch=True
            elif ans=='b':
                ch=False
            else:
                print("Wrong input!!")
            if ch==data1["results"][i]["correct_answer"]:
                c+=1
    return c

print()
print('''"Knowledge becomes power only when we put it into some use"
So let's honour our knowledge by answering some general questions in this "Out of nowhere" quiz

Rules:

1)You get to select the number of questions you want to answer.
2)This format permits answering 5,10 and 15 questions respectively.
3)Point awarded : 1 points for each question
4)There is no negative marking for wrong answers.

Hope you enjoy this quiz!
    Happy Quizzing!''')

while True:
    print()
    print("Choose no. of questions: \n1. 5 questions\n2. 10 questions\n3. 15 questions\n4. Exit")
    try:
        choice=int(input("Enter your choice: "))
    except Exception as e:
        print("Please input integer value")
        continue
    if choice==1:
        print("5 question quiz:- ")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        resp1=requests.get("https://opentdb.com/api.php?amount=5")
        data1=json.loads(resp1.text)
        print("Your final score: ", func1(data1, 5),"out of",5)
        print('''"Knowledge has a beginning but no end," so let's keep ourselves going.
Thank you for attempting this quiz.''')
    elif choice==2:
        print("10 question quiz:- ")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        resp1=requests.get("https://opentdb.com/api.php?amount=10")
        data1=json.loads(resp1.text)
        print("Your final score: ", func1(data1, 10),"out of",10)
        print('''"Knowledge has a beginning but no end," so let's keep ourselves going.
Thank you for attempting this quiz.''')
    elif choice==3:
        print("15 question quiz:- ")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        resp1=requests.get("https://opentdb.com/api.php?amount=15")
        data1=json.loads(resp1.text)
        print("Your final score: ", func1(data1, 15),"out of",15)
        print('''"Knowledge has a beginning but no end," so let's keep ourselves going.
Thank you for attempting this quiz.''')
    elif choice==4:
        print('''"Knowledge has a beginning but no end," so let's keep ourselves going.
Attempt this anytime you want.
We will miss you till then.''')
        break
    else:
        print("Invalid input!!")