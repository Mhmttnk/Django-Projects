from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import CustomerUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Hospital,Sport,Dental_Clinic,Hair_Dresser

def login_register(request):
    login_form = AuthenticationForm() # login_form nesnesi oluşturduk
    register_form = CustomerUserCreationForm() # register_form nesnesi oluşturduk
    show_register = request.GET.get('register') == 'true' or 'register' in request.POST
    
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = AuthenticationForm(data = request.POST) # Hazır build-in yapısı olduğu için data=.... yazılır
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')
            
        elif 'register' in request.POST:
            register_form = CustomerUserCreationForm(request.POST) # Burada ise kendimiz oluşturduğumuz için data=.... yapmamıza gerek yok
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Kayıt Başarılı. Giriş Yapabilirsiniz.')
                return redirect('login_register')
            
    return render(request, 'appointments/login.html', {'login_form': login_form, 'register_form': register_form, 'show_register': show_register})

@login_required
def home(request):
    return render(request, 'appointments/home.html')

@login_required
def add_hospital_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        policlinic = request.POST.get('policlinic')
        gender = request.POST.get('gender')
        day = request.POST.get('day')
        time = request.POST.get('time')

        if all([name and surname and policlinic and gender and day and time]):
            existing=Hospital.objects.filter(policlinic = policlinic, day = day, time = time).exists()
            if existing:
                messages.error(request, 'Bu Randevu Saati Dolu ❌')
            else:
                Hospital.objects.create(
                    name = name,
                    surname = surname,
                    policlinic = policlinic,
                    gender = gender,
                    day = day,
                    time = time
                    )
                messages.success(request, ' Hastane Randevusu Başarıyla Oluşturuldu ✅')
                return redirect('add_hospital_appointment')
        else:
            messages.error(request, ' Tüm Alanları Doldurmalısınız ❌')
        
    hospital_appointments = Hospital.objects.all()        
    return render(request, 'appointments/add_hospital_appointment.html', {'hospital_appointments': hospital_appointments})

@login_required
def add_sport_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        gender = request.POST.get('gender')
        day = request.POST.get('day')
        time = request.POST.get('time')

        if all([name and surname and gender and day and time]):
            existing=Sport.objects.filter(day = day, time = time).exists()
            if existing:
                messages.error(request, 'Bu Randevu Saati Dolu ❌')
            else:
                Sport.objects.create(
                    name = name,
                    surname = surname,
                    gender = gender,
                    day = day,
                    time = time 
                )
                messages.success(request, 'Spor Randevusu Başarıyla Oluşturuldu ✅')
                return redirect('add_sport_appointment')    
        else:
            messages.error(request, 'Tüm Alanları Doldurmalısınız ❌')

    sport_appointments = Sport.objects.all()
    return render(request, 'appointments/add_sport_appointment.html', {'sport_appointments': sport_appointments})

@login_required
def add_dental_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname') 
        gender = request.POST.get('gender')
        day = request.POST.get('day')
        time = request.POST.get('time')

        if all([gender, day, time]):
            existing=Dental_Clinic.objects.filter(day = day, time = time).exists()
            if existing:
                messages.error(request, 'Bu Randevu Saati Dolu ❌')
            else:    
                Dental_Clinic.objects.create(
                    name = name,
                    surname = surname,
                    gender = gender,
                    day = day,
                    time = time
                )
                messages.success(request, 'Diş Randevusu Başarıyla Oluşturuldu ✅')
                return redirect('add_dental_appointment')
        else:
            messages.error(request, 'Tüm Alanları Doldurmalısınız ❌')

    dental_appointments = Dental_Clinic.objects.all()
    return render (request, 'appointments/add_dental_appointment.html', {'dental_appointments':dental_appointments})

@login_required
def add_hairdresser_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        day = request.POST.get('day')
        time = request.POST.get('time')

        if all([name and surname and day, time]):
            existing=Hair_Dresser.objects.filter(day = day, time = time).exists()
            if existing:
                messages.error(request, 'Bu Randevu Saati Dolu ❌')
            else:
                Hair_Dresser.objects.create(
                    name = name,
                    surname = surname,
                    day = day,
                    time = time
                )
                messages.success(request, 'Kuaför Randevusu Başarıyla Oluşturuldu ✅')
                return redirect('add_hairdresser_appointment')
        else:
            messages.error(request, 'Tüm Alanları Doldurmalısınız ❌')
    
    hairdresser_appointments = Hair_Dresser.objects.all()         
    return render(request, 'appointments/add_hairdresser_appointment.html', {'hairdresser_appointments': hairdresser_appointments}) 