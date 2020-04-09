from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Todo
# Create your views here.

def index(request):
  todos = Todo.objects.all()
  return render(request, "index.html",{"todos":todos})

def addTodo(request):
  if request.method == "GET":
    #bir get request olduğu zaman tekrardan anasayfaya gelmek istiyoruz
    return redirect("/")
  else:
    #asıl olayımız burda post kısmı formdan gelen bilgileri name parametresiyle alalım
    title = request.POST.get("title")
    newTodo = Todo(title = title,completed = False) #yeni eklediğim todo her zaman false olacak
    
    newTodo.save()
    return redirect("/")

def updateTodo(request,id):
  todo = get_object_or_404(Todo, id = id)
  todo.completed = not todo.completed

  #veritabanına gönderelim
  todo.save()
  return redirect("/")

def deleteTodo(request,id):
  todo= get_object_or_404(Todo, id = id)
  todo.delete()

  return redirect("/")