# @Time : 2024/10/30
# @Auth : renjie926@foxmail.com 
# @File : test_chartbar.py  
# @IDE : PyCharm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches  # 导入 patches
from color_3 import colors  # 导入颜色列表

# 数据
labels = ['A', 'B', 'C']
colors = [
    ['#f9dbbd', '#fca17d', '#da627d'],
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
    axs[0].set_axisbelow(True)  # 确保网格在所有元素之下


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
    plt.show()
    # plt.savefig(f'A:/项目图片/柱状图/{idx + 1}.jpg', dpi=400)  # 保存图像，按序号
    plt.close(fig)  # 关闭图形，避免显示
