from django.shortcuts import render,redirect
from Userdetail.forms import *
from Userdetail.models import *
# from Userdetail.models import cuser
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import JsonResponse,HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import *
from django.views.generic import *
# from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
# from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from django.conf import settings
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib import messages
import urllib.parse
# from urlparse import urlparse
#from login.html mixin
from urllib.parse import urlparse, urlunparse
from django.views.generic import View, UpdateView
from Userdetail.forms import SignUpForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from Userdetail.tokens import account_activation_token

from django.contrib.auth import login
# from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from Userdetail.tokens import account_activation_token
import random


from django.conf import settings
# Avoid shadowing the login.html() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import (
    url_has_allowed_host_and_scheme, urlsafe_base64_decode,
)
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_protect
def home_view(request):
    return render(request, 'Userdetail/userhome.html')

def activation_sent_view(request):
    return render(request, 'Userdetail/activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('userhome')
    else:
        return render(request, 'Userdetail/activation_invalid.html')

def signup_view(request):
    if(request.user.is_authenticated==False):

        if request.method  == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()
                user.profile.first_name = form.cleaned_data.get('first_name')
                user.profile.last_name = form.cleaned_data.get('last_name')
                user.profile.email = form.cleaned_data.get('email')
                # user can't login until link confirmed
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                subject = 'Please Activate Your Account'
                # load a template like get_template()
                # and calls its render() method immediately.
                message = render_to_string('Userdetail/activation_request.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    # method will generate a hash value with user related data
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message)
                return redirect('activation_sent')
        else:
            form = SignUpForm()
        return render(request, 'Userdetail/signup.html', {'form': form})
    else:
        messages="Please logout before logging in"
        form=SignUpForm(initial={"messages": messages})
        return render(request,'Userdetail/signup.html', {"form": form, "messages": messages})
class createUser(TemplateView):
    form_class=RegistrationForm

    model_name=User

    template_name = "Userdetail/registration.html"
    template_name1 = "Userdetail/registrationo.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        # context["form1"] = self.form_class1
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        # form1=self.form_class1(request.POST)
        # User = get_user_model()
        if form.is_valid():
            print("aa2")
            # form.save()
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            # accno = form.cleaned_data["accno"]
            # username, first_name, last_name, email, password, accno = kwargs['username'], kwargs['first_name'], kwargs[
            #     'last_name'], kwargs['email'], kwargs['password1'], kwargs['accno']
            # import pdb;pdb.set_trace()
            # qs=accno = accno

            if(password1==password2):
                if User.objects.filter(username=username).exists():
                    messages.add_message(
                        request=self.request,
                        level=messages.MessageFailure,
                        message=('UserTaaken'),
                        extra_tags='page-level1'
                    )
                    return render(request, self.template_name, {"form": form})


                elif User.objects.filter(email=email).exists():
                    print("rr")
                    messages.add_message(
                        request=self.request,
                        level=messages.SUCCESS,
                        message=('Email Taken'),
                        extra_tags='page-level2'
                    )

                    return redirect("register")

                else:
                    qs = User.objects.create_user(username=username, email=email, first_name=first_name,
                                                  last_name=last_name)
                    qs.set_password(password1)
                    qs.save()
                    rs = User.objects.get(username=username)
                    print("rs:", rs.username)
                    pk = rs.id
                    print(pk)
                    context = {}
                    context["pk"] = pk
                    return redirect("login")
            else:
                messages.add_message(
                    request=self.request,
                    level=messages.MessageFailure,
                    message=('Password does not match'),
                    extra_tags='page-level3'
                )

                return redirect("register")

        else:

            return render(request, self.template_name, {"form": form})


class userUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = User
    form_class=UpdateForm
    template_name="Userdetail/update.html"

    def get_context_data(self, **kwargs):
        context={}
        print("SS:::",self.request.user.id)
        print("dd::",self.kwargs['pk'])
        if (self.request.user.id==self.kwargs['pk']):
            context = super().get_context_data(**kwargs)
            print("AA")
            load_template = 'Userdetail/update.html'
            context['load_template'] = load_template
            return context
        else:
            print("BB")
            context = super().get_context_data(**kwargs)
            messages.add_message(
                request=self.request,
                level=messages.SUCCESS,
                message=('You are trying to upload t he wrong record.Pls upload the right one'),
                extra_tags='page-level'
            )
            load_template='Userdetail/update.html'
            context['load_template'] = load_template
            return context

    def form_valid(self, form):
        print("pk::", self.kwargs['pk'])
        print("pk22::",self.request.user.id)
        if(self.kwargs['pk'] == self.request.user.id):
            form.save(commit=False)
            print("aa")
            # post.updated_by = self.request.user
            # post.updated_at = timezone.now()
            form.save()
            # context={}
            # context["pk"]=self.kwargs['pk']
            return redirect('userhome')
        else:
            messages.add_message(
                request=self.request,
                level=messages.SUCCESS,
                message=('You are trying to upload t he wrong record.Pls upload the right one'),
                extra_tags='page-level'
            )

            return redirect("login")

def userHome(request):
    print(request.user)
    return render(request, "Userdetail/userhome.html", context={'user': request.user})

# def rand_gen():
#     return random.randint(100000000000,999999999999)
@method_decorator(login_required(login_url='Userdetail/userhome.html'),name="dispatch")
class createProfile(LoginRequiredMixin,TemplateView):

    # login_url = 'userhome.html'
    form_class = Profilecreateform1
    # form_class1 = Profilecreateform
    model_name = Profile
    template_name = "Userdetail/profilecreate.html"
    # template_name1 = "Userdetail/profilecreate.html"

    def get(self, request, *args, **kwargs):

        print("kw", self.kwargs['pk'])
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        # if request.user.is_authenticated():
        #     return redirect('crprofile')
        # else:
        #     user = authenticate(username=username, password=password)
        print("kw", self.kwargs['pk'])

        print("ss")
        # if(self.kwargs['pk'])
        if form.is_valid():
            kw = self.kwargs['pk']
            print("kw",kw)
            rs = User.objects.get(id=kw)
            print("RS:::",rs)
            print("rsu:::",rs.username)
            print("accn")
            # # first_name = form.cleaned_data["first_name"]
            # # last_name = form.cleaned_data["last_name"]
            telephone = form.cleaned_data["telephone"]
            # # email = form.cleaned_data["email"]
            dob = form.cleaned_data["dob"]
            address = form.cleaned_data["address"]
            accno_rand=random.randint(100000000000,999999999999)
            accno_rand=int(accno_rand)
            print("acc:::::",accno_rand)
            acc_exist=Profile.objects.filter(user_id=rs.id).count()
            print("actr::",acc_exist)
            while(Profile.objects.filter(accno=accno_rand).count()==1):
                print("a")
                accno_rand=random.randint(100000000000,999999999999)
            else:
                print("b")
                accno=int(accno_rand)
            print("Acn::",accno)
            # accno = form.cleaned_data["accno"]

            # isActive=True
            ns=Profile.objects.filter(user_id=rs.id)
            print("ct::",Profile.objects.filter(user_id=rs.id).count())
            if(Profile.objects.filter(user_id=rs.id).count()==1):
                print("gg")

                qs = Profile.objects.filter(user_id=rs.id).update(telephone=telephone,profile_created_by=rs.username,address=address,dob=dob,accno=accno,signup_confirmation=True)
                # qs.save()
                # for item in qs:
                #     item.save()
            else:
                ws = Profile.objects.get(user_id=rs.id)
                if (self.kwargs['pk'] ==request.user.id):
                # if(self.kwargs['pk']==ws.user_id):

                    print("hh")
                    qs = Profile.objects.create(user_id=rs.id,first_name=rs.first_name, last_name=rs.last_name,telephone=telephone,email=rs.email,profile_created_by=rs.username,address=address,dob=dob,accno=accno,signup_confirmation=True)
                    qs.save()
                else:

                    print("nn")
                    messages.add_message(
                        request=self.request,
                        level=messages.ERROR,
                        message=('You are trying to upload t he wrong record.Pls upload the right one'),
                        extra_tags='page-level'
                    )

                    return redirect("login")


            print("d1")
            # form.save(commit=False)
            print("d2")
            # for item in qs:
            #     item.save()
            # qs.save()
            print("d3")
            request.session['accno']=accno
            request.session['username'] = rs.username
            return redirect("Account_create")
            # return JsonResponse({"message": "loginSuccess", 'status': 200})

        else:
            print("mm")
            messages.add_message(
                request=self.request,
                level=messages.ERROR,
                message=('You are trying to upload t he wrong record.Pls upload the right one'),
                extra_tags='page-level'
            )

            # return redirect("login")
            return render(request, self.template_name, {"form": form})
class viewProfile(LoginRequiredMixin,DetailView):
    model = Profile
    fields="__all__"
    # success_url = reverse_lazy('userhome')
    template_name = "userdetail/profileview.html"
class deleteProfile(LoginRequiredMixin,DeleteView):
    model = Profile
    success_message = "deleted..."
    success_url = '/uh'

    def get(self, request, *args, **kwargs):
        print("kw", self.kwargs['pk'])
        id=self.kwargs['pk']
        sk=Profile.objects.get(user_id=id)
        self.kwargs['pk'] =sk.id
        print("at::",self.kwargs['pk'])
        return self.delete(request, *args, **kwargs)
    
  def userLogout(request):
    del request.session['username']
    del request.session['accno']
    logout(request)
    return redirect("login")
