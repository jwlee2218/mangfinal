from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields


class Post(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'review_post_set')

    title = models.CharField(max_length = 100, verbose_name = '제목')

    content = summer_fields.SummernoteTextField(default='',verbose_name='내용')

    photo = models.ImageField(blank = True, upload_to = 'review/post', verbose_name='대표 사진')

    tags = models.CharField(max_length = 20, blank = True)

    tag_set = models.ForeignKey('Tag')

    hits = models.IntegerField(default = 0, null = True, blank = True)

    created_at = models.DateTimeField(auto_now_add = True)

    updated_at = models.DateTimeField(auto_now = True)

    name_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column = 'likeuser', default = '0')

    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True, related_name = 'like_user_set', through = 'Like')

    like_num = models.IntegerField(default = 0)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review:post_detail', args = [self.id])

    @property
    def like_count(self):
        return self.like_user_set.count()


class Tag(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name


class Comment(models.Model):

    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    '''
    class Meta:
        ordering = ['-likes']
    '''
    def __str__(self):
        return self.message

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SummerNote(summer_model.Attachment):
    summer_field = summer_fields.SummernoteTextField(default='')
