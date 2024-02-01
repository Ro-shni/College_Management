from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    fullname = models.CharField(max_length=60)
    branch = models.CharField(max_length=100)
    stdyear = models.CharField(max_length=6, null=True, blank=True)
    phno = models.CharField(max_length=12)
    git = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    hrank = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=16)
    addr = models.TextField()
    adnum=models.CharField(max_length=11)
    image = models.ImageField(default='mysite\templates\avatar.jpg',upload_to='contact_images')
    def __str__(self):
        return f'{self.fullname}-{self.adnum}'


'''
class Internship(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title

class Certification(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title

#def save_internships_and_certifications(request):
#    internship_titles = request.POST.getlist('internship_title')
#    internship_urls = request.POST.getlist('internship_url')
#    certification_titles = request.POST.getlist('certification_title')
#    certification_urls = request.POST.getlist('certification_url')

#    for title, url in zip(internship_titles, internship_urls):
#        internship = Internship(title=title, url=url)
#        internship.save()

    for title, url in zip(certification_titles, certification_urls):
        certification = Certification(title=title, url=url)
        certification.save()
'''
CATEGORY=(
    ('Web Development','web development'),
    ('hello world','helloworld'),
)
TYPES=(
    ('nptel','nptel'),
    ('workshops','workshops'),
    ('seminar','seminar'),
    ('sports','sports'),
)
LEVELS=(
    ( 'easy', 'easy' ),
    ('moderate','moderate'),
    ('hard', 'hard'),
)
class certi(models.Model):
    type = models.CharField(max_length=100,choices=TYPES,null=True)
    #category = models.CharField(max_length=20,choices=CATEGORY)
    credits = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=75,null=True)
    score = models.PositiveIntegerField(null=True)
    level=models.CharField(max_length=100,choices=LEVELS,null=True)
    adnum=models.CharField(max_length=10,null=True)
    image = models.FileField(upload_to='media/', null=True, blank=True)
    def __str__(self):
        return f'{self.type}-{self.adnum}'

class orders(models.Model):
    certi_name = models.CharField(max_length=100)
    drivelink = models.CharField(max_length=100)
    certi_no = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    credits = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.certi_name}-{self.drivelink}'
