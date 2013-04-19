from django.conf.urls import patterns, include, url
from views import ListNoteView, CreateNoteView, UpdateNoteView, DeleteNoteView, NoteView

urlpatterns = patterns('',

       url(r'^delete/(?P<pk>\d+)/$', DeleteNoteView.as_view(), name='notes-delete'),                       
       url(r'^create/$',CreateNoteView.as_view(), name='notes-create',),
       url(r'^$', ListNoteView.as_view(), name='notes-list',),    
       url(r'^edit/(?P<pk>\d+)/$', UpdateNoteView.as_view(), name='notes-edit',), 
       url(r'^(?P<pk>\d+)/$', NoteView.as_view(), name='notes-view',),             )
