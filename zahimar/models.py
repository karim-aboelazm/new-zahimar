from django.db import models

class ZahimarImagePrediction(models.Model):
    image = models.ImageField(upload_to='zahimar/')
    classes = models.CharField(max_length=225,null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Zahimar Image Prediction'
    def __str__(self):
        return self.classes
    
    
    