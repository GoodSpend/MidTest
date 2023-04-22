from django.urls import path
from django.contrib.auth.decorators import login_required
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', show_posts, name='show_posts'),
    path('create', create_post, name='create_post'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('modify/<int:id>', modify_post, name='modify_post'),
    path('delete/<int:id>', delete_post, name='delete_post'),
    path('create-ajax/', create_post_ajax, name='create_post_ajax'),
]