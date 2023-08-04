from django.shortcuts import render,redirect
from .models import event
from .forms import UserRegisterationForm,UserAuthenticationForm,EventForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.

# this view takes all events created and passes them to events.html template to show on the frontend
def events(request):
    
        et=event.objects.all()
        if request.user.is_authenticated:
            # this query here gets only those events that are liked by the loggedin user(current user) and passes those events to events.html template
            # so that user can see those events that are liked by user
            user=request.user
            user=User.objects.get(username=user)
            liked_events=event.objects.filter(liked_by_users=user.id)
            return render(request,'app/events.html',{'event':et,'liked_events_byuser':liked_events})
        else:
            return render(request,'app/events.html',{'event':et})

# view function to create account
def signupform(request):
    fm=UserRegisterationForm()
    if request.method=="POST":
        fm=UserRegisterationForm(request.POST)
       
        if fm.is_valid():
            messages.success(request,'Account Created Successfully.....')
            fm.save()
           
            return redirect('/')
        else:
            return render(request,'app/signup.html',{'form':fm})
    return render(request,'app/signup.html',{'form':fm})

# view function to loggedin the account 

def userlogin(request):
    # if user is not logged in then if statement is true and code inside it runs 
    if not request.user.is_authenticated:
        if request.method =="POST":
            fm=UserAuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                usname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=usname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged in Successfullly!!!!')   
                    return HttpResponseRedirect('/')
        else:
            fm=UserAuthenticationForm()
            return render(request,'app/login.html',{'form':fm})
    # if user loggedin then user will be redirected to the home page or events.html template
    else:
        return redirect('/')

@login_required(login_url='/login/')   
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
# view function to create events on loggedin users can create events
@login_required(login_url='/login/')
def createevent(request):
    if request.method =="POST":
        fm=EventForm(request.POST,request.FILES)
        if fm.is_valid():
            eventname=  fm.cleaned_data['event_name']
            date=  fm.cleaned_data['date']
            time=fm.cleaned_data['time']
            location=  fm.cleaned_data['location']
            image = fm.cleaned_data['image']
            reg=event(name=request.user,event_name=eventname,date=date,time=time,location=location,image=image)
            reg.save()
            messages.success(request,"Event Created Successfully!!")
            return  redirect('/')
    else:
        fm=EventForm()
    return render(request,'app/createevent.html',{'form':fm})

# view function to views events created by current logged in user, it filters the data according to the current user.
@login_required(login_url='/login/')
def userevents(request):
    if request.user.is_authenticated:
        et=event.objects.filter(name=request.user)
        return render(request,'app/user events.html',{'event':et})

# view function to like the event and store the record of event with the user details who liked it.
def eventliked(request):
    if request.user.is_authenticated:
        if request.method=='GET':
        #    we get the eventid from the request sent by the javascript function whn the event is liked
            event_id=request.GET['event_id']
            print(type(event_id))
            User=request.user
            # using that eventid we get the event details 
            c=event.objects.get(id=event_id)
            
            
                # Check if the user has already liked the event
            if User in c.liked_by_users.all():
                # User has already liked the event, so we remove the like
                c.liked_by_users.remove(User)
                msg="Event unliked"
            
                
                # c.is_liked=False
            else:
            # User hasn't liked the event yet, so we add the like
                c.liked_by_users.add(User)
                msg="Event liked"
        
                c.is_liked=True
                c.save()
            # when there is not user remains, who like the event, we put is _liked status to false.    
            list=[nm for nm in c.liked_by_users.all()]
            if len(list)==0:
                c.is_liked=False
                c.save()
                
            for nm in c.liked_by_users.all():
                print(nm)
            # we sent the msg to the javacript fucntion with ajax in json form
            data={
                    'msg':msg
            }
            return JsonResponse(data)
        else:
            return JsonResponse("")
    else:
        return redirect('/login/')
    
