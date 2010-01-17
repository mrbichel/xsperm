from django.db import models
from xsperm.utils import filterBadWords

class Fact(models.Model):
    text = models.CharField('fact', max_length=256)
    rating = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('-rating',)

    def __unicode__(self):
    	return self.text
    
    def save(self):
        self.text = filterBadWords(self.text)
        super(Fact, self).save()
    	
