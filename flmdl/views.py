import random
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

list = ["Abyss", "Alfie", "Alien", "Alive", "Angel", "Annie", "Anzio", "Ariel", "Babel", "Bambi", "Bobby", "Bugsy", "Cobra", "Crash", "Digby", "Doubt", "Dumbo", "Earth", "Equus", "Evita", "Fargo", "Freud", "Ghost", "Giant", "Gilda", "Greed", "Gypsy", "Heidi", "Hotel", "Julia", "Kipps", "Kitty", "Klute", "Kotch", "Laura", "Mammy", "Mandy", "Marty", "Otley", "Pinky", "Prime", "Rambo", "Rocky", "Sally", "Shaft", "Shane", "Shine", "Shrek", "Sleep", "Tommy", "Twins", "Wings", "Yanks", "Yentl", "Zelig"]

word = random.choice(list)

def analyze(request):

    # Get the text
    text = word.lower()
    print(word)
    djtext = request.POST.get('text', 'default')
    analyzed=djtext.lower()
    arr = ["","","","",""]
    color = ["","","","",""]
    if(len(djtext)!=5):
        message = "danger"
        message_text = "Error! Word must be 5 alphabets long"
        color[0] = "secondary"
        color[1] = "secondary"
        color[2] = "secondary"
        color[3] = "secondary"
        color[4] = "secondary"
        params = {'a': arr[0], 'b': arr[1], 'c': arr[2], 'd': arr[3], 'e': arr[4], 'msg': message, 'c1': color[0], 'c2': color[1], 'c3': color[2], 'c4': color[3], 'c5': color[4], 'msg_text': message_text}
        return render(request,'index.html',params)
    else:
        if(djtext!=text):
            message = "warning"
            message_text = "Incorrect word. Please try again by seeing hints in the colored boxes"
        else:
            message = "success"
            message_text = "Success! You have guessed the correct word. Reload to page to try again with a new word"
        for i in range(5):
            if(djtext[i]==text[i]):
                color[i] = "success"
            elif ((djtext[i]==text[0] or djtext[i]==text[1] or djtext[i]==text[2] or djtext[i]==text[3]) or djtext[i]==text[4] and djtext[i]!=text[i]):
                color[i] = "dark"
            else:
                color[i] = "secondary"

            arr[i] = analyzed[i]
        params = {'a': arr[0], 'b': arr[1], 'c': arr[2], 'd': arr[3], 'e': arr[4], 'msg': message, 'c1': color[0], 'c2': color[1], 'c3': color[2], 'c4': color[3], 'c5': color[4], 'msg_text': message_text}
        return render(request,'index.html',params)