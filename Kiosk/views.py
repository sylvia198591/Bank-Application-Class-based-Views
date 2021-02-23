from django.db.models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from django.urls import *
# from Kiosk.models import *
from Kiosk.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
from Userdetail.models import *
from Kiosk.models import *
import plotly
from plotly.offline import plot
from plotly.graph_objs import Scatter
# import plotly.graph_objs as Scatter
import plotly.graph_objs as go
import plotly.graph_objects as go

class createAccount(LoginRequiredMixin,TemplateView):
    form_class = Accountcreateform
    model_name = Account
    template_name = "Kiosk/createAccount.html"

    def get(self, request, *args, **kwargs):
        context = {}


        # Accno = request.session['Accno']
        context["form"] = self.form_class
        rr = request.session['accno']
        rr1 = request.session['username']
        rr2=request.user.id
        if(rr==0):
            pr_acc=Profile.objects.get(user_id=rr2)

            if(pr_acc.accno==0):
                messages="Please generate/update the profile information before creating/deposting/withdrawing money"
                form = self.form_class(initial={"messages": messages})  # Change is here <<<<
                # return render(request, 'test.html', {"form": form, "Accno": rr})
                return render(request, 'Userdetail/profilecreate.html', {"form": form, "messages": messages})
            else:
                form = self.form_class(initial={"Accno": rr, "Name": rr1})  # Change is here <<<<
                # return render(request, 'test.html', {"form": form, "Accno": rr})
                return render(request, self.template_name, {"form": form, "Accno": rr, "Name": rr1})
                # return render(request, self.template_name, context)
        else:
            form = self.form_class(initial={"Accno": rr,"Name":rr1})  # Change is here <<<<
            # return render(request, 'test.html', {"form": form, "Accno": rr})
            return render(request, self.template_name, {"form": form, "Accno": rr,"Name":rr1})
            # return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        form = self.form_class(request.POST)
        if form.is_valid():
            Name = request.session['username']
            Accno = request.session['accno']

            # Amt_c = form.cleaned_data["Amt_c"]
            # Amt_d = form.cleaned_data["Amt_d"]
            Amount = form.cleaned_data["Amount"]
            Dfield = form.cleaned_data["Dfield"]
            Type = form.cleaned_data["Type"]
            # qs = Account.objects.filter(Accno=Accno).order_by('Dfield')[0].values_list('Amt')
            #
            # context = {}
            # context["accdtl"] = qs
            # x_data = [i.get("Amt") for i in qs]
            # if(x_data==)
            # isActive=True
            # if (request.session['Accno'] == Accno):
            print("tYPE",str(Type))
            if(str(Type)=="Debit"):
                Amount=Amount*(-1)
                print("Amt",Amount)
            print("Amto", Amount)
            qs = Account.objects.create(Name=Name, Accno=Accno,Dfield=Dfield,\
                                         Amount=Amount, Type=Type)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return redirect("Account_view")
        else:
            rr=request.session['accno']
            form = self.form_class(initial={"Accno":rr })  # Change is here <<<<
            # return render(request, 'test.html', {"form": form, "Accno": rr})
            return render(request, self.template_name, {"form": form, "Accno": rr})

class Account_ns(LoginRequiredMixin,TemplateView):
    form_class = Accountcreateform
    model_name = Account
    template_name = "Kiosk/createAccount.html"

    def get(self, request, *args, **kwargs):
        context = {}


        # Accno = request.session['Accno']
        context["form"] = self.form_class
        uid=self.kwargs['pk']
        pr_acc = Profile.objects.get(user_id=uid)
        u_acc = User.objects.get(id=uid)
        print("gg:::",u_acc.username)
        if ((pr_acc.accno!=0) and (pr_acc.user!='')):
            print("hdgfh")
            request.session['accno']=pr_acc.accno
            request.session['username'] = u_acc.username
            rr=request.session['accno']
            rr1=request.session['username']
            print("ll", rr)
            print("ll",rr1)
            form = self.form_class(initial={"Accno": rr, "Name": rr1})  # Change is here <<<<
            # return render(request, 'test.html', {"form": form, "Accno": rr})
            return render(request, self.template_name, {"form": form, "Accno": rr, "Name": rr1})
        else:

            messages = "Please generate/update the profile information before creating/deposting/withdrawing money"
            form = self.form_class(initial={"messages": messages})  # Change is here <<<<
            # return render(request, 'test.html', {"form": form, "Accno": rr})
            return render(request, 'Userdetail/profilecreate.html', {"form": form, "messages": messages})


    def post(self, request, *args, **kwargs):
        print("djfh")
        # import pdb;pdb.set_trace()
        form = self.form_class(request.POST)
        if form.is_valid():
            Name = request.session['username']
            Accno = request.session['accno']

            # Amt_c = form.cleaned_data["Amt_c"]
            # Amt_d = form.cleaned_data["Amt_d"]
            Amount = form.cleaned_data["Amount"]
            Dfield = form.cleaned_data["Dfield"]
            Type = form.cleaned_data["Type"]
            # qs = Account.objects.filter(Accno=Accno).order_by('Dfield')[0].values_list('Amt')
            #
            # context = {}
            # context["accdtl"] = qs
            # x_data = [i.get("Amt") for i in qs]
            # if(x_data==)
            # isActive=True
            # if (request.session['Accno'] == Accno):
            print("tYPE",str(Type))
            if(str(Type)=="Debit"):
                Amount=Amount*(-1)
                print("Amt",Amount)
            print("Amto", Amount)
            qs = Account.objects.create(Name=Name, Accno=Accno,Dfield=Dfield,\
                                         Amount=Amount, Type=Type)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return redirect("Account_view")
        else:
            rr=request.session['accno']
            form = self.form_class(initial={"Accno":rr })  # Change is here <<<<
            # return render(request, 'test.html', {"form": form, "Accno": rr})
            return render(request, self.template_name, {"form": form, "Accno": rr})

class viewAccount(LoginRequiredMixin,TemplateView):
    model_name = Account
    form_class = ViewAccountform
    # context_object_name = 'viewaccount'
    # template_name = "Kiosk/viewAccount.html"
    template_name = "Kiosk/viewAccounto.html"

    # def get(self, request, *args, **kwargs):
    #     context = {}
    #     context["form"] = self.form_class
    #     accno=request.session['accno']
    #     context['Accno']=request.session['accno']
    #     return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print("0000")
        # if form.is_valid():
        print("11111")
            # Name = request.session["Name"]
            # Accno = form.cleaned_data["Accno"]
            # Startdate = form.cleaned_data["Startdate"]
            # Enddate = form.cleaned_data["Enddate"]
            # print("sess:", request.session["Username"])
            # print("pay:",Paymode)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
        Accno=request.session['accno']

        if(request.session['accno']!=''):
            qs = Account.objects.filter(Accno=Accno)
            qs1 = Account.objects.filter(Accno=Accno).aggregate(Total=Sum('Amount'))

                    # .order_by('Accno') \

                    # .order_by('Accno').aggregate(Sum('Amount'))

                # .aggregate(Total=Sum('Amount'))
                # print(qs.Total)
                # qs =Entry.objects.filter(Q(Username=Username)& \
                #                          Q(Dfield__gte=Startdate)&\
                #                          Q(Dfield__lte=Enddate)&\
                #                          Q(Category__Category=Category)).\
                #     aggregate(Sum('Amount')).get('Amount__sum')
            print("d1")
            context = {}
            context["viewaccount"] = qs
            context["viewaccount1"] = qs1
            # form.save()
            print("d2",Accno)
            # qs.save()
            print("d3")
            return render(request, self.template_name, context)


                # return redirect("Categorywise_view")
            # else:
            #     return render(request, self.template_name, {"form": form})
        else:

            return render(request, self.template_name, {"form": form})


class updateAccount(LoginRequiredMixin,UpdateView):
    model = Account
    fields = ['Name', 'Type', 'Amount', 'Dfield' ]
    success_url = '/Viewaccount'
    # success_url = reverse_lazy('getRes')
    # context_object_name = "form"
    template_name = 'Kiosk/createAccount.html'


class deleteAccount(LoginRequiredMixin,DeleteView):
    model = Account

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    fields = ['Name', 'Trans_type',  'Amount', 'Dfield']
    # template_name_suffix = "_del"
    success_url = '/Viewaccount'

class createDatewise(LoginRequiredMixin,TemplateView):
    form_class=Adddatewiseform
    model_name=Account
    template_name = "Kiosk/createDatewise.html"
    template_name1 = "Kiosk/viewDatewise.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("0000")
        if form.is_valid():
            print("11111")
            # Username = request.session["Username"]
            Accno = request.session['accno']
            Startdate = form.cleaned_data["Startdate"]
            Enddate = form.cleaned_data["Enddate"]
            # print("sess:",request.session["Username"])
            # print("pay:",Paymode)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            qs = Account.objects.filter(Accno=Accno, \
                                        Dfield__range=[Startdate, Enddate])
            qs1 =Account.objects.filter(Accno=Accno, \
                    Dfield__range=[Startdate,Enddate]).aggregate(Total=Sum('Amount'))\
                                        # Dfield__lte=Enddate, \
                    # Category__Category=Category)\

            # print(qs.Total)
            # qs =Entry.objects.filter(Q(Username=Username)& \
            #                          Q(Dfield__gte=Startdate)&\
            #                          Q(Dfield__lte=Enddate)&\
            #                          Q(Category__Category=Category)).\
            #     aggregate(Sum('Amount')).get('Amount__sum')
            print("d1")
            context = {}
            context["vdw"] = qs
            context["vdw1"] = qs1
            # context[""]=Username
            # context["sd"]=Startdate
            # context["ed"]=Enddate
            # context["Accno"]=Accno
            return render(request, self.template_name1, context)

            # form.save()
            print("d2")
            # qs.save()
            print("d3")
            # return redirect("Categorywise_view")
        else:
            return render(request, self.template_name,{"form":form})

class createTrans(LoginRequiredMixin,TemplateView):
    form_class = Addtranstypeform
    model_name = Trans_type
    template_name = "Kiosk/createTrans.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            Trans_symbol = form.cleaned_data["Trans_symbol"]
            Type = form.cleaned_data["Type"]


            qs = Trans_type.objects.create(Trans_symbol=Trans_symbol, Type=Type)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return redirect("Account_create")

        else:
            return render(request, self.template_name, {"form": form})

class createTransfer(LoginRequiredMixin,TemplateView):
    form_class = Addtransferform
    model_name = Account
    template_name = "Kiosk/createAccount.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Name=form.cleaned_data["Accno"]
            Accno = form.cleaned_data["Accno"]
            Accnoto = form.cleaned_data["Accnoto"]
            # Dfieldt = form.cleaned_data["Dfieldt"]
            Amount= form.cleaned_data["Amount"]
            print("a",Accno)
            print("at",Accnoto)
            qs=Account.objects.filter(Accno=Accnoto).annotate(Count('Accno', distinct=True))
            if((qs[0].Accno__count)==1):
                n1=Account.objects.filter(Accno=Accno)

                qs1 = Account.objects.create(Name=n1[0].Name, Accno=Accno,\
                                             Amount=(Amount*-1), Type=(Trans_type.objects.get(id=2)))
                qs1.save()
                qs2 = Account.objects.create(Name=qs[0].Name, Accno=Accnoto,\
                                             Amount=(Amount), Type=(Trans_type.objects.get(id=1)))
                print("d1")
                # form.save(commit=False)
                print("d2")

                qs2.save()
                print("d3")
                return redirect("Account_view")
            else:
                return render(request, self.template_name, {"form": form})


        else:
            return render(request, self.template_name, {"form": form})

def spendanalysis(request):

    accno = request.session["accno"]
    print("LL::",accno)
    # Category = form.cleaned_data["Category"]
    # print("sess:", request.session["Username"])
    # print("pay:",Paymode)
    # Username1 = request.session.Username
    # Username=form.cleaned_data["Username"]
    qs = Account.objects.filter(Accno=accno).values('Type__Type') \
        .annotate(Total=Sum('Amount'))
    print("d1",qs)
    # xx=[]
    # for i in qs:
    #     print(i.get("Category__Category"))
    # x=[i.get("Category__Category") for i in qs]
    # print(x)
    # y = [i.get("Total") for i in qs]
    # print(y)

    # print(qs.Category__Category)

    x_data = [i.get("Type__Type") for i in qs]
    print(x_data)
    y_data = [i.get("Total") for i in qs]
    fig = go.Figure(data=[go.Pie(labels=x_data, values=y_data)])
    fig.show()
    # fig = go.Figure(data=[go.Bar(
    #     x=x_data, y=y_data,
    #     text=y_data,
    #     textposition='auto',
    # )])
    #
    # fig.show()
    plot_div = plot(fig, output_type='div')
    # plot_div = plot([Scatter(x=x_data, y=y_data,
    #                          mode='lines', name='test',
    #                          opacity=0.8, marker_color='green')],
    #                 output_type='div',include_plotlyjs=False)
    context = {}
    context["viewoverall"] = qs
    return render(request, 'Kiosk/spendanalysis.html',
              context={'plot_div': plot_div, "viewoverall": qs})

    # form.save()
    # print("d2")
    # qs.save()
    # print("d3")
    # return redirect("Categorywise_view")
# else:
#     return render(request, self.template_name,{"form":form})
