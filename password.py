import random
import string

def generate_password(length,use_uppercase,use_lowercase,use_digits,use_special):
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        print("Error: At least one of the options must be enabled.")
        return None
    
    characters=""
    c=0
    if use_uppercase:
        characters+=string.ascii_uppercase
        c=c+1
    if use_lowercase:
        characters+=string.ascii_lowercase
        c=c+1
    if use_digits:
        characters+=string.digits
        c=c+1
    if use_special:
        characters+=string.punctuation
        c=c+1
    
    result=""

    if(c==0 or length<c):
        print("can't generate password with these parameters. Please try again.")
    else:
        i=0
        while(i<c):
            if(use_uppercase):
                result+=random.choice(string.ascii_uppercase)
                i=i+1
            if(use_lowercase):
                result+=random.choice(string.ascii_lowercase)
                i=i+1
            if(use_digits):
                result+=random.choice(string.digits)
                i=i+1
            if(use_special):
                result+=random.choice(string.punctuation)
                i=i+1
        c=length-c
        
        for i in range(c):
            result += random.choice(characters)
        return result

def yes_or_no(stri):
    while True:
        choice=input(stri).strip().lower()
        if choice=='y' or choice=='yes':
            return True
        elif choice=='n' or choice=='no':
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    print("Welcome to the Random Password Generator!")
    print("Please specify the parameters for your password.")
    
    length=0
    while length<=0:
        try:
            length=int(input("Enter the length of the password: "))
            if length<=0:
                print("Length must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the length.")
    
    use_uppercase=yes_or_no("Include uppercase letters? (yes/no): ")
    use_lowercase=yes_or_no("Include lowercase letters? (yes/no): ")
    use_digits=yes_or_no("Include digits? (yes/no): ")
    use_special=yes_or_no("Include special characters? (yes/no): ")
    
    password=generate_password(length,use_uppercase,use_lowercase,use_digits,use_special)
    if password:
        print("Generated password:",password)

if __name__=="__main__":
    main()
