# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import random
# import secrets
# # subject_dic = {"Physics": "Phy_teacher", "Chemistry": "Che_teacher", "Maths": "Mat_teacher", "Biology": "Bio_teacher"}
# # # Phy_teacher = ["mr Dada"]
# # # Che_teacher = ["mr Kolapo", "mr Dada"]
# # # Mat_teacher = ["Mrs Agness", "Mr Kolapo"]
# # # Bio_teacher = ["mr Paul"]
# #
# # teacher_dic = {"Phy_teacher": "mr Dada",
# #     "Che_teacher": ["mr Kolapo", "mr Dada"],
# #     "Mat_teacher": ["Mrs Agness", "Mr Kolapo"],
# #     "Bio_teacher": "Mr Paul"}
# #
# # for i in  subject_dic:
# #     for k in teacher_dic:
# #         time_table = {i: k}
# #         print(time_table)
#
# subject = {
#               "Physics": "mr Dada",
#           "Chemistry": ["mr Kolapo"],
#           "Chemistry": ["mr Dada"],
#           "Maths": "Mrs Agness",
#           "Maths": "Mr Kolapo",
#           "Biology": "mr Paul"}
# time_table_1 = random.choice(subject.popitem())
# subject_2 = subject
# time_table_2 = subject_2.popitem()
# subject_3 = subject_2
# time_table_3 = subject_3.popitem()
# subject_4 = subject_3
# time_table_4 = subject_4.popitem()
# # time_table_2 = subject.popitem()
# # time_table_3 = subject.popitem()
# print(time_table_1, time_table_2, time_table_3, time_table_4)
# # subject, teacher = random.choice(list(subject_teacher.items()))
# # time_table = []
# #
# # time_table += (subject, teacher)
# #
# # print(time_table)
#
# # if __name__ == '__main__':
# #     subject = d.items()
# #     random.shuffle(subject)
# # for key, value in subject:
# #     print(key, value)
# # key = random.choice(list(subject))
# # print("Subject: ", key, ",  " "Teacher: ", subject[key])
#
# # Phy_teacher = ["mr Dada"]
# # Che_teacher = ["mr Kolapo", "mr Dada"]
# # Mat_teacher = ["Mrs Agness", "Mr Kolapo"]
# # Bio_teacher = ["mr Paul"]
#
# # for i in subject:
# #     time_table = random.)
# #     print(time_table)
# # time_table = []
# # for i in subject:
# #     time_table.append(random.sample(subject))
#
# # print(time_table)
#
# # import random
# #
# # weight_dict = {
# #     "Kelly": 50,
# #     "Red": [68, 78],
# #     "Scott": 70,
# #     "Emma": 40
# # }
# # # random key
# # key = random.choice(list(weight_dict))
# # # fetch value using key name
# # print("Random key-value pair is ", key, ":", weight_dict[key])
# # # Output Random key-value pair is  Red : 68

# def Cloning(subject_to_study):
#     subject_to_study_copy = subject_to_study[:]
#     return subject_to_study_copy


# subject_to_study_copy_new = Cloning(subject_to_study)


import random

subject_to_study = []
subject_teacher = []


def input_subject():
    insert_subjects = input("type subject one by one:  ")
    subject_to_study.append(insert_subjects)
    insert_subject_teacher = input("teachers name according to subject:  ")
    subject_teacher.append(insert_subject_teacher)


no_of_subject = input("number of subject")
subjects_in_timetable = int(no_of_subject)
i = 1
while i < subjects_in_timetable:
    input_subject()
    if i == subjects_in_timetable:
        break
    i += 1
input_subject()

subject_per_day = int(input("number of subject per day:  "))




def daily_time_table():
    subjec_list = []
    teacher_list = []
    for i in subject_to_study:
        subjec_list = random.sample(subject_to_study, subject_per_day)
    for k in subjec_list:
        teacher_table_populate = subject_teacher[subject_to_study.index(k)]
        teacher_list.append(teacher_table_populate)
    time_table = list(zip(subjec_list, teacher_list))

    print(time_table)

# print(subject_to_study)
# print(time_table)
# print(teacher_table)


monday = daily_time_table()

teusday = daily_time_table()

wednesday = daily_time_table()

thursday = daily_time_table()

friday = daily_time_table()

print(monday)