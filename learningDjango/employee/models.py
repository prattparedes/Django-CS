from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

# create Table 'employee_employee' (
#     'id' Int NOT NULL PRIMARY KEY AUTOINCREMENT,
#     'name': varchar(255) NOT NULL,
#     'title': varchar(255) NOT NULL,
# )