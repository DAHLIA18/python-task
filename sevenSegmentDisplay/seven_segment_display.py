import time

segment_layout = [[0] * 4 for _ in range(5)]


def fill_segment(row_start, col_start, row_end, col_end):
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            segment_layout[i][j] = 1


def fill_top():
    fill_segment(0, 0, 0, 3)


def fill_top_left():
    fill_segment(0, 3, 2, 3)


def fill_top_right():
    fill_segment(2, 3, 4, 3)


def fill_middle():
    fill_segment(4, 0, 4, 3)


def fill_bottom_left():
    fill_segment(2, 0, 4, 0)


def fill_bottom_right():
    fill_segment(0, 0, 2, 0)


def fill_bottom():
    fill_segment(2, 0, 2, 3)


def display():
    for row in segment_layout:
        for value in row:
            if value == 1:
                print("* ", end="")
            else:
                print("  ", end="")
            time.sleep(0.2)
        print()


def input_value(binary_number):
    if len(binary_number) > 9:
        binary_number = binary_number[:9]

    for i in binary_number:
        if i not in ['0', '1']:
            raise ValueError("Input must be 0 or 1")

    if '1' in binary_number:
        for i, bit in enumerate(binary_number):
            if bit == '1':
                if i == 0:
                    fill_top()
                elif i == 1:
                    fill_top_left()
                elif i == 2:
                    fill_top_right()
                elif i == 3:
                    fill_middle()
                elif i == 4:
                    fill_bottom_left()
                elif i == 5:
                    fill_bottom_right()
                elif i == 6:
                    fill_bottom()
        else:
            pass

#
# if __name__ == "__main__":
#     value = input("Enter binary number: ")
#     input_value(value)
#     display()
