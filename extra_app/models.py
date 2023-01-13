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
        verbose_name_plural = 'Статистика по профессии'


class SalaryLevel(models.Model):
    city = models.CharField('Город', max_length=15)
    level_salary = models.CharField('Уровень зарплат', max_length=8)

    def str(self):
        return str(self.city)

    class Meta:
        verbose_name = 'Статистика по уровню зарплат'
        verbose_name_plural = 'Статистика по уровню зарплат'


class SalaryPart(models.Model):
    city = models.CharField('Город', max_length=15)
    part_salary = models.CharField('Уровень зарплат', max_length=8)

    def str(self):
        return str(self.city)

    class Meta:
        verbose_name = 'Статистика по доле вакансий'
        verbose_name_plural = 'Статистика по доле вакансий'


class TopSkills2015(models.Model):
    skill = models.CharField('Навык', max_length=30)
    count = models.CharField('Количество', max_length=150)

    def str(self):
        return str(self.skill)

    class Meta:
        verbose_name = 'Топ-10 навыков за 2015 год'
        verbose_name_plural = 'Топ-10 навыков за 2015 год'


class TopSkills2016(models.Model):
    skill = models.CharField('Навык', max_length=30)
    count = models.CharField('Количество', max_length=150)

    def str(self):
        return str(self.skill)

    class Meta:
        verbose_name = 'Топ-10 навыков за 2016 год'
        verbose_name_plural = 'Топ-10 навыков за 2016 год'


class TopSkills2017(models.Model):
    skill = models.CharField('Навык', max_length=30)
    count = models.CharField('Количество', max_length=150)

    def str(self):
        return str(self.skill)

    class Meta:
        verbose_name = 'Топ-10 навыков за 2017 год'
        verbose_name_plural = 'Топ-10 навыков за 2017 год'


class TopSkills2018(models.Model):
    skill = models.CharField('Навык', max_length=30)
    count = models.CharField('Количество', max_length=150)

    def str(self):
        return str(self.skill)

    class Meta:
        verbose_name = 'Топ-10 навыков за 2018 год'
        verbose_name_plural = 'Топ-10 навыков за 2018 год'


class TopSkills2019(models.Model):
    skill = models.CharField('Навык', max_length=30)
    count = models.CharField('Количество', max_length=150)

    def str(self):
        return str(self.skill)

    class Meta:
        verbose_name = 'Топ-10 навыков за 2019 год'
        verbose_name_plural = 'Топ-10 навыков за 2019 год'


class TopSkills2020(models.Model):
    skill = models.CharField('Навык', max_length=30)
    count = models.CharField('Количество', max_length=150)

    def str(self):
        return str(self.skill)

    class Meta:
        verbose_name = 'Топ-10 навыков за 2020 год'
        verbose_name_plural = 'Топ-10 навыков за 2020 год'


class TopSkills2021(models.Model):
    skill = models.CharField('Навык', max_length=30)
    count = models.CharField('Количество', max_length=150)

    def str(self):
        return str(self.skill)

    class Meta:
        verbose_name = 'Топ-10 навыков за 2021 год'
        verbose_name_plural = 'Топ-10 навыков за 2021 год'


class TopSkills2022(models.Model):
    skill = models.CharField('Навык', max_length=30)
    count = models.CharField('Количество', max_length=150)

    def str(self):
        return str(self.skill)

    class Meta:
        verbose_name = 'Топ-10 навыков за 2022 год'
        verbose_name_plural = 'Топ-10 навыков за 2022 год'