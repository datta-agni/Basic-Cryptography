# Python Program for Reverse Cipher
plain_txt = input("Please enter plain text : ")

cipher_txt = ''

for i in plain_txt:
    cipher_txt = i + cipher_txt
    

print("The cipher text = ", cipher_txt)