class HansogGretaSp(object):
     def getName(self): pass
     def getDescription(self): pass
     def answer(self): pass
     def move(self): pass
     def kill(self): pass
     def clue(self): pass
     def removeElement(self): pass
     def eldhusLokad(self): pass

class Herbergi(HansogGreta):
    def __init__(self, name, herb):
        self.name= name
        self.herb= herb
        self.herb1='Herbergi 1'
        self.herb2='Herbergi 2'
        self.description= description

    def StartingHerbergi():
        description= self.getDescription()
        self.promblem1()

    def getName(self):
        return self.name
    def getDescription(self):
        if self.herb == 1:
            print('þú ert í herbergi :',self.herb1)
            return 'Stórt herbergi, sem inniheldur sófa og arinn'
            self.getname()
        elif herb == 2:
            return 'Herbergið þar sem vonda nornin sefur'
        else:
            return 'Herbergið þar sem vonda nornin fer á klósettið'

class Persona(Herbergi):
    def __init__(self, kyn, name, description):
        self.name= name
        self.description= description
        self.kyn= kyn

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description
    def kyn(self):
        if self.kyn == 1:
            return 'Kvenkyns'
        else:
            return 'Karlkyns'

def main():
    win = False #Verður true þegar allar þrautirnar i leiknum hafa verið leystar
    while(1):
        print("Hvort viltu leika Hans eða Grétu? Skrifaðu 1 fyrir Grétu eða 2 fyrir Hans.")
        val = input('Mitt val:' )
        val = int(val)
        if val == 1:
            print("Þú hefur valið Grétu")
            s = Persona(1, 'Gréta', 'Lítil stelpa með ljóst hár')
            break
        elif val == 2:
            print("Þú hefur valið Hans")
            name = 'Hans'
            s = Persona(0, 'Hans', 'Lítill strákur með dökkt hár')
            break
        else:
            print("Þú þarft að srifa 1 fyrir Grétu eða 2 fyrir Hans.")
            val = input ('Mitt val: ')
            val = int(val)
    while(win == False):
        herb = input('Hvaða herbergi viltu fara í? Veldu 1 fyrir stofu, 2 fyrir svefnherbergi og 3 fyrir baðherbergi.')
        herb = int(herb)
        des = 1
        d = Herbergi(herb, des)
        #input nýtt herbergi

        des=2
        d2=Herbergi(herb, des)

if __name__ == "__main__":
    main()
