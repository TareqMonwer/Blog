from django.conf import settings
from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel



class Article(TimeStampedModel):
  STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published')
  )
  title = models.CharField("Article Title", max_length=255)
  slug = AutoSlugField("Article Address", unique=True,
                       always_update=False, populate_from='title')
  author = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.SET_NULL)
  content = models.TextField("Article Content")
  status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')
  
  class Meta:
    ordering = ['-created']
  
  def __str__(self):
    return self.title