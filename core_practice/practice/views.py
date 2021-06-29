from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import PostModel
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm


def post_model_create_view(request):
    # if request.method == "POST":
    #     print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)
    form = PostModelForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'created new blog post')
        # print(form.cleaned_data)
        # return HttpResponseRedirect('/practice/{num}'.format(num=obj.id))
    context = {
        'form': PostModelForm()
    }
    template = "blog/create-view.html"
    return render(request, template, context)


def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'Updated post')
        return HttpResponseRedirect('/practice/{num}'.format(num=obj.id))

    template = "blog/update-view.html"
    return render(request, template, context)


def post_model_delete_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Post deleted')
        return HttpResponseRedirect('/practice/')
    context = {
        "object": obj,
    }
    template = "blog/delete-view.html"
    return render(request, template, context)


def post_model_detail_view(request, id=None):
    # try:
    #     obj = PostModel.objects.get(id=1)
    # except:
    #     raise Http404
    # OR
    # qs = PostModel.objects.filter(id=1)
    # if not qs.exists() and qs.count() != 1:
    #     raise Http404
    # else:
    #     obj = qs.first()

    # obj = PostModel.objects.get(id=1)
    # OR
    obj = get_object_or_404(PostModel, id=id)

    context = {
        "object": obj,
    }
    template = "blog/detail-view.html"
    return render(request, template, context)


def post_model_list_view(request):
    # print(request.GET)
    query = request.GET.get('q', None)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {
        "object_list": qs,
    }
    template = "blog/list-view.html"
    return render(request, template, context)


# @login_required(login_url='/login/')
def login_required_view(request):
    print(request.user)
    qs = PostModel.objects.all()
    print(qs)
    context = {
        "object_list": qs,
        # "some_dict": {"abc",123},
        # "num": 456,
        # "array_list": [123,456],
        # "boolean": True,
    }
    ###
    # this method checks authenticated admin user
    ###
    if request.user.is_authenticated:
        # print('logged in')
        template = "blog/list-view.html"
    else:
        print("not logged in")
        template = "blog/list-view-public.html"
        # raise Http404
        return HttpResponseRedirect('/login')
    ###
    # return HttpResponse('some data')
    return render(request, template, context)


def post_model_robust_view(request, id=None):
    obj = None
    context = {}
    success_message = 'A new post is created'

    if id is None:
        'obj is could be created'
        template = "blog/create-view.html"
    else:
        'obj prob exist'
        obj = get_object_or_404(PostModel, id=id)
        success_message = 'A new post is created'
        context['object'] = obj
        template = "blog/detail-view.html"

        if 'update' in request.get_full_path():
            template = "blog/update-view.html"
        if 'delete' in request.get_full_path():
            template = "blog/delete-view.html"
            if request.method == "POST":
                obj.delete()
                messages.success(request, 'Post deleted')
                return HttpResponseRedirect('/practice/')

    if 'update' in request.get_full_path() or 'create' in request.get_full_path():
        form = PostModelForm(request.POST or None, instance=obj)
        context['form'] = form
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, success_message)
            if obj is not None:
                return HttpResponseRedirect('/practice/{num}'.format(num=obj.id))
            context['form'] = PostModelForm()
    return render(request, template, context)
