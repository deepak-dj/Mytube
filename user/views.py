from django.shortcuts import render,redirect,reverse
from .forms import user_form,profile_form,register_form
from django.http import HttpResponse



def register_view(request):
    if request.method=='POST':
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form = register_form()
        return render(request,'user/register.html',{"form":form})




def profile_view(request):
    if request.method=='POST':
        u_form = user_form(request.POST,instance=request.user)
        p_form = profile_form(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('profile')
        else:
            return HttpResponse('invalid input')
    else:
        context={
            'u_form':user_form(instance=request.user),
            'p_form':profile_form(instance=request.user.profile)
        }
        return render(request,'user/profile.html',context=context)


