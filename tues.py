user_score = int(input("what is your score?"))
if user_score >=70 and user_score <=100 :
    print("you had an A")
elif user_score>=60 and user_score<=69:
    print("you had a B")
elif user_score>=50 and user_score<=59:
    print("you had a C")
elif user_score>=45 and user_score<=49:
    print("you had a D")
elif user_score>=40 and user_score<=44:
    print("you had an E")
elif user_score>=0 and user_score<=39:
    print("you had a F")
else:
    print("invalid score")