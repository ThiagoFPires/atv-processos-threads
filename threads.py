import time
import threading


def eh_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


resultados = []


def processar(inicio, fim):
    quantidade = 0

    for numero in range(inicio, fim):
        if eh_primo(numero):
            quantidade += 1

    resultados.append(quantidade)


if __name__ == "__main__":
    inicio = time.perf_counter()

    threads = [
        threading.Thread(target=processar, args=(2, 50000)),
        threading.Thread(target=processar, args=(50000, 100000)),
        threading.Thread(target=processar, args=(100000, 150000)),
        threading.Thread(target=processar, args=(150000, 200000))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    quantidade = sum(resultados)

    fim = time.perf_counter()

    print("Quantidade de primos:", quantidade)
    print("Tempo:", fim - inicio, "segundos")
