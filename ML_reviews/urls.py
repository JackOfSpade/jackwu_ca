import django.urls as urls
import ML_reviews.views as views


app_name = "ML_reviews"

urlpatterns = [
    urls.path(route="", view=views.ML_reviews.as_view(), name=app_name)
]