from distutils.command.upload import upload
from django.db import models
from django.forms import FileField

# Create your models here.
from django.utils.translation import gettext_lazy as _

class Video(models.Model):

    caption = models.CharField(_("caption"), max_length=350)
    video = models.FileField(_("video"), upload_to='video/', max_length=100)
    thumbnail = models.FileField(upload_to="thumbnail/" , blank=True)
    

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.caption

   