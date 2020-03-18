from django.db import models

class Blogs(models.Model):
    blogtitle = models.CharField(max_length = 20)
    blogdate = models.DateTimeField()
    blogtext = models.TextField()
    blogmedia = models.ImageField(upload_to='images/')

    def summary(self):
        return self.blogtext[:100]

    def objectTitle(self):
        return self.blogtitle

    def __str__(self):
        return self.blogtitle 
