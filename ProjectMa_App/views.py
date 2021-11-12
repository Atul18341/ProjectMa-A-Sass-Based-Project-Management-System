from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import ProjectForm,GroupDetailsForm,ProjectReportPPTForm
from .models import MCE_CSE_Faculties,MCE_Student_Records

# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,"index.html",{})

class ProjectFormView(View):
    def get(self,request):
        pform=ProjectForm()
        return render(request,"ProjectForm.html",{"projectform":pform})

    def post(self,request):
        pform=ProjectForm(request.POST)
        if pform.is_valid():
            group=pform.cleaned_data['Group_Name']
            form = MCE_Student_Records.objects.get(Group_Name=group)
            form.save()
            name = pform.cleaned_data['Mentor_Teacher']
            count = MCE_CSE_Faculties.objects.get(faculty_name=name)
            count.project_count += 1
            count.save()
            return redirect("Confirmation")

class LoginView(View):
    def get(self, request):
        form=AuthenticationForm()
        return render(request,"login.html",{"form":form})
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("ProjectForm")
        return render(request, "login.html")

class ConfirmationView(View):
    def get(self,request):
        return render(request,"confirmation.html")

class SignUpView(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,"Register.html",{"form":form})
    def post(self,request):
        form=GroupDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

class ProjectDashboardView(View):
    def get(self,request):
        return render(request,"ProjectDashboard.html")

class GroupFormView(View):
    def get(self,request):
        GroupForm=GroupDetailsForm()
        return render(request,"GroupDetails.html",{"GroupForm":GroupForm})
    def post(self,request):
        GroupForm=GroupDetailsForm(request.POST)
        GroupForm.save()
        return redirect("Dashboard")

class ProjectReportPPTFormView(View):
    def get(self,request):
        ReportForm=ProjectReportPPTForm()
        return render(request,"ProjectReport&PPT.html",{"ReportForm":ReportForm})
    def post(self,request):
        ReportForm=ProjectReportPPTForm(request.POST,request.FILES)
        if ReportForm.is_valid():
            group = ReportForm.post['Group_Name']
            form = MCE_Student_Records.objects.get(Group_Name=group)
            form.Project_PPT = ReportForm.post['Project_PPT']
            form.Project_Report = ReportForm.post['Project_Report']
            form.save()
        return redirect("Dashboard")