from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from account_social.models import Profile
class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/reg.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Create a new user object but avoid saving it yet
        new_user = form.save(commit=False)
        # Save the User object
        profile = Profile.objects.create(user = new_user)
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
