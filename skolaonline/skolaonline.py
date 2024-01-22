class SkolaOnline:
   def __init__(self):
       self.students = []

   def create(self):
       while True:
           student_name = input("Zadej jméno studenta: ")
           student_class = input("Zadej třídu studenta: ")
           subject = input("Zadej název předmětu: ")
           grade = input("Zadej známku studenta: ")

           self.students.append({'jmeno': student_name, 'trida': student_class, 'znamka': grade, 'predmet': subject})

           question = input("Chceš vytvořit další záznam? (ano/ne): ")
           if question.lower() != 'ano':
               break
           
   def extract(self):
       for note in self.students:
           print(f"Student: {note['jmeno']}, Třída: {note['trida']}, Předmět: {note['predmet']}, Známka: {note['znamka']}")

   def all(self):
       for note in self.students:
           print()
           print(f"Jméno: {note['jmeno']}")
           print(f"Třída: {note['trida']}")          
           print (f"Předmět: {note['predmet']}")
           print(f"Známka: {note['znamka']}")

skola = SkolaOnline()
skola.create()
skola.all()