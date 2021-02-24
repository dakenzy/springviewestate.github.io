from django.db import models


# Create your models here.
class Gender(models.Model):
    sexuality = models.CharField(max_length=10)

    def __str__(self):
        return self.sexuality


class HseNumber(models.Model):
    code = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.code)


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Residents(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    id_number = models.PositiveIntegerField()
    mobile_number = models.PositiveIntegerField()
    hse_number = models.ForeignKey(HseNumber, on_delete=models.CASCADE)

    def __str__(self):
        return self.surname


class Occupants(models.Model):
    fullname = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    hse_number = models.ForeignKey(HseNumber, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Staff(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    id_number = models.PositiveIntegerField()
    mobile_number = models.PositiveIntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname
