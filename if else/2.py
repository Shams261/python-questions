#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.

#if employee is a male and age is in between 20 to 40 then he may work in anywhere

#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

#And any other input of age should print "ERROR".


#age = int(input("enter the age:"))
#sex = eval(input("sex ? M or F:"))
#marital_status = eval(input("married? Y or N"))

#if sex is F:
#    print("work only in urban areas")
#
#if sex is M and 20<age<40:
#    print("work in antwhere")



#if sex is M and 40<age<60:
#    print("work in urban")


print ("Enter age")
age = input()
print ("SEX? (M or F)")
sex = input()
print ("MARRIED? (Y or N)")
marry = input()
if sex == "F" and age>=20 and age<=60:
  print ("Urban areas only")
elif sex == "M" and age>=20 and age<=40:
  print ("You can work anywhere")
elif sex == "M" and 40<age<60:
  print ("Urban areas only")
else:
  print ("ERROR")