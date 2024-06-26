from django.shortcuts import render, redirect
from django.shortcuts import render
from customer.models import Ihas, Customer, Ihas, Rent
from django.http import JsonResponse
from datetime import datetime

def index(request):
    contex = {
        # CRUD + LIST
        "ihalar": Ihas.objects.all().order_by('Iha_id')
    }
    return render(request, 'customer/index.html', contex)


def ihalar(request):
    contex = {
        "ihalar": Ihas.objects.all().order_by('Iha_id')
    }
    return render(request, 'customer/ihas.html', contex)


def register(request):
    if request.method == "GET":
        return render(request, 'customer/users/register.html')

    if request.method == "POST":
        ad = request.POST["Ad"]
        soyad = request.POST["Soyad"]
        mail = request.POST["Mail"]
        gsm_no = request.POST["GsmNo"]
        password = request.POST["id_sifre"]
        repassword = request.POST["id_sifre_tekrar"]

        ######################################
        if not request.POST["id_sifre"]:
            return render(request, "customer/users/register.html", {
                "error": "Şifre boş bırakılamaz.",
                "Mail": mail,
                "Ad": ad,
                "Soyad": soyad,
            })
        ######################################
        if password != repassword:
            return render(request, "customer/users/register.html", {
                "error": "Parola eşleşmiyor.",
                "Mail": mail,
                "Ad": ad,
                "Soyad": soyad,
            })
        ######################################
        if Customer.objects.filter(Mail=mail).exists():
            return render(request, "customer/users/register.html",
                          {
                              "error": "email kullanılıyor.",
                              "Ad": ad,
                              "Soyad": soyad,
                              "GsmNo": gsm_no
                          })
        ######################################
        if password == repassword:
            customer = Customer(Ad=ad, Soyad=soyad, Mail=mail,
                                GsmNo=gsm_no, Sifre=password, Status=True)
            customer.save()
            return redirect("login")


def login(request):
    if request.method == "GET":
        if request.session.get('user_logged_in'):
            # Kullanıcı oturumu açık
            return render(request, "customer/users/index.html")
        return render(request, 'customer/users/login.html')

    if request.method == "POST":
        mail = request.POST["Mail"]
        sifre = request.POST["password"]

        if not Customer.objects.filter(Mail=mail).exists():
            return render(request, "customer/users/login.html", {
                "error": "Böyle bir mail yok.",
            })
        ######################################
        if sifre != Customer.objects.filter(Mail=mail)[0].Sifre:
            return render(request, "customer/users/login.html", {
                "error": "Şifre yanlış.",
                "Mail": mail
            })
        else:
            # giriş başarılı demektir.
            request.session['user_logged_in'] = True
            request.session['customer_id'] = Customer.objects.get(Mail=mail).Customer_id
            request.session['customer_name'] = Customer.objects.get(Mail=mail).Ad
            return redirect("index")


def logout(request):
    request.session['user_logged_in'] = False
    return redirect('login')


def rentable_detail(request, id):
    # CRUD (READ)
    iha = Ihas.objects.filter(Iha_id=id)[0]
    return render(request, 'customer/rentable-detail.html', {
        "iha": iha
    })


# def rented_detail(request, id):
#     return render(request, 'customer/rented-detail.html', {
#         "adet": id
#     })

def renting(request, id):
    if request.method == "GET":
        if request.session.get('user_logged_in'):
            # Kullanıcı oturumu açık
            iha_id = id
            return render(request, 'customer/renting.html', {
                "iha": Ihas.objects.filter(Iha_id=iha_id)[0]
            })
        return redirect("login")  # Kullanıcı oturumu yoksa giriş sayfasına yönlendir

    if request.method == "POST":
        # Kullanıcı doğrulaması
        customer_id = request.session.get('customer_id')
        if not customer_id:
            return redirect("login")  # Kullanıcı oturumu yoksa giriş sayfasına yönlendir

        iha_id = id

        datetimes = request.POST.get("datetimes")
        start_date_str, end_date_str = datetimes.split(' - ')
        start_date = datetime.strptime(start_date_str, '%m/%d/%Y %H:%M')
        end_date = datetime.strptime(end_date_str, '%m/%d/%Y %H:%M')

        ######################################
        if not Ihas.objects.filter(Iha_id=iha_id).exists():
            return render(request, "customer/renting.html", {
                "error": "Böyle bir iha yok.",
            })
        ######################################
        if start_date > end_date:
            return render(request, "customer/renting.html", {
                "error": "Kiralama başlangıcı ve bitişinde bir sorun var. Lütfen Kontrol edin.",
                "iha": Ihas.objects.filter(Iha_id=iha_id)[0]
            })
        ######################################
        if Ihas.objects.filter(Iha_id=iha_id)[0].Musaitlik == 0:
            return render(request, "customer/renting.html", {
                "error": "İstediğiniz iha müsait değil.",
                "iha": Ihas.objects.filter(Iha_id=iha_id)[0]
            })
        ######################################
        if not Ihas.objects.filter(Iha_id=iha_id)[0].Bakim_yapildi_mi:
            return render(request, "customer/renting.html", {
                "error": "İstediğiniz iha'nın bakımları henüz tamamlanmadı. Lütfen başka bir iha seçiniz.",
                "iha": Ihas.objects.filter(Iha_id=iha_id)[0]
            })
        ######################################
        if not Ihas.objects.filter(Iha_id=iha_id)[0].Status:
            return render(request, "customer/renting.html", {
                "error": "Bu iha geçici süreliğine kullanılamamaktadır.",
                "iha": Ihas.objects.filter(Iha_id=iha_id)[0]
            })
        ######################################
        else:
            # koşullar sağlanmış demektir..
            # CRUD (CREATE)
            rented = Rent(Customer_id=Customer.objects.filter(Customer_id=customer_id)[0],
                          Iha_id=Ihas.objects.filter(Iha_id=iha_id)[0],
                          kira_baslangic=start_date,
                          kira_bitis=end_date)
            rented.save()

            # kiralanan ihanın stok güncellemesini gerçekleştirmeliyiz.
            # CRUD (UPDATE)
            iha_stok = Ihas.objects.filter(Iha_id=iha_id)[0]
            iha_stok.Musaitlik -= 1
            iha_stok.save()

            return render(request, "customer/renteds.html",
                          {
                              "success": "Tebrikler iha kiralama işleminiz başarılı. İyi sürüşler.",
                              "renteds": Rent.objects.filter(Customer_id=customer_id)
                          })


def renteds(request):
    if request.method == "GET":
        if not request.session.get('user_logged_in'):
            # Kullanıcı oturumu kapalı
            return redirect('login')

        customer_id = request.session.get('customer_id')
        return render(request, 'customer/renteds.html', {
            "renteds": Rent.objects.filter(Customer_id=customer_id),
            "customer_id": Customer.objects.filter(Customer_id=customer_id)[0].Customer_id
        })

    if request.method == "POST":
        # Kullanıcı doğrulaması
        customer_id = request.session.get('customer_id')
        if not customer_id:
            return redirect("login")  # Kullanıcı oturumu yoksa giriş sayfasına yönlendir


def rent_update(request, id):
    if request.method == "GET":
        if not request.session.get('user_logged_in'):
            # Kullanıcı oturumu kapalı
            return redirect('login')
        ################################################
        rent = Rent.objects.filter(id=id)[0]
        return render(request, 'customer/rent-update.html', {
            "rent": rent
        })

    if request.method == "POST":
        # Kullanıcı doğrulaması
        customer_id = request.session.get('customer_id')
        rent = Rent.objects.filter(id=id)[0]

        datetimes = request.POST.get("datetimes")
        start_date_str, end_date_str = datetimes.split(' - ')
        rent.kira_baslangic = datetime.strptime(start_date_str, '%m/%d/%Y %H:%M')
        rent.kira_bitis = datetime.strptime(end_date_str, '%m/%d/%Y %H:%M')

        if not customer_id:
            return redirect("login")  # Kullanıcı oturumu yoksa giriş sayfasına yönlendir
        ################################################
        if not request.POST.get("datetimes"):
            return render(request, "customer/rent-update.html", {
                "error": "Tarihler boş bırakılamaz.",
                "rent": rent
            })
        ######################################
        if rent.kira_baslangic > rent.kira_bitis:
            return render(request, "customer/rent-update.html", {
                "error": "Kiralama başlangıcı ve bitişinde bir sorun var. Lütfen Kontrol edin.",
                "rent": Rent.objects.filter(id=id)[0]
            })
        ################################################
        # kiralama update
        # CRUD (UPDATE)
        rent.save()
        iha_by_rent_id = Ihas.objects.filter(Iha_id=Rent.objects.filter(id=id)[0].Iha_id_id)[0]
        success_message = f"Başarılı. <b>{rent.id}</b> kiralama numaralı <b>{iha_by_rent_id.Marka}</b> / <b>{iha_by_rent_id.Model}</b> kiralamanızın tarihleri başarıyla değiştirildi."
        return render(request, "customer/renteds.html",
                      {
                          "success": success_message,
                          "renteds": Rent.objects.filter(Customer_id=customer_id)
                      })


def rent_delete(request):
    #  CRUD (DELETE) İPTAL İŞLEMİNİ AJAX KULLANARAK GERÇEKLEŞTİRİR.
    # burada gerçekleştirilen işlem gerçek bir silme işlemi değildir.
    # böyle çalışmalarda veritabanından veri silinmesi pek tercih edilen bir yöntem değildir.
    if request.method == "POST" and request.accepts('application/json'):
        obj_id = request.POST.get("obj_id")
        try:
            rent = Rent.objects.filter(id=obj_id)[0]
            rent.Status = False
            rent.save()
            return JsonResponse({"success": True})
        except Rent.DoesNotExist:
            return JsonResponse({"success": False, "error": "Object not found"})
    else:
        return JsonResponse({"success": False, "error": "Invalid request"})
