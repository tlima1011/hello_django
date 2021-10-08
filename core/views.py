from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade ):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))


def soma(request, num1, num2):
    s = num1 + num2
    return HttpResponse('<h1>{}  +  {} = {}'.format(num1, num2, s))


def multi(request, num1, num2):
    m = num1 * num2
    return HttpResponse('<h1>{}  +  {} = {}'.format(num1, num2, m))


def dividi(request, num1, num2):
    d = num1 / num2
    return HttpResponse('<h1>{}  +  {} = {}'.format(num1, num2, d))

def subtracao(request, num1, num2):
    sub = num1 - num2
    return HttpResponse('<h1>{}  +  {} = {}'.format(num1, num2, sub))
