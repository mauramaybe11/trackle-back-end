from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Log(models.Model):
  """Log model"""
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  game = models.CharField(max_length=100)
  word = models.CharField(max_length=100)
  guesses = models.IntegerField()
  date_guessed = models.DateField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The game is'{self.game}' and word is {self.word} which took {self.guesses} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Log models"""
    return {
        'id': self.id,
        'game': self.game,
        'word': self.word,
        'guesses': self.guesses,
        'date_guessed': self.date_guessed,
        'owner': self.owner
    }
