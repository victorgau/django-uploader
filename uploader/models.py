# -*- coding: utf-8 -*-
from django.db import models


class Photo(models.Model):
    #imagefile = models.ImageField(upload_to='documents/%Y/%m/%d')
    imagefile = models.ImageField(upload_to='products/')
