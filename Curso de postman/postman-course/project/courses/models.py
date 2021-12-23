from django.db import models

# Create your models here.

VIDEO_PROVIDERS = (
    ('A', 'Provider A'),
    ('B', 'Provider B'),
    ('C', 'Provider C'),
    ('YouTube', 'YouTube'),
)


class Course(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    teachers = models.ManyToManyField("courses.Teacher", blank=True)
    ranking = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    badge = models.ImageField(upload_to='badges', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    course = models.ForeignKey(
        Course, related_name='materials', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    current_job = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    material = models.ForeignKey(
        Material, related_name='videos', on_delete=models.CASCADE
    )
    provider = models.CharField(max_length=50, choices=VIDEO_PROVIDERS)
    url = models.URLField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.provider} {self.material.title}'


class Comment(models.Model):
    material = models.ForeignKey(
        Material, related_name='comments', on_delete=models.CASCADE
    )
    content = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
