def list_sort(lst):
    n = len(lst)
    for index in range(n):
        for j in range(0, n-index-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def print_ascending_order(ascending_sample_list):
    list_sort(ascending_sample_list)
    for number in ascending_sample_list:
        print(number, end=' ')

ascending_sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
print_ascending_order(ascending_sample_list)

