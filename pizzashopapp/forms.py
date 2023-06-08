from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=10, min_length=2,)
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "40", "rows": "5"}))
    rating = forms.IntegerField(max_value=5, min_value=1)

class AddInBascetForm(forms.Form):
    amount = forms.IntegerField()
