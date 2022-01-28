# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Define the alphabetss
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    final_text = ""

    # This condition encrypts the message
    if direction == "encode":
        for letter in text:
            position = alphabets.index(letter)
            
            new_position = position + shift
            
            final_text += alphabets[new_position]
        
        print(f"The encoded text is: {final_text}")

    # This condition decrypts the message
    elif direction == "decode":
        for letter in text:
            position = alphabets.index(letter)
            
            new_position = position - shift
            
            final_text += alphabets[new_position]
        
        print(f"The decoded text is: {final_text}")

    else:
        print("Sorry, this function is not available. Maybe you made an Typo!")

# Print the logo from art.py
from art import logo
print(logo)

# To loop again
should_end = False
while not should_end:
    # Get the inputs from the user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    #If the user enters a shift that is greater than the number of letters in the alphabet
    shift = shift % 26

    caesar(text = text, shift = shift, direction = direction)

    restart = input("Type 'yes' or 'no' to run again or not:\n")
    
    if restart == "no":
        should_end = True
        print("Thank you for using Caesar Cipher!")