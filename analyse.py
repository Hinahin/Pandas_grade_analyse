from os import listdir
import pandas as pnd
import grade_settings as gs

REQUESTS_FILES = listdir(gs.REQUESTS_DIRECTORY)
GRADE_REPORT_FILES = listdir(gs.GRADE_REPORTS_DIRECTORY)


def get_columns(list_columns: list):
    new_list = list_columns[list_columns.index('Grade'):list_columns.index('Cohort Name')]
    for name in new_list:
        if ('(Avg)' in name) or ("Grade Percent" in name):
            new_list.pop(new_list.index(name))
    final_list = ['Email'] + new_list
    return final_list


def get_min_report_settings(request_file: str):
    # print(request_file)   # Проверка какой файл обрабатывается
    crs_request_df = pnd.read_excel(gs.REQUESTS_DIRECTORY + '/' + request_file, 0)  # Берем первый лист заявки
    grade_report_file = crs_request_df.iloc[9, 1] + '.csv'                          # Получаем имя выгрузки
    grade_settings = "_".join(grade_report_file.split(sep='_')[:-1]).casefold()     # ключ настроек
    if grade_report_file not in GRADE_REPORT_FILES:
        print("Нет файла с выгрузкой в папке для " + grade_report_file)
        return 0
    elif grade_settings not in gs.courses:
        print("Нет словаря с настройками для курса для " + grade_settings)
        return 0
    else:
        grade_settings = gs.courses[grade_settings]
        return [grade_report_file, grade_settings]


def get_max_report_settings(request_file: str):
    # print(request_file)   # Проверка какой файл обрабатывается
    crs_request_df = pnd.read_excel(gs.REQUESTS_DIRECTORY + '/' + request_file, 0)  # Берем первый лист заявки
    grade_report_file = crs_request_df.iloc[9, 1] + '.csv'                          # Получаем имя выгрузки

    grade_report_df = pnd.read_csv(gs.GRADE_REPORTS_DIRECTORY + '/' + grade_report_file)
    columns_list = get_columns(grade_report_df.columns.tolist())

    grade_settings = {"Columns_for_order": list(columns_list),
                      "Columns_for_report": list(columns_list),
                      }

    if grade_report_file not in GRADE_REPORT_FILES:
        print("Нет файла с выгрузкой в папке для " + grade_report_file)
        return 0
    else:
        return [grade_report_file, grade_settings]


def make_grade_column(course_order,             # DataFrame заявки на курс
                      grade_report,             # DataFrame отчета об оценках курса
                      possible_mail: list,      # Список возможных электронных адресов
                      col_name: str,            # Название столбца, из которого забираем оценку
                      rate: float,              # Коэффициент для итоговой оценки
                      ):
    grade_list = []                             # Пустой список с оценками. Добавлется в DataFrame столбцом
    number_of_rows = course_order.shape[0]      # Количество строк в DataFrame заявки на курс
    for x in range(number_of_rows):
        email = str(course_order["Адрес электронной почты"][x]).lower()  # Переводим почту в нижний регистр
        if email in possible_mail:
            grade = grade_report[grade_report["Email"] == email][col_name].iloc[0]
            if (grade == "Not Attempted") or (grade == "Not Available"):
                grade_list.append("Не приступал")
            else:
                tst = float(grade_report[grade_report["Email"] == email][col_name].iloc[0])
                digit = tst / rate
                grade_list.append(int(digit.__round__(0)))
        else:
            grade_list.append("Нет на курсе")
    return grade_list


def get_statement(file_name: str):
    gr_report_file, gr_settings = get_min_report_settings(file_name)              # Получаем ссылки на настройки

    course_request_df = pnd.read_excel(gs.REQUESTS_DIRECTORY + '/' + file_name, 1)  # DF заявки

    grade_report_df = pnd.read_csv(gs.GRADE_REPORTS_DIRECTORY +
                                   '/' + gr_report_file, delimiter=',')[
        gr_settings["Columns_for_report"]]                                          # DF выгрузки

    grade_report_df["Email"].str.lower()                                            # переводи все почты в нижний рег

    possible_mail = grade_report_df["Email"].tolist()  # список возможных почт для обработки исключений

    for x, y in zip(gr_settings["Columns_for_report"][1:], gr_settings["Columns_for_order"]):
        test_list = make_grade_column(course_request_df, grade_report_df, possible_mail, x, gr_settings[x])
        course_request_df[y] = test_list

    course_request_df.to_excel(gs.STATEMENTS_DIRECTORY +
                               '/' + file_name.rstrip('.xlsx') + "_ведомость.xlsx", index=False)

    print(file_name.rstrip('.xlsx') + "_ведомость.xlsx" + " - OK!")


def get_full_statement(file_name: str):
    gr_report_file, gr_settings = get_max_report_settings(file_name)                # Получаем ссылки на настройки

    course_request_df = pnd.read_excel(gs.REQUESTS_DIRECTORY + '/' + file_name, 1)  # DF заявки

    grade_report_df = pnd.read_csv(gs.GRADE_REPORTS_DIRECTORY +
                                   '/' + gr_report_file, delimiter=',')[
        gr_settings["Columns_for_report"]]                                          # DF выгрузки

    grade_report_df["Email"].str.lower()               # переводим все почты в нижний регистр

    possible_mail = grade_report_df["Email"].tolist()  # список возможных почт для обработки исключений

    for x, y in zip(gr_settings["Columns_for_report"][1:], gr_settings["Columns_for_order"][1:]):
        test_list = make_grade_column(course_request_df, grade_report_df, possible_mail, x, 0.01)
        course_request_df[y] = test_list

    course_request_df.to_excel(gs.STATEMENTS_DIRECTORY +
                               '/' + file_name.rstrip('.xlsx') + "_полная_ведомость.xlsx", index=False)

    print(file_name.rstrip('.xlsx') + "_полная_ведомость.xlsx" + " - OK!")


for file in REQUESTS_FILES:
    get_statement(file)

# for file in REQUESTS_FILES:
#     get_full_statement(file)

# get_statement('UrFU_0004.xlsx')
# get_full_statement('UrFU_0004.xlsx')
