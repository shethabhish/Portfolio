from django.db import models

class Jobs(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length = 300)

    def __str__(self):
        name = self.image.name[7]
        return name
