from django.shortcuts import render, HttpResponse
from .models import PoolTable, Review
from .forms import TableForm, ReviewForm
from django.http import HttpResponseRedirect

# Create your views here.


def feedback_view(request):
    if request.method == 'POST':
        table_form = TableForm(request.POST)
        review_form = ReviewForm(request.POST)
        
        if table_form.is_valid() and review_form.is_valid():
            table_form.save()
            review_form.save()
            return HttpResponseRedirect('feedback_received') #redirect after POST       
        else:
            context = {
                'table_form': table_form,
                'review_form': review_form,
            }
    else:
        context = {
            'table_form': TableForm(),
            'review_form': ReviewForm(),
        }
    return render(request, "feedback/feedback.html", context)


def feedback_received(request):
    template = 'feedback/feedback_received.html'
    context = {
        
    }

    return render(request, template, context)