from django.shortcuts import render,HttpResponse,redirect
from . models import Post
# Create your views here.
def faqhome(request):
    allposts =Post.objects.all()
    print(allposts)
    context = {'allposts':allposts}
    return render(request,'faq/faqHome.html',context)

def faqPost(request,slug):
    posts = Post.objects.filter(slug=slug)[0]
    return render(request,'faq/faqPost.html',{'posts':posts})