from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from todo_app.forms import task_form
from todo_app.models import task_table
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic import DetailView


class task_listview(ListView):
    model = task_table
    template_name = 'index.html'
    context_object_name = 't_list'


class task_detailview(DetailView):
    model = task_table
    template_name = 'detail.html'
    context_object_name = 'task'


class task_updateview(UpdateView):
    model = task_table
    template_name = 'upadte.html'
    context_object_name = 'task'
    fields = ('t_name', 'priority', 'date')
    #success_url = '/'
    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class task_deleteview(DeleteView):
    model = task_table
    template_name = 'delete.html'
    success_url = '/'


# Create your views here.
def first_fun(request):
    t_list = task_table.objects.all()
    if request.method == 'POST':
        t_name = request.POST.get('t_name', )
        priority = request.POST.get('priority', )
        date = request.POST.get('date', )
        if t_name == "" or priority == "" or date == "":
            return render(request, 'index.html', {'message': "Please Fill The Fields",
                                                  't_list': t_list})
        else:
            task = task_table(t_name=t_name, priority=priority, date=date)
            task.save()
    return render(request, 'index.html', {'t_list': t_list})


def delete(request, id):
    if request.method == "POST":
        movie = task_table.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, id):
    task = task_table.objects.get(id=id)
    form = task_form(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'task': task})
