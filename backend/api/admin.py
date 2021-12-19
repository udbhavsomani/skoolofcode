from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Subject, AvailableTiming


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'is_staff',
        'is_teacher', 'is_student',
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_student', 'is_teacher')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_student', 'is_teacher',)
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    fields = ('name', 'teacher')


admin.site.register(Subject, SubjectAdmin)


class AvailableTimingAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'e_n', 'n_t', 't_e',
                    'e_t', 't_o', 'o_t', 't_th')
    fields = ('teacher', 'e_n', 'n_t', 't_e', 'e_t', 't_o', 'o_t', 't_th')


admin.site.register(AvailableTiming, AvailableTimingAdmin)
