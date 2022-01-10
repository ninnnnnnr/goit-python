from django.db import models


class Income(models.Model):
    cash_income = models.DecimalField('Доход', max_digits=50, decimal_places=2)
    INCOME_CATEGORIES = (
        ('zp', 'Зарплата'),
        ('bs', 'Бизнес'),
        ('dr', 'Другое'),
    )
    categories = models.CharField('Категория', max_length=3, choices=INCOME_CATEGORIES, default='dr')
    comment = models.CharField('Комментарий', max_length=130, blank=True)
    pub_date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']


class Costs(models.Model):
    cash_out = models.DecimalField('Расход', max_digits=50, decimal_places=2)
    OUTCOME_CATEGORIES = (
        ('av', 'Автомобиль'),
        ('dm', 'Дом'),
        ('zd', 'Здоровье'),
        ('ls', 'Личные расходы'),
        ('od', 'Одежда'),
        ('pt', 'Питание'),
        ('pd', 'Подарки'),
        ('sr', 'Семейные расходы'),
        ('tx', 'Техника'),
        ('us', 'Услуги'),
    )
    categories = models.CharField('Категория', max_length=3, choices=OUTCOME_CATEGORIES, default='ls')
    comment = models.CharField('Комментарий', max_length=130, blank=True)
    pub_date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']


