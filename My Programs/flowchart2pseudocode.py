#LearningPythonFlowchart/PsuedoCode into > Code.
#27/02/25/7:35pm
#@author zj
#defining score as int(input("zj...\n")) [REMINDER = correct SYNTAX is no dots.]
score = int(input("Enter Your Marks :...\n"))
#check the score, argument sets limit as 0 & 100 the ':' Denotes indentation of the line below.
#INDENTATION - required to tell the computer to run the line below before
if score < 0 or score > 100:
    print("invalid range, please enter integer between 0 and 100...")
else: #proceed with other checks.
    #Check for grades
    if score >= 80:
        print("You passed, A!")
    elif score >= 60:
        print("You passed, B!")
#if score is '>=50 :' then print c : denotes new line printing c
    elif score >= 50:
       print(" C.")
#else if the score is < 50 print("you fail)
    elif score < 50:
        print("You Failed!")
    else:
        print("end!")





