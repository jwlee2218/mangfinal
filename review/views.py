from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Like
from django.db.models import Q
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_list(request):

    post_list_all = Post.objects.all()
    keyword = request.GET.get('keyword','')

    likes_list = []
    for post in post_list_all:
        likes_list.append(post.like_num)
    likes_list.sort(reverse = True)
    if len(likes_list) > 5:
        criteria = likes_list[4]
    else:
        criteria = min(likes_list)
    best_list_all = Post.objects.filter(like_num__gte = criteria)
    ordered_best_list = best_list_all.order_by('-hits')
    best_list = []
    for post in ordered_best_list:
        best_list.append(post)
    page = request.GET.get('page')
    if keyword:
        condition = Q(title__icontains = keyword)|Q(content__icontains=keyword)
        filtered_post_list = post_list_all.filter(condition)
        postlist = Paginator(filtered_post_list, 10)
        keyword = request.GET.get('keyword','')
        page = request.GET.get('page')
    else:
        postlist = Paginator(post_list_all, 10)
        keyword = request.GET.get('keyword','')
        page = request.GET.get('page')

    try:
        post_list = postlist.page(page)
    except PageNotAnInteger:
        post_list = postlist.page(1)
    except EmptyPage:
        post_list = postlist.page(postlist.num_pages)
    return render(request, 'review/post_list.html', {'post_list' : post_list, 'keyword' : keyword, 'best_list':best_list,})

def tag_filter(request, keyword):
    post_list_all = Post.objects.all()
    page = request.GET.get('page')
    likes_list = []
    for post in post_list_all:
        likes_list.append(post.like_num)
    likes_list.sort(reverse = True)
    if len(likes_list) > 5:
        criteria = likes_list[4]
    else:
        criteria = min(likes_list)
    best_list_all = Post.objects.filter(like_num__gte = criteria)
    ordered_best_list = best_list_all.order_by('-hits')
    best_list = []
    for post in ordered_best_list:
        best_list.append(post)
    if keyword:
        filtered_post_list = post_list_all.filter(tag_set__name__icontains = keyword)
        postlist = Paginator(filtered_post_list, 10)
    try:
        post_list = postlist.page(page)
    except PageNotAnInteger:
        post_list = postlist.page(1)
    except EmptyPage:
        post_list = postlist.page(postlist.num_pages)

    return render(request, 'review/post_list.html', {'post_list' : post_list, 'keyword' : keyword,'best_list':best_list, })

def post_detail(request, id):
    post = Post.objects.get(id = id)
    Post.objects.filter(id = id).update(hits = post.hits +1)


    comment_list_all = Comment.objects.filter(post = post)
    page = request.GET.get('page')
    commentlist = Paginator(comment_list_all, 10)

    try:
        comment_list = commentlist.page(page)
    except PageNotAnInteger:
        comment_list = commentlist.page(1)
    except EmptyPage:
        comment_list = commentlist.page(commentlist.num_pages)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/review/{}/'.format(post.id))
    else:
        form = CommentForm()

    return render(request, 'review/post_detail.html',{
        'post' : post, 'form' : form, 'comment_list':comment_list,
        })

@login_required
def post_like(request, id):
    post = get_object_or_404(Post, id = id)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        post.like_num = post.like_num - 1

    post.like_num = post.like_num + 1

    return redirect(post)

@login_required
def post_new(request):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            messages.success(request, '저장되었습니다.')
            return redirect('/review/')
    else:
        form = PostForm()
    return render(request, 'review/post_form.html',{
            'form' : form,
            })

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post,id = id)
    if post.user == request.user:

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance = post)
            if form.is_valid():
                post = form.save()
                messages.success(request, '수정되었습니다.')
                return redirect('/review/')
        else:
            form = PostForm(instance = post)

        return render(request, 'review/post_form.html',{'form' : form, })
    else:
        return redirect(post)
    return render(request, 'review/post_form.html',{'form' : form,
    })

@login_required
def post_delete(request, id):
    post = Post.objects.get(id = id)
    if post.user == request.user:


        post.delete()

    else:
        return redirect(post)

    return redirect('/review/')

@login_required
def comment_edit(request, id):

    comment = Comment.objects.get(id = id )
    if request.method =='POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            comment = form.save()
            return redirect(comment.post)
    else:
        form = CommentForm(instance = comment)
    return render(request, 'review/post_form.html', {'form' : form,})

@login_required
def comment_delete(request, id):
    comment = Comment.objects.get(id = id)
    comment.delete()
    return redirect(comment.post)
