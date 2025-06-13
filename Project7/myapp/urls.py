from django.urls import path
from myapp.views import myfunview1, myfunview2, homefunview, aboutfunview, newsfunview, contactfunview, MyClassView1, MyClassView2, MyClassView3, MyChildClassView3, HomeClassView, AboutClassView, NewsClassView, ContactClassView, AboutTemplateView, ContactTemplateView, ProfileTemplateView
from django.views.generic.base import TemplateView
from myapp import views

urlpatterns = [
    # Urls for Function Based View
    path('fun1/', myfunview1, name='myfunview1'),
    path('fun2/', myfunview2, name='myfunview2'),
    path('homefun/', homefunview, name='home_fun_view'),
    path('aboutfun/', aboutfunview, name='about_fun_view'),
    # path('newsfun/', newsfunview, name='newsfun'),
    path('newsfun/', newsfunview, {'template_name':'myapp/news.html'}, name='news_fun_view'),
    path('newsfun2/', newsfunview, {'template_name':'myapp/news2.html'}, name='news_fun2_view'),
    path('contactfun/', contactfunview, name='contact_fun_view'),

    # Urls for Class Based View
    path('cl1/', MyClassView1.as_view(), name='myclassview1'),
    path('cl2/', MyClassView2.as_view(), name='myclassview2'),
    # path('cl3/', MyClassView3.as_view(), name='myclassview3'),
    path('cl3/', MyClassView3.as_view(name='Ritik'), name='myclassview3'),
    path('chcl3/', MyChildClassView3.as_view(), name='mychildclassview3'),
    path('homecl/', HomeClassView.as_view(), name='home_class_view'),
    path('aboutcl/', AboutClassView.as_view(), name='about_class_view'),
    path('newscl/', NewsClassView.as_view(template_name='myapp/news.html'), name='newscl'),
    path('newscl2/', NewsClassView.as_view(template_name='myapp/news2.html'), name='newscl2'),
    path('contactcl/', ContactClassView.as_view(), name='contact_class_view'),


    # TemplateView
    path('home/', TemplateView.as_view(template_name='myapp/home.html'), name='home'),
    path('index/', views.TemplateView.as_view(template_name='myapp/index.html'), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    # path('contact/', ContactTemplateView.as_view(), name='about'),
    path('contact/', ContactTemplateView.as_view(extra_context={'course':'Python'}), name='contact'),
    path('profile/<int:id>', ProfileTemplateView.as_view(), name='profile'),

]
