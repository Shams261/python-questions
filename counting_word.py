# WORD COUNTER IN DICT
## COUNT THE WORD OF YOUR NAME 
# EX: "SHAMS" = {'S':2,'H':1,A:'1','M':1}

def word_count(n):
    count = {}
    for char in n:
        count[char] = n.count(char)
    return count
name = input("enter your name:") 
print(word_count(name))       