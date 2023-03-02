from django.urls import path
import blog_app.views as v


urlpatterns = [
    path('', v.home, name="home"),
    path('blog/', v.blog, name="blog"),
    path('author/', v.author, name="author"),
    path('login/', v.login, name="login"),
    path('signup/', v.signup, name="signup"),
]
