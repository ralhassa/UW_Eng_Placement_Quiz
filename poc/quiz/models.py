from django.db import models

class Results(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    OUTLOOK = models.CharField(max_length=200)
    TEMPERATURE = models.CharField(max_length=200)
    HUMIDITY = models.CharField(max_length=200)
    WINDY = models.CharField(max_length=200)
    PLAY = models.CharField(max_length=200)

    def __str__(self):
        return_value = (
                        str(self.name) + " , " +
                        str(self.email) + " , " +
                        str(self.OUTLOOK) + " , " +
                        str(self.TEMPERATURE) + " , " +
                        str(self.HUMIDITY) + " , " +
                        str(self.WINDY) + " , " +
                        str(self.PLAY)
                        )
        return return_value
