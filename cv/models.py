from django.db import models
from .SVGS import SVG_CHOICE

class Skill(models.Model):
    name = models.CharField(max_length=256)
    progress = models.IntegerField()

    def __str__(self):
        return self.name


class Services(models.Model):
    svg = models.CharField(max_length=1000,choices=SVG_CHOICE)
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.title

class Achivmenet(models.Model):
    worksCompleted = models.IntegerField()
    yearOfExperiance = models.IntegerField()
    totalclients = models.IntegerField()
    awardWon = models.IntegerField()


class CV(models.Model):
    name = models.CharField(max_length=256)
    background = models.ImageField(upload_to='photo/')
    photo = models.ImageField(upload_to='photo/')
    job = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.IntegerField()
   
    def __str__(self):
        return self.name
   

class About_Paragraph(models.Model):
    cv = models.ForeignKey(CV,on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    
    def __str__(self):
        return str(self.cv)
    
class Blog(models.Model):
    title = models.CharField(max_length=256)
    Main_photo = models.ImageField(upload_to='blog/')
    category = models.CharField(max_length=256)
    client = models.CharField(max_length=256)
    projectDate = models.DateField()
    projectUrl = models.URLField(blank=True)
    subtitle = models.CharField(max_length=256)
    text = models.TextField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogImgs(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    imgName = models.CharField(max_length=256)
    img = models.ImageField(upload_to='blogimgs/')

    def __str__(self):
        return self.imgName


