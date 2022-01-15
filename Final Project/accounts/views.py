
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, ProfileForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.





def login_view(request):
    template_name = "accounts/login.html"
    context = {}
    context["form"] = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)



        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if not User.objects.filter(username=username).exists():
                messages.warning(request, "User not found!")
                return render(request, template_name, context)
                
    
            user = authenticate(username=username, password=password)
    
            if user is not None:
                login(request, user)
                messages.success(request, "you're loging successfuly")
                return redirect("accounts:profile_view_just")
    
            else:
                messages.error(request, "Username or password is incorrect!")
                return render(request, template_name, context)
        else:
            messages.error(request, "error!")

    return render(request, template_name, context)



def logout_view(request):

    logout(request)
    messages.success(request, "Good Bye")

    #by below we will sent to the login page after logout from our page.
    return redirect("accounts:login")


@login_required()
def profile_view(request):
    template_name = 'accounts/profile.html'
    context = {}
    user = request.user

    initial = {
        "bio": user.profile.bio,
        "phone_number":user.profile.phone_number,
        "age":user.profile.age,
        "job":user.profile.job,
        "gender":user.profile.gender,
        "nc":user.profile.nc,
        "first_name":user.profile.first_name,
        "last_name":user.profile.last_name,
        "date_employment":user.profile.date_employment,
        "is_author":user.profile.is_author,
        "resume":user.profile.image
    }


    form = ProfileForm(request.POST or None, instance=user, initial=initial)

    form.fields["username"].disabled = True


    if request.method == 'POST':
        

        if form.is_valid():
            form.save()
            bio = form.cleaned_data['bio']
            user.profile.bio = bio

            phone_number = form.cleaned_data['phone_number']
            user.profile.phone_number = phone_number

            age = form.cleaned_data['age']
            user.profile.age = age

            job = form.cleaned_data['job']
            user.profile.job = job

            gender = form.cleaned_data['gender']
            user.profile.gender = gender

            nc = form.cleaned_data['nc']
            user.profile.nc = nc

            first_name = form.cleaned_data['first_name']
            user.profile.first_name = first_name

            last_name = form.cleaned_data['last_name']
            user.profile.last_name = last_name

            user.profile.save()

            messages.success(request, "profile updated")
            return redirect("accounts:profile")

        else:
            context["form"] = form
            return render(request, template_name, context)

    context["form"] = form

    return render(request, template_name, context)





@login_required()
def profile_view_just(request):
    template_name = 'accounts/profile_view_just.html'
    context = {}
    user = request.user

    initial = {
        "bio": user.profile.bio,
        "phone_number":user.profile.phone_number,
        "age":user.profile.age,
        "job":user.profile.job,
        "gender":user.profile.gender,
        "nc":user.profile.nc,
        "first_name":user.profile.first_name,
        "last_name":user.profile.last_name,
        "date_employment":user.profile.date_employment,
        "is_author":user.profile.is_author,
        "resume":user.profile.image
    }


    form = ProfileForm(request.POST or None, instance=user, initial=initial)

    form.fields["username"].disabled = True
    form.fields["first_name"].disabled = True
    form.fields["last_name"].disabled = True
    form.fields["email"].disabled = True
    form.fields["bio"].disabled = True
    form.fields["phone_number"].disabled = True
    form.fields["age"].disabled = True
    form.fields["job"].disabled = True
    form.fields["gender"].disabled = True
    form.fields["nc"].disabled = True
    form.fields["date_employment"].disabled = True
    form.fields["is_author"].disabled = True
    form.fields["resume"].disabled = True


    if request.method == 'POST':
        

        if form.is_valid():
            form.save()
            bio = form.cleaned_data['bio']
            user.profile.bio = bio

            phone_number = form.cleaned_data['phone_number']
            user.profile.phone_number = phone_number

            age = form.cleaned_data['age']
            user.profile.age = age

            job = form.cleaned_data['job']
            user.profile.job = job

            gender = form.cleaned_data['gender']
            user.profile.gender = gender

            nc = form.cleaned_data['nc']
            user.profile.nc = nc

            first_name = form.cleaned_data['first_name']
            user.profile.first_name = first_name

            last_name = form.cleaned_data['last_name']
            user.profile.last_name = last_name

            user.profile.save()

            messages.success(request, "profile updated")
            return redirect("accounts:profile_view_just")

        else:
            context["form"] = form
            return render(request, template_name, context)

    context["form"] = form

    return render(request, template_name, context)




def signup_view(request):
    template_name = 'accounts/signup.html'
    context = {}
    form = SignupForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            bio = form.cleaned_data['bio']
            

            phone_number = form.cleaned_data['phone_number']


            age = form.cleaned_data['age']
            

            job = form.cleaned_data['job']
            

            gender = form.cleaned_data['gender']
            

            nc = form.cleaned_data['nc']
            

            first_name = form.cleaned_data['first_name']
            

            last_name = form.cleaned_data['last_name']


            resume = form.cleaned_data['resume']
            

            user.profile.save()



            user.refresh_from_db()
            user.profile.bio = bio
            user.profile.phone_number = phone_number
            user.profile.age = age
            user.profile.job = job
            user.profile.gender = gender
            user.profile.nc = nc
            user.profile.first_name = first_name
            user.profile.last_name = last_name
            user.profile.image = resume


            user.profile.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Your account created successfully.")
            return redirect("blog:index")

        else:
            context["form"] = form
            return render(request, template_name, context)
    else:
        context["form"] = form

    return render(request, template_name, context)