from django.shortcuts import render,redirect,get_object_or_404
from.models import Contact
from .forms import ContactForm
# Create your views here.

def home(request):
    contacts=Contact.objects.all()
    return render(request,'contacts/contact.html',{'contacts':contacts})

def create_contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form=ContactForm()
    return render(request,'contacts/contact_form.html',{'form':form})

def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/contact_form.html', {'form': form})

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')

    return redirect('contact_list')
   
def detail_contact(request,id):
    contact=get_object_or_404(Contact,id=id)
    return render(request,'contacts/contact_detail.html',{'contact':contact})

