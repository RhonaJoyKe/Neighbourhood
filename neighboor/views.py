from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import Business, NeighbourHood, Post, Profile
from django.contrib.auth.decorators import login_required
from.forms import UpdateProfileForm,NeighbourhoodForm,PostForm,BusinessForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.admin = request.user
            neighborhood.save()
            messages.success(request,'Neighborhood created successfully.')
            return redirect('home')
    else:
        form = NeighbourhoodForm()
        neighborhoods = NeighbourHood.objects.all()
        neighborhoods = neighborhoods[::-1]
    return render(request, 'index.html', {'form': form, 'neighborhoods': neighborhoods})



  
def profile(request,user_id):
  	#Get the profile
    current_user=get_object_or_404(User,id=user_id)
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
    return render(request,'profile/profile.html',{'form':form})
def search_hood(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_hoods = NeighbourHood.search_by_name(search_term)
        print(searched_hoods)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"hoods": searched_hoods})
@login_required
def neighborhood(request, neighborhood_id):
    neighborhood = NeighbourHood.objects.get(id=neighborhood_id)
    if request.method == 'POST':
        form_post = PostForm(request.POST, request.FILES)
        business_form = BusinessForm(request.POST, request.FILES)
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.neighbourhood = neighborhood
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been added successfully.')
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.neighbourhood = neighborhood
            business.user = request.user
            business.save()
            messages.success(request, 'Business added successfully.')
            return redirect('neighbourhood', neighborhood_id)
    else:
        post_form = PostForm()
        business_form = BusinessForm()
        current_user = request.user
        neighborhood = NeighbourHood.objects.get(id=neighborhood_id)
        business = Business.objects.filter(neighbourhood_id=neighborhood)
        users = Profile.objects.filter(neighbourhood=neighborhood)
        posts = Post.objects.filter(neighbourhood=neighborhood)
    return render(request, 'neighbourhood.html', {'post_form':post_form, 'business_form': business_form, 'users':users,'current_user':current_user, 'neighborhood':neighborhood,'business':business,'posts':posts})
@login_required
def join_hood(request, neighborhood_id):
    neighborhood = get_object_or_404(NeighbourHood, id=neighborhood_id)
    request.user.profile.neighbourhood = neighborhood
    request.user.profile.save()
    return redirect('neighbourhood', neighborhood_id = neighborhood.id)
@login_required
def leave_hood(request, neighborhood_id):
    neighborhood = get_object_or_404(NeighbourHood, id=neighborhood_id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('home')



