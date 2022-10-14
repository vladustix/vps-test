from django.db import models


class Server(models.Model):
    uid = models.AutoField(primary_key=True, verbose_name="Идентификатор")
    cpu = models.IntegerField(blank=True, null=False, verbose_name="Количество ядер")
    ram = models.IntegerField(blank=True, null=False, verbose_name="Объем RAM (МБ)")
    hdd = models.IntegerField(blank=True, null=False, verbose_name="Объем HDD (ГБ)")
    STATUS = (
        ("started", "Запущен"),
        ("blocked", "Заблокирован"),
        ("stopped", "Остановлен")
    )
    status = models.CharField(max_length=32, choices=STATUS, default="started", verbose_name="Статус сервера")

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"

    def str(self):
        return self.uid
