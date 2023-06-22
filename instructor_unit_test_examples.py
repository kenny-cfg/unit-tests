def red_or_blue(num):
    return 'Blue' if num % 2 == 0 and num > 20 else 'Red'


def average_exam_score(names_and_marks):
    total_length = 0
    total_mark = 0
    for name_and_mark in names_and_marks:
        if 'mark' in name_and_mark:
            mark = name_and_mark['mark']
            total_length = total_length + 1
            try:
                total_mark = total_mark + mark
            except:
                raise ValueError('Mark in not an integer.')
    return total_mark /  total_length


def increment_line_number():
    pass
