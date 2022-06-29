# -*- coding: utf-8 -*-
"""
@author: riosv, carolina, angel
"""
import sys
import os
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from PyQt5 import (uic,QtGui)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import math
from sympy import *
import sympy as sp
import numpy as np
from sympy.abc import x,y
from wolframclient.language import*
from wolframclient.evaluation import *

session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
rootdir=os.path.dirname(os.path.abspath(__file__))
Interfaz1=rootdir+'\Metodos.ui'
Interfaz2=rootdir+'\TrapSimple.ui'
Interfaz3=rootdir+'\Simp13Simple.ui'
Interfaz4=rootdir+'\Simp38Simple.ui'
Interfaz5=rootdir+'\TrapComp.ui'
Interfaz6=rootdir+'\Simp13Comp.ui'
Interfaz7=rootdir+'\Simp38Comp.ui'
Interfaz8=rootdir+'\ExtrapolRich.ui'
Interfaz9=rootdir+'\CuadraGauss.ui'

DesignerQt1,BaseQt1=uic.loadUiType(Interfaz1)
       
class VentanaMetodos(DesignerQt1,BaseQt1):
    def __init__(self):
        DesignerQt1.__init__(self)
        BaseQt1.__init__(self)
        self.setupUi(self)
        self.TS.clicked.connect(self.VincularTraS)
        self.S13S.clicked.connect(self.VincularSim13S)
        self.S38S.clicked.connect(self.VincularSim38S)
        self.TC.clicked.connect(self.VincularTraC)
        self.S13C.clicked.connect(self.VincularSim13C)
        self.S38C.clicked.connect(self.VincularSim38C)
        self.ER.clicked.connect(self.VincularExtraRich)
        self.CG.clicked.connect(self.VincularCuadGauss)
        
    def VincularTraS(self):
        self.VTS=VentanaTrapecioSimple()
        self.VTS.show()
        
    def VincularSim13S(self):
        self.VS13S=VentanaSimpson13S()
        self.VS13S.show()
        
    def VincularSim38S(self):
        self.VS38S=VentanaSimpson38S()
        self.VS38S.show()
        
    def VincularTraC(self):
        self.VTC=VentanaTrapecioComp()
        self.VTC.show()
        
    def VincularSim13C(self):
        self.VS13C=VentanaSimpson13Comp()
        self.VS13C.show()
        
    def VincularSim38C(self):
        self.VS38C=VentanaSimpson38Comp()
        self.VS38C.show()
        
    def VincularExtraRich(self):
        self.VER=VentanaExtrapolRich()
        self.VER.show()
        
    def VincularCuadGauss(self):
        self.VCG=VentanaCuadGaussian()
        self.VCG.show()
        
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
          
DesignerQt2,BaseQt2=uic.loadUiType(Interfaz2)

class VentanaTrapecioSimple(DesignerQt2,BaseQt2):
    def __init__(self):
        DesignerQt2.__init__(self)
        BaseQt2.__init__(self)
        self.setupUi(self)
        self.Simple.clicked.connect(self.Integral)
        self.Doble.clicked.connect(self.Integral)
        self.IngresarValores.clicked.connect(self.IngVal)
        self.Valora.setEnabled(False)
        self.Valorb.setEnabled(False)
        self.Valorc.setEnabled(False)
        self.Valord.setEnabled(False)
        self.Orden.setEnabled(False)
        self.Funcion.setEnabled(False)
        self.Funcion2.setEnabled(False)
        self.Valora.setValidator(QtGui.QDoubleValidator())
        self.Valorb.setValidator(QtGui.QDoubleValidator())
        self.Valorc.setValidator(QtGui.QDoubleValidator())
        self.Valord.setValidator(QtGui.QDoubleValidator())
        
    
    def Integral(self):
        if self.Simple.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(False)
            self.Valord.setEnabled(False)
            self.Orden.setEnabled(False)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Funcion.clear()
            self.c.clear()
            self.d.clear()
            self.ordenint.clear()
            
        if self.Doble.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.c.setAlignment(Qt.AlignCenter)
            self.d.setAlignment(Qt.AlignCenter)
            self.ordenint.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral de 'x' ")
            self.b.setText("Ingrese el limite superior de la integral de 'x' ")
            self.c.setText("Ingrese el limite inferior de la integral de 'y' ")
            self.d.setText("Ingrese el limite superior de la integral de 'y' ")
            self.ordenint.setText("Ingrese el orden (dxdy o dydx)")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(True)
            self.Valord.setEnabled(True)
            self.Orden.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Funcion.clear()
        
    def IngVal(self):
        if self.Simple.isChecked()==True:
            a=self.Valora.text()
            b=self.Valorb.text()
            f=sp.sympify(self.Funcion.text())
            f2=self.Funcion2.text()
            
            vaprox=((b-a)/2)*(f.subs(x,a)+f.subs(x,b))
            session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
            session.evaluate('f[x_]:='+f2)
            session.evaluate('fi[x_]:='+a)
            session.evaluate('fs[x_]:='+b)

            real=session.evaluate(wl.NIntegrate(Global.f(Global.x),[Global.x,Global.fi(Global.x),Global.fs(Global.x)]))
            everd=abs(real-vaprox.evalf(10))
            eporc=abs((real-vaprox.evalf(10))/real*100)
        
            self.ValAprox2.setText(str(vaprox.evalf(8)))
            self.ValEx2.setText(str(real))
            self.ErrVer2.setText(str(everd.evalf(8)))
            self.ErrRelPor2.setText(str(eporc.evalf(8)))
            session.terminate()
        if self.Doble.isChecked()==True:
            ax=self.Valora.text()
            bx=self.Valorb.text()
            ay=self.Valorc.text()
            by=self.Valord.text()
            orden=str(self.Orden.text())
            fxy=sp.sympify(self.Funcion.text())
            fxy2=self.Funcion2.text()
            
            I1=0
            if orden == "dxdy":
                hy = (by - ay)
                ys = [by, ay]
                for i in range(0, 2):
                    hx = bx.subs(y, ys[i]) - ax.subs(y, ys[i])
                    I1 = I1 + (hx*(fxy.subs([(x, bx.subs(y, ys[i])), (y, ys[i])]) + fxy.subs([(x, ax.subs(y, ys[i])), (y, ys[i])]))/2)
                vaprox = (hy*I1/2)
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:='+fxy2)
                session.evaluate('fi[y_]:='+ax)
                session.evaluate('fs[y_]:='+bx)
                session.evaluate('fi2[y_]:='+ay)
                session.evaluate('fs2[y_]:='+by)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.y,Global.fi2(Global.y),Global.fs2(Global.y)],[Global.x,Global.fi(Global.y),Global.fs(Global.y)]))                
                everd=abs(real-vaprox.evalf(10))
                eporc=abs((real-vaprox.evalf(10))/real*100)
                
                self.ValAprox2.setText(str(vaprox.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
            
            else:
                hx = (bx - ax)
                xs = [bx, ax]
                for i in range(0, 2):
                    hy = by.subs(x, xs[i]) - ay.subs(x, xs[i])
                    I1 = I1 + (hy*(fxy.subs([(y, by.subs(x, xs[i])), (x, xs[i])]) + fxy.subs([(y, ay.subs(x, xs[i])), (x, xs[i])]))/2)
                vaprox = (hx*I1/2)
                
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:='+fxy2)
                session.evaluate('fi[x_]:='+ay)
                session.evaluate('fs[x_]:='+by)
                session.evaluate('fi2[x_]:='+ax)
                session.evaluate('fs2[x_]:='+bx)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.x,Global.fi2(Global.x),Global.fs2(Global.x)],[Global.y,Global.fi(Global.x),Global.fs(Global.x)]))
                
                everd=abs(real-vaprox.evalf(10))
                eporc=abs((real-vaprox.evalf(10))/real*100)
                
                self.ValAprox2.setText(str(vaprox.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
                session.terminate()
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply== QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
       
        
DesignerQt3,BaseQt3=uic.loadUiType(Interfaz3)

class VentanaSimpson13S(DesignerQt3,BaseQt3):
    def __init__(self):
        DesignerQt3.__init__(self)
        BaseQt3.__init__(self)
        self.setupUi(self)
        self.Simple.clicked.connect(self.Integral)
        self.Doble.clicked.connect(self.Integral)
        self.IngresarValores.clicked.connect(self.IngVal)
        self.Valora.setEnabled(False)
        self.Valorb.setEnabled(False)
        self.Valorc.setEnabled(False)
        self.Valord.setEnabled(False)
        self.Orden.setEnabled(False)
        self.Funcion.setEnabled(False)
        self.Funcion2.setEnabled(False)
        self.Valora.setValidator(QtGui.QDoubleValidator())
        self.Valorb.setValidator(QtGui.QDoubleValidator())
        self.Valorc.setValidator(QtGui.QDoubleValidator())
        self.Valord.setValidator(QtGui.QDoubleValidator()) 
           
        
    def Integral(self):
        if self.Simple.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(False)
            self.Valord.setEnabled(False)
            self.Orden.setEnabled(False)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Funcion.clear()
            self.Funcion2.clear()
            self.c.clear()
            self.d.clear()
            self.ordenint.clear()
            
        if self.Doble.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.c.setAlignment(Qt.AlignCenter)
            self.d.setAlignment(Qt.AlignCenter)
            self.ordenint.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral de 'x' ")
            self.b.setText("Ingrese el limite superior de la integral de 'x' ")
            self.c.setText("Ingrese el limite inferior de la integral de 'y' ")
            self.d.setText("Ingrese el limite superior de la integral de 'y' ")
            self.ordenint.setText("Ingrese el orden (dxdy o dydx)")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(True)
            self.Valord.setEnabled(True)
            self.Orden.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Funcion.clear()
            self.Funcion2.clear()
            
            
    def IngVal(self):
        if self.Simple.isChecked()==True:
            a=self.Valora.text()
            b=self.Valorb.text()
            f=sp.sympify(self.Funcion.text())
            f2=self.Funcion2.text()
            
            session.evaluate('f[x_]:=' + f2)
            session.evaluate('fi[x_]:='+a)
            session.evaluate('fs[x_]:='+b)
            real=session.evaluate(wl.Integrate(Global.f(Global.x),[Global.x,Global.fi(Global.x),Global.fs(Global.x)]))
            
            h=(sympify(b)-sympify(a))/2
            vaprox=(h*(f.subs(x,sympify(a))+4*(f.subs(x,sympify(a)+sympify(h)))+f.subs(x,sympify(b))))/3
            
            everd=abs(real-vaprox)
            eporc=abs((real-vaprox)/real)*100
            session.terminate() 
            
            self.ValAprox2.setText(str(vaprox.evalf(8)))
            self.ValEx2.setText(str(real))
            self.ErrVer2.setText(str(everd.evalf(8)))
            self.ErrRelPor2.setText(str(eporc.evalf(8)))
            
        if self.Doble.isChecked()==True: 
            ax=self.Valora.text()
            bx=self.Valorb.text()
            ay=self.Valorc.text()
            by=self.Valord.text()
            orden=str(self.Orden.text())
            fxy=sp.sympify(self.Funcion.text())
            fxy2=self.Funcion2.text()
            
            if orden == "dxdy":
                session.evaluate('fi[y_]:='+ ax)
                session.evaluate('fs[y_]:='+ bx)
                session.evaluate('f[x_,y_]:=' + fxy2)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.x,Global.fi(Global.y),Global.fs(Global.y)],[Global.y,float(ay),float(by)]))
                
                hx=(sympify(bx)-sympify(ax))/2
                vaprox=sp.sympify((hx*(fxy.subs(x,sympify(ax))+4*fxy.subs(x,(sympify(ax)+sympify(bx))/2)+fxy.subs(x,sympify(bx))))/3)
                hy=(sympify(by)-sympify(ay))/2
                vaprox2=(hy*(vaprox.subs(y,sympify(ay))+4*vaprox.subs(y,(sympify(ay)+sympify(by))/2)+vaprox.subs(y,sympify(by))))/3 
                
                everd=abs(real-vaprox2.evalf(10))
                eporc=abs((real-vaprox2.evalf(10))/real*100)
                session.terminate() 
                
                self.ValAprox2.setText(str(vaprox2.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
                
            else:
                session.evaluate('fi[x_]:='+ ay)
                session.evaluate('fs[x_]:='+ by)
                session.evaluate('fi2[x_]:='+ ax)
                session.evaluate('fs2[x_]:='+ bx)                
                session.evaluate('f[x_,y_]:=' + fxy2)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.y,Global.fi(Global.x),Global.fs(Global.x)],[Global.x,Global.fi2(Global.x),Global.fs2(Global.x_)]))
                
                hy=(sympify(by)-sympify(ay))/2
                vaprox=sp.sympify((hy*(fxy.subs(y,sympify(ay))+4*fxy.subs(y,(sympify(ay)+sympify(by))/2)+fxy.subs(y,sympify(by))))/3)
                hx=(sympify(bx)-sympify(ax))/2
                
                vaprox2=(hx*(vaprox.subs(x,sympify(ax))+4*vaprox.subs(x,(sympify(ax)+sympify(bx))/2)+vaprox.subs(x,sympify(bx))))/3 
                everd=abs(real-vaprox2.evalf(10))
                eporc=abs((real-vaprox2.evalf(10))/real*100)
                session.terminate() 
                
                self.ValAprox2.setText(str(vaprox2.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
            
        
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply== QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
                
        
DesignerQt4,BaseQt4=uic.loadUiType(Interfaz4)

class VentanaSimpson38S(DesignerQt4,BaseQt4):
    def __init__(self):
        DesignerQt4.__init__(self)
        BaseQt4.__init__(self)
        self.setupUi(self)
        self.Simple.clicked.connect(self.Integral)
        self.Doble.clicked.connect(self.Integral)
        self.IngresarValores.clicked.connect(self.IngVal)
        self.Valora.setEnabled(False)
        self.Valorb.setEnabled(False)
        self.Valorc.setEnabled(False)
        self.Valord.setEnabled(False)
        self.Orden.setEnabled(False)
        self.Funcion.setEnabled(False)
        self.Funcion2.setEnabled(False)
        self.Valora.setValidator(QtGui.QDoubleValidator())
        self.Valorb.setValidator(QtGui.QDoubleValidator())
        self.Valorc.setValidator(QtGui.QDoubleValidator())
        self.Valord.setValidator(QtGui.QDoubleValidator())
        
    
    def Integral(self):
        if self.Simple.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(False)
            self.Valord.setEnabled(False)
            self.Orden.setEnabled(False)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Funcion.clear()
            self.c.clear()
            self.d.clear()
            self.ordenint.clear()
            
        if self.Doble.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.c.setAlignment(Qt.AlignCenter)
            self.d.setAlignment(Qt.AlignCenter)
            self.ordenint.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral de 'x' ")
            self.b.setText("Ingrese el limite superior de la integral de 'x' ")
            self.c.setText("Ingrese el limite inferior de la integral de 'y' ")
            self.d.setText("Ingrese el limite superior de la integral de 'y' ")
            self.ordenint.setText("Ingrese el orden (dxdy o dydx)")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(True)
            self.Valord.setEnabled(True)
            self.Orden.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Funcion.clear()
        
        
    def IngVal(self):
        if self.Simple.isChecked()==True:
            a=self.Valora.text()
            b=self.Valorb.text()
            f=sp.sympify(self.Funcion.text())
            f2=self.Funcion2.text()
            
            session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
            h=(sympify(b)-sympify(a))/3
            vaprox=(3/8*h)*(f2.subs(x,sympify(a))+3*f2.subs(x,(2*sympify(a)+sympify(b))/3)+3*f2.subs(x,(sympify(a)+2*sympify(b))/3)+f2.subs(x,sympify(b)))
            
            session.evaluate('f[x_]:='+f2)
            session.evaluate('fi[x_]:='+a)
            session.evaluate('fs[x_]:='+b)
            vreal=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.x,Global.fi(Global.x),Global.fs(Global.x)]))
            
            everd=abs(vreal-vaprox.evalf(10))
            eporc=abs((vreal-vaprox.evalf(10))/vreal*100)
            session.terminate()
            
            self.ValAprox2.setText(str(vaprox.evalf(8)))
            self.ValEx2.setText(str(vreal))
            self.ErrVer2.setText(str(everd.evalf(8)))
            self.ErrRelPor2.setText(str(eporc.evalf(8)))
        
        if self.Doble.isChecked()==True: 
            ax=self.Valora.text()
            ax2=sympify(ax)
            bx=self.Valorb.text()
            bx2=sympify(bx)
            ay=self.Valorc.text()
            ay2=sympify(ay)
            by=self.Valord.text()
            by2=sympify(by)
            orden=str(self.Orden.text())
            fxy=sp.sympify(self.Funcion.text())
            fxy2=self.Funcion2.text()
            
            
            I1=0
            if orden == "dxdy":
                hy = (by2 - ay2)
                ys = [by2, ay2]
                for i in range(0, 2):
                    hx = bx2.subs(y, ys[i]) - ax2.subs(y, ys[i])
                    I1 = I1 + (hx*(fxy.subs([(x, bx2.subs(y, ys[i])), (y, ys[i])]) + fxy.subs([(x,ax2.subs(y, ys[i])), (y, ys[i])]))/2)
                vaprox = (hy*I1/2)
                
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:='+fxy2)
                session.evaluate('fi[x_]:='+ax)
                session.evaluate('fs[x_]:='+bx)
                session.evaluate('fi2[y_]:='+ay)
                session.evaluate('fs2[y_]:='+by)
                vreal=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.y,Global.fi2(Global.y),Global.fs2(Global.y)],[Global.x,Global.fi(Global.y),Global.fs(Global.y)]))
                
                everd=abs(vreal-vaprox.evalf(10))
                eporc=abs((vreal-vaprox.evalf(10))/vreal*100)
                
                self.ValAprox2.setText(str(vaprox.evalf(8)))
                self.ValEx2.setText(str(vreal))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
            
            else:
                hx = (bx2 - ax2)
                xs = [bx2, ax2]
                for i in range(0, 2):
                    hy = by2.subs(x, xs[i]) - ay2.subs(x, xs[i])
                    I1 = I1 + (hy*(fxy.subs([(y, by2.subs(x, xs[i])), (x, xs[i])]) + fxy.subs([(y, ay2.subs(x, xs[i])), (x, xs[i])]))/2)
                vaprox = (hx*I1/2)
                
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:=' + fxy2)
                session.evaluate('fi[y_]:='+ ax)
                session.evaluate('fs[y_]:='+ bx)
                session.evaluate('fi2[y_]:='+ay)
                session.evaluate('fs2[y_]:='+by)
                vreal=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.x,Global.fi(Global.y),Global.fs(Global.y)],[Global.y,Global.fi2(Global.y),Global.fs2(Global.y)]))
                
                everd=abs(vreal-vaprox.evalf(10))
                eporc=abs((vreal-vaprox.evalf(10))/vreal*100)
                
                self.ValAprox2.setText(str(vaprox.evalf(8)))
                self.ValEx2.setText(str(vreal))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))

    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply== QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        

DesignerQt5,BaseQt5=uic.loadUiType(Interfaz5)

class VentanaTrapecioComp(DesignerQt5,BaseQt5):
    def __init__(self):
        DesignerQt5.__init__(self)
        BaseQt5.__init__(self)
        self.setupUi(self)
        self.Simple.clicked.connect(self.Integral)
        self.Doble.clicked.connect(self.Integral)
        self.IngresarValores.clicked.connect(self.IngVal)
        self.Valora.setEnabled(False)
        self.Valorb.setEnabled(False)
        self.Valorc.setEnabled(False)
        self.Valord.setEnabled(False)
        self.Orden.setEnabled(False)
        self.Valorn.setEnabled(False)
        self.Funcion.setEnabled(False)
        self.Funcion2.setEnabled(False)
        self.Valora.setValidator(QtGui.QDoubleValidator())
        self.Valorb.setValidator(QtGui.QDoubleValidator())
        self.Valorc.setValidator(QtGui.QDoubleValidator())
        self.Valord.setValidator(QtGui.QDoubleValidator())
        self.Valorn.setValidator(QtGui.QDoubleValidator())
        
    
    def Integral(self):
        if self.Simple.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(False)
            self.Valord.setEnabled(False)
            self.Orden.setEnabled(False)
            self.Valorn.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Valorn.clear()
            self.Funcion.clear()
            self.c.clear()
            self.d.clear()
            self.ordenint.clear()
            
        if self.Doble.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.c.setAlignment(Qt.AlignCenter)
            self.d.setAlignment(Qt.AlignCenter)
            self.ordenint.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral de 'x' ")
            self.b.setText("Ingrese el limite superior de la integral de 'x' ")
            self.c.setText("Ingrese el limite inferior de la integral de 'y' ")
            self.d.setText("Ingrese el limite superior de la integral de 'y' ")
            self.ordenint.setText("Ingrese el orden (dxdy o dydx)")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(True)
            self.Valord.setEnabled(True)
            self.Orden.setEnabled(True)
            self.Valorn.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Valorn.clear()
            self.Funcion.clear()  
            
            
    def IngVal(self):
        if self.Simple.isChecked()==True:
            a=self.Valora.text()
            a2=sympify(a)
            b=self.Valorb.text()
            b2=sympify(b)
            n=int(self.Valorn.text())
            f=sp.sympify(self.Funcion.text())
            f2=self.Funcion2.text()
            
            h = (b2-a2)/n
            vaprox = 0
            puntos = [a2]
            for i in range(1, n):
                puntos.append(puntos[i-1] + h)
            puntos.append(b2)
            for i in range(n+1):
                if i == 0 or i == n:
                    vaprox = vaprox + f.subs(x, puntos[i])/2
                else:
                    vaprox = vaprox + f.subs(x, puntos[i])        
            vaprox = h*vaprox
            session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
            session.evaluate('f[x_]:='+f2)
            session.evaluate('fi[x_]:='+a)
            session.evaliate('fs[x_]:='+b)
            real=session.evaluate(wl.NIntegrate(Global.f(Global.x),[Global.x,Global.fi(Global.x),Globalfs(Global.x)]))            
            everd = real - vaprox
            eporc = (everd*100)/real
            
            self.ValAprox2.setText(str(vaprox.evalf(8)))
            self.ValEx2.setText(str(real))
            self.ErrVer2.setText(str(everd.evalf(8)))
            self.ErrRelPor2.setText(str(eporc.evalf(8)))
            session.terminate()
        if self.Doble.isChecked()==True:
            ax=self.Valora.text()
            ax2=sympify(ax)
            bx=self.Valorb.text()
            bx2=sympify(bx)
            ay=self.Valorc.text()
            ay2=sympify(ay)
            by=self.Valord.text()
            by2=sympify(by)
            orden=str(self.Orden.text())
            n=int(self.Valorn.text())
            fxy=sp.sympify(self.Funcion.text())
            fxy2=self.Funcion2.text()
            
            I=0
            if orden == "dxdy":
                hy = (by2-ay2)/n
                ys = [ay2]
                for i in range(1, n):
                    ys.append(ys[i-1] + hy)
            
                ys.append(by2)
                    
                Isi = []
                for i in range(n+1):
                    Ii = 0
                    ar= ax2.subs(y, ys[i])
                    br= bx2.subs(y, ys[i])
                    hx = (br-ar)/n
                    xs = []
                    for j in range(n+1):
                        xi = ar + hx*j
                        xs.append(xi)
                        
                    for j in range(n+1):
                        if j == 0 or j == n:
                            Ii = Ii + (fxy.subs([(x, xs[j]), (y, ys[i])]))/2
                        else:
                            Ii = Ii + (fxy.subs([(x, xs[j]), (y, ys[i])]))
                    Ii = hx*Ii
                    Isi.append(Ii)
                    
                for i in range(n+1):
                    if i == 0 or i == n:
                        I = I + Isi[i]/2
                    else:
                        I = I + Isi[i]
                vaprox= hy*I
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y]:'+fxy2)
                session.evaluate('fi[y_]:='+ax)
                session.evaluate('fs[y_]:='+bx)
                session.evaluate('fi2[y_]:='+ay)
                session.evaluate('fs2[y_]:='+by)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.y,Global.fi(Global.y),Global.fs(Global.y)],[Global.x,Global.fi2(Global.y),Global.fs2(Global.y)]))
                everd=abs(real-vaprox.evalf(10))
                eporc=abs((real-vaprox.evalf(10))/real*100)
                self.ValAprox2.setText(str(vaprox.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
                session.terminate()                
            else:
                hx = (bx2-ax2)/n
                I = 0
                xs = [ax2] 
                for i in range(1, n):
                    xs.append(xs[i-1] + hx)
            
                xs.append(bx2)
                
                Isi = []
                for i in range(n+1):
                    Ii = 0
                    ar= ay.subs(x, xs[i])
                    br= by.subs(x, xs[i])
                    hy = (br-ar)/n
                    ys = []
                    for j in range(n+1):
                        yi = ar + hy*j
                        ys.append(yi)
                        
                    for j in range(n+1):
                        if j == 0 or j == n:
                            Ii = Ii + (fxy.subs([(x, xs[i]), (y, ys[j])]))/2
                        else:
                            Ii = Ii + (fxy.subs([(x, xs[i]), (y, ys[j])]))
                    Ii = hy*Ii
                    Isi.append(Ii)
                    
                for i in range(n+1):
                    if i == 0 or i == n:
                        I = I + Isi[i]/2
                    else:
                        I = I + Isi[i]
                vaprox= hx*I
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:='+fxy2)
                session.evaluate('fi[x_]:='+ax)
                session.evaluate('fs[x_]:='+bx)
                session.evaluate('fi2[x_]:='+ay)
                session.evaluate('fs2[x_]:='+by)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.x,Global.fi(Global.x),Global.fs(Global.x)],[Global.y,Global.fi2(Global.x),Global.fs2(Global.x)]))
                everd=abs(real-vaprox.evalf(10))
                eporc=abs((real-vaprox.evalf(10))/real*100)
                self.ValAprox2.setText(str(vaprox.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
                session.terminate()
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply== QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
       
        
DesignerQt6,BaseQt6=uic.loadUiType(Interfaz6)

class VentanaSimpson13Comp(DesignerQt6,BaseQt6):
    def __init__(self):
        DesignerQt6.__init__(self)
        BaseQt6.__init__(self)
        self.setupUi(self)
        self.Simple.clicked.connect(self.Integral)
        self.Doble.clicked.connect(self.Integral)
        self.IngresarValores.clicked.connect(self.IngVal)
        self.Valora.setEnabled(False)
        self.Valorb.setEnabled(False)
        self.Valorc.setEnabled(False)
        self.Valord.setEnabled(False)
        self.Orden.setEnabled(False)
        self.Valorn.setEnabled(False)
        self.Funcion.setEnabled(False)
        self.Funcion2.setEnabled(False)
        self.Valora.setValidator(QtGui.QDoubleValidator())
        self.Valorb.setValidator(QtGui.QDoubleValidator())
        self.Valorc.setValidator(QtGui.QDoubleValidator())
        self.Valord.setValidator(QtGui.QDoubleValidator())
        self.Valorn.setValidator(QtGui.QDoubleValidator())
        
    
    def Integral(self):
        if self.Simple.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(False)
            self.Valord.setEnabled(False)
            self.Orden.setEnabled(False)
            self.Valorn.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Valorn.clear()
            self.Funcion.clear()
            self.c.clear()
            self.d.clear()
            self.ordenint.clear()
            
        if self.Doble.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.c.setAlignment(Qt.AlignCenter)
            self.d.setAlignment(Qt.AlignCenter)
            self.ordenint.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral de 'x' ")
            self.b.setText("Ingrese el limite superior de la integral de 'x' ")
            self.c.setText("Ingrese el limite inferior de la integral de 'y' ")
            self.d.setText("Ingrese el limite superior de la integral de 'y' ")
            self.ordenint.setText("Ingrese el orden (dxdy o dydx)")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(True)
            self.Valord.setEnabled(True)
            self.Orden.setEnabled(True)
            self.Valorn.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Valorn.clear()
            self.Funcion.clear()
        
    def IngVal(self):
        if self.Simple.isChecked()==True:
            a=self.Valora.text()
            b=self.Valorb.text()
            a2=sympify(a)
            b2=Sympify(b)
            n=int(self.Valorn.text())
            f=sp.sympify(self.Funcion.text())
            f2=self.Funcion2.text()
            
            m=2*n
            h=(b2-a2)/m
            s=0
            for i in range(1,m):
                s=s+2*(i%2+1)*f.subs(x,a2+i*h)
            s=h/3*(f.subs(x,a2)+s+f.subs(x,b2))
            session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
            session.evaluate('f[x_]:='+f2)
            session.evaluate('fi[x_]:='+a)
            session.evaluate('fs[x_]:='+b)
            real=session.evaluate(wl.NIntegrate(Global.f(Global.x),[Globa.x,Global.fi(Global.x),Global.fs(Global.x)]))            
            everd=abs(real-s.evalf(10))
            eporc=abs((real-s.evalf(10))/real*100)
                
            self.ValAprox2.setText(str(s.evalf(8)))
            self.ValEx2.setText(str(real))
            self.ErrVer2.setText(str(everd.evalf(8)))
            self.ErrRelPor2.setText(str(eporc.evalf(8)))
            session.terminate()
        if self.Doble.isChecked()==True: 
            ax=self.Valora.text()
            bx=self.Valorb.text()
            ay=self.Valorc.text()
            by=self.Valord.text()
            orden=str(self.Orden.text())
            n=int(self.Valorn.text())
            fxy=sp.sympify(self.Funcion.text())
            fxy2=self.Funcion2.text()
            
            if orden == "dydx":
                hx = (bx-ax)/(2*n)
                puntos_x = []
                for i in range(0, 2*n+1):
                    xi = ax + hx*i
                    puntos_x.append(xi)
            
                VaproxIs = []
                for i in range(0, 2*n+1):
                    hy = (by.subs(x, puntos_x[i]) - ay.subs(x, puntos_x[i]))/(2*n)
                    puntos_y = []
                    for j in range(0, 2*n+1):
                        yi = ay.subs(x, puntos_x[i]) + hy*j
                        puntos_y.append(yi)
            
                    VaproxIi = 0
                    for j in range(0, 2*n+1):
                        if j == 0 or j == 2*n:
                            VaproxIi = VaproxIi + fxy.subs({x: puntos_x[i], y: puntos_y[j]})
                        else:
                            if j%2 == 0:
                                VaproxIi = VaproxIi + 2*fxy.subs({x: puntos_x[i], y: puntos_y[j]})
                            else:
                                VaproxIi = VaproxIi + 4*fxy.subs({x: puntos_x[i], y: puntos_y[j]})
            
                    VaproxIi = VaproxIi*hy/3
                    VaproxIs.append(VaproxIi)
                    
                
                Vaprox = 0
                for i in range(2*n+1):
                    if i == 0 or i == 2*n:
                        Vaprox = Vaprox + VaproxIs[i]
                    else:
                        if i%2 == 0:
                            Vaprox = Vaprox + 2*VaproxIs[i]
                        else:
                            Vaprox = Vaprox + 4*VaproxIs[i]
                Vaprox = hx*Vaprox/3
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:='+fxy2)
                session.evaluate('fi[y_]:='+ax)
                session.evaluate('fs[y_]:='+bx)
                session.evaluate('fi2[y_]:='+ay)
                session.evaluate('fs2[y_]:='+by)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.x,Global.fi(Global.y),Global.fs(Global.y)],[Global.y,Global.fi2(Global.y),Global.fs2(Global.y)]))                
                everd=abs(real-Vaprox.evalf(10))
                eporc=abs((real-Vaprox.evalf(10))/real*100)
                
                self.ValAprox2.setText(str(Vaprox.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
                session.terminate()
            else:
                hy = (by-ay)/(2*n)
                puntos_y = []
                for i in range(0, 2*n+1):
                    yi = ay + hy*i
                    puntos_y.append(yi)
            
                VaproxIs = []
                for i in range(0, 2*n+1):
                    hx = (bx.subs(y, puntos_y[i]) - ax.subs(y, puntos_y[i]))/(2*n)
                    puntos_x = []
                    for j in range(0, 2*n+1):
                        xi = ax.subs(y, puntos_y[i]) + hx*j
                        puntos_x.append(xi)
            
                    VaproxIi = 0
                    for j in range(0, 2*n+1):
                        if j == 0 or j == 2*n:
                            VaproxIi = VaproxIi + fxy.subs({y: puntos_y[i], x: puntos_x[j]})
                        else:
                            if j%2 == 0:
                                VaproxIi = VaproxIi + 2*fxy.subs({y: puntos_y[i], x: puntos_x[j]})
                            else:
                                VaproxIi = VaproxIi + 4*fxy.subs({y: puntos_y[i], x: puntos_x[j]})
            
                    VaproxIi = VaproxIi*hx/3
                    VaproxIs.append(VaproxIi)
                
                Vaprox = 0
                for i in range(2*n+1):
                    if i == 0 or i == 2*n:
                        Vaprox = Vaprox + VaproxIs[i]
                    else:
                        if i%2 == 0:
                            Vaprox = Vaprox + 2*VaproxIs[i]
                        else:
                            Vaprox = Vaprox + 4*VaproxIs[i]
                Vaprox = hx*Vaprox/3
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:='+fxy2)
                session.evaluate('fi[x_]:='+ax)
                session.evaluate('fs[x_]:='+bx)
                session.evaluate('fi2[x_]:='+ay)
                session.evaluate('fs2[x_]:='+by)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.x,Global.fi(Global.x),Global.fs(Global.x)],[Global.y,Global.fi2(Global.x),Global.fs2(Global.x)]))

                everd=abs(real-Vaprox.evalf(10))
                eporc=abs((real-Vaprox.evalf(10))/real*100)
                
                self.ValAprox2.setText(str(Vaprox.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
                session.terminate()
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply== QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
                
        
DesignerQt7,BaseQt7=uic.loadUiType(Interfaz7)

class VentanaSimpson38Comp(DesignerQt7,BaseQt7):
    def __init__(self):
        DesignerQt7.__init__(self)
        BaseQt7.__init__(self)
        self.setupUi(self)
        self.Simple.clicked.connect(self.Integral)
        self.Doble.clicked.connect(self.Integral)
        self.IngresarValores.clicked.connect(self.IngVal)
        self.Valora.setEnabled(False)
        self.Valorb.setEnabled(False)
        self.Valorc.setEnabled(False)
        self.Valord.setEnabled(False)
        self.Orden.setEnabled(False)
        self.Valorn.setEnabled(False)
        self.Funcion.setEnabled(False)
        self.Funcion2.setEnabled(False)
        self.Valora.setValidator(QtGui.QDoubleValidator())
        self.Valorb.setValidator(QtGui.QDoubleValidator())
        self.Valorc.setValidator(QtGui.QDoubleValidator())
        self.Valord.setValidator(QtGui.QDoubleValidator())
        self.Valorn.setValidator(QtGui.QDoubleValidator())
        
    
    def Integral(self):
        if self.Simple.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(False)
            self.Valord.setEnabled(False)
            self.Orden.setEnabled(False)
            self.Valorn.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Valorn.clear()
            self.Funcion.clear()
            self.c.clear()
            self.d.clear()
            self.ordenint.clear()
            self.Valorn.setValidator(QtGui.QDoubleValidator())
            
        if self.Doble.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.c.setAlignment(Qt.AlignCenter)
            self.d.setAlignment(Qt.AlignCenter)
            self.ordenint.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral de 'x' ")
            self.b.setText("Ingrese el limite superior de la integral de 'x' ")
            self.c.setText("Ingrese el limite inferior de la integral de 'y' ")
            self.d.setText("Ingrese el limite superior de la integral de 'y' ")
            self.ordenint.setText("Ingrese el orden (dxdy o dydx)")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Valorc.setEnabled(True)
            self.Valord.setEnabled(True)
            self.Orden.setEnabled(True)
            self.Valorn.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Valorc.clear()
            self.Valord.clear()
            self.Orden.clear()
            self.Valorn.clear()
            self.Funcion.clear()
            

    def IngVal(self):
        if self.Simple.isChecked()==True: 
            a=self.Valora.text()
            b=self.Valorb.text()
            n=int(self.Valorn.text())
            f=sp.sympify(self.Funcion.text())
            f2=self.Funcion2.text()
            
            h = (b-a)/(3*n)
            puntos = []
            for i in range(0, 3*n):
                puntos.append(a + i*h)
            puntos.append(b)
            Vaprox = (3*h*(f.subs(x,a) + f.subs(x,b)))/8
            sum1 = 0
            sum2 = 0
            sum3 = 0
            for k in range(1, n):
                sum1 = sum1 + f.subs(x, puntos[3*k])
            
            sum1 = 3*h*sum1/4
            
            for k in range(1, n+1):
                sum2 = sum2 + f.subs(x, puntos[3*k-2])
            
            sum2 = 9*h*sum2/8
            
            for k in range(1, n+1):
                sum3 = sum3 + f.subs(x, puntos[3*k-1])
            
            sum3 = 9*h*sum3/8
            
            Vaprox = Vaprox + sum1 + sum2 + sum3
            session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
            session.evaluate('f[x_]:='+f2)
            session.evaluate('fi[x_]:='+a)
            session.evaluate('fs[x_]:='+b)
            real=session.evaluate(wl.NIntegrate(Global.f(Global.x),[Global.x,Global.fi(Global.x),Global.fs(Global.x)]))
            
            everd=abs(real-Vaprox.evalf(10))
            eporc=abs((real-Vaprox.evalf(10))/real*100)
                
            self.ValAprox2.setText(str(s.evalf(8)))
            self.ValEx2.setText(str(real))
            self.ErrVer2.setText(str(everd.evalf(8)))
            self.ErrRelPor2.setText(str(eporc.evalf(8)))
            session.terminate()
        if self.Doble.isChecked()==True: 
            ax=self.Valora.text()
            bx=self.Valorb.text()
            ay=self.Valorc.text()
            by=self.Valord.text()
            orden=str(self.Orden.text())
            n=int(self.Valorn.text())
            fxy=sp.sympify(self.Funcion.text())
            fxy2=self.Funcion2.text()

            if orden == "dydx":
                hx = (bx-ax)/(3*n)
                puntos_x = []
                for i in range(0, 3*n+1):
                    xi = ax + hx*i
                    puntos_x.append(xi)
                VaproxIs = []
                for i in range(0, 3*n+1):
                    hy = (by.subs(x, puntos_x[i]) - ay.subs(x, puntos_x[i]))/(3*n)
                    puntos_y = []
                    for j in range(0, 3*n+1):
                        yi = ay.subs(x, puntos_x[i]) + hy*j
                        puntos_y.append(yi)
            
                    VaproxIi = (3*hy*(fxy.subs({x: puntos_x[i], y: puntos_y[0]}) + fxy.subs({x: puntos_x[i], y: puntos_y[3*n]})))/8
                    sum1 = 0
                    sum2 = 0
                    sum3 = 0
                    for k in range(1, n):
                        sum1 = sum1 + fxy.subs({x: puntos_x[i], y: puntos_y[3*k]})
            
                    sum1 = 3*hy*sum1/4
            
                    for k in range(1, n+1):
                        sum2 = sum2 + fxy.subs({x: puntos_x[i], y: puntos_y[3*k-2]})
            
                    sum2 = 9*hy*sum2/8
            
                    for k in range(1, n+1):
                        sum3 = sum3 + fxy.subs({x: puntos_x[i], y: puntos_y[3*k-1]})
            
                    sum3 = 9*hy*sum3/8
            
                    VaproxIi = (VaproxIi + sum1 + sum2 + sum3).evalf()
                    VaproxIs.append(VaproxIi)
            
                Vaprox = (3*hx*(VaproxIs[0] + VaproxIs[3*n]))/8
                sum1 = 0
                sum2 = 0
                sum3 = 0
                for k in range(1, n):
                    sum1 = sum1 + VaproxIs[3*k]
            
                sum1 = 3*hx*sum1/4
            
                for k in range(1, n+1):
                    sum2 = sum2 + VaproxIs[3*k-2]
            
                sum2 = 9*hx*sum2/8
            
                for k in range(1, n+1):
                    sum3 = sum3 + VaproxIs[3*k-1]
            
                sum3 = 9*hx*sum3/8
            
                Vaprox = (Vaprox + sum1 + sum2 + sum3)
                
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:='+fxy2)
                session.evaluate('fi[y_]:='+ax)
                session.evaluate('fs[y_]:='+bx)
                session.evaluate('fi2[y_]:='+ay)
                session.evaluate('fs2[y_]:='+by)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.y,Global.fi2(Global.y),Global.fs2(Global.y)],[Global.x,Global.fi(Global.y),Global.fs(Global.y)]))
                
                everd=abs(real.evalf(10)-Vaprox.evalf(10))
                eporc=abs((real-Vaprox.evalf(10))/real*100)
                
                self.ValAprox2.setText(str(Vaprox.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
                session.terminate()
            else:
                hy = (by-ay)/(3*n)
                puntos_y = []
                for i in range(0, 3*n+1):
                    yi = ay + hy*i
                    puntos_y.append(yi)
                VaproxIs = []
                for i in range(0, 3*n+1):
                    hx = (bx.subs(y, puntos_y[i]) - ax.subs(y, puntos_y[i]))/(3*n)
                    puntos_x = []
                    for j in range(0, 3*n+1):
                        xi = ax.subs(y, puntos_x[i]) + hx*j
                        puntos_x.append(xi)
            
                    VaproxIi = (3*hx*(fxy.subs({y: puntos_y[i], x: puntos_x[0]}) + fxy.subs({y: puntos_y[i], x: puntos_x[3*n]})))/8
                    sum1 = 0
                    sum2 = 0
                    sum3 = 0
                    for k in range(1, n):
                        sum1 = sum1 + fxy.subs({y: puntos_y[i], x: puntos_x[3*k]})
            
                    sum1 = 3*hx*sum1/4
            
                    for k in range(1, n+1):
                        sum2 = sum2 + fxy.subs({y: puntos_y[i], x: puntos_x[3*k-2]})
            
                    sum2 = 9*hx*sum2/8
            
                    for k in range(1, n+1):
                        sum3 = sum3 + fxy.subs({y: puntos_y[i], x: puntos_x[3*k-1]})
            
                    sum3 = 9*hy*sum3/8
            
                    VaproxIi = VaproxIi + sum1 + sum2 + sum3
                    VaproxIs.append(VaproxIi)
            
                Vaprox = (3*hy*(VaproxIs[0] + VaproxIs[3*n]))/8
                sum1 = 0
                sum2 = 0
                sum3 = 0
                for k in range(1, n):
                    sum1 = sum1 + VaproxIs[3*k]
            
                sum1 = 3*hy*sum1/4
            
                for k in range(1, n+1):
                    sum2 = sum2 + VaproxIs[3*k-2]
            
                sum2 = 9*hy*sum2/8
            
                for k in range(1, n+1):
                    sum3 = sum3 + VaproxIs[3*k-1]
            
                sum3 = 9*hy*sum3/8
            
                Vaprox = Vaprox + sum1 + sum2 + sum3
                session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
                session.evaluate('f[x_,y_]:='+fxy2)
                session.evaluate('fi[x_]:='+ay)
                session.evaluate('fs[x_]:='+by)
                session.evaluate('fi2[x_]:='+ax)
                session.evaluate('fs2[x_]:='+bx)
                real=session.evaluate(wl.NIntegrate(Global.f(Global.x,Global.y),[Global.x,Global.fi2(Global.x),Global.fs2(Global.x)],[Global.y,Global.fi(Global.x),Global.fs(Global.x)]))

                everd=abs(real-Vaprox.evalf(10))
                eporc=abs((real-Vaprox.evalf(10))/real*100)
                
                self.ValAprox2.setText(str(Vaprox.evalf(8)))
                self.ValEx2.setText(str(real))
                self.ErrVer2.setText(str(everd.evalf(8)))
                self.ErrRelPor2.setText(str(eporc.evalf(8)))
                session.terminate()

    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply== QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

DesignerQt8,BaseQt8=uic.loadUiType(Interfaz8)

class VentanaExtrapolRich(DesignerQt8,BaseQt8):
    def __init__(self):
        DesignerQt8.__init__(self)
        BaseQt8.__init__(self)
        self.setupUi(self)
        self.IngresarValores.clicked.connect(self.IngVal)
        self.a.setAlignment(Qt.AlignCenter)
        self.b.setAlignment(Qt.AlignCenter)
        self.a.setText("Ingrese el limite inferior de la integral")
        self.b.setText("Ingrese el limite superior de la integral")
        self.Valora.setEnabled(True)
        self.Valorb.setEnabled(True)
        self.Valorn.setEnabled(True)
        self.Funcion.setEnabled(True)
        self.Valora.setValidator(QtGui.QDoubleValidator())
        self.Valorb.setValidator(QtGui.QDoubleValidator())
        self.Valorn.setValidator(QtGui.QDoubleValidator())
        
    def IngVal(self):
        def trapecio(n):
            h = (b-a)/n
            Vaprox = 0
            puntos = [a]
            for i in np.arange(1, n):
                puntos.append(puntos[i-1] + h)
        
            puntos.append(b)
        
            for i in np.arange(n+1):
                if i == 0 or i == n:
                    Vaprox = Vaprox + fx.subs(x, puntos[i])/2
                else:
                    Vaprox = Vaprox + fx.subs(x, puntos[i])
            Vaprox = h*Vaprox
            return Vaprox
        

        a=float(self.Valora.text())
        b=float(self.Valorb.text())
        k=int(self.Valorn.text())
        fx=sp.sympify(self.Funcion.text())
        R = []
        for i in np.arange(k):
            R.append([])
            for j in np.arange(i):
                R[i].append("")
            if i == 0:
                for j in np.arange(1, k+1):
                    R[i].append(trapecio(pow(2, j-1)))
            else:
                for j in np.arange(i, k):
                    R[i].append((R[i-1][j]*(4**(i)) - R[i-1][j-1])/(4**(i)-1))
                    
        Vaprox = R[k-1][k-1]
        vreal = sp.integrate(fx,(x,a,b))
        everd = vreal - Vaprox
        eporc = (everd*100)/vreal
        self.ValAprox_2.setText(str(Vaprox.evalf(8)))
        self.ValEx_2.setText(str(vreal.evalf(8)))
        self.ErrVer_2.setText(str(everd.evalf(8)))
        self.ErrRelPor_2.setText(str(eporc.evalf(8)))
            
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply== QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
                
        
DesignerQt9,BaseQt9=uic.loadUiType(Interfaz9)

class VentanaCuadGaussian(DesignerQt9,BaseQt9):
    def __init__(self):
        DesignerQt9.__init__(self)
        BaseQt9.__init__(self)
        self.setupUi(self)
        self.n0.clicked.connect(self.Integral)
        self.n1.clicked.connect(self.Integral)
        self.n2.clicked.connect(self.Integral)
        self.IngresarValores.clicked.connect(self.IngVal)
        self.Valora.setEnabled(False)
        self.Valorb.setEnabled(False)
        self.Funcion.setEnabled(False)
        self.Funcion2.setEnabled(False)
        self.Valora.setValidator(QtGui.QDoubleValidator())
        self.Valorb.setValidator(QtGui.QDoubleValidator())
        
    
    def Integral(self):
        if self.n0.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Funcion.clear()
            self.Funcion2.clear()
            
        if self.n1.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Funcion.clear()
            self.Funcion2.clear()
            
        if self.n2.isChecked()==True:
            self.a.setAlignment(Qt.AlignCenter)
            self.b.setAlignment(Qt.AlignCenter)
            self.a.setText("Ingrese el limite inferior de la integral")
            self.b.setText("Ingrese el limite superior de la integral")
            self.Valora.setEnabled(True)
            self.Valorb.setEnabled(True)
            self.Funcion.setEnabled(True)
            self.Funcion2.setEnabled(True)
            self.Valora.clear()
            self.Valorb.clear()
            self.Funcion.clear()
            self.Funcion2.clear()
            

    def IngVal(self):
        if self.n0.isChecked()==True:
            a=float(self.Valora.text())
            b=float(self.Valorb.text())
            fx=sp.sympify(self.Funcion.text())
            fx2=str(self.Funcion2.text())
            t1=-(b-a)/2*0+(b+a)/2
            vaprox=(b-a)/2*(2*fx.subs(x,t1))
            session.evaluate('f[x_]:='+fx2)
            vreal=session.evaluate(wl.NIntegrate(Global.f(Global.x),[Global.x,a,b]))
            everd=abs(vreal-vaprox.evalf(10))
            eporc=abs((vreal-vaprox.evalf(10))/vreal*100)
            
            self.ValAprox_2.setText(str(vaprox.evalf(8)))
            self.ValEx_2.setText(str(vreal))
            self.ErrVer_2.setText(str(everd.evalf(8)))
            self.ErrRelPor_2.setText(str(eporc.evalf(8)))
            
            session.terminate()
        
        if self.n1.isChecked()==True:
            a=float(self.Valora.text())
            b=float(self.Valorb.text())
            fx=sp.sympify(self.Funcion.text())
            fx2=str(self.Funcion2.text())
            t1=-(b-a)/2*1/3**(1/2)+(b+a)/2
            t2=(b-a)/2*1/3*(1/2)+(b+a)/2
            vaprox=(b-a)/2*(fx.subs(x,t1)+fx.subs(x,t2))
            session.evaluate('f[x_]:='+fx2)
            vreal=session.evaluate(wl.NIntegrate(Global.f(Global.x),[Global.x,a,b]))
            everd=abs(vreal-vaprox.evalf(10))
            eporc=abs((vreal-vaprox.evalf(10))/vreal*100)

            self.ValAprox_2.setText(str(vaprox.evalf(8)))
            self.ValEx_2.setText(str(vreal))
            self.ErrVer_2.setText(str(everd.evalf(8)))
            self.ErrRelPor_2.setText(str(eporc.evalf(8)))
            
            session.terminate()
            
        if self.n2.isChecked()==True:
            a=float(self.Valora.text())
            b=float(self.Valorb.text())
            fx=sp.sympify(self.Funcion.text())
            fx2=str(self.Funcion2.text())
            t0=-(b-a)/2*(15**(1/2)/5)+(b+a)/2
            t1=(a+b)/2
            t2=(b-a)/2*(15**(1/2)/5)+(b+a)/2
            vaprox=((b-a)/2)*(5/9)*(fx.subs(x,t0)+8/5*fx.subs(x,t1)+fx.subs(x,t2))
            session.evaluate('f[x_]:='+fx2)
            vreal=session.evaluate(wl.NIntegrate(Global.f(Global.x),[Global.x,a,b]))
            everd=abs(vreal-vaprox.evalf(10))
            eporc=abs((vreal-vaprox.evalf(10))/vreal*100)

            self.ValAprox_2.setText(str(vaprox.evalf(8)))
            self.ValEx_2.setText(str(vreal))
            self.ErrVer_2.setText(str(everd.evalf(8)))
            self.ErrRelPor_2.setText(str(eporc.evalf(8)))

            session.terminate()

    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Advertencia',"¿Esta seguro que desea cerrar esta ventana?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply== QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app=QApplication(sys.argv)
V1=VentanaMetodos()
VentanaTrapecioSimple()
VentanaSimpson13S()
VentanaSimpson38S()
VentanaTrapecioComp()
VentanaSimpson13Comp()
VentanaSimpson38Comp()
VentanaExtrapolRich()
VentanaCuadGaussian()
V1.show()
app.exec_()
del(app)