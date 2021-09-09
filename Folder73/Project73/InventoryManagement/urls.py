from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.addProductView,name='add-product'),
    path('show/',views.showProductsView,name='show-products'),
    path('update/<int:id>',views.updateProductView,name='update'),
    path('delete/<int:id>',views.deleteProductView,name='delete')
]