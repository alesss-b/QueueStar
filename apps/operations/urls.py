from django.urls import path

from . import views

urlpatterns = [
    path('', views.OperationsView.as_view(), name='operations'),
    path('service/details', views.ServiceDetailsView.as_view(), name="service_details"),
    path('service/create', views.ServiceFormView.as_view(), name="create_service"),
    path('service/edit', views.ServiceFormView.as_view(), name="edit_service"),
    path("service_ticket/fulfill", views.ServiceTicketFulfillmentFormView.as_view(), name='fulfill_service_ticket')
]