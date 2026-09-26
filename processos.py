import time
from multiprocessing import Process, Queue


def eh_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def processar(inicio, fim, fila):
    quantidade = 0

    for numero in range(inicio, fim):
        if eh_primo(numero):
            quantidade += 1

    fila.put(quantidade)


if __name__ == "__main__":
    inicio = time.perf_counter()

    fila = Queue()

    p1 = Process(target=processar, args=(2, 50000, fila))
    p2 = Process(target=processar, args=(50000, 100000, fila))
    p3 = Process(target=processar, args=(100000, 150000, fila))
    p4 = Process(target=processar, args=(150000, 200000, fila))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    quantidade = (
        fila.get() +
        fila.get() +
        fila.get() +
        fila.get()
    )

    fim = time.perf_counter()

    print("Quantidade de primos:", quantidade)
    print("Tempo:", fim - inicio, "segundos")
