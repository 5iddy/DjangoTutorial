from django.shortcuts import redirect


def unauthenticated_user_only(view_func, redirect_url='home'):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func