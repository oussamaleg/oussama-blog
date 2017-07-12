from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from technology.models import Blog, Part, Profile
from django.contrib.auth.models import User
# Create your views here.

best_blogs = Blog.objects.order_by("views").reverse()[:8]
parts = Part.objects.all()

def index(request):
	latest_blogs = Blog.objects.order_by("date").reverse()[:10]
	parts = Part.objects.all()
	context = {'latest_blogs':latest_blogs,
	           'best_blogs':best_blogs,
	           'parts':parts,
	           }
	return render(request,'technology/index.html',context)

def blog(request,blog_id):
	blog = get_object_or_404(Blog,pk=blog_id)
	if request:
		blog.views += 1
		blog.save()
	context = {'best_blogs':best_blogs,
	           'blog':blog,
	           'parts':parts,}
	return render(request,'technology/blog.html',context)

def profile(request,user_id):
	profile = get_object_or_404(Profile,pk=user_id)
	user = profile.user
	latest_blogs = Blog.objects.filter(publisher=user).order_by("date").reverse()
	context = {'latest_blogs':latest_blogs,'best_blogs':best_blogs,
	 'profile':profile,'user':user,'parts':parts,
}
	return render(request,'technology/profile.html',context)

def part(request,part_id):
	part = get_object_or_404(Part,pk=part_id)
	latest_blogs = Blog.objects.filter(part=part).order_by("date").reverse()[:5]
	context = {'latest_blogs':latest_blogs,'best_blogs':best_blogs,'parts':parts,
}
	return render(request,'technology/part.html',context)