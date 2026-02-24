from django.db import models
import os

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    uploaded_to = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete_old_image(self):
       "Delete the old image file from storage"
       if self.pk:
            try:
               old_image=Image.objects.get(pk=self.pk)
               if old_image and old_image.image!=self.image:
                   if os.path.isfile(old_image.image.path):
                       os.remove(old_image.image.path)
            except Image.DoesNotExist:
               pass
           
           
    def save(self, *args, **kwargs):
        "override and save to handle the image deletion"
        self.delete_old_image()
        super().save(*args, **kwargs)
        
        
    
    def delete(self, *args, **kwargs):
        "delete imaeg file when model instance is deleted"
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
        