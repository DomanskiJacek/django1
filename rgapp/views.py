from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# from . import models as RModels
from . import models
from django.forms import inlineformset_factory, Form
from django.template import Context, RequestContext
from django.forms import inlineformset_factory
from django.http import Http404

studx = models.Student()
studx.first_name = 'Alicja'
str_info = 'str_info'

obstud = models.StudentNoModel()
store_form = models.RgannForm()


def rgann(request):
    sFromForm = ''
    form = models.RgannModelForm()
    if request.method == 'POST':
        context_instance = RequestContext(request)
#        event_form = EventForm(request.POST, instance=event)
        form = models.RgannModelForm(request.POST)
        # form.body += 'a'          #exception !
        if form.is_valid():
#            print('rgann(request): form.is_valid()')
            sFromForm = form.cleaned_data['rgapattern']

            form.save()
            # form.rgatext += 'vv'

            # return render(request, 'rgann.html', {'form1': form})
            # return HttpResponseRedirect('rgann2')
            # return redirect("rgann2")             # causes the page reload ? (blank page shows)
    ctx = {'form1': form, 'stoform': sFromForm, 'stoform2': sFromForm + '; text added in views.rgann'}
    # ctx['stoform'] = sFromForm
    # ctx['stoform2'] = sFromForm + '; text added in views.rgann2'

#    print('rgann2(request): not POST  request.method:', request.method)
    return render(request, 'rgann.html', ctx)
