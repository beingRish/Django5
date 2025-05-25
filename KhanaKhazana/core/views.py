from django.shortcuts import render

# Create your views here.

def home(req):
    dishes = [
        {
            "image": "core/images/paneerbuttermasala.png",
            "name": "Paneer Butter Masala",
            "desc": "Creamy and rich, with a delightful blend of spices, perfect with naan or rice."
        },
        {
            "image": "core/images/fishcurry.png",
            "name": "Salmon Fish Curry",
            "desc": "Succulent salmon in creamy, spiced curry with a perfect balance of flavors."
        },
        {
            "image": "core/images/buttorchicken.png",
            "name": "Butter Chicken",
            "desc": "A royal dish with a creamy, nutty gravy that offers a rich unforgettable taste."
        },
    ]
    return render(req, 'core/home.html', {'dishes': dishes})

def menu(req):
    return render(req, 'core/menu.html')

def tracking(req):
    return render(req, 'core/tracking.html')

def reservation(req):
    return render(req, 'core/reservation.html')

def contact(req):
    return render(req, 'core/contact.html')