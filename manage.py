#!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octopus_bi_project.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()
import pandas as pd
from data_visualizer.models import School, Class,Assessment_Areas,Student,Answers,Awards,Subject,Summary

def load_data():
    # Load data from CSVs into the tables
    data1 = pd.read_csv('D:\AAA SEMESTER 04\Interview_dataset\Ganison_dataset/Ganison_dataset_1.csv')
    data2 = pd.read_csv('D:\Django project\Interview_dataset\Ganison_dataset/Ganison_dataset_2.csv')
    data3 = pd.read_csv('D:\Django project\Interview_dataset\Ganison_dataset/Ganison_dataset_3.csv')
    data4 = pd.read_csv('D:\Django project\Interview_dataset\Ganison_dataset/Ganison_dataset_4.csv')
    data5 = pd.read_csv('D:\Django project\Interview_dataset\Ganison_dataset/Ganison_dataset_5.csv')
    data6 = pd.read_csv('D:\Django project\Interview_dataset\Ganison_dataset/Ganison_dataset_6.csv')


    for index, row in data1.iterrows():
        School.objects.create(column1=row['Id'], column2=row['Name'])

    for index, row in data2.iterrows():
        Class.objects.create(column1=row['Id'], column2=row['Class'])

    for index, row in data3.iterrows():
        Assessment_Areas.objects.create(column1=row['Id'], column2=row['Name'])

    for index, row in data4.iterrows():
        Student.objects.create(column1=row['Id'], column2=row['Fullname'])

    for index, row in data5.iterrows():
        Answers.objects.create(column1=row['Id'], column2=row['Answers'])

    for index, row in data6.iterrows():
        Awards.objects.create(column1=row['Id'], column2=row['Awards']) 

    for index, row in data6.iterrows():
        Subject.objects.create(column1=row['Id'], column2=row['Subject'], column2=row['Subject_Score'])   
