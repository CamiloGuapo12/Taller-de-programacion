from concurrent.futures import ThreadPoolExecutor

def print_numbers():
    for i in range(1, 6):
        print(f"Task 1: {i}")

def print_letters():
    for ch in 'ABCDE':
        print(f"Task 2: {ch}")

def print_more_numbers():
    for i in range(6, 11):
        print(f"Task 3: {i}")

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(print_numbers)
        executor.submit(print_letters)
        executor.submit(print_more_numbers)

if __name__ == "__main__":
    main()
