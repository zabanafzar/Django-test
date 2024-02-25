from django.shortcuts import render,redirect
from account.models import Account
from django.contrib.auth import logout


# Create your views here.
def home_screen_view(request):
    context={}

#selects all database objects for account
    accounts=Account.objects.all()
    context['accounts']=accounts

    print(accounts)
    
    # return render(request, "base.html", {})
    return render(request, "personal/home.html", {})
