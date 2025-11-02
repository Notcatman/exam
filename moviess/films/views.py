from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def films(request):
    context = [
        {'title':'The Joker', 'rating': '7.3'},
        {'title':'Batman', 'rating': '7.5'},
        {'title':'Superman', 'rating': '7.9'}
    
    ]
    return render(request, 'films.html', {"context": context})