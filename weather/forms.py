import django.forms as forms

exercise_choices = (
    ("walking", "Walking"),
    ("jogging", "Jogging"),
    ("cycling", "Cycling")
)

unit_choices = (
    ("imperial", "Imperial"),
    ("metric", "Metric")
)


class exercise_form(forms.Form):
    exercise = forms.ChoiceField(label="Exercise", choices=exercise_choices)

class unit_form(forms.Form):
    unit = forms.ChoiceField(label="Unit", choices=unit_choices)

class zip_postal_form(forms.Form):
    zip_postal = forms.CharField(label="Zip/Postal Code", max_length=7)