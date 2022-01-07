from django.shortcuts import render
import random
import pyperclip as pc # importing the library for copying sting to clipboard

def home(request):
    return render(request, 'generator/home.html')

def generate_password(request):
    return render(request, 'generator/generate_password.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?><:;'))

    length = int(request.GET.get("length"))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

        # copying text to clipboard
        pc.copy(thepassword)

        # pasting the text from clipboard
        thepassword_copied = pc.paste()

    return render(request, 'generator/password.html', {
                "password":thepassword,
                "thepassword_copied": thepassword_copied
            })