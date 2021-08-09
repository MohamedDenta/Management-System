from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from EmployeeApp import views

urlpatterns = [
                  url(r'^department$', view=views.departmentApi),
                  url(r'^department/([0-9]+)$', view=views.departmentApi),

                  url(r'^employee$', view=views.employeeApi),
                  url(r'^employee/([0-9]+)$', view=views.employeeApi),

                  url(r'^employee/savefile', views.SaveFile),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
