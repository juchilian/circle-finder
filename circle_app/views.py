from django.shortcuts import render, get_object_or_404, redirect
from circle.models import Circle

def top_view(request):
    template_name = 'top.html'
    top_circle_list = Circle.objects.all()[:3]
    return render(request, template_name, context={"circles":top_circle_list})

def mypage_view(request):
    template_name = 'mypage.html'
    if request.user.is_staff:
        my_circle = Circle.objects.all().filter(owner=request.user).first()
        # my_circle = get_object_or_404(Circle, owner=request.user)
        context = {"my_circle": my_circle}
        return render(request, template_name, context)
    
    else: # 生徒なら
        # keep_circles = Circle.objects.filter(id=request.user.keep)
        context = {"keep_circles": keep_circles}
        return render(request, template_name, context)


