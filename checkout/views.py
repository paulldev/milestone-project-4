from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You haven't ordered anything yet.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HgZsDANqxLd0au22EpGRpjdTtumRvkYzBrgEzayerMn6v4TBRYOHIYAV6a9NCRFgGboOXtOp0os85YGfturFKWq008hviwjBp',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)