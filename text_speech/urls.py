import django.urls as urls
import text_speech.views as views

app_name = "text_speech"

urlpatterns = [
    urls.path(route="", view=views.text_speech.as_view(), name=app_name)
]