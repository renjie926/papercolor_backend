import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches  # 导入 patches
from color_3 import colors  # 导入颜色列表

# 数据
labels = ['A', 'B', 'C']

colors = [
    ['#FFBE7A', '#82B0D2', '#FA7F6F'],
    ['#EEEEEE', '#00ADB5', '#393E46'],
    ['#112D4E', '#3F72AF', '#DBE2EF'],
    ['#FFFBE9', '#E3CAA5', '#AD8B73'],
    ['#FFF5E4', '#FFD1D1', '#FF9494'],
    ['#8785A2', '#F6F6F6', '#FFC7C7'],  # 5
    ['#424874', '#A6B1E1', '#DCD6F7'],
    ['#EAEAEA', '#FF2E63', '#252A34'],
    ['#F9ED69', '#B83B5E', '#F08A5D'],
    ['#6A2C70', '#B83B5E', '#F08A5D'],
    ['#95E1D3', '#FCE38A', '#F38181'],  # 10
    ['#BBE1FA', '#3282B8', '#0F4C75'],
    ['#1B262C', '#3282B8', '#0F4C75'],
    ['#B7C4CF', '#EEE3CB', '#D7C0AE'],
    ['#967E76', '#EEE3CB', '#D7C0AE'],
    ['#A8D8EA', '#AA96DA', '#FCBAD3'],  # 15
    ['#FFB6B9', '#FAE3D9', '#BBDED6'],
    ['#6096B4', '#93BFCF', '#BDCDD6'],
    ['#6096B4', '#93BFCF', '#EEE9DA'],
    ['#61C0BF', '#FAE3D9', '#BBDED6'],
    ['#DDE6ED', '#9DB2BF', '#526D82'],  # 20
    ['#DDE6ED', '#526D82', '#27374D'],
    ['#BF9270', '#E3B7A0', '#FFEDDB'],
    ['#F1DEC9', '#C8B6A6', '#8D7B68'],
    ['#FCDEC0', '#E5B299', '#B4846C'],
    ['#E5B299', '#B4846C', '#7D5A50'],  # 25
    ['#3FC1C9', '#F5F5F5', '#FC5185'],
    ['#F8EDE3', '#BDD2B6', '#A2B29F'],
    ['#F8EDE3', '#A2B29F', '#798777'],
    ['#FCD1D1', '#ECE2E1', '#AEE1E1'],
    ['#FCD1D1', '#D3E0DC', '#AEE1E1'],  # 30
    ['#DEFCF9', '#CADEFC', '#CCA8E9'],
    ['#FFF8EA', '#9E7676', '#594545'],
    ['#E8DFCA', '#AEBDCA', '#7895B2'],
    ['#F5EFE6', '#AEBDCA', '#7895B2'],
    ['#DCD7C9', '#A27B5C', '#3F4E4F'],  # 35
    ['#DBA39A', '#F0DBDB', '#F5EBE0'],
    ['#F67280', '#C06C84', '#6C5B7B'],
    ['#F67280', '#C06C84', '#355C7D'],
    ['#EDF1D6', '#9DC08B', '#609966'],
    ['#EDF1D6', '#9DC08B', '#40513B'],  # 40
    ['#40514E', '#11999E', '#30E3CA'],
    ['#E4F9F5', '#11999E', '#30E3CA'],
    ['#A75D5D', '#F0997D', '#FFC3A1'],
    ['#FF9292', '#FFB4B4', '#FFE8E8'],
    ['#F2D7D9', '#D3CEDF', '#748DA6'],  # 45
    ['#D3CEDF', '#9CB4CC', '#748DA6'],
    ['#EAC7C7', '#A0C3D2', '#F7F5EB'],
    ['#F3DEBA', '#ABC4AA', '#675D50'],
    ['#D0C9C0', '#EFEAD8', '#6D8B74'],
    ['#ed6a5a', '#f4f1bb', '#9bc1bc'],  # 50
    ['#f4f1de', '#e07a5f', '#3d405b'],
    ['#233d4d', '#fe7f2d', '#fcca46'],
    ['#f79256', '#fbd1a2', '#7dcfb6'],
    ['#eee2df', '#eed7c5', '#c89f9c'],
    ['#f9dbbd', '#fca17d', '#da627d'], # 55
]

A = [0.6, 0.7, 0.65]
B = [0.6, 0.85, 0.6]
C = [0.65, 0.75, 0.8]

# 创建图形和子图
for idx, color_set in enumerate(colors):
    fig, axs = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [6, 1]})

    # 第一子图：柱状图
    x = np.arange(len(labels))  # 横轴位置
    y = np.round(np.arange(0, 1.1, 0.1), 1)

    width = 0.25  # 柱的宽度

    # 绘制柱状图
    axs[0].bar(x - width, A, width, label='Model A', color=color_set[0])
    axs[0].bar(x, B, width, label='Model B', color=color_set[1])
    axs[0].bar(x + width, C, width, label='Model C', color=color_set[2])

    # 添加标签、标题和自定义x轴刻度
    axs[0].set_ylabel('Example', fontsize=30)
    axs[0].set_yticks(y)
    axs[0].set_yticklabels(y, fontsize=30)
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(labels, fontsize=30)
    axs[0].legend(fontsize=25)

    # 设置网格线
    axs[0].grid(True, zorder=0)  # 设置网格线，zorder=0 使其在底部
    axs[0].set_axisbelow(True)    # 确保网格在所有元素之下

    # 添加数值标签
    def add_labels(rects):
        for rect in rects:
            height = rect.get_height()
            axs[0].annotate(f'{height:.2f}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=25)

    add_labels(axs[0].containers[0])  # A
    add_labels(axs[0].containers[1])  # B
    add_labels(axs[0].containers[2])  # C

    # 第二子图：颜色块
    # 第二子图：颜色块
    for i, (color, label) in enumerate(zip(color_set, labels)):
        rect = mpatches.Rectangle((i * 1 + 0.25, 0), 0.6, 1, color=color)  # 绘制颜色块
        axs[1].add_patch(rect)
        axs[1].annotate(color, xy=(i * 1 + 0.28, 0.45), fontsize=35, ha='left', va='center')  # 添加标签

    axs[1].set_xlim(0, len(labels))  # 设置x轴范围，使用标签数量
    axs[1].set_ylim(0, 1)  # 设置y轴范围
    axs[1].axis('off')  # 关闭第二个子图的坐标轴
    # 保存图像
    plt.tight_layout()  # 调整子图布局
    plt.savefig(f'A:/项目图片/柱状图/{idx + 1}.jpg', dpi=400)  # 保存图像，按序号
    plt.close(fig)  # 关闭图形，避免显示
