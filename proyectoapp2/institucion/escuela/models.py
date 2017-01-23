from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
    
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
    
    
class Materia(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.CharField(max_length=200, blank=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
  	
  	# def __str__(self):
   #      return self.name
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '%s' % (self.title)


class Profesor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.CharField(max_length=200, blank=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
  	
  	# def __str__(self):
   #      return self.name
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '%s' % (self.title)



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    # OJO creo que si no creas primero el META y hace el migratiosn 
    # te dara error luego para el serializable. crea de una
    def __str__(self):
            return self.title

