from django.db import models

class GenderChoices(models.Model):
    GENDER_CHOICES = [
        ('erkek', 'Erkek'),
        ('kadın', 'Kadın'),
    ]
    class Meta:
        abstract = True
         
class DateChoices(models.Model):
    DAY_CHOICES = [
        ('pazartesi', 'Pazartesi'),
        ('salı', 'Salı'),
        ('çarşamba', 'Çarşamba'),
        ('perşembe', 'Perşembe'),
        ('cuma', 'Cuma'),
    ]
    TIME_CHOICES = [
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
    ]
    class Meta:
        abstract = True

class NameandSurname(models.Model):
    name = models.CharField(max_length = 15, null = True, blank = True)
    surname = models.CharField(max_length = 15, null = True, blank = True)

    class Meta:
        abstract = True        

class Hospital(NameandSurname, GenderChoices, DateChoices):
    POLİCLİNİC_CHOICES = [ # Python'da sabitler, büyük harflerle yazılır. Teknik bir şey değil ama yazılım kültürüdür.
        ('dahiliye', 'Dahiliye'),
        ('kbb', 'KBB'),
        ('onkoloji', 'Onkoloji'),
        ('psikoloji', 'Psikoloji'),
        ('radyoloji', 'Radyoloji'),
        ('nöroloji', 'Nöroloji'),
        ('kardiyoloji', 'Kardiyoloji'),
    ]
    
    policlinic = models.TextField(
        max_length = 20,
        choices = POLİCLİNİC_CHOICES,
    )
    gender = models.CharField(max_length = 5, choices = GenderChoices.GENDER_CHOICES)
    day = models.CharField(max_length = 9, choices = DateChoices.DAY_CHOICES)
    time = models.CharField(max_length = 5, choices = DateChoices.TIME_CHOICES)

class Sport(NameandSurname, GenderChoices, DateChoices):
    gender = models.CharField(max_length = 5, choices = GenderChoices.GENDER_CHOICES)
    day = models.CharField(max_length = 9, choices = DateChoices.DAY_CHOICES)
    time = models.CharField(max_length = 5, choices = DateChoices.TIME_CHOICES)

class Dental_Clinic(NameandSurname, GenderChoices, DateChoices,):
    gender = models.CharField(max_length = 5, choices = GenderChoices.GENDER_CHOICES)
    day = models.CharField(max_length = 9, choices = DateChoices.DAY_CHOICES)
    time = models.CharField(max_length = 5, choices = DateChoices.TIME_CHOICES)

class Hair_Dresser(NameandSurname, DateChoices):
    day = models.CharField(max_length = 9, choices = DateChoices.DAY_CHOICES)
    time = models.CharField(max_length = 5, choices = DateChoices.TIME_CHOICES)