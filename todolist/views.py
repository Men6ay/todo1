from django.shortcuts import render, redirect
from .models import Todo
from django.db.models import Q

def index(request):
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        todos = Todo.objects.filter(Q(title__icontains=key))
    else:
        todos = Todo.objects.all()
    return render(request, 'todolist/index.html', {'todos' : todos})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        todo_obj = Todo.objects.create(title=title)
        return redirect('index')
    return render(request, 'todolist/index.html')

def delete(request, id):
    if request.method == 'POST':
        todo_obj = Todo.objects.get(id = id)
        todo_obj.delete()
        return redirect('index')
    return render(request, 'todolist/index.html')

def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        todo_obj = Todo.objects.get(id = id)
        todo_obj.title = title
        todo_obj.save()
        return redirect('index')
    return render(request, 'todolist/update.html')



