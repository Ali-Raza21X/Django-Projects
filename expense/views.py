from django.shortcuts import render,redirect,get_object_or_404
from.models import Expense
from. forms import ExpenseForm


# Create your views here.
def home(request):
    exp=Expense.objects.all()

    return render(request,'home.html',{"expenses":exp})

def add_exp(request):
    if request.method=="POST":
        form=ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ExpenseForm()
    return render(request,'add_exp.html',{'form':form})
    
def delete_exp(request, id):
    exp = Expense.objects.get(id=id)

    if request.method == "POST":
        exp.delete()
        return redirect('home')

    return render(request, 'delete.html', {'exp': exp})



   
    
def update_exp(request,id):
    exp=Expense.objects.get(id=id)
    if request.method=="POST":
        form=ExpenseForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ExpenseForm(instance=exp)
        
    return render(request, 'update.html', {'form': form})

