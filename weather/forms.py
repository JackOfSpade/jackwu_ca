import django.forms as forms
from django.core.exceptions import ValidationError

import weather.retrieve_info_class as retrieve_info_class

exercise_choices = (
    ("walking", "Walking"),
    ("jogging", "Jogging"),
    ("cycling", "Cycling")
)

unit_choices = (
    ("imperial", "Imperial"),
    ("metric", "Metric")
)


class input_form(forms.Form):
    exercise = forms.ChoiceField(label="Exercise", choices=exercise_choices)
    unit = forms.ChoiceField(label="Unit", choices=unit_choices)
    zip_postal = forms.CharField(label="Zip/Postal Code", max_length=7)

    def clean_zip_postal(self):
        data = self.cleaned_data["zip_postal"]
        accuweather_api_key = retrieve_info_class.retrieve_info.get_accuweather_api_key(0)
        location = retrieve_info_class.retrieve_info.get_location(accuweather_api_key, data)

        if location is None:
            raise ValidationError("Zip/postal code is invalid.")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

