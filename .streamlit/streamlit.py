import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
 
# Para la distribucion binomial
def distribucion_binomial(n, p):
    # Para los valores de x 
    x = np.arange(0, n+1)
    # Formula de la distribucion binomial 
    y = np.array([np.math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in x])

 #Para la gráfica
    # Mayor parte de los códigos los leí aqui "https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html" :3

    #para el color
    #plt.bar(x, Prob, color='black')
    plt.bar(x, y, color="black")
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
    st.pyplot()

 

#para el nombre de la persona
#name = input('Por favor indicame tu nombre:')
#print(f'Hola {name}')


#definimos los valores para n y para p
def valores_de_n_y_p():
 # Para el título
    st.title('Distribución binomial')
 #una breve descrippcion del programa
    st.write("Esta app fue creada con el propósito de mostrar distribuciones binomiales. La distribución binomial modela la probabilidad discreta del número de éxitos en una serie de ensayos independientes, donde cada ensayo tiene una probabilidad fija de éxito. ")

    # #para los valores de n (número de experimentos realizados)
    n = st.number_input("Por favor ingrese un valor de n menor que 100:  ",  min_value=1, max_value=100, value=1, step=1)
     #para los valores de p (probabilidad)
    p = st.number_input("Por favor ingrese un valor de p, tal que p es mayor que 0 pero menor que 1 : ", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

 #usando los widgets
    if st.button("Graficar"):
        if p > 1:
            st.error("¿Podrías ingresar un valor de p mayor a 0 y menor que 1?.")
        else:
         distribucion_binomial(int(n), p)
         
if __name__ == "__main__":
    valores_de_n_y_p()
