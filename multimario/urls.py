from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path("upcomingraces", views.upcomingraces),
    path("glossary", views.glossary, name="glossary")
    #path("create/", views.create, name="create"),
]