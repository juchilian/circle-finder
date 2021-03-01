from django.shortcuts import render
from .models import Circle
# Create your views here.

def circle_list_view(request):
    circles = Circle.objects.all()
    context = {"title": "サークル一覧" ,"circles": circles}
    template_name = 'circle/list.html'
    return render(request, template_name, context)