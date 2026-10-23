from django.shortcuts import render,redirect,get_object_or_404
from.models import Project,Skill,Experience,Education,ContactMesssage
from.forms import ContactForm
# Create your views here.

def home(request):
    project=Project.objects.filter(is_featured=True)
    # project=Project.objects.all()
    return render(request,'home.html',{'project':project})



def about(request):
    abouts = Experience.objects.all()
    abouts1 = Education.objects.all()

    return render(request, 'about.html', {
        'abouts': abouts,
        'abouts1': abouts1,
    })



def skills(request):
    skills=Skill.objects.all()
    return render(request,'skills.html',{'skills':skills})


def projects(request):
    projects=Project.objects.all()
    return render(request,'projects.html',{'projects':projects})


def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ContactForm()        
    return render(request,'contact.html',{'form':form})


def project_detail(request,id):
    detail=get_object_or_404(Project,id=id)
    return render(request,'project_detail.html',
                  {'detail':detail})

