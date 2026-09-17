#definicion de estudiantes, profesores y materias
estudiantes = ["Luz", "Naomi","Carlos"]
profesores = ["Ana","Pedro","Luis"]
materias = ["Programacion","Calculo","Taller"]
graduados = ["Yosseline"]

# declaracion de los hechos

# quien esta incrito en que materia
inscripciones = [
    ("Luz", "Programacion"),
    ("Naomi", "Calculo"),
    ("Carlos", "Taller"),
    ("Carlos", "Programacion"),
    ("Carlos", "Calculo"),
]

#quien imparte que materia
imparte = {
    "Ana": "Programacion",
    "Pedro": "Calculo",
    "Luis": "Taller",
}
# quien aprobo que materia
aprobados = [
    ("Luz", "Programacion"),
    ("Naomi", "Calculo"),
]

#quien tiene beca
becas = ["Yosseline", "Luz"]

#Predicados seleccionados 

def Est(x):
    """Est(x): 'x es estudiante'"""
    return x in estudiantes


def Prof(x):
    """Prof(x): 'x es profesor'"""
    return x in profesores


def Mat(x):
    """Mat(x): 'x es una materia'"""
    return x in materias


def Ins(x, y):
    """Ins(x, y): 'x está inscrito en la materia y'"""
    return (x, y) in inscripciones


def Imp(x, y):
    """Imp(x, y): 'x imparte la materia y'"""
    return imparte.get(x) == y


def Apr(x, y):
    """Apr(x, y): 'x aprobó la materia y'"""
    return (x, y) in aprobados


def Bec(x):
    """Bec(x): 'x tiene beca'"""
    return x in becas

#Consultas de prueba

def main():
    print("=== Comprobación de predicados (Universo: Universidad) ===\n")

    print("1) Est(x): x es estudiante")
    print(f"   Est('Luz') -> {Est('Luz')}   (esperado: True)")
    print(f"   Est('Ana') -> {Est('Ana')}   (esperado: False)")

    print("\n2) Prof(x): x es profesor")
    print(f"   Prof('Pedro')  -> {Prof('Pedro')}   (esperado: True)")
    print(f"   Prof('Carlos') -> {Prof('Carlos')}   (esperado: False)")

    print("\n3) Mat(x): x es una materia")
    print(f"   Mat('Taller') -> {Mat('Taller')}   (esperado: True)")
    print(f"   Mat('Luis')   -> {Mat('Luis')}   (esperado: False)")

    print("\n4) Ins(x, y): x está inscrito en la materia y")
    print(f"   Ins('Carlos', 'Calculo') -> {Ins('Carlos', 'Calculo')}   (esperado: True)")
    print(f"   Ins('Naomi', 'Taller')   -> {Ins('Naomi', 'Taller')}   (esperado: False)")

    print("\n5) Imp(x, y): x imparte la materia y")
    print(f"   Imp('Luis', 'Taller')  -> {Imp('Luis', 'Taller')}   (esperado: True)")
    print(f"   Imp('Pedro', 'Taller') -> {Imp('Pedro', 'Taller')}   (esperado: False)")

    print("\n6) Apr(x, y): x aprobó la materia y")
    print(f"   Apr('Luz', 'Programacion')       -> {Apr('Luz', 'Programacion')}   (esperado: True)")
    print(f"   Apr('Naomi', 'Programacion')     -> {Apr('Naomi', 'Programacion')}   (esperado: False)")

    print("\n7) Bec(x): x tiene beca")
    print(f"   Bec('Yosseline') -> {Bec('Yosseline')}   (esperado: True)")
    print(f"   Bec('Naomi')     -> {Bec('Naomi')}   (esperado: False)")


if __name__ == "__main__":
    main()