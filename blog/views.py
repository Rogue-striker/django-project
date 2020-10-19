from django.shortcuts import render
from django.shortcuts import HttpResponse , HttpResponseRedirect
from .models import todolist
def indexpage(request):
    all_items = todolist.objects.all()
    return render(request,'index.html' 
    ,{'allitemslist':all_items})
def additem(request):
    context = request.POST['content']
    todolist(content = context).save()
    return HttpResponseRedirect('/views/')
def deleteitem(request,todo_id):
    item_to_be_deleted = todolist.objects.get(todo_id)
    item_to_be_deleted.delete()
    return HttpResponseRedirect('/views/')