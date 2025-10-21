from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=100)  # Название точки
    description = models.TextField()  # Краткое описание
    latitude = models.FloatField()  # Широта
    longitude = models.FloatField()  # Долгота
    buffer_radius = models.FloatField(default=0.01)  # Радиус буферной зоны в градусах (примерно 1 км)
    image = models.ImageField(upload_to='point_images/', null=True, blank=True)  # Поле для изображения
    year = models.PositiveIntegerField(null=True, blank=True, db_index=True)  # Год проведения (для поиска)

    def __str__(self):
        return self.name