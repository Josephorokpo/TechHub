from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from .models import Blog, Comment, Category
from .forms import BlogForm, CommentForm, ReplyForm

# Create your views here.
def home(request):
    featured_blog = Blog.objects.filter(featured=True).first()
    all_blogs = Blog.objects.filter(featured=False).order_by('-created')  # Assuming 'created' is your date field

    paginator = Paginator(all_blogs, 4)  # Show 4 blogs per page
    page_number = request.GET.get('page')
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'featured_blog': featured_blog,
    }
    return render(request, 'blog_app/home.html', context)

def about(request):
    context = {}
    return render(request, 'blog_app/about.html', context)

def contact_us(request):
    context = {}
    return render(request, 'blog_app/contact_us.html', context)


@login_required
def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.filter(parent__isnull=True)
    new_comment = None

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to the login page if the user is not authenticated
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = blog
            new_comment.user = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                new_comment.parent = Comment.objects.get(id=parent_id)
            new_comment.save()
            return redirect('detail', slug=blog.slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog_app/detail.html', {
        'blog': blog,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })
    
    
@login_required(login_url='signin')
def create_article(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user  # Associate the blog with the current user
            blog.slug = slugify(request.POST["title"])
            blog.save()
            messages.success(request, "Article created successfully!")
            return redirect('profile')  # Redirect to user's profile after successful creation
    else:
        form = BlogForm()
    return render(request, 'blog_app/create_article.html', {'form': form})

@login_required(login_url='signin')
def update_article(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    if request.user != blog.user:
        messages.error(request, 'You are not authorized to edit this article.')
        return redirect('home')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully!')
            return redirect('detail', slug=blog.slug)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog_app/create_article.html', {'form': form, 'blog': blog})

@login_required(login_url='signin')
def delete_article(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    if request.user != blog.user:
        messages.error(request, 'You are not authorized to delete this article.')
        return redirect('home')

    if request.method == 'POST':
        if 'confirm' in request.POST:
            blog.delete()
            messages.success(request, 'Article deleted successfully.')
            return redirect('profile')
        elif 'cancel' in request.POST:
            messages.info(request, 'Article deletion canceled.')
            return redirect('detail', slug=blog.slug)
    
    return render(request, 'blog_app/delete_article_confirm.html', {'blog': blog})

@login_required
def reply_comment(request, comment_id):
    # Retrieve the parent comment
    parent_comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.method == 'POST':
        # Create a form instance with POST data
        form = ReplyForm(request.POST)
        if form.is_valid():
            # Process the form data and save the reply
            reply = form.save(commit=False)
            reply.user = request.user
            reply.parent = parent_comment
            reply.article = parent_comment.article
            reply.save()
            return redirect('detail', slug=parent_comment.article.slug)
    else:
        form = ReplyForm()
    
    return redirect('detail', slug=parent_comment.article.slug)



def search_results(request):
    query = request.GET.get('q')
    results = Blog.objects.filter(title__icontains=query) if query else Blog.objects.none()
    return render(request, 'blog_app/search_results.html', {'results': results, 'query': query})

@login_required
def category_articles(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = category.blogs.all()

    paginator = Paginator(articles, 4)  # Paginate articles, assuming 4 per page
    page_number = request.GET.get('page')
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'category_articles.html', context)
