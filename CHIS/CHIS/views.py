# This is the view file for the CHIS project
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from chis_sl.forms import ContactForm
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


# this view is used to display the content of the about page
class AboutView(TemplateView):
    template_name = 'about.html'


# This view is used to display the content of the Contact Form
def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['bigsahkall@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            return redirect('success')
    return render(request, "contact_us.html", {'form': form})


class SuccessView(TemplateView):
    template_name = 'success.html'
