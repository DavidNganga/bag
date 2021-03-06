from django.db import models

# Create your models here.
class Blog(models.Model):
     article = models.CharField(max_length=20)
     post = models.TextField(max_length=1000)

     image= models.ImageField(upload_to = 'images/',blank=True, null = True )
     date = models.DateField(null=True)

     @classmethod
     def get_all(cls):
        pics = cls.objects.all()
        return pics

     def __str__(self):
        return self.article

     def snippet (self):
         return self.post[:100] + '...'

     def get_Blog_by_id(cls,id):
        pics = cls.objects.get(id=id)
        return pics

     @classmethod
     def search_results(cls,search_term):
        news = cls.objects.filter(article__icontains=search_term)

        return news

class Comment(models.Model):
     content = models.TextField(max_length=150, null = True)
     name=models.CharField(max_length=50,null=True)
     article = models.ForeignKey(Blog,null=True, on_delete=models.CASCADE)

     def __str__(self):
        return self.content

     def save_comment(self):
            self.save()

     @classmethod
     def get_all(cls):
            opinions = cls.objects.all()
            return opinions

     def get_Comment_by_id(cls,id):
            comments = cls.objecs.filter(article=id)
            return comments
