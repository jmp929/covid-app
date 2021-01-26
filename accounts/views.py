from django.shortcuts import render, redirect
from .forms import NewAccountForm


def NewAccount(response):
	if response.method == "POST":
		accountForm = NewAccountForm(response.POST)
		if accountForm.is_valid():
			accountForm.save()
			return redirect("/dashboard/National")
	else:
		accountForm = NewAccountForm()


	return render(response, "accounts/new_account.html", {"accountForm": accountForm})
