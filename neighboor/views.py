from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import Profile,UpdateProfileForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
 return render(request,'index.html')
def profile(request,user_id):

    current_user=get_object_or_404(User,id=user_id)
    # current_user = request.user
    
    profile = Profile.objects.filter(user = current_user.id).first()
    
    return render(request, 'profile/profile.html', {"profile": profile})
  
def update_profile(request):
  	#Get the profile
    current_user=request.user
    profile = Profile.objects.filter(id=current_user.id).first()
    if request.method == 'POST':
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if  profileform.is_valid:
            profileform.save(commit=False)
            profileform.user=request.user
            profileform.save()
            return redirect('profile')
    else:
        form=UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'form':form})

