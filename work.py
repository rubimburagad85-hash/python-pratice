# Online Exam 
Registered = input("are you registered for exam(yes/no):")
school_fee = input("are you Tution Paid Aready?:):(yes/no:")
if Registered == "yes"and school_fee =="yes":
    print("you're cleared")
elif Registered == "yes" and school_fee =="no":
    print("you not allowed into exam")
else:
    print("you are not allowed to come to school")        



# # Choice
Number =float(input("Enter the number of your choice:"))
if Number > 0 :
 print("the number is positive!")
elif Number < 0:
 print("the number is negative!")
else:
 print("the number is neutral")
    

    # Grading System Simulation

score= float(input("Enter the Your Score:"))
if score >= 80:
 print("This grade is A")
elif score >= 70:
 print("This is Grade B")
elif score >=60:
  print("This is Grade C")
elif score >=50:
 print("This Grade D")
else:
 print("You have failed")

# example to calculate increment in salary

salary= float(input("Enter the salary:"))
experience =int(input("Enter the experience"))

if experience>=10:
   new_salary=salary+0.5*salary
   print(f"your new salary is salary is {new_salary}rwf")
elif experience>=5:
    new_salary =salary+ 0.2*salary
    print(f"your new salaray is {new_salary}rwf")
else:
   print(f"your salary is {salary}rwf")


    

