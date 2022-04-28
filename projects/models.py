from django.db import models
from datetime import date, datetime
from django.urls import reverse
from django.db.models.fields import BLANK_CHOICE_DASH
#from django.views.generic.list import T


class rootdetail(models.Model):
    slug = models.SlugField(null=True)
    headline = models.CharField(max_length=255, default="Ajax opensource turnkey projects")
    footer = models.CharField(max_length=255, default=" 2021 Ajax")
    body = models.CharField(max_length=8192, blank=True, null=True)
    projects = models.BigIntegerField(default=0)
    projectsbuild = models.BigIntegerField(default=0)
    packages = models.BigIntegerField(default=0)
    packagesbuild = models.BigIntegerField(default=0)
    contactname = models.CharField(max_length=64, default="John Doe")
    contactmail = models.CharField(max_length=64, default="JohnDoe@mail.ajax.void")
    contactorg = models.CharField(max_length=128, default="Ajax corp.")
    logo = models.URLField(default="http://repos.pip2scl.dk/logos/sclbuilder.png")
    def __str__(self):
      return self.slug




class project2(models.Model):
    thismoment = datetime.now
    STATUSES = (
        ('Initial', 'Initial stated - Work to be done'),
        ('Building', 'Building in progress'),
        ('Completed', 'Build completed succesfully'),
        ('Failed', 'Build failed and interaction'),
    )
    slug = models.SlugField(null=True) # new
    projectname = models.CharField(max_length=50, unique=True)
    projectname = models.CharField(max_length=50, unique=True)
    projectversion = models.CharField(max_length=50, default="001")
    projectdescription = models.CharField(max_length=256, default="This is the project description")
    projectstatus = models.CharField( max_length=256, choices=STATUSES, default="Initial")
    projectcreated = models.DateField(default=thismoment)
    projectdeployed = models.DateField(blank=True, null=True)
    projecturl = models.URLField(blank=True, default="http://repos.pip2scl.dk/PROJECTS/README.md", null=True)
    projectlogourl = models.ForeignKey('projects.sclbuilderlogos', to_field='sclbuilderlogoname', on_delete=models.CASCADE, default="default", null=True)
    totalsubprojects = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    totalsubprojectsbuilding = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    totalsubprojectsbuild = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    totalsubprojectsfailed = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.projectname
    
    

class project(models.Model):
    thismoment = datetime.now
    STATUSES = (
        ('Initial', 'Initial stated - Work to be done'),
        ('Building', 'Building in progress'),
        ('Completed', 'Build completed succesfully'),
        ('Failed', 'Build failed and interaction'),
    )
    slug = models.SlugField(null=True) # new
    projectname = models.CharField(max_length=50, unique=True)
    projectversion = models.CharField(max_length=50, default="001")
    projectdescription = models.CharField(max_length=256, default="This is the project description")
    projectstatus = models.CharField( max_length=256, choices=STATUSES, default="Initial")
    projectcreated = models.DateField(default=thismoment)
    projectdeployed = models.DateField(blank=True, null=True)
    projecturl = models.URLField(blank=True, default="http://repos.pip2scl.dk/PROJECTS/README.md", null=True)
    projectlogourl = models.ForeignKey('projects.sclbuilderlogos', to_field='sclbuilderlogoname', on_delete=models.CASCADE, default="default", null=True)
    totalsubprojects = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    totalsubprojectsbuilding = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    totalsubprojectsbuild = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    totalsubprojectsfailed = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.projectname
    
    


class subproject(models.Model):
    thismoment = datetime.now
    STATUSES = (
        ('Initial', 'Initial stated - Work to be done'),
        ('Building', 'Building in progress'),
        ('Completed', 'Build completed succesfully'),
        ('Failed', 'Build failed and interaction'),
    )
    projectname = models.ForeignKey( 'projects.project', to_field='projectname', on_delete=models.CASCADE)
    subprojectname = models.CharField(max_length=50, unique=True)
    subprojectversion = models.CharField(max_length=50, default="001")
    subprojectdescription = models.CharField(max_length=256, default="This is the description of the sub project" )
    subprojectstatus = models.CharField( max_length=256, choices=STATUSES, default="Initial")
    subprojectcreated = models.DateField(default=thismoment)
    subprojectdeployed = models.DateField(blank=True, null=True)
    subprojecturl = models.URLField(blank=True, null=True)
    subprojectlogourl = models.ForeignKey('projects.sclbuilderlogos', to_field='sclbuilderlogoname', on_delete=models.CASCADE, default="default", null=True)
    subprojectreleases = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    subprojectreleasesbuilding = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    subprojectreleasesbuild = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    subprojectreleasesfailed = models.PositiveSmallIntegerField(default=0, null=True)
    slug = models.SlugField(null=True, default=projectname)
    def __str__(self):
        return self.subprojectname



class subprojectrelease(models.Model):
    thismoment = datetime.now
    STATUSES = (
        ('Initial', 'Initial stated - Work to be done'),
        ('Building', 'Building in progress'),
        ('Completed', 'Build completed succesfully'),
        ('Failed', 'Build failed and interaction'),
    )
    subprojectname = models.ForeignKey( 'projects.subproject', to_field='subprojectname', on_delete=models.CASCADE)
    releasename = models.CharField(max_length=50, unique=True)
    releaseversion = models.CharField(max_length=50)
    releasebuild = models.CharField(max_length=50, default="001")
    releasedescription = models.CharField(max_length=256, default="This is the description of the releas")
    releasestatus = models.CharField( max_length=256, choices=STATUSES, default="Initial")
    releasecreated = models.DateField(default=thismoment)
    releasedeployed = models.DateField(blank=True, null=True)
    releaserequirementurl = models.URLField(blank=True, null=True)
    releaserequirements = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    releaserequirementsbuilding = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    releaserequirementsbuild = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    releaserequirementsfailed = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    slug = models.SlugField(null=True, default=subprojectname)

    def __str__(self):
        specificrelease = "%s:%s/%s" % (self.subprojectname, self.releaseversion , self.releasename)
        return specificrelease


class package(models.Model):
    thismoment = datetime.now
    # Countries Choices
    STATUSES = (
        ('Initial', 'Initial stated - Work to be done'),
        ('Building', 'Building in progress'),
        ('Completed', 'Build completed succesfully'),
        ('Failed', 'Build failed and interaction'),
    )
    PYTHONVERSIONS = (
        ('3.9', 'python3.9'),
        ('3.8', 'python3.8'),
        ('2', 'python2')
    )
    slug = models.SlugField(null=True, unique=True)
    packagename = models.CharField(max_length=50)
    packageversion = models.CharField(max_length=50)
    packagestatus = models.CharField(max_length=50, choices=STATUSES, default="Initial")
    packagestatusurl = models.URLField(blank=True, null=True)
    packagecreated = models.DateField(blank=True, null=True)
    packagedescription = models.CharField(max_length=256, default="This is the package description", blank=True, null=True)
    packagepythonversion = models.CharField(max_length=12, choices=PYTHONVERSIONS, default="3.8", blank=True, null=True)

    packagesourcefileurlorg = models.URLField(blank=True, null=True)
    packagesourcefileurl = models.URLField(blank=True, null=True)
    packagesourcefilestatus = models.CharField(max_length=50, choices=STATUSES, default="Initial", blank=True, null=True)
    packagepackagesourcefileurlorgmeta = models.CharField(max_length=256, choices=STATUSES, default="Initial", blank=True, null=True)
    packagesourcefilecreated = models.DateField(blank=True, null=True)
    packagesourcefileverified = models.DateField(blank=True, null=True)
    packagesourcefiledeployed = models.DateField(blank=True, null=True)

    packageorgspecfileurl = models.URLField(blank=True, null=True)
    packageorgspecfilestatus = models.CharField(max_length=50, choices=STATUSES, default="Initial", blank=True, null=True)
    packageorgspecfilecreated = models.DateField(blank=True, null=True)
    packageorgspecfileverified = models.DateField(blank=True, null=True)
    packageorgspecfiledeployed = models.DateField(blank=True, null=True)
    
    packagespecfileurl = models.URLField(blank=True, null=True)
    packagespecfilestatus = models.CharField(max_length=50, choices=STATUSES, default="Initial", blank=True, null=True)
    packagespecfilecreated = models.DateField(blank=True, null=True)
    packagespecfileverified = models.DateField(blank=True, null=True)
    packagespecfiledeployed = models.DateField(blank=True, null=True)
    
    packagerpmfilesurl = models.URLField(blank=True, null=True)
    packagerpmfilestatus = models.CharField(max_length=50, choices=STATUSES, default="Initial", blank=True, null=True)
    packagerpmfilecreated = models.DateField(blank=True, null=True)
    packagerpmfileverified = models.DateField(blank=True, null=True)
    packagerpmfiledeployed = models.DateField(blank=True, null=True)
    packagerpmfileurl = models.URLField(blank=True, null=True)
    
    packagesclfilemeta = models.CharField(max_length=50, choices=STATUSES, default="Initial", blank=True, null=True)
    packagesclfilestatus = models.CharField(max_length=50, choices=STATUSES, default="Initial", blank=True, null=True)
    packagesclfilecreated = models.DateField(blank=True, null=True)
    packagesclfileverified = models.DateField(blank=True, null=True)
    packagesclfiledeployed = models.DateField(blank=True, null=True)
    
    packagesclrpmfilestatus = models.CharField(max_length=51, choices=STATUSES, default="Initial", blank=True, null=True)
    packagesclrpmfilelog = models.CharField(max_length=51, choices=STATUSES, default="Initial", blank=True, null=True)
    packagesclrpmfilesurl = models.URLField(blank=True, null=True)
    packagesclrpmfilecreated = models.DateField(blank=True, null=True)
    packagesclrpmfileverified = models.DateField(blank=True, null=True)
    packagesclrpmfiledeployed = models.DateField(blank=True, null=True)

    packagetweak = models.BooleanField(blank=True, null=True, default=False)
    packagetweakscript = models.URLField(blank=True, null=True)

    def __str__(self):
        specificpackage = "%s-%s" % (self.packagename , self.packageversion)
        return specificpackage


class packagetweak(models.Model):
    thismoment = datetime.now
    packagetweakname = models.CharField(max_length=256)
    packagetweakbuild = models.DateField(blank=True, null=True)
    packagetweakverified = models.DateField(blank=True, null=True)
    packagetweakdeployed = models.DateField(blank=True, null=True)
    packagetweakscript = models.URLField(blank=True, null=True)
    def __str__(self):
      return self.packagetweakname


class requirement(models.Model):
    thismoment = datetime.now
    releaseid = models.ForeignKey(
        'projects.subprojectrelease', on_delete=models.CASCADE)
    packageid = models.ForeignKey(
        'projects.package', on_delete=models.CASCADE)
    def __str__(self):
        specificrequirement = "%s requires %s" % (self.releaseid , self.packageid)
        return specificrequirement
    slug = models.SlugField(default=releaseid)


class packagetweakrelation(models.Model):
    thismoment = datetime.now
    packagetweakname = models.ForeignKey(
        'projects.packagetweak', on_delete=models.CASCADE)
    packagename = models.ForeignKey(
        'projects.package', on_delete=models.CASCADE)
    def __str__(self):
      specifictweak = "%s tweaks %s" % (self.packagetweakname , self.packagename )
      return specifictweak

class sclbuilderlogos(models.Model):
    sclbuilderlogoname = models.CharField(max_length=256, unique=True)
    sclbuilderlogourl = models.URLField(blank=True, default="http://repos.pip2scl.dk/logos/sclbuilder.png")
    def __str__(self):
      return self.sclbuilderlogourl

