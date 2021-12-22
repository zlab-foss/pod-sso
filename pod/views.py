import requests
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView

from pod.provider import PodProvider


class PodAdapter(OAuth2Adapter):
    provider_id = PodProvider.id

    access_token_url = 'https://accounts.pod.ir/oauth2/token/'
    profile_url = 'https://accounts.pod.ir/users'
    authorize_url = 'https://accounts.pod.ir/oauth2/authorize/'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(PodAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(PodAdapter)
