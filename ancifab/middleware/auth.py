from django.shortcuts import redirect

from ancifab.views import login


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if not request.session.get('customer'):
            returnurl = request.META['PATH_INFO']
            return redirect(f'/login?return_url={returnurl}')
            # print('middleware')
        response = get_response(request)
        return response

    return middleware