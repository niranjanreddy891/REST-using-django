from django.db import models

class Employees(models.Model):
    id = models.IntegerField(primary_key=True, null=False)

    employee_name=models.CharField(max_length=255, null=False)

    manager_name=models.CharField(max_length=255, null=False)

    def _str_(self):
        return "{} - {} - {}".format(self.id, self.employee_name, self.manager_name)

