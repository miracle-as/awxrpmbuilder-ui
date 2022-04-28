from django.contrib import admin

# Register your models here.

from projects.models import rootdetail
from projects.models import project
from projects.models import subproject
from projects.models import package
from projects.models import subprojectrelease
from projects.models import requirement
from projects.models import packagetweak
from projects.models import packagetweakrelation
from projects.models import sclbuilderlogos



admin.site.register(rootdetail)
admin.site.register(project)
admin.site.register(subproject)
admin.site.register(package)
admin.site.register(subprojectrelease)
admin.site.register(requirement)
admin.site.register(packagetweak)
admin.site.register(packagetweakrelation)
admin.site.register(sclbuilderlogos)

