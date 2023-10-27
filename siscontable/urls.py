from django.urls import path
from . import views

#creacion de urls del sistema
urlpatterns = [
    path('', views.inicio,name='inicio'),

    #tratamiento de cuentas
    path('cuentas',views.cuenta,name='cuenta'),
    path('registrarCuenta/',views.registrarCuenta,name='registrarCuenta'),#agregar nueva cuenta
    path('editarCuenta/<codigo>',views.editarCuenta,name='editarCuenta'),#iniciar edicion de cuenta existente
    path('edicionCuenta/',views.edicionCuenta, name='edicionCuenta'),#modificacion de cuenta en tiempo real
    path('eliminarCuenta/<codigo>',views.eliminarCuenta, name='elminarCuenta'),#eliminacion de ccuenta

    #tratramiento de transacciones
    path('transacciones',views.transaccion,name="transaccion"),
    path('registrarTransaccion/',views.registrarTransaccion,name="registrarTransaccion"),
    path('eliminarTransaccion/<id>',views.eliminarTransaccion,name="eliminarTransaccion"),

    #balance general
    path('balanceGeneral',views.balanceGeneral,name="balanceGeneral"),
]