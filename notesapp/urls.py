from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path


urlpatterns = [
    path('',views.main, name='home'),
    path('note_delete/<int:noteid>/', views.delete_note, name='note_delete'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
