from threading import Thread
from multiprocessing import Process

lista = []

def add1(n, a):
    for i in range(1, n+1):
        lista.append(i)
    print(f'Thread número {a} concluída')

def main():
    thread = []
    for i in range(5):
        threads = Process(target=add1, args=(5, i+1))
        thread.append(threads)
    print("antes da conclusão")
    for threads in thread:
        threads.start()
    for threads in thread:
        threads.join()
    print("após conclusão")
    print(lista)

if __name__ == '__main__':
    main()