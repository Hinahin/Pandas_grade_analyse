STATEMENTS_DIRECTORY = './statements'
REQUESTS_DIRECTORY = './requests'
GRADE_REPORTS_DIRECTORY = './grade_reports'
STATISTIC_DIRECTORY = './statistic'

calc = {"Тест (Avg)": 0.001,
        "Рубежный тест (Avg)": 0.005,
        "Итоговый контроль (Avg)": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Тесты (проходной балл 40)",
                              "Рубежные тесты (проходной балл 40)",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email", "Тест (Avg)", "Рубежный тест (Avg)", "Итоговый контроль (Avg)", "Grade Percent"]
        }

tepl = {"Техническая термодинамика (Avg)": 0.002,
        "Теплообмен (Avg)": 0.002,
        "Энергетическое оборудование (Avg)": 0.002,
        "Итоговый контроль (Avg)": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Техническая термодинамика (проходной балл 40)",
                              "Теплообмен (проходной балл 40)",
                              "Энергетическое оборудование (проходной балл 40)",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email",
                               "Техническая термодинамика (Avg)",
                               "Теплообмен (Avg)",
                               "Энергетическое оборудование (Avg)",
                               "Итоговый контроль (Avg)",
                               "Grade Percent"]
        }

teco = {"Тест для самоконтроля (Avg)": 0.003,
        "Задание (Avg)": 0.003,
        "Итоговое тестирование (Avg)": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Тесты (проходной балл 40)",
                              "Задания (проходной балл 40)",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email",
                               "Тест для самоконтроля (Avg)",
                               "Задание (Avg)",
                               "Итоговое тестирование (Avg)",
                               "Grade Percent"]
        }

chemso = {"Задание (Avg)": 0.006,
          "Итоговый контроль (Avg)": 0.004,
          "Grade Percent": 1,
          "Columns_for_order": ["Задания (проходной балл 40)",
                                "Экзамен (проходной балл 40)",
                                "Итоговый балл"],
          "Columns_for_report": ["Email",
                                 "Задание (Avg)",
                                 "Итоговый контроль (Avg)",
                                 "Grade Percent"]
          }

elb = {"Домашная работа (Avg)": 0.006,
       "Итоговое задание (Avg)": 0.004,
       "Grade Percent": 1,
       "Columns_for_order": ["Домашняя работа (проходной балл 40)",
                             "Экзамен (проходной балл 40)",
                             "Итоговый балл"],
       "Columns_for_report": ["Email",
                              "Домашная работа (Avg)",
                              "Итоговое задание (Avg)",
                              "Grade Percent"]
       }

ecos = {"Задание (Avg)": 0.0015,
        "Практическое задание (Avg)": 0.004,
        "Эссе": 0.0005,
        "Итоговое тестирование (Avg)": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Задания (проходной балл 40)",
                              "Практические задания (проходной балл 40)",
                              "Эссе",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email",
                               "Задание (Avg)",
                               "Практическое задание (Avg)",
                               "Эссе",
                               "Итоговое тестирование (Avg)",
                               "Grade Percent"]
        }

lifesafety = {"Тестовое задание (Avg)": 0.004,  # Требует доработки после доабвления экзамена
              "Grade Percent": 1,
              "Columns_for_order": ["Тесты (проходной балл 40)",
                                    "Итоговый балл"],
              "Columns_for_report": ["Email",
                                     "Тестовое задание (Avg)",
                                     "Grade Percent"]
              }

mcs = {"Тестовое задание (Avg)": 0.0015,
       "Учебное задание (Avg)": 0.0015,
       "Контрольные задания (Avg)": 0.003,
       "Итоговый контроль (Avg)": 0.004,
       "Grade Percent": 1,
       "Columns_for_order": ["Тесты (проходной балл 40)",
                             "Учебные задания (проходной балл 40)",
                             "Контрольные задания (проходной балл 40)",
                             "Экзамен (проходной балл 40)",
                             "Итоговый балл"],
       "Columns_for_report": ["Email",
                              "Тестовое задание (Avg)",
                              "Учебное задание (Avg)",
                              "Контрольные задания (Avg)",
                              "Итоговый контроль (Avg)",
                              "Grade Percent"]
       }

hist_view = {"Test (Avg)": 0.003,
             "modul (Avg)": 0.003,
             "Final Exam (Avg)": 0.004,
             "Grade Percent": 1,
             "Columns_for_order": ["Тесты (проходной балл 40)",
                                   "Модули (проходной балл 40)",
                                   "Экзамен (проходной балл 40)",
                                   "Итоговый балл"],
             "Columns_for_report": ["Email",
                                    "Test (Avg)",
                                    "modul (Avg)",
                                    "Final Exam (Avg)",
                                    "Grade Percent"]
             }

hist = {"Тестовое задание (Avg)": 0.003,
        "Учебное задание (Avg)": 0.003,
        "Итоговый контроль": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Тесты (проходной балл 40)",
                              "Учебные задания (проходной балл 40)",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email",
                               "Тестовое задание (Avg)",
                               "Учебное задание (Avg)",
                               "Итоговый контроль",
                               "Grade Percent"]
        }

rubscult = {"Тестовые задания (Avg)": 0.002,
            "Учебные задания (Avg)": 0.002,
            "Контрольные задания (Avg)": 0.002,
            "Итоговый контроль (Avg)": 0.004,
            "Grade Percent": 1,
            "Columns_for_order": ["Тесты (проходной балл 40)",
                                  "Учебные задания (проходной балл 40)",
                                  "Контрольные задания (проходной балл 40)",
                                  "Экзамен (проходной балл 40)",
                                  "Итоговый балл"],
            "Columns_for_report": ["Email",
                                   "Тестовые задания (Avg)",
                                   "Учебные задания (Avg)",
                                   "Контрольные задания (Avg)",
                                   "Итоговый контроль (Avg)",
                                   "Grade Percent"]
            }

designbasics = {"Тестовое задание (Avg)": 0.003,
                "Практическое задание (Avg)": 0.003,
                "Итоговый контроль (Avg)": 0.004,
                "Grade Percent": 1,
                "Columns_for_order": ["Тесты (проходной балл 40)",
                                      "Практики (проходной балл 40)",
                                      "Экзамен (проходной балл 40)",
                                      "Итоговый балл"],
                "Columns_for_report": ["Email",
                                       "Тестовое задание (Avg)",
                                       "Практическое задание (Avg)",
                                       "Итоговый контроль (Avg)",
                                       "Grade Percent"]
                }

metr = {"Метрология (Avg)": 0.002,
        "Стандартизация (Avg)": 0.002,
        "Оценка соответствия (Avg)": 0.002,
        "Итоговый контроль (Avg)": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Метрология (проходной балл 40)",
                              "Стандартизация (проходной балл 40)",
                              "Оценка соответствия (проходной балл 40)",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email",
                               "Метрология (Avg)",
                               "Стандартизация (Avg)",
                               "Оценка соответствия (Avg)",
                               "Итоговый контроль (Avg)",
                               "Grade Percent"]
        }

csharp = {"Упражнения (Avg)": 0.002,
          "Практика (Avg)": 0.004,
          "Итоговый контроль (Avg)": 0.004,
          "Grade Percent": 1,
          "Columns_for_order": ["Упражнения (проходной балл 40)",
                                "Практики (проходной балл 40)",
                                "Экзамен (проходной балл 40)",
                                "Итоговый балл"],
          "Columns_for_report": ["Email",
                                 "Упражнения (Avg)",
                                 "Практика (Avg)",
                                 "Итоговый контроль (Avg)",
                                 "Grade Percent"]
          }

intpr = {"Тест (Avg)": 0.003,
         "Учебные задания (Avg)": 0.003,
         "Final Exam (Avg)": 0.004,
         "Grade Percent": 1,
         "Columns_for_order": ["Тесты (проходной балл 40)",
                               "Учебные задания (проходной балл 40)",
                               "Экзамен (проходной балл 40)",
                               "Итоговый балл"],
         "Columns_for_report": ["Email",
                                "Тест (Avg)",
                                "Учебные задания (Avg)",
                                "Final Exam (Avg)",
                                "Grade Percent"]
         }

edubase = {"Контрольное задание (Avg)": 0.003,
           "Промежуточная аттестация (Avg)": 0.003,
           "Final Exam (Avg)": 0.004,
           "Grade Percent": 1,
           "Columns_for_order": ["Контрольные задания (проходной балл 40)",
                                 "Промежуточная аттестация (проходной балл 40)",
                                 "Экзамен (проходной балл 40)",
                                 "Итоговый балл"],
           "Columns_for_report": ["Email",
                                  "Контрольное задание (Avg)",
                                  "Промежуточная аттестация (Avg)",
                                  "Final Exam (Avg)",
                                  "Grade Percent"]
           }

psymedia = {"Кроссворд (Avg)": 0.002,
            "Контрольное задание (Avg)": 0.002,
            "Учебное задание (Avg)": 0.002,
            "Итоговое тестирование (Avg)": 0.004,
            "Grade Percent": 1,
            "Columns_for_order": ["Кроссворды (проходной балл 40)",
                                  "Контрольные задания (проходной балл 40)",
                                  "Учебные задания (проходной балл 40)",
                                  "Экзамен (проходной балл 40)",
                                  "Итоговый балл"],
            "Columns_for_report": ["Email",
                                   "Кроссворд (Avg)",
                                   "Контрольное задание (Avg)",
                                   "Учебное задание (Avg)",
                                   "Итоговое тестирование (Avg)",
                                   "Grade Percent"]
            }

inclus_m2 = {"Тестирование к разделу (Avg)": 0.002,
             "Задание к разделу (Avg)": 0.004,
             "Итоговое тестирование (Avg)": 0.004,
             "Grade Percent": 1,
             "Columns_for_order": ["Тесты (проходной балл 40)",
                                   "Задания (проходной балл 40)",
                                   "Экзамен (проходной балл 40)",
                                   "Итоговый балл"],
             "Columns_for_report": ["Email",
                                    "Тестирование к разделу (Avg)",
                                    "Задание к разделу (Avg)",
                                    "Итоговое тестирование (Avg)",
                                    "Grade Percent"]
             }

smngm = {"Учебное задание (Avg)": 0.006,
         "Итоговый контроль (Avg)": 0.004,
         "Grade Percent": 1,
         "Columns_for_order": ["Учебные задания (проходной балл 40)",
                               "Экзамен (проходной балл 40)",
                               "Итоговый балл"],
         "Columns_for_report": ["Email",
                                "Учебное задание (Avg)",
                                "Итоговый контроль (Avg)",
                                "Grade Percent"]
         }

elecd = {"Домашние задания1 (Avg)": 0.004,
         "Домашние задания2 (Avg)": 0.002,
         "Итоговый контроль (Avg)": 0.004,
         "Grade Percent": 1,
         "Columns_for_order": ["Домашние задания 1 (проходной балл 40)",
                               "Домашние задания 2 (проходной балл 40)",
                               "Экзамен (проходной балл 40)",
                               "Итоговый балл"],
         "Columns_for_report": ["Email",
                                "Домашние задания1 (Avg)",
                                "Домашние задания2 (Avg)",
                                "Итоговый контроль (Avg)",
                                "Grade Percent"]
         }

sigproc = {"Тесты (Avg)": 0.006,
           "Итоговый контроль (Avg)": 0.004,
           "Grade Percent": 1,
           "Columns_for_order": ["Тесты (проходной балл 40)",
                                 "Экзамен (проходной балл 40)",
                                 "Итоговый балл"],
           "Columns_for_report": ["Email",
                                  "Тесты (Avg)",
                                  "Итоговый контроль (Avg)",
                                  "Grade Percent"]
           }

philosophy = {"Тест (Avg)": 0.002,
              "Учебное задание (Avg)": 0.002,
              "Контрольное задание (Avg)": 0.003,
              "Итоговый контроль (Avg)": 0.003,
              "Grade Percent": 1,
              "Columns_for_order": ["Тесты (проходной балл 40)",
                                    "Учебные задания (проходной балл 40)",
                                    "Контрольные задания (проходной балл 40)",
                                    "Экзамен (проходной балл 40)",
                                    "Итоговый балл"],
              "Columns_for_report": ["Email",
                                     "Тест (Avg)",
                                     "Учебное задание (Avg)",
                                     "Контрольное задание (Avg)",
                                     "Итоговый контроль (Avg)",
                                     "Grade Percent"]
              }

bioeco = {"Учебное задание (Avg)": 0.002,
          "Промежуточное задание (Avg)": 0.004,
          "Итоговый контроль (Avg)": 0.004,
          "Grade Percent": 1,
          "Columns_for_order": ["Учебные задания (проходной балл 40)",
                                "Промежуточные задания (проходной балл 40)",
                                "Экзамен (проходной балл 40)",
                                "Итоговый балл"],
          "Columns_for_report": ["Email",
                                 "Учебное задание (Avg)",
                                 "Промежуточное задание (Avg)",
                                 "Итоговый контроль (Avg)",
                                 "Grade Percent"]
          }

its = {"Тестовые задания (Avg)": 0.004,  # Требует доработки после доабвления экзамена
       "Grade Percent": 1,
       "Columns_for_order": ["Тесты (проходной балл 40)",
                             "Итоговый балл"],
       "Columns_for_report": ["Email",
                              "Тестовые задания (Avg)",
                              "Grade Percent"]
       }

ecoeff = {"Тестирование (Avg)": 0.002,
          "Учебное задание (Avg)": 0.0015,
          "Контрольные задания (Avg)": 0.0025,
          "Итоговое тестирование (Avg)": 0.004,
          "Grade Percent": 1,
          "Columns_for_order": ["Тесты (проходной балл 40)",
                                "Учебные задания (проходной балл 40)",
                                "Контрольные задания (проходной балл 40)",
                                "Экзамен (проходной балл 40)",
                                "Итоговый балл"],
          "Columns_for_report": ["Email",
                                 "Тестирование (Avg)",
                                 "Учебное задание (Avg)",
                                 "Контрольные задания (Avg)",
                                 "Итоговое тестирование (Avg)",
                                 "Grade Percent"]
          }

systeng = {"Задания (Avg)": 0.002,
           "Практика (Avg)": 0.004,
           "Итоговый контроль (Avg)": 0.004,
           "Grade Percent": 1,
           "Columns_for_order": ["Задания (проходной балл 40)",
                                 "Практики (проходной балл 40)",
                                 "Экзамен (проходной балл 40)",
                                 "Итоговый балл"],
           "Columns_for_report": ["Email",
                                  "Задания (Avg)",
                                  "Практика (Avg)",
                                  "Итоговый контроль (Avg)",
                                  "Grade Percent"]
           }

cellbio = {"Учебное задание (Avg)": 0.001,
           "Контрольное задание (Avg)": 0.003,
           "Промежуточный контроль (Avg)": 0.002,
           "Final Exam (Avg)": 0.004,
           "Grade Percent": 1,
           "Columns_for_order": ["Учебные задания (проходной балл 40)",
                                 "Контрольные задания (проходной балл 40)",
                                 "Промежуточный контроль (проходной балл 40)",
                                 "Экзамен (проходной балл 40)",
                                 "Итоговый балл"],
           "Columns_for_report": ["Email",
                                  "Учебное задание (Avg)",
                                  "Контрольное задание (Avg)",
                                  "Промежуточный контроль (Avg)",
                                  "Final Exam (Avg)",
                                  "Grade Percent"]
           }

introbe = {"Тестовое задание (Avg)": 0.0015,
           "Промежуточный контроль (Avg)": 0.003,
           "Учебное задание (Avg)": 0.0015,
           "Итоговый контроль (Avg)": 0.004,
           "Grade Percent": 1,
           "Columns_for_order": ["Тесты (проходной балл 40)",
                                 "Промежуточный контроль (проходной балл 40)",
                                 "Учебные задания (проходной балл 40)",
                                 "Экзамен (проходной балл 40)",
                                 "Итоговый балл"],
           "Columns_for_report": ["Email",
                                  "Тестовое задание (Avg)",
                                  "Промежуточный контроль (Avg)",
                                  "Учебное задание (Avg)",
                                  "Итоговый контроль (Avg)",
                                  "Grade Percent"]
           }

crithink = {"Тесты (Avg)": 0.0015,
            "Кейсы (Avg)": 0.0015,
            "Взаимопроверка": 0.001,
            "Задания по разделу (Avg)": 0.002,
            "Итоговый контроль (Avg)": 0.004,
            "Grade Percent": 1,
            "Columns_for_order": ["Тесты (проходной балл 40)",
                                  "Кейсы (проходной балл 40)",
                                  "Взаимопроверка",
                                  "Задания по разделу (проходной балл 40)",
                                  "Экзамен (проходной балл 40)",
                                  "Итоговый балл"],
            "Columns_for_report": ["Email",
                                   "Тесты (Avg)",
                                   "Кейсы (Avg)",
                                   "Взаимопроверка",
                                   "Задания по разделу (Avg)",
                                   "Итоговый контроль (Avg)",
                                   "Grade Percent"]
            }

archc = {"Тестирование (Avg)": 0.006,
         "Итоговый контроль (Avg)": 0.004,
         "Grade Percent": 1,
         "Columns_for_order": ["Тесты (проходной балл 40)",
                               "Экзамен (проходной балл 40)",
                               "Итоговый балл"],
         "Columns_for_report": ["Email",
                                "Тестирование (Avg)",
                                "Итоговый контроль (Avg)",
                                "Grade Percent"]
         }

philsci = {"Тестовое задание (Avg)": 0.0025,
           "Учебное задание (Avg)": 0.0025,
           "Промежуточная аттестация (Avg)": 0.001,
           "Итоговый контроль (Avg)": 0.004,
           "Grade Percent": 1,
           "Columns_for_order": ["Тесты (проходной балл 40)",
                                 "Учебные задания (проходной балл 40)",
                                 "Промежуточная аттестация",
                                 "Экзамен (проходной балл 40)",
                                 "Итоговый балл"],
           "Columns_for_report": ["Email",
                                  "Тестовое задание (Avg)",
                                  "Учебное задание (Avg)",
                                  "Промежуточная аттестация (Avg)",
                                  "Итоговый контроль (Avg)",
                                  "Grade Percent"]
           }

triz = {"Homework (Avg)": 0.005,
        "Midterm Exam": 0.001,
        "Final Exam (Avg)": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Домашняя работа (проходной балл 40)",
                              "Эссе",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email",
                               "Homework (Avg)",
                               "Midterm Exam",
                               "Final Exam (Avg)",
                               "Grade Percent"]
        }

prgrmm = {"Упражнения (Avg)": 0.002,
          "Практика (Avg)": 0.004,
          "Final Exam (Avg)": 0.004,
          "Grade Percent": 1,
          "Columns_for_order": ["Упражнения (проходной балл 40)",
                                "Практики (проходной балл 40)",
                                "Экзамен (проходной балл 40)",
                                "Итоговый балл"],
          "Columns_for_report": ["Email",
                                 "Упражнения (Avg)",
                                 "Практика (Avg)",
                                 "Final Exam (Avg)",
                                 "Grade Percent"]
          }

nucmed = {"Контрольное заданние (Avg)": 0.004,
          "Учебное задание (Avg)": 0.002,
          "Final Exam (Avg)": 0.004,
          "Grade Percent": 1,
          "Columns_for_order": ["Контрольные задания (проходной балл 40)",
                                "Учебные задания (проходной балл 40)",
                                "Экзамен (проходной балл 40)",
                                "Итоговый балл"],
          "Columns_for_report": ["Email",
                                 "Контрольное заданние (Avg)",
                                 "Учебное задание (Avg)",
                                 "Final Exam (Avg)",
                                 "Grade Percent"]
          }

geom = {"Начертательная геометрия (Avg)": 0.003,
        "Инженерная графика (Avg)": 0.003,
        "Итоговый контроль (Avg)": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Начертательная геометрия (проходной балл 40)",
                              "Инженерная графика (проходной балл 40)",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email",
                               "Начертательная геометрия (Avg)",
                               "Инженерная графика (Avg)",
                               "Итоговый контроль (Avg)",
                               "Grade Percent"]
        }

engm = {"Тест (Avg)": 0.0015,
        "Домашнее задание (Avg)": 0.0030,
        "Базовый проект (Avg)": 0.0015,
        "Итоговый  тест (Avg)": 0.004,
        "Grade Percent": 1,
        "Columns_for_order": ["Тесты (проходной балл 40)",
                              "Домашние задания (проходной балл 40)",
                              "Базовый проект (проходной балл 40)",
                              "Экзамен (проходной балл 40)",
                              "Итоговый балл"],
        "Columns_for_report": ["Email",
                               "Тест (Avg)",
                               "Домашнее задание (Avg)",
                               "Базовый проект (Avg)",
                               "Итоговый  тест (Avg)",
                               "Grade Percent"]
        }

datainf = {"Практика (Avg)": 0.006,
           "Итоговый контроль (Avg)": 0.004,
           "Grade Percent": 1,
           "Columns_for_order": ["Практика (проходной балл 40)",
                                 "Экзамен (проходной балл 40)",
                                 "Итоговый балл"],
           "Columns_for_report": ["Email",
                                  "Практика (Avg)",
                                  "Итоговый контроль (Avg)",
                                  "Grade Percent"]
           }

personalsafety = {"Тестирование к теме (Avg)": 0.0032,
                  "Интерактивное задание (Avg)": 0.0028,
                  "Итоговое тестирование (Avg)": 0.004,
                  "Grade Percent": 1,
                  "Columns_for_order": ["Тесты (проходной балл 40)",
                                        "Интерактивные задания (проходной балл 40)",
                                        "Экзамен (проходной балл 40)",
                                        "Итоговый балл"],
                  "Columns_for_report": ["Email",
                                         "Тестирование к теме (Avg)",
                                         "Интерактивное задание (Avg)",
                                         "Итоговое тестирование (Avg)",
                                         "Grade Percent"]
                  }

manegemach = {"Тестовое задание (Avg)": 0.0015,
              "Учебное задание (Avg)": 0.0015,
              "Контрольное задание (Avg)": 0.0030,
              "Итоговое тестирование (Avg)": 0.004,
              "Grade Percent": 1,
              "Columns_for_order": ["Тестовые задания (проходной балл 40)",
                                    "Учебные задания (проходной балл 40)",
                                    "Контрольные задания (проходной балл 40)",
                                    "Экзамен (проходной балл 40)",
                                    "Итоговый балл"],
              "Columns_for_report": ["Email",
                                     "Тестовое задание (Avg)",
                                     "Учебное задание (Avg)",
                                     "Контрольное задание (Avg)",
                                     "Итоговое тестирование (Avg)",
                                     "Grade Percent"]
              }

telecom = {"Тестовое задание (Avg)": 0.006,
           "Final Exam (Avg)": 0.004,
           "Grade Percent": 1,
           "Columns_for_order": ["Тесты (проходной балл 40)",
                                 "Экзамен (проходной балл 40)",
                                 "Итоговый балл"],
           "Columns_for_report": ["Email",
                                  "Тестовое задание (Avg)",
                                  "Final Exam (Avg)",
                                  "Grade Percent"]
           }

legal = {"Тест по разделу (Avg)": 0.008,
         "Final Exam (Avg)": 0.002,
         "Grade Percent": 1,
         "Columns_for_order": ["Тесты (проходной балл 40)",
                               "Экзамен (проходной балл 40)",
                               "Итоговый балл"],
         "Columns_for_report": ["Email",
                                "Тест по разделу (Avg)",
                                "Final Exam (Avg)",
                                "Grade Percent"]
         }

courses = {'calc': calc,  # Математический анализ
           'tepl': tepl,  # Теплотехника
           'teco': teco,  # Технология конструкционных материалов
           'chemso': chemso,  # Аккумуляторы, топливные элементы и их роль в современном мире
           'elb': elb,  # Основы электротехники и электроники
           'ecos': ecos,  # Системная динамика устойчивого развития (Системная экология)
           'lifesafety': lifesafety,  # Безопасность жизнедеятельности
           'mcs': mcs,  # Естественнонаучная картина мира
           'hist_view': hist_view,  # История: 5 подходов к историческому развитию
           'hist': hist,  # История
           'rubscult': rubscult,  # Культура русской деловой речи
           'designbasics': designbasics,  # Основы дизайна
           'metr': metr,  # Основы метрологии, стандартизация и оценка соответствия
           'csharp': csharp,  # Программирование на C#
           'intpr': intpr,  # Управление интеллектуальной собственностью
           'edubase': edubase,  # Основы педагогической деятельности
           'psymedia': psymedia,  # Психология медиакоммуникаций цифровой эпохи
           'inclus_m2': inclus_m2,  # Развитие ресурсов организма (для лиц с ОВЗ)
           'smngm': smngm,  # Самоменеджмент
           'elecd': elecd,  # Электродинамика
           'sigproc': sigproc,  # Основы цифровой обработки сигналов
           'philosophy': philosophy,  # Философия
           'bioeco': bioeco,  # Основные концепции биологии и экологии
           'its': its,  # Информационные технологии и сервисы
           'ecoeff': ecoeff,  # Основы экономической эффективности производства
           'systeng': systeng,  # Практики системной инженерии
           'cellbio': cellbio,  # Введение в биологию клетки
           'introbe': introbe,  # Введение в биологию и экологию
           'crithink': crithink,  # Основы критического мышления
           'archc': archc,  # Основы архитектуры и строительных конструкций
           'philsci': philsci,  # Философия и методология науки
           'triz': triz,  # Теория решения изобретательских задач
           'prgrmm': prgrmm,  # Технологии программирования
           'nucmed': nucmed,  # Ядерная медицина
           'geom': geom,  # Начертательная геометрия и инженерная графика
           'engm': engm,  # Инженерная механика
           'datainf': datainf,  # Методы доступа к данным и информационного поиска
           'personalsafety': personalsafety,  # Личная безопасность
           'manegemach': manegemach,  # Управление машиностроительным предприятием
           'telecom': telecom,  # Беспроводные телекоммуникационные системы
           'legal': legal,  # Нормативно-правовое обеспечение онлайн-обучения
           }
