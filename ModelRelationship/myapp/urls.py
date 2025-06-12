from django.urls import path
from myapp.views import home, show_user_data, show_page_data, show_post_data, show_song_data

urlpatterns = [
    path('', home, name='home'),
    path('user/', show_user_data, name='user'),
    path('page/', show_page_data, name='page'),
    path('post/', show_post_data, name='post'),
    path('song/', show_song_data, name='song'),
]
