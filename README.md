# RuufSolarTarea
tarea postulacion Ruuf

primero se necesita encontrar la formula para que el algoritmo pueda hacer el calculo de cuantos paneles caben dentro del techo, para poder suplir cada prueba unitaria que se solicita ingrese un menu
donde pudiese ingresar manualmente cada valor y asi probar con otro valores si se quiere.

la formula a utilizar es:

  total = | X/a | X | Y/b |

  en caso de que quedasen espacios sobrantes en una orientacion distinta esta se calcula usando la variable sobra_x en caso orizontal y sobra_y vertical

el algoritmo repite intercambiando a y b para ver en cual de las dos orientaciones consigue mas cupos y el print final es el maximo definido con:
          maximo = max (colocacion(a,b),colocacion(b,a))

