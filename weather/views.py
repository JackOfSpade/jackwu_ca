import django.views.generic.base as base
import django.http as http
import django.shortcuts as shortcuts
import weather.forms as forms
import weather.interface as interface

class weather(base.TemplateView):
    template_name = "weather/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.input_form()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        exercise = None
        unit = None
        zip_postal = None
        results_matrix = None

        # if this is a POST request we need to process the form data
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = forms.input_form(request.POST)

            # check whether it's valid:
            if form.is_valid():
                # process the data
                exercise = form.cleaned_data["exercise"]
                unit = form.cleaned_data["unit"]
                zip_postal = form.cleaned_data["zip_postal"]

                results_matrix = interface.get_results_matrix(unit, exercise, zip_postal)

        # GET request
        else:
            # Blank form
            form = forms.input_form()

        return shortcuts.render(request, "weather/index.html", {"form": form, "results_matrix": results_matrix})
