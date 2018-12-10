# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from image.models import Image


class UserProfile(models.Model):
    """
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telephone = models.CharField('手机号', max_length=50, blank=True)
    logo = models.ForeignKey(Image, verbose_name="头像", null=True)

    class Meta:
        verbose_name = 'User Profile'
        db_table = 'user_profile'
        app_label = 'user'

    def __str__(self):
        """
        :return:
        """
        return "{}'s profile".format(self.user.__str__())
