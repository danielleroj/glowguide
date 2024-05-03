from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('routines/', views.routines_index, name='index'),
    path('routines/<int:routine_id>/', views.routines_detail, name='detail'),
    path('routines/create', views.RoutineCreate.as_view(), name='routines_create'),
    path('routines/<int:pk>/update/', views.RoutineUpdate.as_view(), name='routines_update'),
    path('routines/<int:pk>/delete/', views.RoutineDelete.as_view(), name='routines_delete'),
    path('routines/<int:routine_id>/assoc_product/<int:product_id>/', views.assoc_product, name='assoc_product'),
    path('routines/<int:routine_id>/unassoc_product/<int:product_id>/', views.unassoc_product, name='unassoc_product'),
    path('products/', views.ProductList.as_view(), name='product_index'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='products_detail'),
    path('products/create/', views.ProductCreate.as_view(), name='products_create'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('products/<int:product_id>/add_photo/', views.add_photo, name='add_photo'),
    path('products/<int:product_id>/add_photo/', views.add_photo, name='add_photo'),
    path('skin-quiz/', views.skin_type_quiz, name='skin_quiz'),
    path('results/', views.skin_type_results, name='skin_type_results'),
    path('account/', views.account, name='account'),
]