from django.db import models
from datetime import datetime

class Testimonial(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    author = models.CharField('author', max_length=40)
    date = models.DateTimeField(default=datetime.now)
    
    class Meta:
        ordering = ('-date',)
        get_latest_by = 'date'

    def __unicode__(self):
    	return self.text
    	
    def save(self):
        self.text = filterBadWords(self.text)
        self.title = filterBadWords(self.title)
        self.author = filterBadWords(self.author)
        super(Testimonial, self).save()	
    

