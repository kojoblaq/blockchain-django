from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from fairwages.models import gradeStructure
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'



ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from grade_data.csv into our Grade Structure"

    def handle(self, *args, **options):
        if  gradeStructure.objects.exists():
            print('grade data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        
        print("Loading grade data for institutions available")
        for row in DictReader(open('./grade_data.csv')):
            grade = gradeStructure()
            grade.inst_name = row['INSTITUTION']
            grade.job_title = row['JOB TITLE']
            grade.ss_grade = row['SS GRADE']
            grade.level = row['Level']
            grade.creator = row['creator']
            grade.wage = row['wage']
            raw_submission_date = row['Date']
            submission_date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            grade.submission_date = submission_date
            grade.save()
            
            
            
