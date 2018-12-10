# -*- coding: utf-8 -*-

from django.db import models
from user.models import UserProfile


class News(models.Model):
    """
    """
    url = models.URLField("讨论主题的url地址", max_length=1024, null=False)
    abstract = models.CharField("讨论主题的摘要", max_length=8192, null=False)
    owner = models.ForeignKey(UserProfile, verbose_name="创建人")

    create_time = models.DateTimeField("创建时间", auto_now=True, auto_created=True)

    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        app_label = 'news'

