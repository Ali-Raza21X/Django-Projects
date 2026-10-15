from django.shortcuts import render, redirect,get_object_or_404

from .models import Task
from .forms import TaskForm



# Create your views here.

def home(request):
    tasks=Task.objects.all()
    context={
        'tasks':tasks
    }



    return render(request,'home.html',context)

 
def create_tasks(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})


def update_tasks(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method == "POST":
           form = TaskForm(request.POST,instance=task)
   
           if form.is_valid():
               form.save()
               return redirect('home')
    else:
           form = TaskForm(instance=task)
   
    return render(request, 'update.html', {'form': form})


def delete_tasks(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.delete()
        return redirect('home')

    return render(request, 'delete.html', {'task': task})

