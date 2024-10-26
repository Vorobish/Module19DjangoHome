from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import *

users = []
buyers = Buyer.objects.all()
for buyer in buyers:
    users.append(buyer.name)

info = {}


def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Игры'
    button_pay = 'Купить'
    games = []
    Games = Game.objects.all()
    for game in Games:
        games.append(f'{game.title} | {game.description}. Стоимость: {game.cost}')
    context = {
        'title': title,
        'games': games,
        'button_pay': button_pay,
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    text = 'Вернитесь в магазин и купите что-нибудь'
    text2 = 'Ну пожалуйста)'
    context = {
        'title': title,
        'text': text,
        'text2': text2,
    }
    return render(request, 'cart.html', context)


def menu(request):
    return render(request, 'menu.html')


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and int(age) >= 18 and not username in users:
            Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        info['username'] = username
        info['password'] = password
        info['repeat_password'] = repeat_password
        info['age'] = age
        return render(request, 'registration_page.html', info)
    info['error'] = ''
    info['username'] = ''
    info['password'] = ''
    info['repeat_password'] = ''
    info['age'] = ''
    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and int(age) >= 18 and not username in users:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            info['username'] = username
            info['password'] = password
            info['repeat_password'] = repeat_password
            info['age'] = age
            info['form'] = form
            return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})

