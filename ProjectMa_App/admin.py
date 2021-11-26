from django.contrib import admin
from .models import Semester,MCE_CSE_Faculties,MCE_Student_Records,MCE_Student_Details,ReportDetails
# Register your models here.
admin.site.register(Semester)
admin.site.register(MCE_CSE_Faculties)
admin.site.register(MCE_Student_Records)
admin.site.register(MCE_Student_Details)
admin.site.register(ReportDetails)