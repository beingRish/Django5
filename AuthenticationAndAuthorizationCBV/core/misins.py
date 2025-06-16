from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

class IsCustomerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_customer') and self.request.user.is_customer
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return render(self.request, "core/403.html", status=403)
        return redirect('login')
    


class IsSellerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_seller') and self.request.user.is_seller
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return render(self.request, "core/403.html", status=403)
        return redirect('login')