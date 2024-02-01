from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random/", views.get_random, name="random-page"),
    path("wiki/search/", views.search, name="search"),
    path("wiki/new/", views.new, name="new-page"),
    path("wiki/edit/", views.edit, name="edit-page"),
    path("wiki/save_edit/", views.save_edit, name="save-edit"),
    path("wiki/<str:title>/", views.entry, name="entry"),
]
