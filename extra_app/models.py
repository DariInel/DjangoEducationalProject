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
        verbose_name_plural = 'Статистик по профессии'


class SalaryLevel(models.Model):
    city = models.CharField('Город', max_length=15)
    level_salary = models.CharField('Уровень зарплат', max_length=8)

    def str(self):
        return str(self.city)

    class Meta:
        verbose_name = 'Статистика по уровню зарплат'
        verbose_name_plural = 'Статистик по уровню зарплат'


class SalaryPart(models.Model):
    city = models.CharField('Город', max_length=15)
    part_salary = models.CharField('Уровень зарплат', max_length=8)

    def str(self):
        return str(self.city)

    class Meta:
        verbose_name = 'Статистика по доле вакансий'
        verbose_name_plural = 'Статистик по доле вакансий'


class TopSkills(models.Model):
    year = models.CharField('Год', max_length=15)
    list_skills = models.CharField('Топ-10 навыков', max_length=150)

    def str(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Топ-10 навыков'
        verbose_name_plural = 'Топ-10 навыков по годам'
