import django.contrib.admin as admin
import django.urls as urls

app_name = "root"

urlpatterns = [
    urls.path(route="admin/", view=admin.site.urls, name="admin"),
    urls.path(route="", view=urls.include("homepage.urls"), name="homepage"),
    urls.path(route="ML_reviews/", view=urls.include("ML_reviews.urls"), name="ML_reviews"),
    urls.path(route="analysis/", view=urls.include("analysis.urls"), name="analysis"),
    urls.path(route="weather/", view=urls.include("weather.urls"), name="weather"),
    urls.path(route="text_speech/", view=urls.include("text_speech.urls"), name="text_speech")
]
