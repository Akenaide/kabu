from django import forms

from tournaments import models


class MatchResultForm(forms.ModelForm):
    is_double_loss = forms.BooleanField(required=False)
    standing = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = models.MatchResult
        fields = ["winner", "loser", "is_double_loss", "standing"]

    def __init__(self, players=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if players is not None:
            self.fields["winner"].queryset = players
            self.fields["loser"].queryset = players

    def clean(self):
        cleaned_data = super().clean()
        winner = cleaned_data.get("winner")
        loser = cleaned_data.get("loser")

        if not winner or not loser:
            raise forms.ValidationError("Both winner and loser must be selected.")
        if winner == loser:
            raise forms.ValidationError("Winner and loser must be different players.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
