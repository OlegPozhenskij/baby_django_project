from django.db import models


# Create your models here.

class StatusName(models.Model):
    status_name = models.CharField(max_length=200,  verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    # дочернее поле выступающее в роли ключа(род класс, принцип удаления)
    # Protect - запрещает удалять элементы полей
    # Cascade - при удалении родителя удаляются все потомки
    # null - нужен для одобрения пустоты в BD
    # blank - нужен для пустоты в полях админ панели (так как у нас уже есть значения в BD)
    order_status = models.ForeignKey(StatusName, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'




