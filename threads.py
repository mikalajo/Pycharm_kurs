import threading
import time
import random


def worker(thread_id):
    """Funktion, die von einem Thread ausgeführt wird."""
    print(f"Thread {thread_id} gestartet.")
    for i in range(5):
        sleep_time = random.uniform(0.5, 1.5)
        print(f"Thread {thread_id} arbeitet... (Iteration {i + 1})")
        time.sleep(sleep_time)  # Füge hier einen Breakpoint hinzu
    print(f"Thread {thread_id} beendet.")


def main():
    print("Starte Multi-Threading-Demo...")

    # Liste zum Speichern der Threads
    threads = []

    # Erstelle und starte mehrere Threads
    for thread_id in range(3):  # Ändere die Anzahl der Threads hier
        thread = threading.Thread(target=worker, args=(thread_id,))
        threads.append(thread)
        thread.start()

    # Warten, bis alle Threads abgeschlossen sind
    for thread in threads:
        thread.join()

    print("Alle Threads abgeschlossen.")


if __name__ == "__main__":
    main()
