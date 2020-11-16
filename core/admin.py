from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from core.models import Product,Flavour,Order,OrderItem

admin.site.site_header = 'Baskotii Admin'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Baskotii'

class InLineFlavour(admin.TabularInline):
    model = Flavour
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [InLineFlavour]
    search_fields = ('name',)

class InLineOrderItem(admin.TabularInline):
    model = OrderItem
    extra = 3

class OrderAdmin(admin.ModelAdmin):
    inlines = [InLineOrderItem]
    exclude = ['confirmation_sent']

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
