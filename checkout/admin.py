from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'total',)

    list_display = ('order_number', 'date', 'full_name', 'total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)