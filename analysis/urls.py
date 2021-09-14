import django.urls as urls
import analysis.views as views

app_name = "analysis"

urlpatterns = [
    urls.path(route="covid/", view=views.covid.as_view(), name="covid_" + app_name),
    urls.path(route="crime/", view=views.crime.as_view(), name="crime_" + app_name)
]
