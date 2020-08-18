import django.views.generic.base as base

class ML_reviews(base.TemplateView):
    template_name = "ML_reviews/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context