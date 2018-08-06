from __future__ import unicode_literals
from django.db import models


class Cat(models.Model):
    GENDER_CHOICES = (
        (u'Кот', u'Мальчик'),
        (u'Кошка', u'Девочка'),
    )
    name = models.CharField(db_column="Name", max_length=40)
    age = models.CharField(db_column="Age", max_length=20)
    sex = models.CharField(db_column="Sex", max_length=10, choices=GENDER_CHOICES)
    image_url = models.URLField(db_column="Image_URL")

    class Meta:
        managed = True
        """Django создаст необходимые таблицы в базе данных при выполнении
                команды migrate и удалит их при выполнении flush."""
        db_table = 'Cat_Info'
