import time 
from rabina_carpa_search import rabin_karp_search
from boyer_moore_search import  boyer_moore_search
from moris_pratta_search import kmp_search 

def measure_time(search_func, main_string, sub_string, repetitions=1):
    start_time = time.time()
    for _ in range(repetitions):
        search_func(main_string, sub_string)
    end_time = time.time()
    return (end_time - start_time) * 1000

def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error {e}")
        return ''

main_string_1 = load_data('text_1.txt')
main_string_2 = load_data('text_2.txt')
sub_string_1 = 'Експерименти проводилися на комп’ютері з процесором AMD Ryzen 5 3600 та 32 Гб'
sub_string_2 = 'Жадібний алгоритм у цьому випадку полягає в'
sub_fakestring = "Відсутній рядок"

algoritms = {
    "boyer_moor": boyer_moore_search,
    "moris_pratta": kmp_search ,
    "rabin_carp": rabin_karp_search
}

for name, func in algoritms.items():
    taken_time_text_1 = measure_time(func, main_string_1, sub_string_1)
    taken_time_text_2 = measure_time(func, main_string_2, sub_string_2)
    print(f"{name} alogorithm has time (text 1) : {taken_time_text_1:.6f} ms")
    print(f"{name} alogorithm has time (text 2): {taken_time_text_2:.6f} ms")
    
    # fake string
    taken_time_fake_1 = measure_time(func, main_string_1, sub_fakestring)
    taken_time_fake_2 = measure_time(func, main_string_2, sub_fakestring)
    print(f"{name} alogorithm has time for searching a fake string: {taken_time_fake_1:.6f} ms")
    print(f"{name} alogorithm has time for searching a fake string: {taken_time_fake_2:.6f} ms")


   


