def add_numbers(a, b):
    return a + b

def sub_numbers(a, b):
    return a - b

def get_user_input():
    # Vérifiez si les entrées sont déjà définies par des variables d'environnement, sinon demandez à l'utilisateur
    import os
    a = float(os.getenv("NUM1", 1))  # Valeur par défaut de 1 si NUM1 n'est pas définie
    b = float(os.getenv("NUM2", 2))  # Valeur par défaut de 2 si NUM2 n'est pas définie
    return a, b

if __name__ == "__main__":
    num1, num2 = get_user_input()
    add_result = add_numbers(num1, num2)
    sub_result = sub_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {add_result}")
    print(f"The difference between {num1} and {num2} is: {sub_result}")
    print("END CI/CD :)")
