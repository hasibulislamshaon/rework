from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
# Create your models here.
selectOne=(
    ('upcoming','Upcoming'),('live','Live'),('done','Done'),
    ('canceled','Canceled'),('waiting','Waiting'),
    ('closed','Closed'),('postponed','Postponed')
    )
    
def validateBannerSize(image):
    #validate the size
    required_width = 1000
    required_height = 523
    
    if image.width != required_width or image.height != required_height:
        raise ValidationError(
            f'The banner image dimensions must be {required_width}x{required_height} pixels.'
        )
    
def validateSecondBanner(image):
    required_width = 1600 
    required_height = 400
    
    if image.width != required_width or image.height != required_height:
        raise ValidationError(
            f'The banner image dimensions must be {required_width}x{required_height} pixels.'
        )
    

def validateHomePageTopBanner(image):
    required_width = 1000 
    required_height = 523
    
    if image.width != required_width or image.height != required_height:
        raise ValidationError(
            f'The banner image dimensions must be {required_width}x{required_height} pixels.'
        )
    

class myDashboard(models.Model):
    title = models.CharField(max_length=100,default='')
    slug = models.SlugField(blank=True, null=False,unique=True)
    gateOpens=models.DateTimeField( blank=True,null=True)
    gateCloses=models.DateTimeField(blank=True,null=True)
    organizer=models.CharField(max_length=500,blank=True)
    categories= models.CharField(max_length=500,blank=True)

    banner=models.ImageField(upload_to='banner',blank=True, validators=[validateBannerSize])
    secondBanner=models.ImageField(upload_to='secondBanner',blank=True,validators=[validateSecondBanner])
    homePageTopBanner=models.ImageField(upload_to='homePageTopBanner',blank=True,validators=[validateHomePageTopBanner])

    artist=models.CharField(max_length=100,blank=True)
    templateName=models.CharField(max_length=200,blank=True)
    location=models.CharField(max_length=250,default='')
    status=models.CharField(max_length=50,choices=selectOne,blank=False)
    isLive=models.BooleanField(default=False)
    description=RichTextField(blank=True)
    acknowledgement=RichTextField(blank=True)
    ticketPolicy=RichTextField(blank=True)
    eventFaq=RichTextField(blank=True)
    ruleBook=models.FileField(default='',upload_to='allPdf')



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    """@property 
    def imageUrl(self):
        try:
            url= self.banner.url
        except:
            url=''
        return url"""#!important If image field is empty.
    


class TicketType(models.Model):
    name=models.CharField(max_length=500)
    price=models.PositiveIntegerField()
    quangtity=models.IntegerField()
    myDashboard=models.ForeignKey(myDashboard,on_delete=models.CASCADE)


    

    
    

 