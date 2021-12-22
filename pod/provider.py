from allauth.account.models import EmailAddress
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class Scope(object):
    EMAIL = 'email'
    PROFILE = 'profile'
    PROFILE_PICTURE = 'profile_picture'
    PROFILE_NICKNAME = 'profile_nickname'


class PodAccount(ProviderAccount):
    pass


class PodProvider(OAuth2Provider):
    id = 'pod'
    name = 'Pod'
    account_class = PodAccount

    def extract_uid(self, data):
        return str(data['id'])

    def get_default_scope(self):
        return [
            Scope.EMAIL, Scope.PROFILE, Scope.PROFILE_PICTURE, Scope.PROFILE_NICKNAME,
        ]

    def extract_common_fields(self, data):
        return dict(
            email=data.get('email'),
            last_name=data.get('family_name'),
            first_name=data.get('given_name'),
        )

    def extract_email_addresses(self, data):
        ret = []
        email = data.get('email')
        if email and data.get('email_verified'):
            ret.append(EmailAddress(email=email, verified=True, primary=True))
        return ret


provider_classes = [PodProvider]
