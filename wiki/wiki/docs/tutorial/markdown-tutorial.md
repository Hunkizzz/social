# О проекте
Проект тестовой социальной сети для отработки навыков

# Работа с MarkDown

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.

# Основные моменты с примерами кода

## Функция авторизации с редиректом в личный кабинет "Dashboard"

```
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render
from account_social.forms import LoginForm
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],password = cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse("Wrong Account")

            else:
                HttpResponse("invalid login")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {'form':form, 'username': auth.get_user(request).username})

def user_logout(request):
    auth.logout(request)
    return redirect('/')
```

## *args - Позиционные аргументы

## **kwargs - Именованные аргументы

# Циклы Djinja
```
    {% for val in values %}
        <p>{{val}}</p>
    {% endfor %}
```

```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

`path('admin/', admin.site.urls)`

<pre><code class="python">
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
</pre>