# @Time : 2024/10/12
# @Auth : renjie926@foxmail.com 
# @File : forms.py  
# @IDE : PyCharm
# paper_app/forms.py
from django import forms
from .models import PaperType, ChartType, Entry
class PaperTypeForm(forms.ModelForm):
    class Meta:
        model = PaperType
        fields = ['type']  # 你希望在表单中使用的字段


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FileFieldForm(forms.Form):
    file_field = MultipleFileField()


class ChartEntryForm(forms.ModelForm):
    image = MultipleFileField()
    class Meta:
        model = Entry
        fields = ['paper_type', 'chart_type', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 检查是否选择了 paper_type 来动态过滤 chart_type
        if 'paper_type' in self.data:
            try:
                paper_type_id = int(self.data.get('paper_type'))
                # 根据选中的 paper_type 过滤出关联的 chart_type
                self.fields['chart_type'].queryset = ChartType.objects.filter(paper_type_id=paper_type_id)
            except (ValueError, TypeError):
                self.fields['chart_type'].queryset = ChartType.objects.none()  # 没有paper_type选择时，不显示chart_type
        elif self.instance.pk:
            # 如果正在编辑已有实例，则显示与实例的 paper_type 相关的 chart_type
            self.fields['chart_type'].queryset = self.instance.paper_type.chart_types.all()
        else:
            # 初始表单加载时，默认不显示任何 chart_type
            self.fields['chart_type'].queryset = ChartType.objects.none()
