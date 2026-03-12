from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo

# def index(request):
#     return HttpResponse("Hello, world! This is the index page of my_tobo_app.")

def index(request):
    #로직 처리 구현
    todos = Todo.objects.all()
    print("DB: ", todos)
    content={'todos': todos }
    return render(request, 'todo_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    print(f"Received user input: {user_input_str}")
    #DB에 저장
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    delete_tobo_id = request.GET['todoNum']
    print('삭제한 todo id: ', delete_tobo_id)
    todo = Todo.objects.get(id=delete_tobo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

def editTodo(request):
    edit_tobo_id = request.POST['todoNum']
    edit_tobo_content = request.POST['todoContent']
    print('수정한 todo id: ', edit_tobo_id)
    todo = Todo.objects.get(id=edit_tobo_id)
    todo.content = edit_tobo_content
    todo.save()
    return HttpResponseRedirect(reverse('index'))