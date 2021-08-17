from headhunter.models import Company, Specialty, Vacancy

companies = Company.objects.all()
specialty = Specialty.objects.all()
vac_spec = Vacancy.objects.all()

print(companies)