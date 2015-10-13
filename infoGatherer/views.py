from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context import RequestContext

# Create your views here.
def index(request):
    return HttpResponse("Welcome")

def user_login(request):
    username = ''
    password = ''
    state = 'Please Log In'
    status_code = 0
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                status_code = 1
                state = 'You have successfully Logged In'
            else:
                state = 'Your account has been deactivated'
        else:
            state = 'Invalid Login Details'
      
    return render_to_response('login.html',{'state':state,'status_code':status_code,'username':username},context_instance=RequestContext(request))    

def user_logout(request):
    logout(request)
    state = 'You have successfully Logged Out'
    return render_to_response('login.html',{'state':state})