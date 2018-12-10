# -*- coding: utf-8 -*-

from django.db import models
from user.models import UserProfile
from news.models import News


class Comments(models.Model):
    """
    """
    content = models.TextField("回复内容")
    disabled = models.BooleanField(default=False, verbose_name="是否屏蔽")
    deleted = models.BooleanField(default=False, verbose_name="删除标识")
    parent_id = models.IntegerField(verbose_name="对那个评论进行回复")

    owner = models.ForeignKey(UserProfile, verbose_name="发表人")
    news = models.ForeignKey(News, verbose_name="所属新闻")

    create_time = models.DateTimeField("创建时间", auto_now=True, auto_created=True)


class CommentPraise(models.Model):
    """
    """
    comment = models.ForeignKey(Comments, verbose_name="所赞许/鄙视的评论")
    owner = models.ForeignKey(UserProfile, verbose_name="发表人")
    praise = models.BooleanField()

