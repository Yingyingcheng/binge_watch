# binge_watch_app/forms.py

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    # 🛑 REMOVE custom field definitions for quality_score and binge_risk_score

    class Meta:
        model = Review
        fields = ['quality_score', 'binge_risk_score', 'review_text']
        
        # 🌟 NEW: Use the widgets dictionary to force HTML5 range input 🌟
        widgets = {
            'quality_score': forms.NumberInput(attrs={
                'type': 'range', 
                'min': 1, 
                'max': 5, 
                'step': 0.1, # Allows for smoother slider movement (e.g., 3.5)
                'value': 3.0 # 🌟 ADD a starting value to prevent NaN 🌟
            }),
            'binge_risk_score': forms.NumberInput(attrs={
                'type': 'range', 
                'min': 1, 
                'max': 5, 
                'step': 0.1,
                'value': 3.0 # 🌟 ADD a starting value to prevent NaN 🌟
            }),
            'review_text': forms.Textarea(attrs={'rows': 4}),
        }