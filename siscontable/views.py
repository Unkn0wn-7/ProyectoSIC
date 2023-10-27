from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse
from .models import Cuenta, Transaccion
# Create your views here.

#creacion de la vista inicio del sisteama
def inicio(request):
    return render(request,'paginas/inicio.html')

#Tratamiento de cuentas
def cuenta(request):
    Listacuentas = Cuenta.objects.all()
    return render(request,'paginas/cuentas.html',{"cuentas":Listacuentas})

def registrarCuenta(request):
    codigo=request.POST['txtcodigo']
    tipo=request.POST['txttipo']
    nombre=request.POST['txtnombre']

    cuenta=Cuenta.objects.create(codigo=codigo,tipo=tipo,nombre=nombre)
    return redirect('/cuentas')

def editarCuenta(request,codigo):
    cuenta = Cuenta.objects.get(codigo=codigo)
    return render(request, "paginas/editarCuenta.html",{"cuenta":cuenta})

def edicionCuenta(request):
    codigo=request.POST['txtcodigo']
    tipo=request.POST['txttipo']
    nombre=request.POST['txtnombre']
    
    cuenta = Cuenta.objects.get(codigo=codigo)
    cuenta.codigo=codigo
    cuenta.tipo=tipo
    cuenta.nombre=nombre
    cuenta.save()
    return redirect('/cuentas')

def eliminarCuenta(request,codigo):
    cuenta = Cuenta.objects.get(codigo=codigo)
    cuenta.delete()
    return redirect('/cuentas')

#Tratamiento de transacciones
def transaccion(request):
    transacciones=Transaccion.objects.all()
    cuentas=Cuenta.objects.all()
    return render(request,"paginas/transaccion.html",{"transacciones":transacciones,"cuentas":cuentas})

def registrarTransaccion(request):
    fecha=request.POST["txtfecha"]
    concepto=request.POST["concepto"]
    nomCuenta=request.POST["cuenta"]
    monto=request.POST["monto"]

    transaccion=Transaccion.objects.create(fecha=fecha,concepto=concepto,nomCuenta=nomCuenta,monto=monto)
    return redirect('/transacciones')

def eliminarTransaccion(request,id):
    transaccion = Transaccion.objects.get(id=id)
    transaccion.delete()
    return redirect('/transacciones')

#balance general
def balanceGeneral(request):
    cuentas = Cuenta.objects.all()

    #inicializar diccionarios para calcular totales debe y haber
    total_debe = {}
    total_haber = {}

    #calcular el total debe
    transacciones_debe  = Transaccion.objects.filter(concepto='Debe')
    for transaccion in transacciones_debe:
        nombre_cuenta = transaccion.nomCuenta
        monto = transaccion.monto
        if nombre_cuenta in total_debe:
            total_debe[nombre_cuenta] += monto
        else:
            total_debe[nombre_cuenta] = monto

    #calcular el total haber
    transacciones_haber = Transaccion.objects.filter(concepto='Haber')
    for transaccion in transacciones_haber:
        nombre_cuenta = transaccion.nomCuenta
        monto = transaccion.monto
        if nombre_cuenta in total_haber:
            total_haber[nombre_cuenta] += monto
        else:
            total_haber[nombre_cuenta] = monto
    
    #Actualizar los campos totaldeb y total haber de cada cuenta
    for cuenta in cuentas:
        nombre_cuenta = cuenta.nombre
        cuenta.totalDebe = total_debe.get(nombre_cuenta, 0)
        cuenta.totalHaber = total_haber.get(nombre_cuenta, 0)
        cuenta.save()

    #calcular saldos
    for cuenta in cuentas:
        if cuenta.totalDebe > cuenta.totalHaber:
            cuenta.totalDebe -= cuenta.totalHaber
            cuenta.totalHaber = 0
        else:
            cuenta.totalHaber -= cuenta.totalDebe
            cuenta.totalDebe = 0
        cuenta.save()
        
    #calcular totales
    total_debe = sum(c.totalDebe for c in cuentas)
    total_haber = sum(c.totalHaber for c in cuentas)
    return render(request,'paginas/balance.html',{'cuentas':cuentas,'total_debe': total_debe, 'total_haber': total_haber})