from django.shortcuts import render, redirect
from pharmacy.forms import EmployeeForm
from pharmacy.models import Employee
from pharmacy.models import Pharmacy
from pharmacy.forms import PharmacyForm
from pharmacy.models import Tablet
from pharmacy.forms import TabletForm
from django.db import connection

def index(request):
    return render(request,'pharmacy/index.html')


# Create your views here.
def eadd(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/eshow')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'pharmacy/eadd.html', {'form': form})


def eshow(request):
    employees = Employee.objects.all()
    return render(request, "pharmacy/eshow.html", {'employees': employees})

def padd(request):
    if request.method == "POST":
        form = PharmacyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/pshow')
            except:
                pass
    else:
        form = PharmacyForm()
    return render(request, 'pharmacy/padd.html', {'form': form})


def pshow(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, "pharmacy/pshow.html", {'pharmacies': pharmacies})


def pedit(request, id):
    pharmacy = Pharmacy.objects.get(id=id)
    return render(request, 'pharmacy/pedit.html', {'pharmacy': pharmacy})


def pupdate(request, id):
    pharmacy = Pharmacy.objects.get(id=id)
    form = PharmacyForm(request.POST, instance=pharmacy)
    if form.is_valid():
        form.save()
        return redirect("/pshow")
    return render(request, 'pharmacy/pedit.html', {'pharmacy': pharmacy})


def pdestroy(request, id):
    pharmacy = Pharmacy.objects.get(id=id)
    pharmacy.delete()
    return redirect("/pshow")

def madd(request):
    if request.method == "POST":
        form = TabletForm(request.POST)
        print(form)

        if form.is_valid():
            try:
                form.save()
                cursor = connection.cursor()
                cursor.execute('update tb set ttprice=tquantity*tprice')
                return redirect('/mshow')
            except:
                pass
    else:
        form = TabletForm()
    return render(request, 'pharmacy/madd.html', {'form': form})


def mshow(request):
    medicines = Tablet.objects.all()
    return render(request, "pharmacy/mshow.html", {'medicines': medicines})


def medit(request, id):
    medicine = Tablet.objects.get(id=id)
    return render(request, 'pharmacy/medit.html', {'medicine': medicine})


def mupdate(request, id):
    medicine = Tablet.objects.get(id=id)
    form = TabletForm(request.POST, instance=medicine)
    if form.is_valid():
        form.save()
        cursor = connection.cursor()
        cursor.execute('update tb set ttprice=tquantity*tprice')
        return redirect("/mshow")

    return render(request, 'pharmacy/medit.html', {'medicine': medicine})


def mdestroy(request, id):
    medicine = Tablet.objects.get(id=id)
    medicine.delete()
    return redirect("/mshow")
def mshowy(request):
    medicines = Tablet.objects.all()
    return render(request, "pharmacy/mshowy.html", {'medicines': medicines})

def mshowm(request):
    medicines = Tablet.objects.all()
    return render(request, "pharmacy/mshowm.html", {'medicines': medicines})
def mshowd(request):
    medicines = Tablet.objects.all()
    return render(request, "pharmacy/mshowd.html", {'medicines': medicines})



# Create your views here.


# Create your views here.


# Create your views here.
