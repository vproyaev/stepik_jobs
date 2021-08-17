from collections import defaultdict

from django.http import Http404, HttpResponseNotFound
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from headhunter.models import Company, Specialty, Vacancy


class MainView(TemplateView):
    name = 'main'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        companies = Company.objects.all()
        specialty = Specialty.objects.all()
        jobs = Vacancy.objects.all()

        jobs_specialty = {i.code: 0 for i in specialty}

        for i in jobs_specialty.keys():
            jobs_specialty[i] = [jobs.filter(specialty_id=Specialty.objects.get(code=i)).count(), specialty.get(code=i)]

        context = {
            'companies': companies,
            'specialty': specialty,
            'jb': jobs_specialty,
        }
        return context


class VacanciesView(TemplateView):
    name = 'vacancies'
    template_name = 'vacancies.html'

    def get_context_data(self, **kwargs):
        context = super(VacanciesView, self).get_context_data(**kwargs)

        vacancies_if = [i for i in context.values()]
        vacancies = Vacancy.objects.all()
        if len(vacancies_if) > 1:
            vacancy_filter = vacancies.filter(specialty_id=Specialty.objects.get(code=vacancies_if[0]))
        else:
            vacancy_filter = [0]

        context = {
            'vacancies_if': vacancies_if,
            'vacancies_all': vacancies.count(),
            'vacancies_list': vacancies,
            'vacancy_filter': vacancy_filter,
        }

        return context


class CompanyView(TemplateView):
    name = 'company'
    template_name = 'company.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)

        company = [i for i in context.items()]
        company_vacancies = Vacancy.objects.filter(company_id=company[0][1])
        company = Company.objects.get(id=company[0][1])

        context = {
            'company': company,
            'company_count': company_vacancies.count(),
            'company_vacancies': company_vacancies,
        }

        return context


class VacancyView(TemplateView):
    name = 'vacancy'
    template_name = 'vacancy.html'

    def get_context_data(self, **kwargs):
        context = super(VacancyView, self).get_context_data(**kwargs)

        vacancy = [i for i in context.items()]
        company = Vacancy.objects.get(id=vacancy[0][1])
        company = Company.objects.get(id=company.company_id_id)
        vacancy = Vacancy.objects.filter(id=vacancy[0][1])

        context = {
            'vacancy': vacancy,
            'company': company,
        }

        return context


# class VacancyReply(View):
#     info = defaultdict(list)
#
#     def post(self, request, *args, **kwargs):
#         user_name = request.user.userName if request.user else 'Anonymos'
#         user_phone = request.user.userPhone if request.user else ''
#         user_message = request.user.userMsg if request.user else ''
#         reply = request.POST.get('reply_vacancy')
#
#         self.info[user_name].append(reply)
#         self.info[user_phone].append(reply)
#         self.info[user_message].append(reply)
#         return redirect('/')


def custom404(request, exception):
    return Http404('Похоже вы что-то напутали. Лучше вернитесь на главную страницу!')


def custom500(request):
    return HttpResponseNotFound('У-уупс. Вы что-то неправильно ввели в адресной строке. Больше так не играйтесь =)')


def custom503(request):
    return HttpResponseNotFound('Что-то HEROKU мудрит. Подождите пожалуйста =)')
