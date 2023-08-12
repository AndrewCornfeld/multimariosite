from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path("", index),
    path("logout", index),
    path("upcomingraces", index),
    path("glossary", index)
    #path("create/", views.create, name="create"),
]

"""urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path("upcomingraces", views.upcomingraces),
    path("glossary", views.glossary, name="glossary")
    #path("create/", views.create, name="create"),
]"""