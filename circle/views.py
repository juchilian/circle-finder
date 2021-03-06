from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Circle
from .forms import CircleModelForm
# Create your views here.

def circle_list_view(request):
    circles = Circle.objects.all()
    context = {"title": "サークル一覧" ,"circles": circles}
    template_name = 'circle/list.html'
    return render(request, template_name, context)
    
def circle_detail_view(request, slug):
    circle = get_object_or_404(Circle, slug=slug)
    context = {"title": "サークル詳細" ,"circle": circle}
    template_name = 'circle/detail.html'
    return render(request, template_name, context)

@staff_member_required
def circle_edit_view(request, slug):
    circle = get_object_or_404(Circle, slug=slug)
    if circle.owner == request.user:
        form = CircleModelForm(request.POST or None, instance=circle)
        if form.is_valid():
            form.save()
            messages.success(request, "正常に更新されました！")
            return redirect("/")
        context = {"title": "サークル情報の編集", 'form': form}
        template_name = 'circle/form.html'
        return render(request, template_name, context)
    else:
        # 権限がない人によるアクセス
        raise Http404