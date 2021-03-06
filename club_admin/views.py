from django.shortcuts import render,redirect
from django.db import models
from django.db import connection
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http import HttpResponse
import requests
# Create your views here.

#@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def delete_session(request):
    
    
    try:
        
        del request.session['userid']
        del request.session['password']
        logout(request)
        return redirect(index)
    except:
        logout(request)
        return redirect(index)
#@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def index(request):
    try:
        a=request.session['userid']
        b=request.session['password']
        return render(request,'super_admin.html')
    except:

        response=requests.get('http://localhost:5000/clubnames')
        club_names=response.json()
        clubs=[]
        for i in club_names:
            clubs.append(i['clubname'])
        return render(request,'index2.html',{'club':clubs})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin(request):
    
    id=request.POST["name"]
    pword=request.POST["pword"]
    request.session['userid'] = id
    request.session['password'] = pword
    return render(request,'admin.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def super_admin(request):
    
    id=request.POST["name"]
    pword=request.POST["pword"]
    
    '''try:
        a=request.session['userid']
        b=request.session['password']
        return render(request,'super_admin.html')
    except:

        return render(request,"index.html")'''
    request.session['userid'] =id
    request.session['password']=pword
    data=(request.session.items())
    if (id in "100") &( pword in "cbit"): #static userid,password
        return render(request,"super_admin.html",{'data':data})
    else:
        return render(request,"index.html")


def adminlog(request):
    print('hello')
    club = request.GET.get("club")
    return HttpResponse("hello world")
    return render(request,'admin2.html')
