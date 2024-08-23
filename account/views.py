from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from .forms import AccountForm

def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'account/list.html', {'accounts': accounts})

def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'account/form.html', {'form': form})

def account_update(request, id):
    account = get_object_or_404(Account, id=id)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)
    return render(request, 'account/form.html', {'form': form})

def account_delete(request, id):
    account = get_object_or_404(Account, id=id)
    if request.method == 'POST':
        account.delete()
        return redirect('account_list')
    return render(request, 'account/confirm_delete.html', {'account': account})

def account_details(request, id):
    account = get_object_or_404(Account, id=id)
    return render(request, 'account/details.html', {'account': account})
