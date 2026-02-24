# def greet():
#     print("Hello")    
#     print("How are you")    
#     print("Long time no see")

# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")    
#     print(f"How are you, {name}")    
#     print(f"Long time no see, {name}")

# greet_with_name("Fatima")

# import math
# years = 90
# age = int(input("How old are you? \n"))
# years_left = years - age
# def life_in_weeks(age):
#     print(f"You have {years_left*52} weeks left\n")

# life_in_weeks(age)



# a = 1
# b = 2
# c = 3

# def my_function(a,b,c):
#     print(a+b+c)
# my_function(a,b,c)



# def greet_with_name(name):
#     print(f"Hello {name}")    
#     print(f"How are you, {name}")    
#     print(f"Long time no see, {name}")

# greet_with_name(name = "Fatima")



# name_1 = input("Write your name:\n").lower()
# name_2 = input("Write second name:\n").lower()
# love = ['l','o','v','e']
# true = ['t','r','u','e']
# count_general = 0
# def calculate_love_in_name(name, counts):
#     count = 0
#     for letter in name:
#         if letter in love:
#            count += 1
#         else:
#             continue
#     counts += count

# def calculate_true_in_name(name, counts):
#     count = 0
#     for letter in name:
#         if letter in true:
#            count += 1
#         else:
#             continue
#     counts += count


# def calculate_love_score(name_1,name_2, count_general):
#     calculate_love_in_name(name_1, count_general)
#     calculate_love_in_name(name_2, count_general)
#     calculate_true_in_name(name_1, count_general)
#     calculate_true_in_name(name_2,count_general)
#     print(count_general)
    

            
# calculate_love_score(name_1, name_2, count_general)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(original_text, shift_amount):
    new_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            new_text += alphabet[shifted_position]
        else:
            new_text += letter
        
    print(new_text)


def decrypt(text, shift_amount):
    new_text = ""
    for letter in text:
        if letter in alphabet:
            new_text += alphabet[(alphabet.index(letter) - shift_amount)]
        else:
            new_text += letter
    print(new_text)


def ceaser(original_text, shift_amount, direction):
    if direction == "encrypt":
        encrypt(original_text, shift_amount)   
    elif direction == "decrypt":
        decrypt(original_text, shift_amount)       
    else:
        print("Try again!")
choice = input("Do you want to continue:(yes or no) \n").lower()

while choice == "yes":
    original_text = input("Write your message:\n").lower()
    direction = input("Write 'encrypt' or 'decrypt':\n").lower()
    shift_amount = int(input("Write your shift amount: \n"))
    ceaser(original_text, shift_amount, direction)
    choice = input("Do you want to continue:(yes or no) \n").lower()








