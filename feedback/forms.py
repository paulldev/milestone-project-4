from django import forms
from .models import PoolTable, Review


class TableForm(forms.ModelForm):
    class Meta:
        model = PoolTable
        fields = ('table_number', 'clean_rating', 'damage_rating')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'table_number': 'Table Number',
            'clean_rating': 'How clean is the table',
            'damage_rating': 'How damaged is the table',
        }

        self.fields['table_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'review_text')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'rating': 'Rate your overall experience',
            'review_text': 'Suggestions for improvement',
        }

#        self.fields['table_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False