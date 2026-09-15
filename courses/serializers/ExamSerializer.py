from rest_framework.serializers import *
from courses.models.course import Course

class ExamSerializer(Serializer):
    course_id = IntegerField()
    title = CharField()
    total_marks = IntegerField()
    date = DateTimeField()
    duration_minutes = IntegerField()

    def create(self, validated_date):
        return Course.objects.create(**self.validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.total_marks = validated_data.get('total_marks', instance.total_marks)
        instance.date = validated_data.get('date', instance.date)
        instance.duration_minutes = validated_data.get('duration_minutes', instance.duration_minutes)
        instance.save()
        return instance
# Create your models here.


