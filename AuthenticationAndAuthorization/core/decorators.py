from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import render

def login_and_role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if required_role == "customer" and not user.is_customer:
                return render(request, "core/403.html", status=403)
            
            if required_role == "seller" and not user.is_seller:
                return render(request, "core/403.html", status=403)
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator