from django.shortcuts import render,redirect
from .form import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # form.save(force_insert=False)
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to Log In.')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'user/register.html',{'form':form})
