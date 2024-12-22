import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi Binary Search Rekursif
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Fungsi Binary Search Iteratif
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Fungsi untuk membandingkan waktu eksekusi dan menampilkan grafik serta tabel
def compare_search_times():
    anime_list = [
        "Naruto",
        "One Piece",
        "Attack on Titan",
        "Dragon Ball",
        "My Hero Academia",
        "Death Note",
        "Fullmetal Alchemist",
    ]
    anime_list.sort()
    targets = ["Naruto", "Death Note", "One Piece", "Attack on Titan"]

    recursive_times = []
    iterative_times = []

    table = PrettyTable()
    table.field_names = ["Target", "Recursive Time (s)", "Iterative Time (s)", "Recursive Index", "Iterative Index"]

    for target in targets:
        # Mengukur waktu eksekusi binary search rekursif
        start_time = time.time() # nge set timer buat ngesearch (titik awal)
        index_recursive = binary_search_recursive(anime_list, target, 0, len(anime_list) - 1)
        end_time = time.time() # titik akhir 
        recursive_time = end_time - start_time # buat ngitung total waktu yang di rekam
        recursive_times.append(recursive_time) # memasukan hasil waktu rekaman kedalam array recursive

        # Mengukur waktu eksekusi binary search iteratif
        start_time = time.time() # set awal waktu atau sebagai titik awal
        index_iterative = binary_search_iterative(anime_list, target)
        end_time = time.time() #  titik akhir
        iterative_time = end_time - start_time # total waktu
        iterative_times.append(iterative_time) # memasukan hasil ke dalam array 

        # Menambahkan data ke tabel
        table.add_row([target, recursive_time, iterative_time, index_recursive, index_iterative])

    # Menampilkan tabel
    print(table)

    # Menampilkan grafik perbandingan waktu eksekusi
    plt.figure(figsize=(10, 6))
    x = range(1, len(targets) + 1)
    plt.plot(x, recursive_times, label="Recursive", marker="o", color="orange")
    plt.plot(x, iterative_times, label="Iterative", marker="o", color="teal")
    plt.xticks(x, targets)
    plt.xlabel("Targets")
    plt.ylabel("Execution Time (s)")
    plt.title("Comparison of Recursive and Iterative Binary Search")
    plt.legend()
    plt.grid()
    plt.show()

# Menjalankan fungsi perbandingan
compare_search_times()
