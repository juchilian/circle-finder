from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Circle, Like
from .forms import CircleModelForm
# Create your views here.

def circle_list_view(request):
    circles = Circle.objects.all()
    paginator = Paginator(circles, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''
    
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    context = {
        "title": "サークル一覧",
        "page": page,
        "next_page_url": next_url,
        "prev_page_url": prev_url,
        }
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

@login_required
def circle_like_unlike(request):
    user = request.user
    if request.method == 'POST':
        circle_id = request.POST.get('circle_id')
        circle_obj = Circle.objects.get(id=circle_id)
        # user = User.objects.get(user=user)

        if user in circle_obj.liked.all():
            circle_obj.liked.remove(user)
        else:
            circle_obj.liked.add(user)
        
        like, created = Like.objects.get_or_create(user=user, circle_id=circle_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

        circle_obj.save()
        like.save()
        data = {
            'value': like.value,
        }
        return JsonResponse(data, safe=False)
    # return redirect('circle:main-circle-view')
        
