
from django.urls import path
from .views import home_page_view,home_page_result

urlpatterns = [
    
    path("view/",home_page_view),
    path("result/",home_page_result)
]