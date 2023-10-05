from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def encryptWord(plaintext, shift):
    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

def encrypt(request):
    if request.method == "POST":
        url_value = request.POST.get("url")
        print(url_value)
        
        shift_value = request.POST.get("shift", 0)  
        
        try:
            shift_value = int(shift_value)
        except ValueError:
            print("Shift value is not a valid integer.")

        data = encryptWord(url_value, shift_value)
        print(data)
        return render(request, "encrypt.html", {"data": data})

    return render(request, "encrypt.html")


def decryptWord(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:

        if char.isalpha():

            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))

            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

def decrypt(request):
    if request.method == "POST":
        url_value = request.POST.get("url")
        print(url_value)
        
        shift_value = request.POST.get("shift", 0) 
        
        try:
            shift_value = int(shift_value)
        except ValueError:
            print("Shift value is not a valid integer.")

        data = decryptWord(url_value, shift_value)
        print(data)
        return render(request, "decrypt.html", {"data": data})

    return render(request, "decrypt.html")
