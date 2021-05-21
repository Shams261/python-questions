## FINDING THE PALINDROME OF THE NUMBER WITH THE HELP OF FUNCTION

def is_palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False
print(is_palindrome("naman"))
print(is_palindrome("shams"))   

#OR 


def palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    return False
name = input("enter the text:")
word = name
print(palindrome(word))  

# OR
def is_palindrome(word):
    return word == word[::-1]
name = input("enter the name:")
print(is_palindrome(word))
