
import django.urls as urls
import homepage.views as views

app_name = "homepage"

urlpatterns = [
    urls.path(route="", view=views.homepage.as_view(), name=app_name)
]
