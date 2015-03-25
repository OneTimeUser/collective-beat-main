from django.contrib.auth import user_logged_in
# from allauth.account.signals import user_logged_in
from django.contrib.sessions.models import Session
from django.dispatch import receiver


@receiver(user_logged_in)
def remove_user_sessions(sender, user, request, **kwargs):
    """
    Removing all previous user's sessions on login signal

    """
    from .models import UserSession

    # request = kwargs.get('request')
    current_session_key = request.session.session_key
    previous_user_sessions_data = UserSession.objects.filter(user=user)

    # finding and removing all the previous user sessions
    Session.objects \
        .filter(session_key__in=previous_user_sessions_data.values_list('session_key', flat=True)) \
        .delete()

    previous_user_sessions_data.delete()

    UserSession.objects.create(
        session_key=current_session_key,
        user=user,
        ip_address=request.META.get('REMOTE_ADDR', '')
    )
