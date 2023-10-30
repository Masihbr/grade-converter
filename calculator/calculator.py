def convert_grade(iranian_grade):
    if iranian_grade <= 14:
        m = (3 - 1) / (14 - 10)
        b = 1 - m * 10
        usa_gpa = m * iranian_grade + b
    else:
        usa_gpa = 3 + (iranian_grade - 14) * (4 - 3) / (20 - 14)
    return usa_gpa


def calculate_gpa(info: dict):
    units_sum = 0
    point_sum = 0
    for _, course in info.items():
        unit = int(course['unit'])
        grade = float(course['grade'])
        point_sum += grade * unit
        units_sum += unit
    total_avg = point_sum / units_sum
    return convert_grade(iranian_grade=total_avg)
