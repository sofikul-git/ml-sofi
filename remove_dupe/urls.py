from django.urls import path
from remove_dupe import views

urlpatterns = [
    #path('',views.index_page),
    path('rem_dupe', views.dupe_remove),
]