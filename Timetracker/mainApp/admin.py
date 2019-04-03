from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import admin
from mainApp.models import *


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(JournalPost)
admin.site.register(NewsPost)

class MyUserAdmin(UserAdmin):
    def get_fieldsets(self, request, obj=None):


        if request.user.is_superuser:
            perm_fields = ('is_active', 'is_staff', 'is_superuser',
                           'groups', 'user_permissions')
        else:
            # modify these to suit the fields you want your
            # staff user to be able to edit
            perm_fields = ('is_active', )

        return [(None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': perm_fields}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')})]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)