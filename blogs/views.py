from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Blog, Category, Comment
from django.db.models import Q

# Create your views here.

def post_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    category = get_object_or_404(Category, pk=category_id)


    context = {
        'posts' : posts,
        'category' : category,
    }

    return render(request, 'post_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(
                user=request.user,
                blog=single_blog,
                comment=comment_text
            )
            # return redirect('blogs', slug=slug)
            return redirect(request.path_info)
    else:
        comments = Comment.objects.filter(blog=single_blog)
    


    context = {
        'single_blog' : single_blog,
        'comments' : comments,
        
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')

    context = {
        'blogs' : blogs,
        'keyword' : keyword,
    }
    return render(request, 'search.html', context)