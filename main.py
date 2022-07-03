# Fritz Raluca-Mihaela
# Grupa 243
# Jocul amazoanelor

import stopit

@stopit.threading_timeoutable(default="intrat in timeout")
def functie(n):
    j=0;
    for i in range(n):
        print(i, end=" ")
    return "functie finalizata"


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

ADANCIME_MAX = 6

    # defineste jocul
class Joc:
    NR_COLOANE = 10
    JMIN = None
    JMAX = None
    GOL = '#'
    SAGEATA = 'X'


    def __init__(self, tabla = None):
        self.matr = tabla or  [self.GOL]*self.NR_COLOANE**2
        self.start()

    @classmethod
    def oponent(cls, jucator):
        if jucator == cls.JMIN:
            return cls.JMAX
        return cls.JMIN

    def final(self):
        # mutariDisponibileMin = []
        # mutariDisponibileMax = []
        # if mutariDisponibileMin is None and mutariDisponibileMax is None:
        #     return 'remiza'
        # elif mutariDisponibileMax is None:
        #     return self.__class__.JMAX
        # elif mutariDisponibileMin is None:
        #     return self.__class__.JMIN
        # # daca nu exista mutari => castiga unul din ei sau remiza
        return False

    def start(self):
        self.changeCoord(0, 3, 'B')
        self.changeCoord(0, 6, 'B')
        self.changeCoord(3, 0, 'B')
        self.changeCoord(3, 9, 'B')
        self.changeCoord(9, 3, 'W')
        self.changeCoord(9, 6, 'W')
        self.changeCoord(6, 0, 'W')
        self.changeCoord(6, 9, 'W')


    def changeCoord(self, linie, coloana, jucator):
        self.matr[linie*self.NR_COLOANE + coloana] = jucator

    def getCoord(self, linie,coloana):
        return self.matr[linie*self.NR_COLOANE + coloana]

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

    def __str__(self):
        return self.sirAfisare()

    def __repr__(self):
        return self.sirAfisare()

    # cautam pe verticala
    # daca nu ne aflam pe coloana potrivita => FALS
    # daca suntem pe verticala => j nu se schimba
    # cautam crescator sau descrescator in functie de locul unde ne aflam fata de linieScop
    # daca se gaseste un spatiu care nu este gol pana ajungem la linieScop => FALS
    # daca ajungem la linieScop si spatiul nu este gol => FALS
    # altfel => TRUE
    # updatam i
    def checkVertical(self, linie, coloana, linieScop, coloanaScop):
        if coloana != coloanaScop:
            return False

        i = linie
        j = coloana

        while i>=0 and i<=9:
            if i < linieScop:
                i += 1
            else:
                i -= 1
            if i != linieScop:
                if self.getCoord(i,j) != self.GOL:
                    return False
            elif i == linieScop:
                if self.getCoord(i,j) != self.GOL:
                    return False
                else:
                    return True

    # cautam pe orizontala
    # daca nu ne aflam pe linia potrivita => FALS
    # daca suntem pe orziontala => i nu se schimba
    # cautam crescator sau descrescator in functie de locul unde ne aflam fata de coloanaScop
    # daca se gaseste un spatiu care nu este gol pana ajungem la coloanaScop => FALS
    # daca ajungem la coloanaScop si spatiul nu este gol => FALS
    # altfel => TRUE
    # updatam j
    def checkOrizontal(self, linie, coloana, linieScop, coloanaScop):
        if linie != linieScop:
            return False

        i = linie
        j = coloana

        while j>=0 and j<=9:
            if j < coloanaScop:
                j += 1
            else:
                j -= 1
            if j != coloanaScop:
                if self.getCoord(i,j) != self.GOL:
                    return False
            elif j == coloanaScop:
                if self.getCoord(i,j) != self.GOL:
                    return False
                else:
                    return True


    # cautam pe diagonala
    # daca ne aflam pe liniaScop dar nu si pe coloanaScop => FALS
    # si vice versa
    # daca i < linieScop si j > coloanaScop => i creste si j scade
    # si vice versa
    # daca se gaseste un spatiu care nu este gol pana ajungem la linieScop si coloanaScop => FALS
    # daca ajungem la linieScop si coloanaScop si spatiul nu este gol => FALS
    # altfel => TRUE
    # updatam i si j
    def checkDiagonala(self, linie, coloana, linieScop, coloanaScop):
        if (linie == linieScop and coloana!= coloanaScop) or (linie != linieScop and coloana == coloanaScop):
            return False

        i = linie
        j = coloana

        while j>=0 and j<=9 and i>=0 and i<=9:
            if j < coloanaScop and i > linieScop:
                j += 1
                i -= 1
            else:
                j -= 1
                i += 1
            if (i == linieScop and j != coloanaScop) or (i != linieScop and j == coloanaScop):
                return False
            if j != coloanaScop and i != linieScop:
                if self.getCoord(i,j) != self.GOL:
                    return False

            elif j == coloanaScop and i == linieScop:
                if self.getCoord(i,j) != self.GOL:
                    return False
                else:
                    return True

# am avut nevoie de aceasta clasa ajutatoare pentru a putea prelua coordonatele unei piese atunci cand
# verificam daca exista vreo mutare posibila catre locatia indicata de jucator.
class Piesa:
    def __init__(self, coordLinie, coordColoana):
        self.coordLinie = coordLinie
        self.coordColoana = coordColoana

    def getCoord(self):
        return self.coordLinie, self.coordColoana


class Stare: # Echiv NodParcurge in Cautare - A*
    # => nod in arborele minmax
    # are ca proprieteate tabla de joc

    def __init__(self, tabla, jCurent, adancime, partine=None, estimare=None):
        self.tabla = tabla
        self.jCurent = jCurent
        self.adancime = adancime
        self.estimare = estimare
        self.mutariPosibile=[]
        # initalizam listele pieseB si pieseW cu locatiile initiale indicate in cerinta
        # pentru piesele negre si albe
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
                # daca final nu este remiza => este black sau white
                # pentru o printare mai naturala, in functie de final = 'B' sau 'W' => transformam in BLACK si WHITE
                if final == 'B':
                    final = "BLACK"
                else:
                    final = "WHITE"
                print(f"A castigat {final}!")

            return True
        return False

def play():
    raspunsValid = False
    # validare raspunsuri
    while not raspunsValid:
        tipAlg = input(f"Algoritmul folosit? (raspundeti cu 1 sau 2)\n "
                       f"1. Minimax \n "
                       f"2. Alpha-beta \n ")
        if tipAlg in ['1', '2']:

            raspunsValid = True
        else:
            print("Nu ati ales o varianta corecta.")

        # initializare jucatori
        raspunsValid = False
        while not raspunsValid:
            Joc.JMIN = input(f"Doriti sa jucati cu 'B' - BLACK sau cu 'W' - WHITE? \n").upper()
            if(Joc.JMIN in ['B', 'W']):
                raspunsValid = True
            else:
                print("Raspunsul trebuie sa fie 'B' sau 'W' ")
        if Joc.JMIN == 'W':
            Joc.JMAX = 'B'
        else:
            Joc.JMAX = 'W'

        # initializare tabla
        tablaCurenta = Joc()
        print("Tabla initiala")
        print(str(tablaCurenta))
        # creare stare initiala
        stareCurenta = Stare(tablaCurenta, 'B', ADANCIME_MAX)
        print(str(tablaCurenta))
        while True:
            # muta jucatorul
            if stareCurenta.jCurent == Joc.JMIN:
                print("Este randul tau! ", stareCurenta.jCurent)
                raspunsValid = False
                alegere = 0
                while not raspunsValid:
                    try:
                        # prezentam posibilitatile si validam alegerea
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
                        # preluam si validam locatia tinta
                        linie = int(input("linie= "))
                        coloana = int(input("coloana= "))

                        if linie in range(Joc.NR_COLOANE) and coloana in range(Joc.NR_COLOANE):
                            # in functie de piesele jucatorului, vom cauta in lista pieselor respective
                            if stareCurenta.jCurent == 'W':
                                piese = stareCurenta.pieseW
                            else:
                                piese = stareCurenta.pieseB

                            for i in range(len(piese)):
                                liniePiesa, coloanaPiesa = piese[i].getCoord()
                                # verificam daca pe verticala, diagonala sau orizontala exista o posibilitate de a ajunge
                                # la locatia data
                                vert = Joc.checkVertical(tablaCurenta, liniePiesa, coloanaPiesa,linie, coloana)
                                diag = Joc.checkDiagonala(tablaCurenta, liniePiesa, coloanaPiesa, linie, coloana)
                                oriz = Joc.checkOrizontal(tablaCurenta, liniePiesa, coloanaPiesa, linie, coloana)
                                if vert or diag or oriz:
                                    # daca unul din drumuri este liber, in functie de alegerea facuta anterior
                                    # se va muta o piesa sau se va aplica o sageata
                                    if alegere == 1:
                                        stareCurenta.tabla.matr[linie*Joc.NR_COLOANE + coloana] = stareCurenta.jCurent
                                        stareCurenta.tabla.matr[liniePiesa*Joc.NR_COLOANE + coloanaPiesa] = Joc.GOL
                                        piese[i].coordLinie = linie
                                        piese[i].coordColoana = coloana
                                    else:
                                        stareCurenta.tabla.matr[linie*Joc.NR_COLOANE + coloana] = Joc.SAGEATA
                                    raspunsValid = True

                            if stareCurenta.jCurent == 'W':
                                stareCurenta.pieseW = piese
                            else:
                                stareCurenta.pieseB = piese
                            if not raspunsValid:
                                print("Locatie invalida => drumul este blocat sau locatia este in afara ariei de acoperire a oricarei piese.")
                        else:
                            print("Linie sau coloana invalida.")
                    except ValueError:
                        print("Linia si coloana trebuie sa fie numere intregi")

                    # afisam starea jocului actuala:

                print("\n Tabla dupa mutarea jucatorului: ")
                print(str(stareCurenta.tabla))

                if stareCurenta.afisFinal(stareCurenta):
                    break

                stareCurenta.jCurent = Joc.oponent(stareCurenta.jCurent)
            else:
                # JMAX = calculator
                # mutare calculator
                print("Este randul calculatorului! ")
                # preiau timpul de dinainte de mutare
                before = int(round(time.time() * 1000))
                # stare actualizata = starea curenta in care am setat urmatoarea mutare
                if tipAlg == 1:
                    stareActualizata = minMax(stareCurenta)
                else:
                    stareActualizata = alphaBeta(-500,500,stareCurenta)

                stareCurenta.tabla = stareActualizata.stareAleasa.tabla

                print("Tabla dupa mutarea calculatorului")
                print(str(stareCurenta))
                # preiau timpul de dupa mutare
                after = int(round(time.time() * 1000))

                print(f"Calculatorul a gandit timp de {str(before-after)} milisecunde")

                if stareCurenta.afisFinal(stareCurenta):
                    break
                stareCurenta.jCurent = Joc.oponent(stareCurenta.jCurent)


def minMax(stare):
    if stare.adancime == 0 or stare.tabla.final():
        stare.estimare = stare.tabla.estimeaza_scor(stare.adancime)
        return stare
    stare.mutariPosibile = stare.mutari()
    mutariCuEstimare = [minMax(x) for x in stare.mutari_posibile]
    if stare.jCurent == Joc.JMAX:
        stare.stareAleasa = max(mutariCuEstimare, key=lambda x: x.estimare)
    else:
        stare.stareAleasa = min(mutariCuEstimare, key=lambda x: x.estimare)
    stare.estimare = stare.stareAleasa.estimare
    return stare

def alphaBeta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tabla.final():
        stare.estimare = stare.tabla.estimeaza_scor(stare.adancime)
        return stare
    if alpha > beta:
        return stare
    stare.mutariPosibile = stare.mutari()
    if stare.jCurent == Joc.JMAX:
        estimareCurenta = float('-inf')
        for mutare in stare.mutariPosibile:
            stareNoua = alphaBeta(alpha, beta, mutare)
            if (estimareCurenta < stareNoua.estimare):
                stare.stareAleasa = stareNoua
                estimareCurenta = stareNoua.estimare
            if (alpha < stareNoua.estimare):
                alpha = stareNoua.estimare
                if alpha >= beta:
                    break
    elif stare.jCurent == Joc.JMIN:
        estimareCurenta = float('inf')
        for mutare in stare.mutari_posibile:
            stareNoua = alphaBeta(alpha, beta, mutare)
            if (estimareCurenta > stareNoua.estimare):
                stare.stareAleasa = stareNoua
                estimareCurenta = stareNoua.estimare
            if (beta > stareNoua.estimare):
                beta = stareNoua.estimare
                if alpha >= beta:
                    break
    stare.estimare = stare.stareAleasa.estimare
    return stare

play()