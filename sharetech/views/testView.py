from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class TestRouteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sharetech/dumy_page.html')

testRouteView = TestRouteView.as_view()

