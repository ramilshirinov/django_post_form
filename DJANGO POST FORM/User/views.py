# from django.shortcuts import render

# # Create your views here.
# # def admin(request):
# #     return render(request , "admin.html")
# def User(request):
#     return render(request , "user.html")


# from django.http import HttpResponse
# from django.template import loader
# from django.contrib.auth.models import User 

# def User(request):
#   mydata = admin.objects.all()
#   template = loader.get_template('user.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))


from django.shortcuts import render

def User(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        # ... process the form data as needed
        return render(request, 'admin.html')
    else:
        # Render the empty form
        return render(request, 'user.html')
