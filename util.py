#Funciones Utiles

def Welcome():
    print("Bienvido a Apylabrado!!")
def Instruction():
    print("Las instrucciones para jugar son:")
    print("1-Introduce las Palabras en MAYUSCULAS")
    print("2-La primera palabra debe pasar por la casilla central")
    print("3-Salvo la primera palabra, todas deben ocupar como minimo una ficha ya existente en el tablero")
    print("4-Solo hay dos direcciones para colores las fichas: Vertical(V) y Horizontal(H)")
    print("5-Puedes Poner LEGENDHELP para ver las leyendas del Tablero.")

def legend():
    """
    Muestra en pantalla, haciendo uso de matplotlib, la leyenda del tablero.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure(figsize=[20,1])
    ax = fig.add_subplot(1,1,1)
    
    #Word x 3
    vertex = np.array([[0.05,0.2],[0.1,0.2],[0.1,0.8],[0.05,0.8]])
    polygon = plt.Polygon(vertex,color="#FFCCCC")
    ax.add_artist(polygon)
    ax.text(0.11,0.4,"3x Palabra",size=15,weight="demibold")

    #Word x 2
    vertex = np.array([[0.22,0.2],[0.27,0.2],[0.27,0.8],[0.22,0.8]])
    polygon = plt.Polygon(vertex,color="#B2FFCD")
    ax.add_artist(polygon)
    ax.text(0.28,0.4,"2x Palabra",size=15,weight="demibold")

    #Pawn x3
    vertex = np.array([[0.4,0.2],[0.45,0.2],[0.45,0.8],[0.4,0.8]])
    polygon = plt.Polygon(vertex,color="#CCCEFF")
    ax.add_artist(polygon)
    ax.text(0.46,0.4,"3x Pawn",size=15,weight="demibold")

    #Pawn x2
    vertex = np.array([[0.55,0.2],[0.6,0.2],[0.6,0.8],[0.55,0.8]])
    polygon = plt.Polygon(vertex,color="#CCF9FF")
    ax.add_artist(polygon)
    ax.text(0.61,0.4,"2x Pawn",size=15,weight="demibold")

    plt.show()