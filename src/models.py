from django.db import models
from django.urls import reverse

class Article(models.Model):
    slug = models.SlugField(null=False,max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    # category = models.TextField()
    image = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
