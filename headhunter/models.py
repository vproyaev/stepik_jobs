from django.db import models


# import stepik_hh.data as db


class Specialty(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.URLField()


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.URLField()
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    specialty_id = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='specialty', default=None,
                                     null=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company', default=None, null=True)
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField()

# for spec in db.specialties:
#     Specialty.objects.create(
#         code=spec['code'],
#         title=spec['title'],
#         picture=''
#     )

# for company in db.companies:
#     Company.objects.create(name=company['title'],
#                            location=company['location'],
#                            logo=company['logo'],
#                            description=company['description'],
#                            employee_count=company['employee_count']
#                            )

# for job in db.jobs:
#     Vacancy.objects.create(
#         title=job['title'],
#         specialty_id=Specialty.objects.get(code=job["specialty"]),
#         company_id=Company.objects.get(id=job['company']),
#         skills=job['skills'],
#         description=job['description'],
#         salary_max=job['salary_to'],
#         salary_min=job['salary_from'],
#         published_at=job['posted']
#     )
