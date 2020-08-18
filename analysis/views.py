import django.views.generic.base as base

class stock(base.TemplateView):
    template_name = "analysis/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"]="analysis/stock/"
        return context

class crime(base.TemplateView):
    template_name = "analysis/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "analysis/crime/"
        return context
