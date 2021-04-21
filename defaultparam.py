## IN PYHTON NONE MEANS NOTHING KUCH HI NAHI
# ALWAYS MAKAE ALST ARGUMENT DEFAULT 

def user_info(first_name,last_name,age):
    print(f"your name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
user_info("SHAMS","TABREZ",21)

# IF WE MAKE THE LAST ARGUMENT DEFAULT THEN THIS PROGTAM WILL BE WRITE


def user_info(first_name,last_name,age = None):
    print(f"your name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
user_info("SHAMS","TABREZ")

# OR IF WE WRITE LIKE THIS


#def user_info(first_name= 'Unknown',last_name='unknown',age):
 #   print(f"your name is {first_name}")
  #  print(f"your last name is {last_name}")
   # print(f"your age is {age}")

#OR     

def user_info(first_name='unknown',last_name='unknown',age=None):
    print(f"your name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
user_info()    