from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Func, F
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Circle, Like, HARD_LIST, ALCOHOL_LIST, EXPERIENCED_LIST, EVENT_LIST
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
    context = {"title": "サークル詳細", "circle": circle}
    template_name = 'circle/detail.html'
    return render(request, template_name, context)


@staff_member_required
def circle_edit_view(request, slug):
    circle = get_object_or_404(Circle, slug=slug)
    if circle.owner == request.user:
        # リクエストがPOSTならrequest.POST, GETならNone
        form = CircleModelForm(request.POST or None, instance=circle)
        if form.is_valid():  # リクエストPOSTで正しい入力だった場合
            form.save()
            messages.success(request, "正常に更新されました！")
            return redirect("/")
        # GETの場合は編集画面表示
        context = {"title": "サークル情報の編集", 'form': form}
        template_name = 'circle/form.html'
        return render(request, template_name, context)
    else:
        # 権限がない人によるアクセス
        raise Http404


@login_required
def circle_like_unlike(request):
    user = request.user
    circle_id = request.POST.get('circle_id')
    circle_obj = Circle.objects.get(id=circle_id)

    if user in circle_obj.liked.all():
        # サークルのlikedカラムにuserが含まれていたら
        circle_obj.liked.remove(user)
    else:
        circle_obj.liked.add(user)

    like, created = Like.objects.get_or_create(
        user=user, circle_id=circle_id)

    if not created:  # レコードが作られなかった場合
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    else:
        like.value = 'Like'

    circle_obj.save()
    like.save()
    data = {
        'value': like.value,
    }
    return JsonResponse(data, safe=False)


def circle_search_view(request):
    hard = request.GET.get('hard')
    experienced = request.GET.get('experienced')
    alcohol = request.GET.get('alcohol')
    # サークル一つ一つに対してscore計算->上位3つをsearched_circlesに格納
    searched_circles = Circle.objects.annotate(score=Func(F('hard') - hard, 2, function='Power')+Func(
        F('experienced') - experienced, 2, function='Power')+Func(F('alcohol') - alcohol, 2, function='Power')).order_by('score')[:3]
    context = {"title": "最適サークル検索結果", 'circles': searched_circles}
    context["params"] = {HARD_LIST, ALCOHOL_LIST, EXPERIENCED_LIST, EVENT_LIST}
    template_name = 'circle/searched.html'
    return render(request, template_name, context)
