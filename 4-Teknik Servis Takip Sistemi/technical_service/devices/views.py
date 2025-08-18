from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Computer,PlayerEquipment,SmartPhone,SmartWatch,TV,Tablet
from django.contrib.auth import logout as django_logout

def login_register(request):
    login_form = AuthenticationForm()
    register_form = CustomerUserCreationForm()
    show_register = request.GET.get('register') == 'true' or 'register' in request.POST

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = AuthenticationForm(data = request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)

                if user.groups.filter(name = 'Teknik Servis Elemanları').exists():
                    return redirect('defective_devices')
                else:
                   return redirect('home')
            
            else:
                messages.error(request, 'Lütfen Geçerli E-posta ve Şifre Giriniz')
                show_register = False

        elif 'register' in request.POST:
            register_form = CustomerUserCreationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Kayıt Başarılı. Giriş Yapabilirsiniz')
                return redirect('login_register')
        
    return render(request, 'devices/login_register.html', {'login_form': login_form, 'register_form': register_form, 'show_register': show_register})

@login_required         
def home(request):  
    return render(request, 'devices/home.html')

@login_required              
def user_logout(request):
    django_logout(request)
    return redirect('login_register')

@login_required  
def computer(request):
    if  request.method == 'POST':
        pc_type = request.POST.get('pc_type')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        issue = request.POST.get('issue')

        if all([pc_type, brand, model, issue]):
            Computer.objects.create(
                user = request.user,
                pc_type = pc_type,
                brand = brand,
                model = model,
                issue = issue
            )
            messages.success(request, 'Talebiniz Başarıyla Alınmıştır ✅')
            return redirect('computer')        
    
    computer_items = Computer.objects.filter(user = request.user)
    return render(request, 'devices/computer.html', {'computer_items': computer_items})

@login_required  
def smart_phone(request):
    if request.method == 'POST':
            brand = request.POST.get('brand')
            model = request.POST.get('model')
            issue = request.POST.get('issue')
        
            if all([brand, model, issue]):
                SmartPhone.objects.create(
                   user = request.user,
                   brand = brand,
                   model = model,
                   issue = issue  
                )
                messages.success(request, 'Talebiniz Başarıyla Alınmıştır ✅')
                return redirect('smart_phone')
            
    smart_phone_items = SmartPhone.objects.filter(user = request.user)
    return render(request, 'devices/smart_phone.html', {'smart_phone_items': smart_phone_items})

@login_required  
def smart_watch(request):
    if  request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        issue = request.POST.get('issue')

        if all([brand, model, issue]):
            SmartWatch.objects.create(
                user = request.user,
                brand = brand,
                model = model,
                issue = issue
            )
            messages.success(request, 'Talebiniz Başarıyla Alınmıştır ✅')
            return redirect('smart_watch')
        
    smart_watch_items = SmartPhone.objects.filter(user = request.user)
    return render(request, 'devices/smart_watch.html', {'smart_watch_items': smart_watch_items})

@login_required  
def tv(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        issue = request.POST.get('issue')

        if all([brand, model,issue]):
            TV.objects.create(
                user = request.user,
                brand = brand,
                model = model,
                issue = issue
            )
            messages.success(request, 'Talebiniz Başarıyla Alınmıştır ✅')
            return redirect('tv')
    
    tv_items = TV.objects.filter(user = request.user)
    return render(request, 'devices/tv.html', {'tv_items': tv_items})

@login_required  
def player_equipment(request):
    if request.method =='POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        issue = request.POST.get('issue')

        if all([brand, model, issue]):
            PlayerEquipment.objects.create(
                user = request.user,
                brand = brand,
                model = model,
                issue = issue
            )
            messages.success(request, 'Talebiniz Başarıyla Alınmıştır ✅')
            return redirect('player_equipment')
         
    player_equipment_items = PlayerEquipment.objects.filter(user = request.user)
    return render(request, 'devices/player_equipment.html', {'player_equipment_items': player_equipment_items})

@login_required  
def tablet(request):
    if request.method =='POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        issue = request.POST.get('issue')

        if all([brand, model, issue]):
            Tablet.objects.create(
                user = request.user,
                brand = brand,
                model = model,
                issue = issue
            )
            messages.success(request, 'Talebiniz Başarıyla Alınmıştır ✅')
            return redirect('tablet')

    tablet_items = Tablet.objects.filter(user = request.user)
    return render(request, 'devices/tablet.html', {'tablet_items': tablet_items})       

@login_required
def defective_devices(request):
    if not request.user.groups.filter(name='Teknik Servis Elemanları').exists():
        return redirect('home')

    # Model eşleme
    model_map = {
        'Computer': Computer,
        'SmartPhone': SmartPhone,
        'SmartWatch': SmartWatch,
        'TV': TV,
        'PlayerEquipment': PlayerEquipment,
        'Tablet': Tablet
    }

    if request.method == 'POST':
        device_ids = request.POST.getlist('device_id')
        device_types = request.POST.getlist('device_type')
        statuses = request.POST.getlist('status')

        for device_id, device_type, status in zip(device_ids, device_types, statuses):
            try:
                model_class = model_map[device_type]
                obj = model_class.objects.get(id=device_id)
                obj.status = status
                obj.save()
            except (KeyError, model_class.DoesNotExist):
                continue

        return redirect('defective_devices')

    # View tarafında device_type bilgisini ekliyoruz
    all_devices = [
        ('Bilgisayarlar', [dict(obj=obj, device_type=obj.__class__.__name__) for obj in Computer.objects.all()]),
        ('Akıllı Telefonlar', [dict(obj=obj, device_type=obj.__class__.__name__) for obj in SmartPhone.objects.all()]),
        ('Akıllı Saatler', [dict(obj=obj, device_type=obj.__class__.__name__) for obj in SmartWatch.objects.all()]),
        ('Televizyonlar', [dict(obj=obj, device_type=obj.__class__.__name__) for obj in TV.objects.all()]),
        ('Oyun Ekipmanları', [dict(obj=obj, device_type=obj.__class__.__name__) for obj in PlayerEquipment.objects.all()]),
        ('Tabletler', [dict(obj=obj, device_type=obj.__class__.__name__) for obj in Tablet.objects.all()]),
    ]

    return render(request, 'devices/defective_devices.html', {'all_devices': all_devices})

@login_required
def customer_devices(request):
    user = request.user
    all_devices = []

    for device_model in [Computer, PlayerEquipment, SmartPhone, SmartWatch, TV, Tablet]:
        user_devices = device_model.objects.filter(user = user)
        for d in user_devices: 
            all_devices.append({
                'type': device_model.__name__,
                'brand': d.brand,
                'model': d.model,
                'issue': d.issue,
                'status': d.status,
            })

    return render(request, 'devices/customer_devices.html', {'all_devices': all_devices})