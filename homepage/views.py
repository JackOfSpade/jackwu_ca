import django.views.generic.base as base

class homepage(base.TemplateView):
    template_name = "homepage/landing/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context