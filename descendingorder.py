def list_sort(lst):
    n = len(lst)
    for index in range(n):
        for j in range(0, n-index-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def print_descending_order(descending_sample_list):
    list_sort(descending_sample_list)
    for number in descending_sample_list:
        print(number, end=' ')

descending_sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
print_descending_order(descending_sample_list)

