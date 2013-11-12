from django.contrib import admin
from django.forms import forms
from devdays_app.models import Comment, Group, Role, UserProfile, Idea, Project, Event, Notification


class IdeaForm(forms.Form):
    subject = forms.TextInput()
    text = forms.Textarea()


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


class NotificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Notification, NotificationAdmin)
