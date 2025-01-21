class Matiere:
    def __init__(self, nom, code, coef, enseignant):
        self.nom = nom
        self.code = code
        self.coef = coef
        self.enseignant = enseignant

    @staticmethod
    def ajouterMatiere():
        nom = input("Entrez le nom de la matière: ")
        code = int(input("Entrez le code de la matière: "))
        coef = int(input("Entrez le coefficient de la matière: "))
        enseignant = input("Entrez le nom de l'enseignant: ")
        return Matiere(nom, code, coef, enseignant)

    def afficherMatiere(self):
        print("Nom de la matière:", self.nom)
        print("Code de la matière:", self.code)
        print("Coefficient de la matière:", self.coef)
        print("Enseignant de la matière:", self.enseignant)
