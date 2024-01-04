from django.db import models
# from fee_api import StudentSerializers


# Create your models here.



# Create your models here.
#Create college models 

class Student(models.Model):
    #change gareko jasto gareko git lai ullu banako
    # student_name=models.CharField(max_length=100)
    student_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    conform_password=models.CharField(max_length=10)
    register_date=models.DateTimeField(auto_now=True)
    
    # types=models.CharField(max_length=100,choices=
    #                        (('IT','IT'),
    #                         ('Non IT','Non IT'),
    #                         ('Mobile phones','Mobile phones')
    #                         ))
    # about=models.TextField()
    # active=models.BooleanField(default=True)




