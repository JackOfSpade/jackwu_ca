import django.views.generic.base as base
import django.http as http
import django.shortcuts as shortcuts
import weather.forms as forms

class weather(base.TemplateView):
    template_name = "weather/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["exercise_form"] = forms.exercise_form()
        context["unit_form"] = forms.unit_form()
        context["zip_postal_form"] = forms.zip_postal_form()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        # if this is a POST request we need to process the form data
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            exercise_form = forms.exercise_form(request.POST)
            unit_form = forms.unit_form(request.POST)
            zip_postal_form = forms.zip_postal_form(request.POST)

            # check whether it's valid:
            if exercise_form.is_valid() and unit_form.is_valid() and zip_postal_form.is_valid():
                # process the data
                exercise = exercise_form.cleaned_data["exercise"]
                unit = unit_form.cleaned_data["unit"]
                zip_postal = zip_postal_form.cleaned_data["zip_postal"]

                # CONTINUE PROCESSING THE DATA INTO THE APP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # GET request
        else:
            # Blank form
            exercise_form = forms.exercise_form()
            unit_form = forms.unit_form()
            zip_postal_form = forms.zip_postal_form()

        return shortcuts.render(request, "weather/index.html", {"exercise_form": exercise_form, "unit_form": unit_form, "zip_postal_form": zip_postal_form})