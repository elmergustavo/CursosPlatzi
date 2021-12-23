from django.contrib import admin

from courses.models import Course, Material, Teacher, Video, Comment

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'ranking')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('url',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
