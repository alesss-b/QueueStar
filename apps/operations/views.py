from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Example login required view:
# class OperationsView(LoginRequiredMixin, TemplateView):
#     """Operations default view; redirects to login if not authenticated."""
#     login_url = 'login'
#     template_name = 'pages/operations_dashboard.html'


class OperationsView(TemplateView):
    """Operations default view; redirects to login if not authenticated."""
    template_name = 'pages/operations_dashboard.html'

class ServiceFormView(TemplateView):
    """Service Form page view."""
    template_name = 'pages/service_form.html'

class ServiceDetailsView(TemplateView):
    """Service Details page view."""
    template_name = 'pages/service_details.html'

class ServiceTicketFulfillmentFormView(TemplateView):
    """Service Ticket Fulfillment Form view."""
    template_name = 'pages/service_ticket_fulfillment_form.html'