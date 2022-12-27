import math


# H μέθοδος abc_inputs() παίρνει τις 3 τιμές που εισάγει απο το πληκτρολόγιο ο χρήστης και τις γυρνάει σε μια λίστα
def abc_inputs():
    while True:
        a, b, c = input("Παρακαλώ εισάγετε τις  σταθερές τιμές \"a\" \"b\" \"c\" γιά το τριώνυμο ax²+bx+c :\n").split()
        if a == "0":
            print("Η τιμή a δέν μπορεί να είναι 0")
            continue
        else:
            return list(map(int, (a, b, c)))


# Η μέθοδος trinomial(abc=[]) παίρνει σαν όρισμα μια λίστα, υπολογίζει την Διακρίνουσα απο τα στοιχεία της λίστας
# και καλεί την μέθοδο rizes_calc για τον υπολογισμό των ριζών της εξίσωσης
def trinomial(abc=[]):
    print(f"Ρίζες του τριωνύμου ax²+bx+c όταν: a={abc[0]} b={abc[1]} c={abc[2]}")
    a = abc[0]
    b = abc[1]
    c = abc[2]
    diakrinousa = b ** 2 - 4 * a * c

    rizes_calc(diakrinousa, a, b, c)


# Η μέθοδος rizes_calc(d, a,b,c) παίρνει σαν όρισμα την διακρίνουσα(d) και τις 3 τιμές όπου έιχε εισάγει ο χρήστης
def rizes_calc(d, a, b, c):
    if d > 0:
        x1 = (-b + math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a
        print(f"Η εξίσωση έχει δύο πραγματικές ρίζες: x1={x1:.2f} και χ2={x2:.2f}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Η εξίσωση έχει μόνο μία πραγματική ρίζα: x={x:.2f}")
    else:
        print("Η εξίσωση δεν έχει πραγματικές ρίζες")


trinomial(abc_inputs())
