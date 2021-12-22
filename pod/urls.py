from django.urls import include, path

from allauth.utils import import_attribute

from pod.provider import PodProvider


def default_urlpatterns(provider):
    login_view = import_attribute(provider.get_package() + ".views.oauth2_login")
    callback_view = import_attribute(provider.get_package() + ".views.oauth2_callback")

    patterns = [
        path("login/", login_view, name=provider.id + "_login"),
        path("callback", callback_view, name=provider.id + "_callback"),
    ]

    return [path(provider.get_slug() + "/", include(patterns))]


urlpatterns = default_urlpatterns(PodProvider)
