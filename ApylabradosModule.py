class Pawn():

    points = {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,
                        "J":8,"K":5,"L":1,"M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,"S":1,
                        "T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}

    def __init__(self):
        """
        Constructor de la Clase Pawn.
        letter: Lista vacia que contendra las letras disponibles.
        """

        self.letter = []
        
    
    def addPawn(self,c):
        """
        Añade el caracter c al array letter.
        """

        self.letter.append(c)
    
    def addPawns(self,c,n):
        """
        Añade n veces el caracter c a letters.
        """

        for i in range(n):
            self.addPawn(c)
    
    def createBag(self):
        """
        Agrega las fichas del archivo csv a un objeto Pawn
        """
        import pandas as pd
        bag = pd.read_csv("bag_of_pawns.csv")
        for item in bag.itertuples():
            self.addPawns(item[1],item[2])
    
    def showPawn(self):
        """
        Muestra en pantalla las fichas que tiene el objeto Pawn
        """

        frecuencia = self.getFrequency()
        frecuencia.showFrequency()
    
    def takeRandomPawn(self):
        """
        Toma un elemento cualquiera del array letter, lo elimina del array y lo devuelve
        """
        import numpy as np

        pa = np.random.choice(np.array(self.letter))
        self.letter.remove(pa)
        return pa
    
    def getFrequency(self):
        """
        Crea un objeto FrequencyTable vacio y le va agregando frecuencias usando update(). Devulve el objeto
        FrequencyTable al final
        """
        frecuencia = FrequencyTable()
        for char in self.letter:
            frecuencia.update(char)
        return frecuencia
    
    def takePawn(self,letra):
        """
        Elimina letra del array letter
        """
        self.letter.remove(letra)
    
    def getTotalPawn(self):
        """
        Devuelve la cantidad de fichas que tiene el jugador
        """
        return len(self.letter)
    
    @staticmethod
    def getPoints(c):
        """
        Devuelve la cantidad de puntos que entrega el caracter c
        """
        print("{}:{}".format(c,Pawn.points[c]))
    
    @staticmethod
    def showPawnPoints():
        """
        Devuelve los caracteres y la cantidad de puntos que entregan.
        """
        for key in Pawn.points:
            Pawn.getPoints(key)
    
class Word():

    def __init__(self):
        """
        Constructor
        """
        self.word = []
    
    def __str__(self):
        """
        str para el print
        """
        return "".join(self.word)
    
    def areEqual(self,w):
        """
        Toma un objeto Word w y lo compara con el objeto self. Si son iguales devuelve True, en caso contrario
        devuelve False
        """
        if len(self.word) == len(w.word):
            for i in range(len(w.word)):
                if self.word[i] != w.word[i]:
                    return False
            return True
        else:
            return False
    
    def isEmpty(self):
        """
        Devuelve True si la palabra es vacia(El array word no tiene elementos)
        False en caso contrario
        """
        if len(self.word) == 0:
            return True
        else:
            return False
    
    @classmethod
    def readWord(cls,palabra):
        """
        Toma un string y devuelve un objeto Word cuyo array contiene cada letra del string
        """
        objeto = Word()
        for char in palabra:
            objeto.word.append(char.upper())
        return objeto
    
    def readWordfromFile(file):
        """
        Lee una linea del fichero y la devuelve.
        """
        return file.readline().split("\n")[0]
    
    def getFrequency(self):
        """
        Crea un objeto FrequencyTable vacio y le va agregando frecuencias usando update(). Devulve el objeto
        FrequencyTable al final
        """
        frecuencia = FrequencyTable()
        for char in self.word:
            frecuencia.update(char)
        return frecuencia
    
    def getLengthWord(self):
        cant = len(self.word)
        return len(self.word)

class Dictionary():

    @staticmethod
    def validateWord(palabra):
        """
        Revisa que el objeto Word palabra este en el diccioanrio
        """
        with open("dictionary.txt") as f:
            w = Word.readWord(Word.readWordfromFile(f))
            while not w.isEmpty() and not w.areEqual(palabra):
                w = Word.readWord(Word.readWordfromFile(f))
        if w.isEmpty():
            return False
        else:
            return True
    
    @staticmethod
    def showWord(player_pawn):
        tabla_pawn = player_pawn.getFrequency()
        with open("dictionary.txt") as f:
            w = Word.readWord(Word.readWordfromFile(f))
            while not w.isEmpty():
                if FrequencyTable.isSubset(w.getFrequency(), tabla_pawn):
                    print(w.__str__())
                w = Word.readWord(Word.readWordfromFile(f))
    
    @staticmethod
    def showWordPlus(player_pawn,c):
        tabla_pawn = player_pawn.getFrequency()
        with open("dictionary.txt") as f:
            w = Word.readWord(Word.readWordfromFile(f))
            while not w.isEmpty():
                if FrequencyTable.isSubset(w.getFrequency(), tabla_pawn) and c in w.word:
                    print(w.__str__())
                w = Word.readWord(Word.readWordfromFile(f))


class FrequencyTable():

    def __init__(self):
        """
        Contructor
        char pasaba un codigo ascii a letra, ord de letra a codigo ascii, por eso que se puede hacer un range
        """

        self.letters = [chr(x) for x in range(ord("A"),ord("Z")+1)]
        self.frecuencies = [0 for _ in range(len(self.letters))]
    
    def showFrequency(self):
        """
        Muestra la frecuencia de las letras que existe(si hay cero letra A no se muestra)
        """
        for i in range(len(self.frecuencies)):
            if self.frecuencies[i] != 0:
                print("{}:{}".format(self.letters[i],self.frecuencies[i]))    
    
    @staticmethod
    def isSubset(frecuencia1,frecuencia2):
        """
        Devuelve True si frecuencia1 es subconjunto de frecuencia2
        """
        for i in range(len(frecuencia1.frecuencies)):
            if frecuencia1.frecuencies[i] > frecuencia2.frecuencies[i]:
                return False
        return True
    
    def update(self,c):
        """
        Le agrega una unidad a la frecuencia del caracter c
        """
        idx= self.letters.index(c)
        self.frecuencies[idx] += 1

class Board():

    def __init__(self):
        import numpy as np
        """
        Constructor
        """
        self.board = np.array([["" for _ in range(15)] for _ in range(15)])
        self.totalPawn = 0
        self.totalWords = 0
        self.score = 0
    
    def showBoard(self):

        """
        Muestra el tablero
        """
        print("\n ", end = " ")
        for n in range(len(self.board)):
          print("{}{} ".format(0 if n <= 9 else "", n), end = " ")
        print("\n+" + "---+" * len(self.board))
        for i in range(len(self.board)):
          print("|", end = " ")
          for j in range(len(self.board)):
            print(self.board[i][j] + " |", end = " ")
          print("{}{}".format(0 if i <= 9 else "", i), end = " ")
          print("\n+" + "---+" * len(self.board))
    
    def placeWord(self,player_pawn,word,x,y,direction):
        """
        Toma un objeto word y va poniendo sus letras el objeto board.
        Si la tabla no contaba con la ficha a poner se elimina esta del objeto player_pawn

        board [n° fila][n° columna]
        """
        if direction == "V":
            for i in range(len(word.word)):
                if self.board[x+i][y] != word.word[i]:
                    self.board[x+i][y] = word.word[i]
                    self.totalPawn += 1
                    player_pawn.takePawn(word.word[i])
                    self.score += Pawn.points[word.word[i]]
        else:
            for i in range(len(word.word)):
                if self.board[x][y+i] != word.word[i]:
                    self.board[x][y+i] = word.word[i]
                    self.totalPawn += 1
                    player_pawn.takePawn(word.word[i])
                    self.score += Pawn.points[word.word[i]]
        self.totalWords += 1
    
    def isPossible(self,palabra,x,y,direction):
        """
        Comprueba que se puede agregar la palabra al board dada ciertas condiciones iniciales.
        """
        #Revisa si el tablera esta vacio
        if self.totalWords == 0:
            #Vertical
            if direction == "V":
                if y != 7 or x>7:
                    return False,"La palabra inicial debe pasar por el centro"
                elif x+palabra.getLengthWord() > 7:
                    return True,"Se puede colocar la palabra"
                return False,"La palabra no alcanza a pasar por el centro" 
            #Horizontal
            else:
                if x != 7 or y>7:
                    return False,"La palabra inicial debe pasar por el centro"
                elif y + palabra.getLengthWord() >= 8:
                    return True,"Se puede colocar la palabra"
                return False,"La palabra alcanza a pasar por el centro"
        #Tablero no vacio
        else:
            #Vertical
            dummy = 0
            utilizadas = 0
            if direction == "V":
                #Verificar que se sale de los limites
                if x+palabra.getLengthWord() >15 or x < 0 or y > 15 or y < 0:
                    return False,"Palabra se sale de los limites"
                #Verificar que pasa por una ficha, como minimo
                for i in range(palabra.getLengthWord()):
                    if self.board[x+i][y] != "":
                        dummy += 1
                        #Verificar que la ficha no se sobrescribe
                        if self.board[x+i][y] != palabra.word[i]:
                            return False,"No se puede reemplazar una ficha ya existente"
                        #Suma una si no se utiliza ficha(la ficha ya esta en el tablero)
                        else:
                            utilizadas += 1
                if dummy == 0:
                    return False,"No pasa por una ficha ya existe"
                #Verificar que se utiliza como minimo una ficha
                if utilizadas-palabra.getLengthWord() == 0:
                    return False,"Se debe utilizar como minimo una ficha"
                #Verificar que no haya fichas vecinas en los extremos
                if (x != 0 and self.board[x-1][y] != "") or (x+palabra.getLengthWord() != 14 and self.board[x+palabra.getLengthWord()][y] != ""):
                    return False,"No pueden haber fichas vecinas en el inicio o fin de la palabra"
                if x+palabra.getLengthWord() != 15:
                    if self.board[x+palabra.getLengthWord()][y] != "":
                        return False,"No pueden haber fichas vecinas en el inicio o fin de la palabra"
                #Regresar solo si cumple todas las condiciones
                return True,"Se puede colocar la palabra"
            #Horizontal
            else:
                #Verificar que sale de los limites
                if y+palabra.getLengthWord() >15 or x < 0 or y > 15 or y < 0:
                    return False,"Palabra se sale de los limites"
                #Verificar que pasa por una ficha, como minimo
                for i in range(palabra.getLengthWord()):
                    if self.board[x][y+i] != "":
                        dummy += 1
                        #Verificar que la ficha no se sobrescribe
                        if self.board[x][y+i] != palabra.word[i]:
                            return False,"No se puede reemplazar una ficha ya existente"
                        #Suma una si no se utiliza ficha(la ficha ya esta en el tablero)
                        else:
                            utilizadas += 1
                if dummy == 0:
                    return False,"No pasa por una ficha ya existe"
                #Verificar que se utiliza como minimo una ficha
                if utilizadas-palabra.getLengthWord() == 0:
                    return False,"Se debe utilizar como minimo una ficha"
                if (y != 0 and self.board[x][y-1] != "") or (y+palabra.getLengthWord() != 14 and self.board[x][y+palabra.getLengthWord()] != ""):
                    return False,"No pueden haber fichas vecinas en el inicio o fin de la palabra"
                #Regresar solo si cumple todas las condiciones
                return True,"Se puede colocar la palabra"
    
    def getPawns(self,palabra,x,y,direction):
        """
        Devuelve un objeto Word que contiene todas ls fichas qur faltan para colocar el objeto Word palabra en el 
        Board
        """
        objeto = Word()
        if not self.isPossible(palabra, x, y, direction)[0]:
            #Retorna palabra vacia en caso de que no se pueda poner la palabra
            return objeto
        #Vertical
        if direction == "V":
            for i in range(palabra.getLengthWord()):
                if palabra.word[i] != self.board[x+i][y]:
                    objeto.word.append(palabra.word[i])
        #Horizontal
        else:
            for i in range(palabra.getLengthWord()):
                if palabra.word[i] != self.board[x][y+i]:
                    objeto.word.append(palabra.word[i])
        return objeto
    
    def showWordPlacement(self,player_pawn,palabra):
        dic = {"H":[],"V":[]}
        tabla_jugador = player_pawn.getFrequency()
        for i in range(15):
            for j in range(15):
                objeto = self.getPawns(palabra, i, j, "H")
                if not objeto.isEmpty() and FrequencyTable.isSubset(objeto.getFrequency(),tabla_jugador):
                    dic["H"].append((i,j))
                objeto = self.getPawns(palabra, i, j, "V")
                if not objeto.isEmpty() and FrequencyTable.isSubset(objeto.getFrequency(),tabla_jugador):
                    dic["V"].append((i,j))
        for key in dic:
            print(key)
            for i in dic[key]:
                print(i.__str__())


