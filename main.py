import os
import math

class Auto(): 
 
    def __init__(self, pojemnosc_zbiornika, ilosc_benzyny):
        self.__waucie = False
        self.__odpal = False
        self.__awaria = False
        self.__bieg = 0
        self.__szybkosc = 0
        self.pojemnosc_zbiornika = pojemnosc_zbiornika
        self.ilosc_benzyny = ilosc_benzyny
 
    def wsiadz(self):
        if self.__waucie == False:
            self.__waucie = True
 
    def wysiadz(self):
        if self.__waucie == True:
            self.__waucie = False
 
    def odpal(self):
        if self.__waucie == True and self.__awaria == False:
          self.__odpal = True
 
    def zgas(self):
        if self.__waucie == True and self.__awaria == False:
          self.__odpal = False
 
    def biegGora(self):
        if self.__waucie == True and self.__odpal == True:
            if self.__bieg < 6:
                self.__bieg += 1
 
    def biegDol(self):
          if self.__bieg > 0:
              self.__bieg -= 1
 
    def przyspiesz(self):
        if self.__waucie == True and \
            self.__odpal == True and \
            self.__bieg > 0 and \
            self.__szybkosc < 100:
                self.__szybkosc += 5
 
    def hamuj(self):
        if self.__waucie == True and \
            self.__odpal == True and \
            self.__bieg > 0 and \
            self.__szybkosc > 5:
                self.__szybkosc -= 5
 
    def __str__(self):
        if self.__waucie == True:
            miejsce_kierowycy = 'Kierowca w aucie'
        else:
            miejsce_kierowycy = 'brak kierowcy'
 
        if self.__bieg < math.floor(self.__szybkosc / 20):
            self.__awaria = True
            self.__bieg = 0
            self.__szybkosc = 0
 
        if self.__awaria == False and self.__odpal == True:
            stan_silnika = 'SPRAWNY'
            tryb_pracy = 'brum brum brum'
        elif self.__awaria == True and self.__odpal == True:
            stan_silnika = 'AWARIA'
            tryb_pracy = ''
        else:
            stan_silnika = 'WYŁĄCZONY'
            tryb_pracy = ''
 
        return f'''
            Obiekt klasy Auto
            ----------------------
            {miejsce_kierowycy}
            {tryb_pracy}
            {stan_silnika}
            ----------------------
            Zbiornik auta pomieści {self.pojemnosc_zbiornika}
            W zbiorniku {self.ilosc_benzyny}
            ----------------------
            Bieg {self.__bieg}
            Na liczniku {self.__szybkosc}
        '''
 
fiat = Auto(50, 10)
gra = True
while gra:
    os.system("clear")
    print(fiat)
    print('\nWybierz:')    
    print('''
            *wsiadz     --     in
            *wysiadz    --    out
            *odpal      --  start 
            *zgaś       --   stop
            *gora       --     up
            *dol        --   down
            *przyspiesz --  speed
            *hamuj      --  break
            *koniec     --   quit
 
            ''')
    decyzja = input(' --> ')
    if decyzja == 'in':
        fiat.wsiadz()
    if decyzja == 'out':
        fiat.wysiadz()
    if decyzja == 'start':
        fiat.odpal()
    if decyzja == 'stop':
        fiat.zgas()
    if decyzja == 'up':
        fiat.biegGora()
    if decyzja == 'down':
        fiat.biegDol()
    if decyzja == 'speed':
        fiat.przyspiesz()
    if decyzja == 'break':
        fiat.hamuj()
    if decyzja == 'quit':
        gra = False