from django.shortcuts import render
from django.views import View

from .models import Tests


class UserView(View):

    def get(self, request):
        users = Tests.objects.all()
        return render(request, 'index.html', {'users': users})

# Create your views here.
