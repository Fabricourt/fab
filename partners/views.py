from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from.models import Partner

def index(request):
  partners = Partner.objects.order_by('-membership_date').filter(is_published=True)

  paginator = Paginator(partners, 6)
  page = request.GET.get('page')
  paged_partners = paginator.get_page(page)

  context = {
    'partners': paged_partners
  }

  return render(request, 'partners/partners.html', context)

def partner(request, partner_id):
  partner = get_object_or_404(Partner, pk=partner_id)

  context = {
    'partner': partner
  }

  return render(request, 'partners/partner.html', context)

