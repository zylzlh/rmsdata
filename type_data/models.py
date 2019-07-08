from django.db import models
from data_platform.models import acmodel

# Create your models here.
#ATA章节号
class ata(models.Model):
    id = models.AutoField(primary_key = True)
    chapter = models.DecimalField("章", max_digits=2, decimal_places=0)
    section = models.DecimalField("节", max_digits=2, decimal_places=0)
    subject = models.DecimalField("题", max_digits=2, decimal_places=0)
    title = models.CharField("系统名称", max_length = 100)
    zh_title = models.CharField("系统名称(中)", max_length = 100)

    class Meta:
        ordering = ('chapter',)
        verbose_name = 'ATA章节号'
        verbose_name_plural = 'ATA章节号'

    def __str__(self):
        return (self.zh_title)


#航空器基本信息
class ac(models.Model):
    id = models.AutoField(primary_key = True)
    tail_number = models.CharField("注册号", max_length = 100)
    acmodel = models.ForeignKey(acmodel, related_name='ac_acmodel', on_delete = models.CASCADE)

    class Meta:
        ordering = ('tail_number',)
        verbose_name = '航空器注册信息'
        verbose_name_plural = '航空器注册信息'

    def __str__(self):
        return (self.tail_number)

#发动机基本信息
class engine_info(models.Model):
    id = models.AutoField(primary_key = True)
    en_model = models.CharField("发动机型号", max_length = 100)
    en_sn = models.CharField("发动机序号", max_length = 100)
    ac = models.ForeignKey(ac, related_name='engine_info_ac', on_delete = models.CASCADE)

    class Meta:
        ordering = ('en_model',)
        verbose_name = '发动机信息'
        verbose_name_plural = '发动机信息'

    def __str__(self):
        return (self.en_sn)

#飞行时间,即航空器基本信息
class flytime(models.Model):
    id = models.AutoField(primary_key = True)
    ac = models.ForeignKey(ac, related_name='flytime_ac', on_delete = models.CASCADE)
    ana = models.DecimalField("可用架日", max_digits=2, decimal_places=0)
    mth = models.DecimalField("月飞行时间", max_digits=6, decimal_places=2)
    mtc = models.DecimalField("月起落架次", max_digits=6, decimal_places=0)
    mdf = models.DecimalField("月营运飞行时间", max_digits=6, decimal_places=2)
    mdr = models.DecimalField("月营运起落架次", max_digits=6, decimal_places=0)
    cth = models.FloatField("总飞行时间")
    cty = models.FloatField("总起落架次")
    date = models.DateField("发生时间")
    mfr = models.CharField("制造商", max_length = 100)

    def __str__(self):
        return (self.ac)

#发动机时间
class entime(models.Model):
    id = models.AutoField(primary_key = True)
    en_sn = models.ForeignKey(engine_info, related_name='engine_info_time', on_delete=models.CASCADE)
    epc = models.CharField("装机位置", max_length=4)
    meth = models.DecimalField("月使用时间", max_digits=6, decimal_places=2)
    metc = models.DecimalField("月使用循环", max_digits=6, decimal_places=0)
    if_overhaul = models.BooleanField(default = False)
    eth_aoh = models.DecimalField("修后使用时间", max_digits=6, decimal_places=2)
    etc_aoh = models.DecimalField("修后使用循环", max_digits=6, decimal_places=0)
    ceth = models.FloatField("总使用时间")
    cetc = models.FloatField("总使用循环")
    re_date = models.DateField("记录时间")
    remove_reson = models.TextField("拆换原因")
    maintance = models.TextField("维修")
    maintance_range = models.TextField("工作范围")

    def __str__(self):
        return (self.entime)

#APU时间
class aputime(models.Model):
    id = models.AutoField(primary_key = True)
    apu_pn = models.CharField("APU件号", max_length = 20)
    meth = models.DecimalField("月使用时间", max_digits=6, decimal_places=2)
    metc = models.DecimalField("月使用循环", max_digits=6, decimal_places=0)
    ceth = models.FloatField("总使用时间")
    cetc = models.FloatField("总使用循环")
    csr = models.DecimalField("计划拆换数", max_digits = 6, decimal_places = 0)
    cuc = models.DecimalField("非计划拆换数", max_digits = 6, decimal_places = 0)
    re_date = models.DateField("记录时间")

    def __str__(self):
        return (self.apu_pn)

#故障模式库
class fm(models.Model):
    id = models.AutoField(primary_key = True)
    acmodel = models.ForeignKey(acmodel, related_name='fm_acmodels', on_delete = models.CASCADE, default = 1)
    fm = models.TextField("故障模式")
    ata = models.ForeignKey(ata, related_name = 'ata_fm', on_delete = models.CASCADE)
    fe = models.TextField("故障影响")
    ru = models.TextField("故障原因")
    re = models.TextField("解决措施")

    class Meta:
        ordering = ('fm',)
        verbose_name = '故障模式库'
        verbose_name_plural = '故障模式库'

    def __str__(self):
        return (self.fm)
