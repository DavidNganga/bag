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
