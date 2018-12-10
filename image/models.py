# -*- coding: utf-8 -*-

from django.db import models


class Image(models.Model):
    """
    """

    class Meta:
        db_table = 'images'
        verbose_name = 'image'
        app_label = 'image'
