import django.views.generic.base as base
import django.http as http
import django.shortcuts as shortcuts
import weather.forms as forms
import weather.interface as interface
import json

class weather(base.TemplateView):
    template_name = "weather/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.input_form()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        # create a form instance and populate it with data from the request:
        form = forms.input_form(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data
            type_of_person = form.cleaned_data["type_of_person"]
            exercise = form.cleaned_data["exercise"]
            unit = form.cleaned_data["unit"]
            zip_postal = form.cleaned_data["zip_postal"]

            results_matrix = interface.get_results_matrix(type_of_person, unit, exercise, zip_postal)
            # return shortcuts.render(request, "weather/index.html", context={"form":form, "results_matrix": results_matrix.tolist()})=
            return http.JsonResponse({"results_matrix": results_matrix.tolist()}, status=200)
        else:
            return http.JsonResponse({"error": form.errors}, status=400)

