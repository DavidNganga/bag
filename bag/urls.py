from django.urls import path
from . import views


urlpatterns = [
    path('welcome/',views.welcome,name='welcome'),
    path('search/',views.search_results,name='search_results'),
    path('article/<int:blog_id>', views.article, name='article'),
    path('commment/<int:blog_id>', views.post_comment, name='comment')

    # path('comment/<int:comment_id>/',views.post_comment, name='comment'),
]
