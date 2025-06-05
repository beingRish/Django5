from django.urls import path
from session.views import setsession, getsession, delsession, flushsession, sessionmethodsinview, sessionmethodsintemplate, sessionclear, settestcookie, checktestcookie, deltestcookie

urlpatterns = [
    path('set/', setsession),
    path('get/', getsession),
    path('del/', delsession),
    path('flush/', flushsession),
    path('inview/', sessionmethodsinview),
    path('intemplatet/', sessionmethodsintemplate),
    path('clear/', sessionclear),
    path('settest/', settestcookie),
    path('checktest/', checktestcookie),
    path('deltest/', deltestcookie),
]
