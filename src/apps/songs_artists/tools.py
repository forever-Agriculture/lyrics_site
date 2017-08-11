from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


class CancelButtonMixin(object):
    """Just a button that iterates over and over"""
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
             reverse('home')
            )
        return super().post(request, *args, **kwargs)
