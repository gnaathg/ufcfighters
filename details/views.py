from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from details.forms import FightersForm, SigninForm, SignupForm
from details.models import Fighters
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

class FightersCreateView(View):

    template_name = "fighters.html"

    form_class = FightersForm


    def get(self, request, *args, **kwargs):

        form_instance = self.form_class()

        return render(request, self.template_name, {'form': form_instance})


    def post(self, request, *args, **kwargs):

        form_instance = self.form_class(request.POST, files=request.FILES)


        if form_instance.is_valid():

            form_instance.save()  # Save the new fighter

            return redirect("fighter-list")  # Corrected redirect name


        return render(request, self.template_name, {'form': form_instance})

class FightersListView(View):

    template_name = "fighters_list.html"


    def get(self, request, *args, **kwargs):

        qs = Fighters.objects.all()  # Get all fighters without filtering

        return render(request, self.template_name, {"data": qs})

class FightersDetailView(View):

    template_name = "fighters_detail.html"

    def get(self, request, *args, **kwargs):

        fighter_id = kwargs.get("id")

        fighter = get_object_or_404(Fighters, id=fighter_id)

        return render(request, self.template_name, {"data": fighter})

class FightersDeleteView(View):
    
    def get(self, request, *args, **kwargs):
        
        fighter_id = kwargs.get("id")
        
        fighter = get_object_or_404(Fighters, id=fighter_id)
        
        fighter.delete()
        
        return redirect("fighter-list")  # Corrected redirect name
        
class FightersUpdateView(View):
    
    template_name = "fighters_edit.html"
    
    form_class = FightersForm
    

    def get(self, request, *args, **kwargs):

        fighter_id = kwargs.get("id")

        fighter = get_object_or_404(Fighters, id=fighter_id)

        form_instance = self.form_class(instance=fighter)

        return render(request, self.template_name, {'form': form_instance})


    def post(self, request, *args, **kwargs):

        fighter_id = kwargs.get("id")

        fighter = get_object_or_404(Fighters, id=fighter_id)

        form_instance = self.form_class(request.POST, files=request.FILES, instance=fighter)


        if form_instance.is_valid():

            form_instance.save()

            return redirect("fighter-list")  # Corrected redirect name

        
        return render(request, self.template_name, {'form': form_instance})

class SignupView(View):

    template_name = "register.html"

    form_class = SignupForm


    def get(self, request, *args, **kwargs):

        form_instance = self.form_class()
        return render(request, self.template_name, {"form": form_instance})


    def post(self, request, *args, **kwargs):

        form_instance = self.form_class(request.POST)


        if form_instance.is_valid():

            data = form_instance.cleaned_data

            User.objects.create_user(**data)  # create_user - hashes the data

            return redirect("signin")  # Changed redirect to signin after registration


        return render(request, self.template_name, {"form": form_instance})

class SigninView(View):

    template_name = "signin.html"

    form_class = SigninForm


    def get(self, request, *args, **kwargs):

        form_instance = self.form_class()

        return render(request, self.template_name, {"form": form_instance})

    def post(self,request,*argss,**kwargs):

        form_data = request.POST

        form_instance = self.form_class(form_data)

        if form_instance.is_valid():

            data = form_instance.cleaned_data

            uname = data.get("username")

            pwd = data.get("password")

            user_object = authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect("fighter-list")
            
            return render(request,self.template_name,{"form":form_instance})
        
class SignoutView(View):

    def get(self,request,*args,**kwargs):

           logout(request)

           return redirect("signin")     

