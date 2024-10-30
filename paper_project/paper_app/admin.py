from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PaperType, Entry
from django.contrib import admin
from .models import PaperType, ChartType, ImageEntry
from django import forms
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect

class PaperTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


class EntryAdmin(admin.ModelAdmin):
    list_display = ('paper_type', 'chart_type', 'image')

class ChartTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'paper_type']  # 显示图的名称和所属论文类型
    list_filter = ['paper_type']  # 增加过滤器，方便按论文类型过滤
    ordering = ['paper_type', 'name']  # 按 paper_type 和 name 排序
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 获取 paper_type 参数
        paper_type_id = self.data.get('paper_type') or self.initial.get('paper_type')
        print('paper_type_id', paper_type_id)
        if paper_type_id:
            # 根据 paper_type_id 过滤 chart_type 选择
            self.fields['chart_type'].queryset = ChartType.objects.filter(paper_type_id=paper_type_id)
        else:
            # 默认显示所有 ChartType
            self.fields['chart_type'].queryset = ChartType.objects.none()  # 空查询集
# class EntryAdmin(admin.ModelAdmin):
#     form = EntryForm
#     list_display = ('paper_type', 'chart_type', 'image', 'color_count')  # 显示字段
#     list_filter = ('paper_type', 'chart_type', 'color_count')  # 根据需要过滤的字段
#
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         # 在这里将 paper_type 参数传递给表单
#         if 'paper_type' in request.GET:
#             form.initial['paper_type'] = request.GET['paper_type']
#         return form

class ImageEntryInline(admin.TabularInline):
    model = ImageEntry
    extra = 1  # 提供一个额外的空行来上传图片

class EntryAdmin(admin.ModelAdmin):
    inlines = [ImageEntryInline]  # 将 ImageEntry 作为内联表单显示在 Entry 中
    form = EntryForm
    list_display = ('paper_type', 'chart_type', 'color_count')  # 显示字段
    list_filter = ('paper_type', 'chart_type', 'color_count')  # 根据需要过滤的字段

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # 在这里将 paper_type 参数传递给表单
        if 'paper_type' in request.GET:
            form.initial['paper_type'] = request.GET['paper_type']
        return form




# 注册 admin 类
admin.site.register(ImageEntry)
admin.site.register(Entry, EntryAdmin)
admin.site.register(PaperType, PaperTypeAdmin)
admin.site.register(ChartType, ChartTypeAdmin)