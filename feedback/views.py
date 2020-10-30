from django.shortcuts import render, HttpResponse
from .models import PoolTable, Review
from .forms import TableForm, ReviewForm

# Create your views here.


def feedback_view(request):
    if request.method == 'POST':
        table_form = TableForm(request.POST)
        review_form = ReviewForm(request.POST)

        if table_form.is_valid() and review_form.is_valid():
            table_form.save()
            review_form.save()
            return HttpResponseRedirect('/success')        
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