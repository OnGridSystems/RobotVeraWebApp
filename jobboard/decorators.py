from __future__ import unicode_literals
import functools
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.decorators import available_attrs

from account.compat import is_authenticated
from account.utils import handle_redirect_to_login
from .models import Employer, Candidate


def choose_role_required(func=None, redirect_field_name=REDIRECT_FIELD_NAME, redirect_url=None):
    """
    Decorator for views that checks that the user choose his role, redirecting
    to the choose page if necessary.
    """
    def decorator(view_func):
        @functools.wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            try:
                Employer.objects.get(user=request.user)
            except Employer.DoesNotExist:
                try:
                    Candidate.objects.get(user=request.user)
                except Candidate.DoesNotExist:
                    return handle_redirect_to_login(
                        request,
                        redirect_field_name=redirect_field_name,
                        login_url=redirect_url
                    )
            if is_authenticated(request.user):
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    if func:
        return decorator(func)
    return decorator