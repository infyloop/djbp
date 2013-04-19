from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Note(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('notes-view', kwargs={'pk': self.id})
