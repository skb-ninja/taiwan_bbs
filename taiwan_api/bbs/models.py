from django.db import models

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    credit = models.IntegerField()
    university = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    faculty = models.CharField(max_length=20)
    difficulty = models.IntegerField()
    required_level = models.CharField(max_length=10)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # データ収集
    clicked_count = models.IntegerField()

    def __str__(self) -> str:
        return self.subject_name
