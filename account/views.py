from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
# Create your views here.

# def login_view(request):
#     if request.method =='POST':
#         form=AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username=form.cleaned_data.get("username")
#             password=form.cleaned_data.get("password")
#             user = authenticate(request=request, username=username,password=password)
#             if user is not None:
#                 login(request, user)
#         return redirect("recommend")
#     else:
#         form = AuthenticationForm()
#         return render(request,'login.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('recommend')
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
    else:
        return render(request, "login.html")