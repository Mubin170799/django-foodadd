from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.http import HttpResponse

def home(Request):
    # return HttpResponse("<h1> hello this is home page </h1>")
    people = [
        {'name':"mubin", "age": 22},
        {"name": "sana", "age":23},
        
    ]
    
    
    
    return render(Request, "home/index.html", context= {"peoples":people})


def succss_t(Request):
    print("*"*10)
    context = {"page":"sucess"}
    return HttpResponse("""<h3 style="color:green">hello this is success page </h3>""", context)


def contact(Request):
    context = {"page":"contact"}
    return render(Request, "home/contact.html", context)

def about(Request):
    context = {"page":"about"}
    return render(Request, "home/about.html", context)

def reciepe_final(request):
    if request.method =="POST":
        data =request.POST
        receipe_image = request.FILES['receipe_image']
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        
        recipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
    
        )
    
        # print(receipe_name)
        # print(receipe_description)
        # print(receipe_image)
        
        return redirect("/receipe/")
    
    queryset = recipe.objects.all()
    context = {"recipes": queryset}
    return render(request, "home/receipe.html", context)



def delete_item(request, name):
    # print(id)
    queryset= recipe.objects.get(name = receipe_name)
    queryset.delete()
    return redirect("/receipe/")
    

    
