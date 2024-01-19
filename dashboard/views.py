from django.shortcuts import render
from django.contrib.auth.decorators  import login_required
from item.models import item
# Create your views here.

@login_required
def index(request):
    items = item.objects.filter(created_by = request.user)

    return render(request, 'dashboard/index.html', {'items':items})
