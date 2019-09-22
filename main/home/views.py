from django.shortcuts import render
from .models import home_page_model
from .forms import home_forms
# Create your views here.

def home_page_view(request):
	# print('user is',request.user)
	# print('method is ',request.method)
	# print('GET is ',request.GET)
	# print('POST is ',request.POST)

	my_form = home_forms(request.POST or None)



	if request.method == 'POST':
		print("it is post")
		
		my_form = home_forms(request.POST or None)

		if my_form.is_valid():
			print('first name is: ' ,my_form.cleaned_data["first_name"])
			data = my_form.cleaned_data
			my_model = home_page_model.objects.create(**data)
			my_form = home_forms()
			
		else:
			home_forms()
		



	#obj = home_page_model.objects.create(first_name='mahmoud',second_name='essa',email='aa@gmail.com')
	context = {

	"page_title" : "Welcome in the home page",
	"forms" : my_form,
	

	}
	return render(request,'home/home.html',context)






def home_page_result(request):


	query = home_page_model.objects.all()


	context = {"page_title":"Welcome in result page" , "db":query}

	return render(request,'home/result.html',context)

