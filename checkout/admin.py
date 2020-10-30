from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'total', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)