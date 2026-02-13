from django.urls import path

from . import views

urlpatterns = [
    path('', views.PortalView.as_view(), name="portal"),
    path('service_ticket/details', views.ServiceTicketDetailsView.as_view(), name='service_ticket_details'),
    path('service_ticket/create', views.ServiceTicketFormView.as_view(), name='create_service_ticket'),
    path('service_ticket/edit', views.ServiceTicketFormView.as_view(), name='edit_service_ticket'),
    path('service_ticket/cancel', views.ServiceTicketCancellationFormView.as_view(), name='cancel_service_ticket')
]