import time


def eh_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    inicio = time.perf_counter()

    numeros = range(2, 200000)

    quantidade = 0

    for numero in numeros:
        if eh_primo(numero):
            quantidade += 1

    fim = time.perf_counter()

    print("Quantidade de primos:", quantidade)
    print("Tempo:", fim - inicio, "segundos")
