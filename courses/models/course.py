from django.db.models import *

# Create yourhere.
class Course(Model):
    name = CharField(max_length=50)
    code = CharField(max_length=7, unique=True)
    description = CharField(max_length=600)

    def __str__(self):
        return "%s %s" (self.name, self.code)
