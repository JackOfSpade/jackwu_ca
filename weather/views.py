import django.views.generic.base as base

class weather(base.TemplateView):
    template_name = "weather/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context