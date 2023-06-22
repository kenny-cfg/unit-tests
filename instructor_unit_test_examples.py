def red_or_blue(num):
    return 'Blue' if num % 2 == 0 and num > 20 else 'Red'


def average_exam_score(names_and_marks):
    total_mark = 0
    for name_and_mark in names_and_marks:
        if 'mark' in name_and_mark:
            mark = name_and_mark['mark']
            total_mark = total_mark + int(mark)
        else:
            total_mark = total_mark + 5
    return total_mark / len(names_and_marks)


def increment_line_number():
    pass
