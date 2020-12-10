from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.conf.urls import url,include



urlpatterns = [
    path('',views.main, name='home'),
    path('note_delete/<int:noteid>/', views.delete_note, name='note_delete'),
    path('api/noteall/', views.NoteList.as_view(), name='notes'),
    url(r'api/noteall/noteid/(?P<pk>[0-9]+)/$',views.Notesingle.as_view(),name='singlenote')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
