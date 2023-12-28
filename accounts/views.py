from django.shortcuts import render,redirect
from django.views.generic import FormView
from. forms import UserRegisterationForm,UpdateUserForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views import View

# Create your views here.
class UserRegistrationView(FormView):
    template_name='registration.html'
    form_class=UserRegisterationForm
    success_url=reverse_lazy('register')
    def form_valid(self,form):
        print(form.cleaned_data)
        user=form.save()
        print(user)
        login(self.request,user)

        return super().form_valid(form)#form valid function call hobe jodi sob thik thake

class UserLoginView(LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')

class UserBankAccountupdateView(View):
    template_name='profile.html'

    def get(self,request):
        form=UpdateUserForm(instance=request.user)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=UpdateUserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,self.template_name,{'form':form})