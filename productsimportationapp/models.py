from django.db import models


class ProductsImportationHistory(models.Model):
    is_connection_good = models.BooleanField(default=True, verbose_name='connection')
    last_time_cron_ran = models.DateTimeField(auto_now_add=True, verbose_name='last time cron ran')
    time_online = models.CharField(max_length=50, verbose_name='time online')
    memory_usage = models.CharField(max_length=200, verbose_name='memory usage')

    def __str__(self):
        return f'{self.last_time_cron_ran}, {self.time_online} - {self.memory_usage}'

    class Meta:
        verbose_name = 'Product Importation History'
        verbose_name_plural = 'Products Importation History'
