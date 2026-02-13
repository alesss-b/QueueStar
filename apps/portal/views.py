from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Example view with login required:
# class PortalView(LoginRequiredMixin, TemplateView):
#     """Portal default view; redirects to login if not authenticated."""
#     login_url = 'login'
#     template_name = 'pages/portal_dashboard.html'

class PortalView(TemplateView):
    """Portal default view; redirects to login if not authenticated."""
    template_name = 'pages/portal_dashboard.html'


class ServiceTicketFormView(TemplateView):
    """Service Ticket Form view."""
    template_name = 'pages/service_ticket_form.html'


class ServiceTicketDetailsView(TemplateView):
    """Service Ticket Details view."""
    template_name = 'pages/service_ticket_details.html'

class ServiceTicketCancellationFormView(TemplateView):
    """Service Ticket Cancellation Form view."""
    template_name = 'pages/service_ticket_cancellation_form.html'
