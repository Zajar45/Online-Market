from django.shortcuts import render, get_object_or_404, redirect
from item.models import item
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def new_conversation(request, item_pk):
    items = get_object_or_404(item, pk=item_pk)
    conversation = Conversation.objects.filter(item = items).filter(members__in=[request.user.id])
    
    if conversation:
        return redirect('Conversation:detail', pk=conversation.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item = items)
            conversation.members.add(request.user)
            conversation.members.add(items.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            form.save()
            messages.success(request, "your message has been sent successfuly..")

            return redirect('item:detail', pk=item_pk)
        
    else:
        form = ConversationMessageForm()
        
    return render(request, 'conversation/new.html', {'form':form, 'item':items})

@login_required
def inbox(request):
    conversation = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {'conversations':conversation})


@login_required
def details(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.created_by = request.user
            conversation_message.conversation = conversation
            conversation_message.save()
            
            conversation.save()
            
            return redirect('Conversation:detail', pk=pk)
            
    form = ConversationMessageForm()
    
    
    return render(request, 'conversation/details.html', {'conversation':conversation, 'form':form})
    



