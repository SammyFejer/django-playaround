
from asyncio.windows_events import NULL
import csv
from django.core.management import BaseCommand
from MyApp1.models import teacher
from MyApp1.models import teacher 
from MyApp1.models import CourseArea 
from MyApp1.models import subCourse
from MyApp1.models import Unit
from MyApp1.models import Assessment
from django.shortcuts import get_object_or_404





class Command(BaseCommand):
    help = ' this is help text'

    def add_arguments(self, parser):
        parser.add_argument("--path", type = str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, 'rt', encoding='utf-8-sig') as f:
            reader = csv.reader(f, dialect='excel')

            for row in reader:
                
                # obj = subCourse.objects.get()
                # courseName = obj.courseTitle
                

                latestThing = subCourse.objects.order_by('-id').first()
                course_area_instance = get_object_or_404(CourseArea, pk=1)
                print(latestThing)
                print(row[1])
                
                if str(latestThing) != str(row[1]):
                    subCourse.objects.create(courseTitle=row[1], coursearea = course_area_instance)
                    latestThing = subCourse.objects.order_by('-id').first()
                    Unit.objects.create(course=latestThing,  UnitName=row[2], Accreditation=row[3],UnitDescription = row[4], UnitGoals = row[5], ContentDescriptions = row[5])
                else:
                
                    latestThing = subCourse.objects.order_by('-id').first()
                   
                    Unit.objects.create(course=latestThing,  UnitName=row[2], Accreditation=row[3],UnitDescription = row[4], UnitGoals = row[5], ContentDescriptions = row[5])
                # print ('Added' + row[1] + row[2]) 
                

