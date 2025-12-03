from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Choices for the 1-5 scoring system
SCORE_CHOICES = [(i, str(i)) for i in range(1, 6)]

class Content(models.Model):
    """Represents a movie or TV show the admin adds to the platform."""
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def average_quality_score(self):
        """Calculates the average Quality Score from all reviews."""
        # Use aggregation to calculate the average efficiently
        return self.review_set.aggregate(Avg('quality_score'))['quality_score__avg']

    @property
    def average_binge_risk_score(self):
        """Calculates the average Binge-Watch Risk Score from all reviews."""
        return self.review_set.aggregate(Avg('binge_risk_score'))['binge_risk_score__avg']

class Review(models.Model):
    """Represents a user's specific review for a piece of content."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    
    # 🌟 CORE SCORING LOGIC 🌟
    quality_score = models.DecimalField(max_digits=2, decimal_places=1, default=3.0) 
    binge_risk_score = models.DecimalField(max_digits=2, decimal_places=1, default=3.0) 
    
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can only review the same content once
        unique_together = ('user', 'content')

    def __str__(self):
        return f'{self.user.username} review for {self.content.title}'