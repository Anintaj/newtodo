from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class detailviewlist(DetailView):
    model=Task
    template_name="detail.html"
    context_object_name='t'

class TasklistView(ListView):
    model=Task
    template_name="home.html"
    context_object_name='ta'

class taskupdateview(UpdateView):
    model=Task
    template_name="update.html"
    context_object_name='tas'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model=Task
    template_name="delete.html"
    context_object_name='t'



# Create your views here.
def task(request):
    taask=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date','')
        tas=Task(name=name,priority=priority,date=date)
        tas.save()
    return render(request,"home.html",{'ta':taask})
def delete(request,taskid):
    ta=Task.objects.all()
    if request.method =='POST':
        ta.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    tas=Task.objects.get(id=id)
    f=Todoform(request. POST or None, instance=tas)
    if f.is_valid():
        f.save()
        return redirect ('/')
    return render(request,"edit.html",{'f':f,'task':tas})