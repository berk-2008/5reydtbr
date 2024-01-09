from django.shortcuts import render, redirect
from .forms import CreateBlogForm
from .models import Blog
from django.http import HttpResponse

def intex(reguest):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(reguest, 'blog/intex.html', context)


def CreateBlog(reguest):
    if reguest.method == 'POST':
        form = CreateBlogForm(reguest.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
        return HttpResponse("Invalid")
    form = CreateBlogForm
    context = {

        'form': form
    }

    return render(reguest,'blog/create_blog.html', context)




def DeleteBlog(reguest, id):
    try:
        blog = Blog.objects.get(pk=id)
        blog.delete()
    except:
        return HttpResponse(" не найдено!")

    return redirect('http://127.0.0.1:8000/')

