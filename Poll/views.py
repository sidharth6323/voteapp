from django.shortcuts import render, render_to_response,RequestContext,HttpResponseRedirect
from models import user,total_votes
import uuid,json
# Create your views here.
def login(request):
	errors=""
	if request.method=="POST":
		name=request.POST.get("name")
		email=request.POST.get("email")
		try:
			ald=user.objects.get(email=email)
		except:
			ald=""
		if ald:
			errors="Email already registered"
			return render_to_response("login.html",{"errors":errors},context_instance=RequestContext(request))
		uid=uuid.uuid1()
		user.objects.create(name=name,email=email,uid=uid)
		return HttpResponseRedirect("/index/"+str(uid))
	return render_to_response("login.html",{"errors":errors},context_instance=RequestContext(request))

def index(request,uid):
	user_m=user.objects.get(uid=uid)
	return render_to_response("index.html",{"uid":uid},context_instance=RequestContext(request))

def vote(request):
	app_name=json.loads(request.body).get("app_name")
	uid=json.loads(request.body).get("uid")
	user_m=user.objects.get(uid=uid)
	setattr(user_m, app_name, getattr(user_m, app_name)+1)
	user_m.save()
	try:
		total=total_votes.objects.all()[0]
	except:
		total=""
	if total:
		print "executed"
		setattr(total, app_name, getattr(total, app_name)+1)
		total.save()
	else:
		print "created"
		total_votes.objects.create()
		total=total_votes.objects.all()[0]
		setattr(total, app_name, getattr(total, app_name)+1)
		total.save()