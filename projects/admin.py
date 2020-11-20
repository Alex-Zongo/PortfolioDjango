from django.contrib import admin
from projects.models import Project, Resume
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    pass


class ResumeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Resume, ResumeAdmin)
