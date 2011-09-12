from django import forms
from django.utils.translation import ugettext_lazy as _

from contact_form.forms import ContactForm as DefaultContactForm

class ContactForm(DefaultContactForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = _("Name")
        self.fields['email'].label = _("Email")
        self.fields['body'].label = _("Message")
