from django.db import models


class Sabscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return "User %s    %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'MySabscriber'
        verbose_name_plural = 'A lot of Sabscribers'
