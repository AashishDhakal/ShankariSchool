from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify


class Notices(models.Model):
    notice_headline = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    notice_image = models.ImageField(upload_to="notices")
    notice = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "Notices"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.notice_headline)
        super(Notices, self).save(*args, **kwargs)

    def __str__(self):
        return self.notice_headline

class CEOMessage(models.Model):
    message = RichTextUploadingField()

    class Meta:
        verbose_name = "Message From CEO"
        verbose_name_plural = "Message From CEO"

    def __str__(self):
        return self.message[:30]

class Testimonials(models.Model):
    testimonial_author = models.CharField(max_length=30)
    testimonial_designation = models.CharField(max_length=100)
    testimonial_picture = models.ImageField(upload_to="testimonials")
    testimonial_text = models.TextField()

    class Meta:
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.testimonial_author

class AboutSection(models.Model):
    thumbnail = models.ImageField(upload_to="aboutsection")
    slug = models.SlugField(blank=True)
    section_title = models.CharField(max_length=100)
    section_details = RichTextUploadingField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.section_title)
        super(AboutSection, self).save(*args, **kwargs)

    def __str__(self):
        return self.section_title


class ImportantNotice(models.Model):
    thumbnail = models.ImageField(upload_to="important")
    url = models.CharField(max_length=300,default="#")
    notice_title = models.CharField(max_length=100)

    def __str__(self):
        return self.notice_title

class Downloads(models.Model):
    title = models.CharField(max_length=300)
    file = models.FileField(upload_to='downloads')

    class Meta:
        verbose_name_plural = 'Downloads'

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery")

    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.title

