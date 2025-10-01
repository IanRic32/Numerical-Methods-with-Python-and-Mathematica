
# Métodos de Integración Numérica con Python y Wolfram Mathematica

Este proyecto es una **aplicación de escritorio** desarrollada en **Python** (usando la librería **PyQt5**) que proporciona una interfaz gráfica para calcular **integrales definidas**, tanto simples como dobles, utilizando una variedad de métodos de integración numérica.

Para la determinación del **valor exacto de la integral** y el cálculo de errores, se integra el poder simbólico de **Wolfram Mathematica** a través de su Kernel.

---

## 🚀 Características Principales

* **Interfaz Gráfica (GUI):** Desarrollada con **PyQt5** y archivos `.ui` de Qt Designer.
* **Métodos de Integración Implementados:**
    * Regla del Trapecio (Simple y Compuesta).
    * Regla de Simpson $1/3$ (Simple y Compuesta).
    * Regla de Simpson $3/8$ (Simple y Compuesta).
    * Extrapolación de Richardson.
    * Cuadratura Gaussiana (para $\int_{-1}^{1} f(x) dx$).
* **Integración de Doble Integral:** Soporte para calcular integrales dobles en la mayoría de los métodos, permitiendo definir límites de integración para $x$ y $y$, así como el orden de integración (`dxdy` o `dydx`).
* **Análisis de Error:** Calcula el **Error Verdadero** y el **Error Relativo Porcentual** utilizando el valor exacto proporcionado por Wolfram Mathematica.

---

## 🛠️ Requisitos del Sistema

Para ejecutar este programa, necesitas tener instalados y configurados los siguientes componentes:

* **Python 3.x**
* **Wolfram Mathematica** (con su Kernel configurado).

### Dependencias de Python

Las siguientes librerías de Python son necesarias. Puedes instalarlas usando `pip`:

```bash
pip install PyQt5 numpy sympy wolframclient
```
# ⚙️ Configuración y Ejecución
La parte más crítica de la configuración es vincular correctamente la sesión de Python con el Kernel de Wolfram Mathematica.

1. Configuración del Kernel de Wolfram
El código requiere la ruta exacta al archivo WolframKernel.exe. Debes modificar la siguiente línea en tu archivo principal de Python (Metodos.py si ese fuera el nombre):

``` Python

session=WolframLanguageSession('D:\mathematicaa\WolframKernel.exe')
```
Pasos para obtener tu ruta:

* Localiza la carpeta de instalación de Wolfram Mathematica.

* Busca el archivo WolframKernel.exe.

* Haz clic derecho y ve a Propiedades para obtener la Ubicación del archivo.

* Reemplaza la ruta en la línea de código con la ubicación correcta en tu sistema.

* Nota sobre la ruta en Windows: Asegúrate de usar barras invertidas dobles (\\) o una cadena sin formato (por ejemplo, anteponiendo r al string) para evitar problemas con secuencias de escape.

2. Archivos de Interfaz (UI)
Asegúrate de que los archivos de interfaz .ui generados con Qt Designer se encuentren en el mismo directorio que el script principal de Python:

Metodos.ui

TrapSimple.ui

Simp13Simple.ui

Simp38Simple.ui

TrapComp.ui

Simp13Comp.ui

Simp38Comp.ui

ExtrapolRich.ui

CuadraGauss.ui

3. Ejecución
Una vez configurado el Kernel y teniendo todos los archivos .ui en su lugar, ejecuta el script principal de Python:

python nombre_del_script.py
📝 Notación para Ingreso de Funciones
La aplicación solicita la función en dos formatos diferentes para su correcto procesamiento:

Propósito	Formato Requerido	Ejemplo (Función: sin(x+y))
Aproximación Numérica (SymPy)	Notación compatible con sympy	sin(x+y)
Valor Exacto (Wolfram)	Notación compatible con Wolfram Language	Sin[Plus[x,y]]

Exportar a Hojas de cálculo
¡Importante! En la notación de Wolfram Mathematica, todas las funciones deben comenzar con mayúscula y usar corchetes ([]) para los argumentos (ej: Sin[x], Exp[x]).
## 🧑‍💻  Autores
* Ian Ricardo Rios Velazquez
* Villasecas Carolina
* angel
