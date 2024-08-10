from django.db import models

# Create your models here.
class SongInfo(models.Model):
    choice_field = ((1,1),
                    (2,2),
                    (3,3),
                    (4,4),
                    (5,5)
                    )
    song_id = models.CharField(max_length=300,null=True,db_index=True)
    title = models.CharField(max_length=200,null=True)
    danceability = models.FloatField(default=0.0,null=True)
    energy =  models.FloatField(default=0.0,null=True)
    mode = models.IntegerField(default=0,null=True)
    acousticness = models.FloatField(default=0.0,null=True)
    tempo = models.FloatField(default=0.0,null=True)
    duration_ms = models.FloatField(default=0.0,null=True)
    num_sections = models.IntegerField(default=0,null=True)
    num_segments = models.IntegerField(default=0,null=True)
    star_rating = models.IntegerField(default=0,choices=choice_field,null=True)

        
