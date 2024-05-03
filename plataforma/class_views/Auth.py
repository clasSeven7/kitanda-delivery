from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'