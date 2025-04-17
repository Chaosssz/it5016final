score = [90, 80, 60, 40, 20]
get_score = int(input("Enter your score:...\n"))

if get_score >= score[0]:
    print("You Passed! A+...\n")
elif get_score >= score[1]:
    print("You passed! A\n")
elif get_score >= score[2]:
    print("You passed! B\n")
elif get_score >= score[3]:
    print("You passed! C\n")
elif get_score >= score[4]:
    print("You passed! D\n")
else:
    print("Indeterminate,\n")