from django.urls import path
from .views import home, portfolio,root_page, home_detail, learning_context, using_bootstrap
urlpatterns = [
    path("home/<int:id>/detail", home_detail, name="home_detail" ),
    path("portfolio/", portfolio, name="portfolio"),
    path("learning-context/", learning_context, name="learning_context"),
    path("using-bootstrap/", using_bootstrap, name = "u_boots"),
    # path("template-inheritance/", )
    path("", root_page, name="root_page"),
    # path("", root_page, name="root_page"),


    path("", home),
]