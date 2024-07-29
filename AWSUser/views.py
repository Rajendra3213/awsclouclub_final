from django.shortcuts import render,redirect
from .forms import AWSMembershipRegisterForm,AWSMembershipLoginForm
from django.views import View
from django.contrib.auth import authenticate,login,logout

class MembershipRegister(View):
    def get(self,request):
        form = AWSMembershipRegisterForm()
        return render(request, 'AWSUser/User_Register.html', {'form': form})
    def post(self,request):
        form=AWSMembershipRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            return redirect('AWSUser:login')
        else:
            return render(request, 'AWSUser/User_Register.html', {'form': form})

class MembershipLogin(View):
    def get(self,request):
        form=AWSMembershipLoginForm()
        return render(request,'AWSUser/User_Login.html',{'form': form})
    def post(self,request):
        form=AWSMembershipLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)        
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')
                else:
                    form.add_error(None, 'Your account is inactive.')
            else:
                form.add_error(None, 'Invalid email or password')
        return render(request, 'AWSUser/User_Login.html', {'form': form})
    
class MembershipLogout(View):
    def get(self,request):
        logout(request)
        return redirect('home:home')