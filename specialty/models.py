from django.db import models


class Specialty(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media/specialties/', default='media/specialties/default.png')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'
