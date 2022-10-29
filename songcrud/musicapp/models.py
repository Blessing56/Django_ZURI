from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'


class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.content) > 50:
            return f"{self.content[0:50]}..."
        else:
            return f"{self.content}"