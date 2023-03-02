from django.shortcuts import render
import blog_app.forms as f


# Create your views here.
def home(request):
    subscribe_form = f.Subscribe()
    if request.POST:
        subscribe_form = f.Subscribe(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            context = {"success": "Thank You for registering! "}
            return render(request, "blog_app/index.html", context=context)

    context = {"subscribe": subscribe_form}
    return render(request, "blog_app/index.html", context=context)


def blog(request):
    context = {}
    return render(request, "blog_app/pages/blog.html", context=context)


def author(request):
    context = {}
    return render(request, "blog_app/pages/author.html", context=context)


def login(request):
    context = {}
    return render(request, "blog_app/pages/login.html", context=context)


def signup(request):
    context = {}
    return render(request, "blog_app/pages/signup.html", context=context)

