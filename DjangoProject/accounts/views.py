from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# view for signup form, if successfull logs in and redirects to articles
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form':form})

# view for login form, if successfull logs in and redirects to articles
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles:list') 
    else:
        form = AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form})

# method for logout if 
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')