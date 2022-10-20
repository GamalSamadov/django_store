from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='store.home'),
    path('product/<int:pid>', views.product, name='store.product'),
    path('category/<int:cid>', views.category, name='store.category'),
    path('category', views.category, name='store.category'),
    path('cart', views.cart, name='store.cart'),
    path('checkout', views.checkout, name='store.checkout'),
    path('checkout/complate', views.checkout_complate,
         name='store.checkout_complate'),
]
