from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators  import login_required
from .models import item, category
#from django.http import HttpResponsePermanentRedirect
from .forms import NewItem, EditItem
from django.db.models import  Q
from django.contrib import messages

# Create your views here.

def items(request):
    items = item.objects.filter(is_sold = False)
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = category.objects.all()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_id:
        items = items.filter(category_id = category_id)

    return render(request, 'items/items.html', 
    {'items':items,
    'query':query,
    'categories':categories,
    'category_id':int(category_id)
    })

def details(request, pk):
    items = item.objects.get(id=pk)
    related_item = item.objects.filter(category = items.category, is_sold=False).exclude(id=pk)[0:3]
    
    
    return render(request, 'items/detail.html',{'item':items, 'related_item':related_item})
    #return HttpResponsePermanentRedirect(request, 'items/detail.html',{'item':items, 'related_item':related_item})

@login_required
def new(request):
    title = 'New'
    if request.method == 'POST':
        form = NewItem(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, "the item has been created successfuly")

        return redirect('item:detail', pk=item.id)
    else:
        form = NewItem()
    
    return render(request, 'items/form.html', {'form':form, 'title':title})

@login_required
def edit(request, pk):
    items = get_object_or_404(item, pk=pk, created_by = request.user)
    if request.method == 'POST':
        form = EditItem(request.POST, request.FILES, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, "the item has been updated successfuly")

        

        return redirect('item:detail', pk=items.id)
    else:
        form = EditItem(instance=items)
    title = 'Edit'
    return render(request, 'items/form.html', {'form':form, 'title':title})

@login_required
def delete(request, pk):
    items = get_object_or_404(item, pk=pk, created_by = request.user)
    items.delete()
    messages.success(request, "the item has been deleted successfuly")
    return redirect('dashboard:index')