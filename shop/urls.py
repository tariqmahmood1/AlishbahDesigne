from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update/<int:item_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),
    path('success/', views.order_success, name='order_success'),
]