from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os

def say(request,x):
    s=os.path.dirname(os.path.realpath(x))
    e="templates"
    a=open('%s\\%s\\%s'%(s,e,x),'r')
    b=a.read().splitlines()
    d={}
    for item in b:
        if item not in d:
            d[item]=1
        else:
            d[item]+=1
    html= "<html><body>%s</body></html>" % d
    return HttpResponse(html)