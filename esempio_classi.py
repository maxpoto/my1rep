class Studente:
    def __init__(self, nome, cognome, corso):
        self.nome = nome
        self.cognome = cognome
        self._corso = corso

    @property
    def corso(self):
        return self._corso

    @corso.setter
    def corso(self, corso):
        if corso:
            self._corso = corso
        else:
            print("Nessun corso coglione")

    def scheda_personale(self):
        """
        Restituisce la scheda studente
        :return: string
        """
        return f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso:{self.corso}"


studente_uno = Studente("Mario", "Rossi", "Filosofia")
studente_due = Studente("Aldo", "Biscarde", "Ingegneria")

print(studente_due.scheda_personale())
studente_uno.cognome = "Pazzi"
print(studente_uno.cognome)
studente_due.corso = ""
