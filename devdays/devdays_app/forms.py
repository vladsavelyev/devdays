from django.contrib import admin
from devdays_app.models import Comment, Group, Role, UserProfile, Idea, Project, Event


class CommentAdmin(admin.ModelAdmin):
    pass


class GroupAdmin(admin.ModelAdmin):
    pass


class RoleAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


class IdeaAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)

