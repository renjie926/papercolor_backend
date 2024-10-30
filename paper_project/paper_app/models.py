from django.db import models

# Create your models here.
from django.db import models

class PaperType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type


# 图的种类模型
class ChartType(models.Model):
    paper_type = models.ForeignKey(PaperType, related_name='chart_types', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # 图种类，如 "柱形图", "散点图"

    def __str__(self):
        return self.name

# class Entry(models.Model):
#     paper_type = models.ForeignKey(PaperType, related_name='entries', on_delete=models.CASCADE)
#     chart_type = models.ForeignKey(ChartType, related_name='entries', on_delete=models.CASCADE)  # 关联到图类型
#     image = models.ImageField(upload_to='examples/')  # 用来存储相应的例图
#     color_count = models.PositiveIntegerField(default=1)
#     def __str__(self):
#         return f"{self.paper_type} - {self.chart_type.name} - Colors: {self.color_count}"

class Entry(models.Model):
    paper_type = models.ForeignKey(PaperType, related_name='entries', on_delete=models.CASCADE)
    chart_type = models.ForeignKey(ChartType, related_name='entries', on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='examples/')  # 用来存储相应的例图
    # 关联到图类型
    color_count = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.paper_type} - {self.chart_type.name} - Colors: {self.color_count}"

class ImageEntry(models.Model):
    entry = models.ForeignKey(Entry, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='examples/')  # 用来存储相应的例图

    def __str__(self):
        return f"Image for {self.entry}"