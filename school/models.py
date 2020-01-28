from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


class Notices(models.Model):
    notice_headline = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    notice_image = models.ImageField(upload_to="notices")
    notice = RichTextField()

    class Meta:
        verbose_name_plural = "Notices"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.notice_headline)
        super(Notices, self).save(*args, **kwargs)

    def __str__(self):
        return self.notice_headline
