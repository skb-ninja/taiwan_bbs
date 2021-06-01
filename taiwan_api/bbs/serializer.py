from rest_framework import serializers

from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject_name', 'professor', 'credit', 'university', 'region', 'faculty',
                  'difficulty', 'required_level', 'comment', 'created_at', 'updated_at')
