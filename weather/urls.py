import django.urls as urls
import weather.views as views

app_name = "weather"

urlpatterns = [
    urls.path(route="", view=views.weather.as_view(), name=app_name)
]