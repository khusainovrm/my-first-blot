from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField('Article title', max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField('Text of the article')
    publish = models.DateTimeField('Data of publish', default=timezone.now)
    created = models.DateTimeField('Data of creation', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.publish >= (timezone.now - datetime.timedelta(days = 7))

class Meta:
    ordering = ('-publish',)