# from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlst = fulltext.split()
    worddct = dict()
    for word in wordlst:
        if word not in worddct:
            worddct[word] = 1
        else:
            worddct[word] += 1
    sorted_words = sorted(worddct.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlst), 'sorted_words': sorted_words})

def about(request):
    return render(request, 'about.html')
