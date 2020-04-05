from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import 自定义注册表单
from .models import 普通会员表

# Create your views here.

def 主页(require):
    return render(require, 'Login/home.html')

def 登录(require):
    if require.method == 'POST':
        用户 = authenticate(require,username=require.POST['用户名'] ,password=require.POST['密码'] )
        if 用户 is None:
            return render(require, 'Login/login.html',{'错误':'该用户名不存在或密码错误!'})
        else:
            login(require,用户)
            return redirect('Login:主页')
    else:
        return render(require, 'Login/login.html')


def 登出(require):
    logout(require)
    return redirect('Login:主页')


def 注册(require):
    if require.method == 'POST':
        注册表单 = 自定义注册表单(require.POST)
        if 注册表单.is_valid():
            注册表单.save()
            用户 = authenticate(username=注册表单.cleaned_data['username'] ,password=注册表单.cleaned_data['password1'] )
            用户.email = 注册表单.cleaned_data['email']
            普通会员表(用户=用户,昵称=注册表单.cleaned_data['昵称'],身份=注册表单.cleaned_data['身份']).save()
            login(require,用户)
            return redirect('Login:主页')
    else:
        注册表单 = 自定义注册表单()

    内容 = {'注册表单':注册表单}
    return render(require, 'Login/register.html', 内容)