from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from .forms import 自定义注册表单,自定义编辑表单,自定义登录表单
from .models import 普通会员表
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='Login:登录')
def 个人中心(require):
    内容 = {'用户': require.user}
    return render(require, 'Login/user-center.html', 内容)

@login_required(login_url='Login:登录')
def 编辑个人信息(require):
    if require.method == 'POST':
        编辑表单 = 自定义编辑表单(require.POST,instance = require.user)
        if 编辑表单.is_valid():
            编辑表单.save()
            require.user.普通会员表.昵称 = 编辑表单.cleaned_data['昵称']
            require.user.普通会员表.身份 = 编辑表单.cleaned_data['身份']
            require.user.普通会员表.save()
            return redirect('Login:个人中心')
    else:
        编辑表单 = 自定义编辑表单(instance = require.user)

    内容 = {'编辑表单':编辑表单, '用户':require.user}
    return render(require, 'Login/edit-profile.html', 内容)



@login_required(login_url='Login:登录')
def 修改密码(require):
    if require.method == 'POST':
        改密表单 = PasswordChangeForm(data= require.POST,user = require.user)
        if 改密表单.is_valid():
            改密表单.save()
            return redirect('Login:登录')
    else:
        改密表单 = PasswordChangeForm(user = require.user)

    内容 = {'改密表单':改密表单, '用户':require.user}
    return render(require, 'Login/change-password.html', 内容)

def 主页(require):
    return render(require, 'Login/home.html')


def 登录(require):
    if require.method == 'POST':
        登录表单 = 自定义登录表单(data= require.POST)
        if 登录表单.is_valid():

            用户 = authenticate(require,username=登录表单.cleaned_data['username'] ,password=登录表单.cleaned_data['password'] )

            login(require,用户)
            return redirect('Login:主页')
    else:
        登录表单 = 自定义登录表单()

    内容 = {'登录表单':登录表单, '用户':require.user}
    return render(require, 'Login/login.html',内容)


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