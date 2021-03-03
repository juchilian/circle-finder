from django.shortcuts import render, get_object_or_404, redirect
from .models import Circle
# Create your views here.

def circle_list_view(request):
    circles = Circle.objects.all()
    context = {"title": "サークル一覧" ,"circles": circles}
    template_name = 'circle/list.html'
    return render(request, template_name, context)
    
def circle_detail_view(request, circle_id):
    circle = get_object_or_404(Circle, id=circle_id)
    is_owner = False
    if circle.owner == request.user:
        is_owner = True
    context = {"title": "サークル詳細" ,"circle": circle}
    template_name = 'circle/detail.html'
    return render(request, template_name, context)
