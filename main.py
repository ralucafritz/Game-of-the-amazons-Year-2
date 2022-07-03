# Fritz Raluca-Mihaela
# Grupa 243
# Jocul amazoanelor

"""
Descrierea jocului Se va implementa jocul amazoanelor (Game of the amazons).
Jocul este turn based. Un jucător va folosi piese albe, celălalt negre.
Jucătorul cu piese negre este cel care mută primul.
Regulile și desfășurarea jocului Jucătorul cu piese albe mută primul.
O mutare are două acțiuni:

1. mutarea unei piese pe tablă oricâte poziții în linie dreaptă, pe rând, coloană sau
diagonală (în stilul reginei de la sah), dar numai cu condiția să nu fie alte piese pe acel traseu (piesa nu poate sări alte piese).

2. Lansarea unei "săgeți" care de asemenea poate merge în linie dreaptă pe rând, coloană sau diagonală însă fără a
trece printr-o celulă cu o altă piesă în ea. În locul în care a ajuns săgeata se plasează o piesă specială
(în imagine e marcat cu un x).
Vom considera liniile și coloanele numerotate de la 0 până la 9 inclusiv.

De exemplu,
în imaginea de mai jos, a mutat jucătorul cu piese albe, piesa de la (linia 9, coloana 6) la (linia 4,
coloana 6) (deci s-a mutat pe coloană). Săgeata a fost trasă la (linia 4, coloana 9) (deci a fost trasă pe linie).


Observăm că în urma ultimei mutări de sus, piesa albă de la (linia 5, coloana 9) este blocată
(nu se mai poate deplasa). Jocul nu e pierdut pentru alb fiindcă mai are piese disponibile.

Terminarea jocului
Jocul se termină când unul dintre jucători nu mai are mutări, caz în care jucătorul respectiv pierde,
iar adversarul său câștigă. De exemplu, în tabla de mai jos, ar fi rândul jucătorului cu piese albe, dar nicio piesă nu mai are un loc
liber în care să se mute. Prin urmare, a câștigat jucătorul cu piese negre.

tabla e de forma initial:

# # # o # # o # # #
# # # # # # # # # #
# # # # # # # # # #
o # # # # # # # # o
# # # # # # # # # #
# # # # # # # # # #
o # # # # # # # # o
# # # # # # # # # #
# # # # # # # # # #
# # # o # # o # # #

linii 0-9
coloane 0-9
NEGRU
    => linia 0 coloanele 3 si 6
    => linia 3 coloanele 0 si 9
ALB
    => linia 9 coloanele 3 si 6
    => linia 6 coloanele 0 si 9
"""

import time

    # defineste jocul
class Joc:
    NR_COLOANE = 10
    JMIN = None
    JMAX = None
    GOL = '#'
    SAGEATA = 'X'

    def __init__(self, tabla = None):
        if tabla is not None:
            self.matr = tabla # 10x10 tabla goala
        else:
            for i in range(10):
                for j in range(10):
                    self.matr[i][j] = self.GOL

    @classmethod
    def oponent(cls, jucator):
        if jucator == cls.JMIN:
            return cls.JMAX
        return cls.JMIN

    def final(self):
        mutariDisponibileMin = []
        mutariDisponibileMax = []
        if mutariDisponibileMin is None and mutariDisponibileMax is None:
            return 'remiza'
        elif mutariDisponibileMax is None:
            return self.__class__.JMAX
        elif mutariDisponibileMin is None:
            return self.__class__.JMIN
        # daca nu exista mutari => castiga unul din ei sau remiza

    def start(self):
        self.matr[0][3], self.matr[0][6], self.matr[3][0], self.matr[3][9] = 'B', 'B', 'B', 'B'
        self.matr[9][3], self.matr[9][6], self.matr[6][0], self.matr[6][9] = 'W', 'W', 'W', 'W'

    def estimeazaScor(self, adancime):
        final = self.final()

        if final == self.__class__.JMAX:
            return (99 + adancime)
        elif final == self.__class__.JMIN:
            return (-99 - adancime)
        elif final == 'remiza':
            return 0


    def sirAfisare(self):
           sir="  |"
           sir+=" ".join([str(i) for i in range(self.NR_COLOANE)])+"\n"
           sir+="-"*(self.NR_COLOANE+1)*2+"\n"
           for i in range(self.NR_COLOANE): #itereaza prin linii
                   sir+= str(i)+" |"+" ".join([str(x) for x in self.matr[self.NR_COLOANE*i : self.NR_COLOANE*(i+1)]])+"\n"
           #[0,1,2,3,4,5,6,7,8]
           return sir

    def checkVertical(self, linie, coloana, linieScop, coloanaScop):
        if coloana != coloanaScop:
            return False

        i = linie
        j = coloana

        while i>=0 and i<=9:
            if i != linieScop:
                if self.matr[i][j] != self.GOL:
                    return False
            elif i == linieScop:
                if self.matr[i][j] != self.GOL:
                    return False
                else:
                    return True
            if i < linieScop:
                i += 1
            else:
                i -= 1

    def checkOrizontal(self, linie, coloana, linieScop, coloanaScop):
        if linie != linieScop:
            return False

        i = linie
        j = coloana

        while j>=0 and j<=9:
            if j != coloanaScop:
                if self.matr[i][j] != self.GOL:
                    return False
            elif j == coloanaScop:
                if self.matr[i][j] != self.GOL:
                    return False
                else:
                    return True
            if j < coloanaScop:
                j += 1
            else:
                j -= 1

    def checkDiagonala(self, linie, coloana, linieScop, coloanaScop):
        if (linie == linieScop and coloana!= coloanaScop) or (linie != linieScop and coloana == coloanaScop):
            return False

        i = linie
        j = coloana


        while j>=0 and j<=9 and i>=0 and i<=9:
            if (i == linieScop and j != coloanaScop) or (i != linieScop and j == coloanaScop):
                return False
            if j != coloanaScop and i != linieScop:
                if self.matr[i][j] != self.GOL:
                    return False

            elif j == coloanaScop and i == linieScop:
                if self.matr[i][j] != self.GOL:
                    return False
                else:
                    return True

            if j < coloanaScop and i > linieScop:
                j += 1
                i -= 1
            else:
                j -= 1
                i += 1

class Piesa:
    def __init__(self, coordLinie, coordColoana):
        self.coordLinie = coordLinie
        self.coordColoana = coordColoana

    def getCoord(self):
        return self.coordLinie, self.coordColoana


class Stare: # Echiv NodParcurge in Cautare - A*
    def __init__(self, tabla, jCurent, adancime, partine=None, estimare=None):
        self.tabla = tabla
        self.jCurent = jCurent
        self.adancime = adancime
        self.estimare = estimare
        self.mutariPosibile=[]
        self.pieseB = [Piesa(0,3),  Piesa(0,6), Piesa(3,0), Piesa(3,9)]
        self.pieseW = [Piesa(9,3),  Piesa(9,6), Piesa(6,0), Piesa(6,9)]
        self.stareAleasa = None

    def mutari(self):
        # luam lista de informatii din nodurile succesoare
        listaMutari = self.tabla.mutari(self.jCurent)
        oponent = Joc.oponent(self.jCurent)

        stariMutari = [Stare(mutare, oponent, self.adancime-1, parinte=self) for mutare in listaMutari]

        return stariMutari

    def afisFinal(stareCurenta):
        final = stareCurenta.tabla.final()
        if final:
            if final == "remiza":
                print("Remiza")
            else:
                if final == 'B':
                    final = "Black"
                else
                    final = "White"
                print(f"A castigat {final}")

            return True
        return False

def joaca():
    raspunsValid = False

    while not raspunsValid:
        tipAlg = input(f"Algoritmul folosit? (raspundeti cu 1 sau 2)\n "
                       f"1. Minimax \n "
                       f"2. Alpha-beta \n ")
        if tipAlg in ['1', '2']:
            raspunsValid = True
        else:
            print("Nu ati ales o varianta corecta.")
        #initializare jucatori

        raspunsValid = False
        while not raspunsValid:
            Joc.JMIN = input(f"Doriti sa jucati cu 'B' - BLACK sau cu 'W' - WHITE?").upper()
            if(Joc.JMIN in ['B', 'W']):
                raspunsValid = True
            else:
                print("raspunsul trebuie sa fie 'B' sau 'W' ")

        if Joc.JMIN == 'W':
            Joc.JMAX = 'B'
        else:
            Joc.JMAX = 'W'

        tablaCurenta = Joc()
        print("Tabla initiala")
        print(str(tablaCurenta))

    stareCurenta = Stare( tablaCurenta, 'B')

    while True:
        # muta omul
        if stareCurenta.jCurent == Joc.JMIN:
            print("Este randul tau! ", stareCurenta.jCurent)
            raspunsValid = False
            alegere = 0
            while not raspunsValid:
                try:
                    alegere = int(input("Ai doua alegeri: \n"
                                        "1. Mutare \n"
                                        "2. Sageata \n"
                                        "Ce alegi? "))
                    if alegere == 1 or alegere == 2:
                        raspunsValid = True
                except ValueError:
                    print("Alegerea facuta trebuie sa fie un numar intreg")
            raspunsValid = False
            while not raspunsValid:
                try:
                    linie = int(input("linie= "))
                    coloana = int(input("coloana= "))

                    if linie in range(Joc.NR_COLOANE) and coloana in range(Joc.NR_COLOANE):
                        if stareCurenta.jCurent == 'W':
                            piese = stareCurenta.pieseW
                        else:
                            piese = stareCurenta.pieseB

                        for piesa in piese:
                            liniePiesa, coloanaPiesa = piesa.getCoord()
                            vert = Joc.checkVertical(tablaCurenta, liniePiesa, coloanaPiesa,linie, coloana)
                            diag = Joc.checkDiagonala(tablaCurenta, liniePiesa, coloanaPiesa, linie, coloana)
                            oriz = Joc.checkOrizontal(tablaCurenta, liniePiesa, coloanaPiesa, linie, coloana)
                            if vert or diag or oriz:
                                if alegere == 1:
                                    stareCurenta.tabla.matr[linie][coloana] = stareCurenta.jCurent
                                    stareCurenta.tabla.matr[liniePiesa][coloanaPiesa] = Joc.GOL
                                else:
                                    stareCurenta.tabla.matr[linie][coloana] = Joc.SAGEATA
                                raspunsValid = True

                        if not raspunsValid:
                            print("Mutare/Sageata invalida.")
                    else:
                        print("Linie sau coloana invalida.")
                except ValueError:
                    print("Linia si coloana trebuie sa fie numere intregi")

                # afisam starea jocului actuala:

            print("\n Tabla dupa mutarea jucatorului: ")
            print(str(stareCurenta))

            if stareCurenta.afisFinal(stareCurenta):
                break

            stareCurenta.jCurent = Joc.oponent(stareCurenta.jCurent)
        else:
            # JMAX = calculator
            # mutare calculator
            print("Este randul calculatorului! ")
            before = int(round(time.time() * 1000))

            if tipAlg == 1:
                stareActualizata = minMax(stareCurenta)
            else:
                stareActualizata = alphaBeta(-500,500,stareCurenta)

            stareCurenta.tabla = stareActualizata.stareAleasa.tabla

            print("Tabla dupa mutarea calculatorului")
            print(str(stareCurenta))

            after = int(round(time.time() * 1000))

            print(f"Calculatorul a gandit timp de {str(before-after)} milisecunde")

            if stareCurenta.afisFinal(stareCurenta):
                break
            stareCurenta.jCurent = Joc.oponent(stareCurenta.jCurent)

# MINMAX SI ALPHABETA NU AU FOST IMPLEMENTATE
def minMax(stareCurenta):
    stareActualizata = stareCurenta
    return stareActualizata
def alphaBeta(stareCurenta):
    stareActualizata = stareCurenta
    return stareActualizata

joaca()