from django.db import models


# Create your models here.
class DataFullstack(models.Model):
    year = models.CharField('Год', max_length=4)
    average_salary = models.CharField('Средняя зарплата', max_length=8)
    profession_average_salary = models.CharField('Средняя зарплата - Fullstack-программист', max_length=8)
    vacancy_count = models.CharField('Количество вакансий', max_length=8)
    profession_vacancy_count = models.CharField('Количество вакансий - Fullstack-программист', max_length=8)

    def str(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Статистика по профессии'
        verbose_name_plural = 'Статистики по профессии'
