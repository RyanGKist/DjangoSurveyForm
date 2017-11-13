from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'formApp/index.html')

def submit(request):
	if request.method == 'POST':
		if "counter" in request.session:
			request.session['name'] = request.POST['name']
			request.session['location'] = request.POST['location']
			request.session['language'] = request.POST['language']
			request.session['comments'] = request.POST['comments']
			request.session['counter'] += 1
			return render(request, 'formApp/success.html')
		else:
			request.session['name'] = request.POST['name']
			request.session['location'] = request.POST['location']
			request.session['language'] = request.POST['language']
			request.session['comments'] = request.POST['comments']
			request.session['counter'] = 1
			return render(request, 'formApp/success.html')
def ri(Request):
	return redirect('/')




# Create your views here.
