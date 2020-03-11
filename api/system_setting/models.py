from django.db import models

# Create your models here.

class SystemSetting(models.Model):
    """
    系统设定
    """
    code = models.CharField(verbose_name="代码", max_length=20)
    title = models.CharField(verbose_name="标题", max_length=20)
    content = models.CharField(verbose_name="内容", max_length=100)
    url = models.CharField(verbose_name="链接", max_length=100, null=True)
    note = models.CharField(verbose_name="备注", max_length=100, null=True)

    class Meta:
        verbose_name = "系统设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code