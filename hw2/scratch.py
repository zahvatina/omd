import csv

imput_file: str = 'C:/Users/Xiaomi/Downloads/funcs_homework_employees_sample.csv'
output_file = 'desc.csv'
columns_report = ['Название департамента', 'Численность', 'Вилка зарплат в отделе', 'Средняя зарптала в отделе']

with open(imput_file, 'r', encoding='utf-8') as file_obj:
    """Open, read csv and saves data by rows in data_employees"""
    reader = csv.reader(file_obj, delimiter=';')
    data_employees = []
    for row in reader:
        data_employees.append(row)

columns = data_employees[0]
data_employees = data_employees[1:]
department = set([data_employees[i][2] for i in range(len(data_employees))])


def filter_dep(department_dict: dict, i: int, dep: str, form: type):
    """Selects all information from the key department. Values in the address column
    change the data type (initially str) and wraps it in a list """
    return list(map(form, [d[i] for d in department_dict[dep]]))


def desc(department_dict: dict, dep: str):
    """Dict is created: keys - columns_report values, key values - Department information"""
    res = {}
    res['Название департамента'] = dep
    res['Численность'] = len(filter_dep(department_dict, 3, dep, str))
    res['Вилка зарплат в отделе'] = '{}-{}'.format(min(filter_dep(department_dict, 3, dep, int)),
                                                   max(filter_dep(department_dict, 3, dep, int)))
    res['Средняя зарптала в отделе'] = sum(filter_dep(department_dict, 3, dep, int)) / res['Численность']
    return res


def write_report(report: list):
    """Reads list and adds it line by line to csv, saves csv"""
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns_report)
        writer.writeheader()
        for row in report:
            writer.writerow(row)


def generate_report():
    """ A dictionary is created with the keys - departments,
    and the remaining information from data_employees is added to the key values.
    A report is added to wdata for each Department """
    department_dict = {dep: [] for dep in department}
    for d in data_employees:
        department_dict[d[2]].append(d[:2] + d[3:])

    wdata = []
    for dep in department_dict:
        res = desc(department_dict, dep)
        wdata.append(res)
    return wdata


def func_1():
    """Displays the names of all departments"""
    print('Название всех отделов:')
    print(department)


def func_2():
    """Formats and outputs a report by Department"""
    wdata = generate_report()
    head = columns_report
    data_employees = [list(wdata[i].values()) for i in range(len(wdata))]
    print('|', end='')
    print('{: <33} | {: <15} | {: <30} | {: <30}'.format(head[0], head[1], head[2], head[3]))
    print('')
    for row in data_employees:
        print('{: <34} | {: <15} | {: <30} | {: <30}'.format(row[0], row[1], row[2], round(row[3], 2)))


def func_3():
    """Generate and save report to file"""
    write_report(generate_report())
    print('Сохранение прошло успешно')
    print('Откройте файл {}'.format(output_file))
    print('Внимание, если файл с именем {} уже существует, он был перезаписан'.format(output_file))


def start():
    print("""Выберите одну из функций:
    1 - Вывести все отделы
    2 - Вывести сводный отчёт
    3 - Сохранить сводный отчёт
    """)
    while True:
        answer = input()
        eval('func_{}()'.format(answer))


if __name__ == "__main__":
    start()
