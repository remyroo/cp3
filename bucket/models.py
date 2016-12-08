from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


class Bucketlist(models.Model):
    """
    Models the bucketlist class.
    """
    name = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bucketlists')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return 'bucketlist name: {}, created by: {}'.format(self.name,
                                                            self.created_by)


class Item(models.Model):
    """
    Models the bucketlist item class.
    """
    name = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bucketlist_item')
    bucket = models.ForeignKey(Bucketlist, on_delete=models.CASCADE,
                               related_name='items')
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return 'item name: {}, done: {}'.format(self.name, self.done)
