from django.urls import path

from bulletins.views import *


urlpatterns = [
    path("bulletins/", BulletinListView.as_view(), name="bulletin_list"),
    path("bulletins/create/", BulletinCreateView.as_view(), name="bulletin_create"),
    path("bulletins/<int:pk>/update", BulletinUpdateView.as_view(), name="bulletin_update"),
    path("bulletins/<int:pk>/delete/", BulletinDeleteView.as_view(), name="bulletin_delete"),
]