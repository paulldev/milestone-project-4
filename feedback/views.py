from django.shortcuts import render
from .models import PoolTable
# Create your views here.

def feedback_view(request):
    pool_table_objects = PoolTable.objects.all()
    context = {
        'pool_table_objects': pool_table_objects
    }
    return render(request, "feedback/feedback.html", context)