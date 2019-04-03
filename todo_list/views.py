from django.shortcuts import render,get_object_or_404
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home(request):
	if(request.method == 'POST'):
		form = ListForm(request.POST or None)
		if(form.is_valid()):
			form.save()
			all_items = List.objects.all
			messages.success(request,('ToDo item is added to the list'))
			return render(request,'home.html',{'all_items':all_items})
		else:
			all_items = List.objects.all	
			return render(request,'home.html',{'all_items':all_items})
	else:
			all_items = List.objects.all
			return render(request,'home.html',{'all_items':all_items})

def edit(request,pk):
	if(request.method == 'POST'):
		item = List.objects.get(pk=pk)
		form = ListForm(request.POST , instance=item)
		if(form.is_valid()):
			form.save()
			messages.success(request,('Item has been edited'))
			return redirect('home')
		
	else:
			item = List.objects.get(pk=pk)
			return render(request,'edit.html',{'item':item})

def delete(request,pk):
	item = get_object_or_404(List,pk=pk)
	item.delete()
	messages.success(request,('Item is deleted from the list'))
	return redirect('home')

def done(request,pk):
	item = get_object_or_404(List,pk=pk)
	item.done = True
	item.save()
	return redirect('home')

def not_done(request,pk):
	item = get_object_or_404(List,pk=pk)
	item.done = False
	item.save()
	return redirect('home')
