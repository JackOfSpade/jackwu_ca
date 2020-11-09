import django.views.generic.base as base
import django.http as http
import text_speech.forms as forms
import text_speech.amazon_polly as amazon_polly

class text_speech(base.TemplateView):
    template_name = "text_speech/index.html"

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
            text = form.cleaned_data["text"]
            voice = form.cleaned_data["voice"]
            speed = request.POST["speed"]

            # Test
            return_text = amazon_polly.amazon_polly(text=text, voice=voice, speed=speed)
            return http.JsonResponse({"return_text": return_text}, status=200)
        else:
            return http.JsonResponse({"error": form.errors}, status=400)

