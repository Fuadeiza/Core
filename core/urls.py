from django.urls import path
from core import views

app_name="core"

urlpatterns = [
    path('',views.index,name = 'index'),
    path('search/',views.search,name = 'search'),
    path('search/ajax/',views.search_ajax,name = 'search_ajax'),

    path('select-area',views.select_area,name="select_area"),

    path('product/<int:pk>/',views.product,name = 'product'),
    path('product/<int:pk>/<int:fpk>/',views.flavour,name = 'flavour'),

    path('order/',views.order,name = 'order'),

    path('order/track/',views.track,name = 'track'),
    path('order/track/ajax/',views.track_ajax,name = 'track_ajax'),

    path('checkout/contact/',views.contact,name = 'contact'),
    path('checkout/confirm/',views.confirm,name = 'confirm'),
    path('checkout/thankyou/<int:id>',views.thankyou,name = 'thankyou'),
]