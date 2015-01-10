from django.http import HttpResponse
from money.models import Entry

# Create your views here.
def index(request):

	if request.user.is_authenticated():
		e = Entry(username_id=request.user.id, month="Jan", amount=1000)
		e.save()
		Entry.objects.all()
		
		
		return HttpResponse("Hi. I saved new entry: " + str(e.id))
	else:
		return HttpResponse("Log in first")
