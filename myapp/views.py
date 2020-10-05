from django.shortcuts import render
from .forms import CustomForm

# Create your views here.

def customForm(request):
    if request.method == "POST":
        pass
    else: 
        form=CustomForm()
        return render(request, 'custom-form.html', {'form':form})