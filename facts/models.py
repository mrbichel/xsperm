from django.db import models

class Fact(models.Model):
    text = models.CharField(max_length=140)
    rating = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('-rating',)

    def __unicode__(self):
    	return self.text
    	
