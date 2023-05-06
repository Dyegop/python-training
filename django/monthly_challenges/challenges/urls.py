from django.urls import path
from . import views

# URLs are included in a list of path objects
urlpatterns = [
    # PATH
    # Django path function returns an element for inclusion in urlpatterns
    # For example, path('january', views.january) recieves the url path your/url/january and returns the given view

    # PLACEHOLDERS
    # <text> is a Django placeholder. The placeholder must match the argument passed in the called function
    # (in this case, monthly_challenge)

    # PATH CONVERTERS
    # We can add a path converter to convert a path into a datatype
    # For example, adding 'int:' converts the path to an integer
    # By default, paths are strings

    # NAME ARGUMENT
    # We can add a name to an url to construct paths that points to that url
    # Bulding an url using name arg allows you to point to this url even if the path is changed

    path('', views.index),  # path to /challenges/
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='month-challenge'),

]
