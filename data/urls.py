from django.urls import path
from .views import *

app_name = 'data'

urlpatterns = [
    path('', show_data, name='show_data'),
    path('create_data/', create_data, name='create_data'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('modify/<int:id>', modify_data, name='modify_data'),
    path('delete/<int:id>', delete_data, name='delete_data'),
    path('create-ajax/', create_data_ajax, name='create_data_ajax'),
    ]