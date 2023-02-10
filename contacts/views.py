from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Contact


def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        show=True
    )
    paginator = Paginator(contacts, 2)

    page_number = request.GET.get('p')
    contacts = paginator.get_page(page_number)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })

def see_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if not contact.show:
        raise Http404()


    return render(request, 'contacts/see_contact.html', {
        'contact': contact
    })


def search(request):
        term = request.GET.get('term')

        if term is None or not term:
             raise Http404

        fields = Concat('name',Value(' '), 'surname')

        contacts = Contact.objects.annotate(
             full_name=fields
        ).filter(
             Q(full_name__icontains=term) | Q(phone_number__icontains=term)
        )

        print(term)

        # contacts = Contact.objects.order_by('-id').filter(
        #     Q(name__icontains = term) | Q(surname__icontains=term),
        #     show=True
        # )
        paginator = Paginator(contacts, 2)

        page_number = request.GET.get('p')
        contacts = paginator.get_page(page_number)

        return render(request, 'contacts/search.html', {
            'contacts': contacts
        })

