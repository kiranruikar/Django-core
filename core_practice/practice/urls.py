
from django.urls import path
from .views import (
    post_model_delete_view,
    post_model_update_view,
    post_model_create_view,
    post_model_list_view,
    post_model_detail_view)


urlpatterns = [
    path('<int:id>/delete/', post_model_delete_view, name='delete'),
    path('<int:id>/update/', post_model_update_view, name='update'),
    path('create/', post_model_create_view, name='create'),
    path('', post_model_list_view , name='list'),
    path('<int:id>/', post_model_detail_view, name='detail'),

]
