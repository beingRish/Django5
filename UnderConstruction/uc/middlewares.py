class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")

    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        # response = render(request, 'uc/under.html')
        print("This is after view")
        return response