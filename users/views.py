from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.models import Post, Views, Likes, Comment
from .models import Profile
from .forms import PostForm, CommentForm, TwisterForm
from django.views.generic.edit import UpdateView
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy

# Create your views here.

@login_required
def homepage(request):
    # All Posts
    posts = Post.objects.all()
    comments = Comment.objects.all().count()
    result = None
    # Users
    search_query = request.GET.get('search', '')
    if search_query:
        users = Profile.objects.filter(Q(user__username__icontains=search_query)|Q(user__last_name__icontains=search_query)).exclude(user__username='admin')
        result = users.count()
    else:
        users = Profile.objects.all().exclude(user__username='admin')


    context = {
        'users':users,
        'posts':posts,
        'comments':comments,
        'result':result
    }

    return render(request, 'users/homepage.html', context)

@login_required
def grid(request):
    users = Profile.objects.all().exclude(user__username='admin')

    result = None
    # Users
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
        result = posts.count()
    else:
        posts = Post.objects.all()

    context = {
        'users':users,
        'posts':posts,
        'result':result
    }


    return render(request, 'users/grid.html', context)

@login_required
def myprofile(request):

    user = request.user
    profile = Profile.objects.get(user=user)
    message = False
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            title = form.cleaned_data.get('title')
            file = form.cleaned_data.get('content')
            about = form.cleaned_data.get('about')
            print(file)
            a = list(file.name)[-3:]
            v = (a[0]+a[1]+a[2])
            if v == 'mp4' or v == 'ogg':
                p, created = Post.objects.get_or_create(file=file, title=title, author=profile, about=about, image=image)
                p.save()
                return HttpResponseRedirect(reverse('users:grid'))
            else:
                message = True
    else:
        form = PostForm()

    template = 'users/myprofile.html'
    context = {
        'my':profile,
        'form':form,
        'img':message,
        'message':'You can create only a video post !'
    }

    return render(request, template, context)


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['bio', 'slogan', 'avatar', 'birthday']
    # template_name_suffix = '_profile'
    template_name = 'users/editprofile.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('users:myprofile')


@login_required
def post_detail(request, pk):
    user = request.user
    profile = Profile.objects.get(user=user)
    post = get_object_or_404(Post, id=pk)

    all_users = Profile.objects.all().exclude(user__username='admin')

    # All Posts
    all_posts = Post.objects.all()
    all_comments = Comment.objects.all().count()

    log = Likes.objects.filter(user=profile, post=post)

    # try:
    #     next_post = post.get_next_by_created()
    #     prev_post = post.get_previous_by_created()
    # except next_post.DoesNotExist:
    #     next_post = Post.objects.last()
    # except prev_post.DoesNotExist:
    #     prev_post = Post.objects.first()


    current_view = post.views

    viewed = Views.objects.filter(user=profile, post=post)

    if not viewed:
        view = Views.objects.create(user=profile, post=post)
        current_view += 1
    else:
        current_view -= 0

    post.views = current_view
    post.save()

    f = Post.objects.first()
    l = Post.objects.last()

    if request.GET.get('show', '') == 'all':
        comments = Comment.objects.filter(post=post, active=True)
    else:
        comments = Comment.objects.filter(post=post, active=True)[:3]

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = profile
            comment.save()
            return HttpResponseRedirect(reverse("users:post_detail", args=[post.id]))
    else:
        form = CommentForm()

    context = {
        'post':post,
        'f':f,
        'l':l,
        'comments':comments,
        'all_users':all_users,
        'all_posts':all_posts,
        'all_comments':all_comments,
        'log':log
    }

    template = 'users/post_detail.html'
    return render(request, template, context)

@login_required
def likes(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(user=user)
    likes = post.likes

    liked = Likes.objects.filter(user=profile, post=post)

    if not liked:
        like = Likes.objects.create(user=profile, post=post)
        likes += 1
        like.active = True
    else:
        like = Likes.objects.filter(user=profile, post=post)
        like.delete()
        likes -= 1

    post.likes = likes
    post.save()

    data = {
        'likes':post.likes
    }

    return JsonResponse(data, safe=False)
    # return HttpResponseRedirect(reverse('users:post_detail', args=[post_id]) + '#likes')
    # + '#content_full')

@login_required
def twister(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = TwisterForm(request.POST)
        if form.is_valid():
            twister = form.save(commit=False)
            twister.author = profile
            twister.save()
            return HttpResponseRedirect(reverse("users:grid") + '#twisters')
    else:
        form = CommentForm()

    return HttpResponseRedirect(reverse("users:grid") + '#twisters')
