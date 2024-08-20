from django.shortcuts import redirect, render
from .models import TodoItem


# Create your views here.


def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todo_items': todo_items})


def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Use .get() to avoid KeyError
        if title:  # Check if title is not None or empty
            TodoItem.objects.create(title=title)
            return redirect('todo_list')
        else:
            return render(request, 'todo/add_todo.html', {'error': 'You must enter a title to add an item'})
    return render(request, 'todo/add_todo.html')


def mark_completed(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')


def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
