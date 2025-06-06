import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import get_cmap

# 设置字体和期刊发表样式
matplotlib.rcParams['font.family'] = 'Arial'  
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.size'] = 14

# 通用函数：设置期刊发表风格的刻度线样式
def set_publication_style(ax):
    # 设置主刻度线粗细
    ax.tick_params(axis='both', which='major', width=2, length=6, pad=6, labelsize=14)
    # 设置次刻度线粗细（如果有的话）
    ax.tick_params(axis='both', which='minor', width=1.5, length=4)
    # 设置坐标轴线条粗细
    for spine in ax.spines.values():
        spine.set_linewidth(2)
    return ax

# 读取数据
df = pd.read_excel('data/pareto_solutions_ranked.xlsx')

# ================= 图1: 优化的热图可视化 =================
print("正在生成热图...")

# 创建相关性矩阵
conc_cols = ['AMP_conc', 'QK_conc', 'YIGSR_conc', 'BMP2_conc']
perf_cols = ['AMP', 'ALP', 'LW', 'CellNum']

correlation_matrix = pd.DataFrame(index=conc_cols, columns=perf_cols)
for conc in conc_cols:
    for perf in perf_cols:
        corr_value = df[conc].corr(df[perf])
        if pd.isna(corr_value):
            corr_value = 0.0
        correlation_matrix.loc[conc, perf] = float(corr_value)

correlation_matrix = correlation_matrix.astype(float)

# 热图可视化 - 使用更适合期刊的颜色方案
plt.figure(figsize=(10, 8))

# 方案1: 蓝-白-红经典科学配色（推荐用于相关性）
# colors_scheme1 = ["#2166ac", "#67a9cf", "#d1e5f0", "#f7f7f7", "#fddbc7", "#ef8a62", "#b2182b"]
# cmap1 = LinearSegmentedColormap.from_list("scientific_diverging", colors_scheme1, N=256)

# 方案2: 紫-白-橙配色（现代期刊常用）
# colors_scheme2 = ["#762a83", "#af8dc3", "#e7d4e8", "#f7f7f7", "#fde0a5", "#f1a340", "#d73027"]
# cmap2 = LinearSegmentedColormap.from_list("purple_orange", colors_scheme2, N=256)

# 方案3: 深蓝-浅蓝-白-浅红-深红（Nature风格）
colors_scheme3 = ["#053061", "#2166ac", "#4393c3", "#92c5de", "#d1e5f0", "#f7f7f7", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]
cmap3 = LinearSegmentedColormap.from_list("nature_style", colors_scheme3, N=256)

ax = plt.gca()
sns.heatmap(correlation_matrix, annot=True, cmap=cmap3, vmin=-1, vmax=1,
            linewidths=0.5, fmt=".3f", annot_kws={"size": 14}, ax=ax,
            cbar_kws={'label': 'Correlation Coefficient'})

plt.title('Correlation Matrix of Peptide Concentration and Performance Metrics', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Performance Metrics', fontsize=14, fontweight='bold')
plt.ylabel('Peptide Concentration', fontsize=14, fontweight='bold')

# 自定义标签
ax.set_xticklabels(['AMP', 'ALP', 'L/W', 'Cell Count'], fontsize=14)
ax.set_yticklabels(['AMP Conc.', 'QK Conc.', 'YIGSR Conc.', 'BMP2 Conc.'], fontsize=14)

set_publication_style(ax)
plt.tight_layout()
plt.savefig('outputs/correlation_heatmap_optimized.png', dpi=600, bbox_inches='tight')
plt.savefig('outputs/correlation_heatmap_optimized.pdf', format='pdf', bbox_inches='tight')
plt.show()

# ================= 图2: 雷达图和堆叠柱状图组合 =================
print("正在生成雷达图和堆叠柱状图...")

# 使用筛选的七组均匀表面值
selected_solutions = pd.read_excel('data/7.xlsx')

# 创建图形对象
fig = plt.figure(figsize=(18, 8))

# 雷达图
ax1 = fig.add_subplot(121, projection='polar')

# 雷达图展示多肽接枝密度
categories = ['AMP_conc', 'QK_conc', 'YIGSR_conc', 'BMP2_conc']
category_labels = ['AMP', 'QK', 'YIGSR', 'BMP2']  # 简化标签用于显示
n = len(categories)

# 设置雷达图角度
angles = np.linspace(0, 2*np.pi, n, endpoint=False).tolist()
angles += angles[:1]  # 闭合雷达图

# 找出每个密度的最大值和最小值用于归一化（用于雷达图显示）
max_vals = selected_solutions[categories].max()
min_vals = selected_solutions[categories].min()

# 雷达图设置
ax1.set_theta_offset(np.pi / 2)
ax1.set_theta_direction(-1)
ax1.set_thetagrids(np.degrees(angles[:-1]), category_labels, fontsize=14)

# 使用更优雅的期刊级配色方案 - 基于性能排序的渐变色
# 根据AMP值排序来分配颜色，AMP值越高颜色越深
amp_sorted_indices = selected_solutions['AMP'].argsort()[::-1]  # 降序排列
colors = sns.color_palette("viridis", n_colors=len(selected_solutions))

# 按AMP排序重新分配颜色
color_map = {}
for rank, idx in enumerate(amp_sorted_indices):
    color_map[idx] = colors[rank]

for i, (_, solution) in enumerate(selected_solutions.iterrows()):
    # 归一化密度数据到0-1（仅用于雷达图显示）
    normalized_data = [(solution[cat] - min_vals[cat]) / (max_vals[cat] - min_vals[cat]) for cat in categories]
    normalized_data += normalized_data[:1]  # 闭合雷达图
    
    # 使用基于AMP性能的颜色
    amp_rank = list(amp_sorted_indices).index(i) + 1
    ax1.plot(angles, normalized_data, linewidth=2.5, 
             label=f'Sol {i+1} (AMP: {solution["AMP"]:.2f}%)', 
             color=color_map[i])
    ax1.fill(angles, normalized_data, alpha=0.15, color=color_map[i])

# 雷达图样式设置
ax1.tick_params(axis='both', which='major', width=2, length=2, pad=8, labelsize=14)
ax1.set_ylim(0, 1)
ax1.set_title('Peptide Grafting Density Profiles of 7 Selected Solutions', fontsize=16, fontweight='bold', pad=20)
ax1.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=12)

# 堆叠柱状图
ax2 = fig.add_subplot(122)

labels = [f"Solution {i+1}" for i in range(len(selected_solutions))]
# 使用更现代的期刊级色彩方案 - 基于科学期刊常用配色
bar_colors = ['#2E8B57', '#FF6347', '#4682B4', '#DAA520']  # 海绿色、番茄红、钢蓝色、金黄色

# 创建堆叠柱状图 - 使用原始密度值（不归一化）
bottoms = np.zeros(len(selected_solutions))
peptide_names = ['AMP', 'QK', 'YIGSR', 'BMP2']
for i, conc in enumerate(conc_cols):
    values = selected_solutions[conc].values
    ax2.bar(labels, values, bottom=bottoms, label=peptide_names[i], color=bar_colors[i], 
            edgecolor='white', linewidth=0.8)
    bottoms += values

ax2.set_title('Peptide Concentration Composition of 7 Selected Solutions', 
              fontsize=16, fontweight='bold')
ax2.set_ylabel('Concentration (molecules/nm²)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Solution Rank', fontsize=14, fontweight='bold')
ax2.legend(title='Peptide Type', title_fontsize=14, fontsize=12)
ax2.grid(axis='y', alpha=0.3)
set_publication_style(ax2)

# 在柱状图上标注总浓度
for i, solution in enumerate(selected_solutions.itertuples()):
    total = sum([getattr(solution, col) for col in conc_cols])
    ax2.text(i, total + 0.1, f'{total:.2f}', ha='center', fontsize=12, fontweight='bold')

# 旋转x轴标签以避免重叠
plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.savefig('outputs/radar_and_composition_plots.png', dpi=600, bbox_inches='tight')
plt.savefig('outputs/radar_and_composition_plots.pdf', format='pdf', bbox_inches='tight')
plt.show()

# ================= 图3: Pareto前沿并行坐标图 =================
'''print("正在生成Pareto前沿并行坐标图...")

from matplotlib.colors import Normalize

# 创建Pareto前沿并行坐标图
plt.figure(figsize=(14, 8))
ax = plt.gca()
fig = plt.gcf()

# 使用前10000个解作为Pareto前沿解
pareto_df = df.head(10000).copy()

# 归一化性能指标以便更好地比较
normalized_pareto = pareto_df.copy()
for col in perf_cols:
    min_val = normalized_pareto[col].min()
    max_val = normalized_pareto[col].max()
    normalized_pareto[col] = (normalized_pareto[col] - min_val) / (max_val - min_val)

# 设置x轴位置
x = np.arange(len(perf_cols))

# 创建颜色映射器 - 使用AMP值作为颜色映射的基础
norm = Normalize(vmin=pareto_df['AMP'].min(), vmax=pareto_df['AMP'].max())

# 使用更加细腻的渐变色方案 - 创建自定义的高质量渐变
# 方案1: 增强版深蓝到亮黄渐变 - 改进颜色平滑度和视觉对比度
colors_enhanced = ['#08306b', '#1f5394', '#3574b8', '#5694d3', '#7ab4e8', 
                   '#9ed3fc', '#c8e8ff', '#fff5b4', '#fed976', '#fd8d3c', 
                   '#fc4e2a', '#e31a1c', '#bd0026', '#800026']
cmap_fine = LinearSegmentedColormap.from_list("enhanced_gradient", colors_enhanced, N=1024)

# 方案2: 现代科学期刊风格渐变（备选）
# colors_enhanced = ['#2c7fb8', '#41b6c4', '#7fcdbb', '#c7e9b4', '#ffffcc',
#                   '#ffeda0', '#fed976', '#feb24c', '#fd8d3c', '#fc4e2a',
#                   '#e31a1c', '#bd0026']
# cmap_fine = LinearSegmentedColormap.from_list("journal_gradient", colors_enhanced, N=1024)

# 方案3: 紫红-橙黄高对比度渐变（备选）
# colors_enhanced = ['#49006a', '#762a83', '#9970ab', '#c2a5cf', '#e7d4e8',
#                   '#f7f7f7', '#d9f0d3', '#a6dba0', '#5aae61', '#1b7837',
#                   '#00441b']
# cmap_fine = LinearSegmentedColormap.from_list("contrast_gradient", colors_enhanced, N=1024)

# 绘制每个解的并行坐标线
for i, (_, solution) in enumerate(normalized_pareto.iterrows()):
    # 获取当前解的性能指标值
    y = [solution[perf] for perf in perf_cols]
    # 使用原始AMP值确定颜色
    line_color = cmap_fine(norm(pareto_df.iloc[i]['AMP']))
    # 绘制连接线，使用优化的线条样式
    # 根据AMP值调整透明度：高性能解更不透明
    alpha_value = 0.3 + 0.4 * norm(pareto_df.iloc[i]['AMP'])  # 0.3-0.7范围
    plt.plot(x, y, '-', color=line_color, alpha=alpha_value, linewidth=0.8, 
             solid_capstyle='round', solid_joinstyle='round')

# 设置x轴标签和刻度
performance_labels = ['AMP (%)', 'ALP (a.u.)', 'L/W', 'Cell Count']
plt.xticks(x, performance_labels, fontsize=14, fontweight='bold')
plt.ylabel('Normalized Performance Value', fontsize=14, fontweight='bold')

# 设置标题和网格
plt.title('Pareto Front Solutions Parallel Coordinates Plot', 
          fontsize=16, fontweight='bold', pad=20)
plt.grid(True, linestyle='--', alpha=0.3)

# 应用期刊级别刻度线和轴样式
set_publication_style(ax)

# 添加颜色条
sm = plt.cm.ScalarMappable(cmap=cmap_fine, norm=norm)
sm._A = []
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label('AMP Performance (%)', fontsize=14, fontweight='bold')

# 设置y轴范围
plt.ylim(-0.05, 1.05)

plt.tight_layout()
plt.savefig('outputs/pareto_parallel_coordinates_optimized.png', dpi=600, bbox_inches='tight')
plt.savefig('outputs/pareto_parallel_coordinates_optimized.pdf', format='pdf', bbox_inches='tight')
plt.show()'''

print("所有图表已生成完成！")
print("生成的文件:")
print("1. correlation_heatmap_optimized.png/pdf - 优化的相关性热图")
print("2. radar_and_composition_plots.png/pdf - 雷达图和堆叠柱状图组合")
print("3. pareto_parallel_coordinates_optimized.png/pdf - Pareto前沿并行坐标图")
