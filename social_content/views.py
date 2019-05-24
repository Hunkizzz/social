from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.views.decorators.http import require_POST

from my_decorators.decorator_ajax import ajax_required
from social_content.forms import ContentCreateForm, DeleteContentForm
from social_content.models import Content
from crispy_forms.helper import FormHelper
from my_decorators import decorator_ajax
from account_social.models import Profile

@login_required
def content_create(request):
    if request.method == 'POST':
        form = ContentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.user = request.user
            new_content.save()
            return redirect(new_content.get_absolute_url())
    else:
        form = ContentCreateForm()
    return render(request, 'contents/content/create.html', {'form': form, 'username': request.user})

# Create your views here.

def content_detail(request, id, slug):
    content_detail = get_object_or_404(Content, id = id, slug = slug)

    return render(request,
                  "contents/content/detail.html",
                  {'content_detail':content_detail, 'username': request.user})
@login_required
def content_edit(request, id, slug):
        new_content = get_object_or_404(Content, id = id, slug = slug)
        if new_content.user == request.user and not request.user.is_superuser:
            pass

        if request.method == 'POST':
            form = ContentCreateForm(instance=new_content, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect(new_content.get_absolute_url())
        else:
            form = ContentCreateForm(instance=new_content)
            context = {'form':form, 'create': False}
            return render(request,'contents/content/create.html', context)

@login_required
def delete_content(request, id, slug):
    new_to_delete = get_object_or_404(Content, id = id, slug = slug)
    if new_to_delete.user != request.user and not request.user.is_superuser:
        messages.error(request,"нет доступа для удаления записи!!!")
        return redirect(new_to_delete.get_absolute_url())
    if request.method == 'POST':
        form = DeleteContentForm(request.POST, instance=new_to_delete)
        if form.is_valid():
            new_to_delete.delete()
            messages.success(request,"Запись удалена");
            return HttpResponseRedirect('/account/news')
    else:
        form = DeleteContentForm(instance=new_to_delete)

    template_vars = {'form':form,}
    return render(request, 'contents/content/delete.html',template_vars)


class Json(object):
    pass

@login_required
@require_POST
@ajax_required
def AddArticlesToFavorites(request):
    content_id = request.POST.get('id')
    content_slug = request.POST.get('slug')
    action = request.POST.get('action')
    content = Content.objects.get(id=content_id)
    current_user = Profile.objects.get(user=request.user)
    print(action)
    if action == 'add_to_favorites':
        current_user.favorite_articles.add(content)
    else:
        current_user.favorite_articles.remove(content)
    current_user.save()
    return JsonResponse({'status':'ok '})

@login_required
@require_POST
@ajax_required
def content_like(request):
    content_id = request.POST.get('id')
    action = request.POST.get('action')

    if content_id and action:
        try:
            content = Content.objects.get(id=content_id)
            if action == 'like':
                content.user_likes.add(request.user)
            else:
                content.user_likes.remove(request.user)
            #JSON
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})
