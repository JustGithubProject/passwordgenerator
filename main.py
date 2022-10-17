import random


def password_generation(k):
    symbols = "@#$%&"
    numbers = "0123456789"
    letters = "qwertyuiopasdfghjklzxcvbnm"
    summa = symbols + numbers + letters
    password_list = random.sample(summa, k)
    result_password = "".join(password_list)
    return result_password


def main():
    while True:
        k = int(input("Enter number of characters: "))
        if k == 0:
            break
        with open("D:/Users/Kropi/Desktop/password.txt", "w") as file:
            file.write(f"Ваш пароль: {password_generation(k)}")
            print("Ваш пароль успешно сохранен на рабочий стол")


if __name__ == "__main__":
    main()