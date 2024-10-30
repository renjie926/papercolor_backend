from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PaperType, Entry
from django.shortcuts import render, redirect,get_object_or_404
from .forms import PaperTypeForm
from .models import ChartType
# 提供一个 JSON 接口，返回所有论文类型的数据，适用于前端异步请求。
def get_paper_types(request):
    paper_types = PaperType.objects.all()
    types_list = [{"id": paper.id, "type": paper.type} for paper in paper_types]
    return JsonResponse({"types": types_list})
# 返回某个论文类型下的所有图种类
# def get_chart_types(request, paper_type_id):
#     paper_type = PaperType.objects.get(id=paper_type_id)
#     chart_types = paper_type.chart_types.all()  # 获取该论文类型下的所有图种类
#     data = {
#         'paper_type': paper_type.type,
#         'chart_types': list(chart_types.values('id', 'name'))  # 返回图种类名称和 ID
#     }
#     return JsonResponse(data)

def get_chart_types(request):
    chart_types = ChartType.objects.all()
    data = [{"id": chart.id, "name": chart.name, "paper_type": chart.paper_type.type} for chart in chart_types]
    return JsonResponse({"chart_types": data})


def get_chart_types_by_paper_type(request, paper_type):
    # 根据 paper_type 过滤 chart_types
    chart_types = ChartType.objects.filter(paper_type=paper_type).values('id', 'name', 'paper_type')
    return JsonResponse({'chart_types': list(chart_types)})


def get_entries(request):
    entries = Entry.objects.all()
    data = []

    for entry in entries:
        data.append({
            "paper_type": entry.paper_type.id,  # 假设 paper_type 模型有 `type` 属性
            "chart_type": entry.chart_type.name,
            "image_url": entry.image.url,  # 返回图片的URL
            "color_count": entry.color_count,
        })

    return JsonResponse({"entries": data})


def get_entries_by_paper_type(request, paper_type_id):
    # 根据 paper_type_id 过滤 Entries
    entries = Entry.objects.filter(paper_type_id=paper_type_id)
    data = []

    for entry in entries:
        data.append({
            "chart_type": entry.chart_type.name,
            "image_url": entry.image.url  # 获取图片的URL
        })

    return JsonResponse({'entries': data})


