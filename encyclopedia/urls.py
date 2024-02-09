from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entry, name='entry'),
    path('search/', views.search, name = 'search'),
    path('create/', views.create_page, name = 'create'),
    path('random/', views.random_page, name = 'random'),
    path('edit/', views.edit, name= 'edit'),
    path('save_edit/', views.save_edit, name= 'save_edit')
]
