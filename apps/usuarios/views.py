from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView,View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
# Create your views here.


def welcome(request):
    if request.user.is_authenticated():
        return render(request, "index.html")
    else:
        return redirect('')   
    
    
def register(request):
    return render(request, "users/register.html")

class LoginViews(TemplateView):
    """Display fields to allow Seller users log in the app.

    Attributes
    ----------
    template_name : string
        The full name of the template used to
        render this view: `seller_login.html`

    Methods
    -------
    post(self, request, *args, **kwargs)
        When requested by the user, logs in the user session.
    """

    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        """When requested by the user, logs in the user session.

        Requieres username and password. If credentials are valid,
        renders the Seller Items View. Else, renders the message:
        "Incorrect Username or Password"

        Parameters
        ----------
        Request: data type?
            POST request containing the username and password
            provided by the user.

        Template
        --------
        Seller Login `online_payments/templates/seller_login.html`
        """

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("index")
        
        #@method_decorator(csrf_protect)
        #@method_decorator(never_cache)

        return render(
            request, "login.html",{
                "error": "Contraseña o usuario incorrecto"})
#class Logout(View, LoginRequiredMixin):
 #   """Ends the user session.
  #  Methods
   # -------
    #post(self, request, *args, **kwargs)
     #   When requested by the user, logs out the user session.
    #"""
    #def post(self, request, *args, **kwargs):
     #   """When requested by the user, logs out the user session.
      #  Redirects the user to the Search Item View.
       # Parameters
        #----------
        #Request: data type?
         #   Description?
        #"""
        #logout(request)
        #return redirect("login")

def Logout(request):
    logout(request)
    return redirect("login")



























   # form = AuthenticationForm()
    #if request.method == "POST":

     #   form = AuthenticationForm(data=request.POST)

      #  if form.is_valid():
            
       #     username = form.cleaned_data['username']
         #   password = form.cleaned_data['password']
        #    user = authenticate  (username = username, password = password)

          #  if user is not None:
            #    do_login(request, user)
           #     return redirect("index")

    #return render(request, "login.html", {'form': form})
 
#def logout(request):
    # Redireccionamos a la portada
 #   return redirect(request, "login.html")


