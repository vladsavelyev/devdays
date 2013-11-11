from django.contrib import admin
from devdays_app.models import Comment, Group, Student, Idea, Project, Event


class CommentAdmin(admin.ModelAdmin):
    pass


class GroupAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class IdeaAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)

