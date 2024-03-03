import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
 
st.set_option('deprecation.showPyplotGlobalUse', False)



# Para la distribucion binomial
def distribucion_binomial(n, p):
    # Para los valores de x 
    x = np.arange(0, n+1)
    # Formula de la distribucion binomial 
    y = np.array([np.math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in x])

 #Para la gráfica
    # Mayor parte de los códigos los leí aqui "https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html" :3

     # Para hacer que la gráfica tenga varios colores 
    norm = Normalize(vmin=0, vmax=max(y))
    cmap = plt.get_cmap('viridis')

    # Para graficar con varios colores cada barrita
    plt.bar(x, y, color=cmap(norm(y)))
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


  # User input for n and p
    n = st.slider("Select the value of n (number of trials)", min_value=1, max_value=100, value=1, step=1)
    p = st.slider("Select the value of p (probability of success)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    if st.button("Plot Distribution"):
        if p > 1:
            st.error("Error: The probability p cannot be greater than 1.")
        else:
            # Call the plot function and display the plot using st.pyplot()
            plot = plot_binomial_distribution(int(n), p)
            st.pyplot(plot)
if __name__ == "__main__":
    valores_de_n_y_p()
