from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return HttpResponse('Hello')
    
def eggs(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
    
def count(request):
    fulltext=request.GET['fulltext']
    # print(fulltext)
    
    wordlist = fulltext.split()
    wordict ={}
    for word in wordlist:
        if word in  wordict:
            wordict[word] +=1
            
        else:
            wordict[word] = 1
        
    sortedwords = sorted(wordict.items(),key=operator.itemgetter(1),reverse=True)
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),"wordict":sortedwords})