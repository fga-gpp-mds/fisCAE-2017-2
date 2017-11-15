from .models import Advisor
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth import logout as django_logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from user.forms import AdvisorForm
# Create your views here.


def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        advisor = Advisor()
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username,
                                            password=password)
            advisor.user = user
        except:
            return render(request, 'registroException.html')
        advisor.name = request.POST['name']
        advisor.phone = request.POST['phone']
        advisor.email = request.POST['email']
        advisor.cpf = request.POST['cpf']
        # endereço
        advisor.cep = request.POST['cep']
        advisor.descricao = request.POST['descricao']
        advisor.tipo_cae = request.POST['tipo_cae']
        advisor.bairro = request.POST['bairro']
        advisor.municipio = request.POST['municipio']
        advisor.uf = request.POST['uf']
        if(advisor.tipo_cae == 'Municipal'):
            advisor.nome_cae = 'CAE'+' '+advisor.tipo_cae+' '+advisor.municipio
        else:
            advisor.nome_cae = 'CAE'+' '+advisor.tipo_cae+' '+advisor.uf
        # endereço
        advisor.save()
        return render(request, 'login.html')
    else:
        return render(request, 'registro.html')


@login_required
def index(request):
    advisor = Advisor.objects.get(user=request.user)
    return render(request,
                  'checklist/templates/index.html',
                  {'advisor': advisor})


@login_required
def userEdit(request, pk):
    user = get_object_or_404(Advisor, pk=pk)
    form = AdvisorForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if pk == user.id:
            form.save()
            return redirect('../../')
    return render(request, 'userEdit.html', {'form': form})
