from django import forms
from django.shortcuts import render


class MyForm(forms.Form):
    foo = forms.CharField()


def base(request):
    form = MyForm()

    return render(request, 'base.html', {'form': form})
