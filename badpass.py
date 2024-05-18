#!/usr/bin/bash/env python3

import hashlib

def check_word_in_list():
    # Load the hashes from the rockyou.txt file
    with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') as file:
        word_list = file.readlines()

    user_input = input("Enter a password: ")

    # Calculate the hash of the user input
    hashed_input = hashlib.sha1(user_input.encode()).hexdigest()

   # Remove newline characters from each word in the list and hash each word
    hashed_word_list = [hashlib.sha1(word.strip().encode()).hexdigest() for word in word_list]

    if hashed_input in hashed_word_list:
        print(f"The hash of '{user_input}' is in the word list.")
    else:
        print(f"The hash of '{user_input}' is not in the word list.")

# Example usage
if __name__ == "__main__":
    check_word_in_list()
