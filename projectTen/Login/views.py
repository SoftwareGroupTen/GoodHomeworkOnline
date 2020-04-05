from django.shortcuts import render,redirect
from django.contrib.projectTen import authenticate,login,logout

# Create your views here.

def page(require):
    return render(require, 'Login/home.html')

def login(require):
    if require.method == 'POST':
        user = authenticate(require,username=require.POST['username'] ,password=require.POST['password'] )
        if user is None:
            return render(require, 'Login/login.html',{'ERROR':'The username does not exit!'})
        else:
            login(require,user)
            redirect('Login:page')
    else:
        return render(require, 'Login/login.html')