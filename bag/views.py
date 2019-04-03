from django.shortcuts import render
from .forms import PostForm
from .models import Blog

# Create your views here.
def welcome(request):

    return render(request, 'welcome.html')

def post(request):
    form= PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('welcome')
    else:
        form = PostForm()
    return render(request, 'post.html', {"form":form})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        print(search_term)

        blogs = Blog.search_results(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"blogs": blogs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def post_comment(request, blog_id):

    current_blog = Blog.objects.get(id=blog_id)


    if request.method=='POST':
            current_user=request.user
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                comment = form.save(commit=False)


                comment.blog = current_blog
                comment.save()
            return redirect('/')
    else:
            form = CommentForm()
    return render(request, 'comment.html', {"form": form, "current_blog":current_blog,"id":blog_id})



def article(request, blog_id):
     id=blog_id
     print(blog_id)
     pics =Blog.objects.filter(id = blog_id)

     comments = Comment.objects.all().filter(article = id)

     return render(request, 'article.html', {"pics":pics,"comments":comments, id:blog_id})
