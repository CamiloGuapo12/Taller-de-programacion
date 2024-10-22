from concurrent.futures import ThreadPoolExecutor
import random

SIZE = 1_000_000
THREAD_COUNT = 4

def calculate_sum(start, end, array):
    return sum(array[start:end])

def main():
    # Crear un arreglo con números aleatorios
    array = [random.randint(0, 100) for _ in range(SIZE)]

    chunk_size = SIZE // THREAD_COUNT
    futures = []

    with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
        for i in range(THREAD_COUNT):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size if i < THREAD_COUNT - 1 else SIZE
            futures.append(executor.submit(calculate_sum, start_index, end_index, array))

    # Obtener resultados
    total_sum = sum(future.result() for future in futures)
    print("Total Sum:", total_sum)

if __name__ == "__main__":
    main()
