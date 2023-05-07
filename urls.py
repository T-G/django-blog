from django.urls import path
from . import views

# Define application namespace
app_name = 'blog'
urlpatterns = [
    # post view
    #path('', views.post_list, name='post_list'),

    path('', views.PostListView.as_view(), name='post_list'),

    # capture the string variable 'id' and convert it to integer
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),

]