from django.urls import path
from myapp.views import myfunview1, myfunview2, homefunview, aboutfunview, newsfunview, contactfunview

urlpatterns = [
    path('fun1/', myfunview1, name='myfunview1'),
    path('fun2/', myfunview2, name='myfunview2'),
    path('homefun/', homefunview, name='home_fun_view'),
    path('aboutfun/', aboutfunview, name='about_fun_view'),
    # path('newsfun/', newsfunview, name='newsfun'),
    path('newsfun/', newsfunview, {'template_name':'myapp/news.html'}, name='news_fun_view'),
    path('newsfun2/', newsfunview, {'template_name':'myapp/news2.html'}, name='news_fun2_view'),
    path('contactfun/', contactfunview, name='contact_fun_view'),
]
