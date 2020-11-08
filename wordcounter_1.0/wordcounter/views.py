from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def count(request):
    text = request.GET['filltext']

    totalwords = text.split()

    wordsdictionary = {}

    for word in totalwords:
        if word in wordsdictionary:
            wordsdictionary[word] += 1
        else:
            wordsdictionary[word] = 1
    
    finaldict = sorted(wordsdictionary.items(), key = operator.itemgetter(1) , reverse=True)

    return render(request, 'count.html', {'text': text, 'wordlength': len(totalwords), 'worddict': finaldict})

def about(request):
    return HttpResponse('About')