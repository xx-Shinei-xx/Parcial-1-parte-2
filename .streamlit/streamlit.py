import streamlit as st
import matplotlib.pyplot as plt
# "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html#scipy.stats.binom"
from scipy.stats import binom

def distribucion_binomial(n, p):
    #para x xd
    x = range(n+1)

    #  distribución binomial
    Prob = binom.pmf(x, n, p)

    #Para la gráfica
    # Mayor parte de los códigos los leí aqui "https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html" :3

    #para el color
    plt.bar(x, Prob, color='black')
    #Título
    plt.title('Distribución binomial ')
    #para el nombre del eje x, el cual es el número de éxitos donde la "x" representa el numero de exitos en la distribución binomial
    plt.xlabel('Número de éxitos "x" ')
    #para el nombre del eje y, el cual es la probabilidad de éxito es p en la distribución binomial 
    plt.ylabel('probabilidad "p"')
    #para los valores en el eje x
    plt.xticks(x)
    #segun entendí, es para ver líneas en la gráfica (no se que tan importante es dentro del código pero lo pongo por si acaso xD)
    plt.grid(True)
    #para ver la gráfica, no puse print porque es para texto
    plt.show()
    st.pyplot(fig)

#para el nombre de la persona
name = input('Por favor indicame tu nombre:')
print(f'Hola {name}')


#definimos los valores para n y para p
def valores_de_n_y_p():
  # para que el usuario solo pueda ingresar los valores válidos, se utiliza el bucle 'while' para que pide los valores repetidamente hasta tener los valroes válidos
    while True:
      #Para los errores, se usará try y except, ya que dentro de try estará el código que se ejecutará para finalizar el progarama programa, mientras que except estará por si no se ponen los valores válidos
        try:
          #para los valroes de n (número de experimentos realizados)
            n = int(input("Por favor ingrese un valor de n menor que 100: "))
            if n >= 100:
                print("Por favor ingrese un valor de n menor que 100")
                continue
                #para los valores de p (probabilidad)
            p = float(input("Por favor ingrese un valor de p, tal que p es mayor que 0 pero menor que 1 : "))
            if p <= 0 or p >= 1:
              #mensaje para solicitar valores correctos
                print("Por favor ingresar un valor de p válido")
                continue

            return n, p
        except ValueError:
            print("Por favor, ingrese valores válidos")

#me guie en esta parte leyendo este codigo "https://stackoverflow.com/questions/419163/what-does-if-name-main-do" 
if __name__ == "__main__":
    choice = input(f"Dime {name}, ¿te gustaría ingresar valores personalizados para n y p? (si/no): ")
    if choice.lower() == 'si':
        n, p = valores_de_n_y_p()
    else:
        # Default values
        n = 1
        p = 0.5

    distribucion_binomial(n, p)
    #fin






