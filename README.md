##### Fritz Raluca-Mihaela
##### Artifical Intelligence KR Mini-Project

---

## 13. Jocul amazoanelor Descrierea jocului
    
Se va implementa jocul amazoanelor (Game of the amazons). Jocul este turn based. Un jucător va folosi piese albe, celălalt negre. Jucătorul cu piese negre este cel care mută primul.  

Jocul se joacă pe tabla de joc stil tablă de șah dar de dimensiune 10X10, și piesele sunt inițial puse ca în imaginea
de mai jos:

![Figura1](images/fig1.jpg)  

Regulile și desfășurarea jocului Jucătorul cu piese albe mută primul. O mutare are două acțiuni:   

1. mutarea unei piese pe tablă oricâte poziții în linie dreaptă, pe rând, coloană sau diagonală (în stilul reginei de la sah), dar numai cu condiția să nu fie alte piese pe acel traseu (piesa nu poate sări alte piese).  

2. Lansarea unei "săgeți" care de asemenea poate merge în linie dreaptă pe rând, coloană sau diagonală însă fără a trece printr-o celulă cu o altă piesă în ea. În locul în care a ajuns săgeata se plasează o piesă specială (în imagine e marcat cu un x).  
   
Vom considera liniile și coloanele numerotate de la 0 până la 9 inclusiv.
De exemplu, în imaginea de mai jos, a mutat jucătorul cu piese albe, piesa de la (linia 9, coloana 6) la (linia 4, coloana 6) (deci s-a mutat pe coloană). Săgeata a fost trasă la (linia 4, coloana 9) (deci a fost trasă pe linie).  

![Figura2](images/fig2.jpg)   

Mai departe mută jucătorul cu piese negre de pe (linia 3, coloana 9) pe (linia 3, coloana 6). Săgeata este trasă pe diagonală la (linia 5, coloana 8). De exemplu, jucătorul cu piese negre nu ar fi putut să tragă săgeata pe coloană în jos, fiindcă era o piesă albă acolo.   

![Figura3](images/fig3.jpg)  

Jucătorul cu piese albe a mutat de la (linia 9, coloana 3) la (linia 1, coloana 3) și a tras săgeata la (linia 3, coloana 5).  

![Figura4](images/fig4.jpg)   

Mai jos e o succesiune de mutări:  

![Figura5](images/fig5.jpg)  

![Figura6](images/fig6.jpg)  

![Figura7](images/fig7.jpg)  

![Figura8](images/fig8.jpg)  

Observăm că în urma ultimei mutări de sus, piesa albă de la (linia 5, coloana 9) este blocată (nu se mai poate deplasa). Jocul nu e pierdut pentru alb fiindcă mai are piese disponibile.

#### Terminarea jocului

Jocul se termină când unul dintre jucători nu mai are mutări, caz în care jucătorul respectiv pierde, iar adversarul său câștigă. De exemplu, în tabla de mai jos, ar fi rândul jucătorului cu piese albe, dar nicio piesă nu mai are un loc liber în care să se mute. Prin urmare, a câștigat jucătorul cu piese negre.  

Exemplu de stare finală:  

![Figura9](images/fig9.jpg)  


