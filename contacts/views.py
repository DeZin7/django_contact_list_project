from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 2)

    page_number = request.GET.get('p')
    contacts = paginator.get_page(page_number)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })

def see_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/see_contact.html', {
        'contact': contact
    })

