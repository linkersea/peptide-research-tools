# Visualization Tools

High-quality scientific visualization tools for peptide research data analysis.

## Features

- **Correlation Heatmaps**: Publication-quality correlation analysis
- **Radar Charts**: Multi-dimensional peptide profile visualization  
- **Stacked Bar Charts**: Composition analysis
- **Pareto Front Analysis**: Optimization results visualization

## Generated Visualizations

1. **Correlation Heatmap** (`correlation_heatmap_optimized.png/pdf`)
   - Nature-style diverging color scheme
   - Concentration vs Performance correlation matrix

2. **Radar & Composition Charts** (`radar_and_composition_plots.png/pdf`)
   - 7 selected uniform surface solutions
   - Peptide density profiles and composition

3. **Pareto Parallel Coordinates** (`pareto_parallel_coordinates_optimized.png/pdf`)
   - Multi-objective optimization visualization
   - Performance trade-off analysis

## Usage

```bash
pip install -r requirements.txt
python selected_visualizations.py
```

## Data Requirements

- `data/pareto_solutions_ranked.xlsx` - Main dataset
- `data/7.xlsx` - Selected uniform surface solutions

## Output

All visualizations are saved to the `outputs/` directory in both PNG (600 DPI) and PDF formats, suitable for scientific publication.

## Color Schemes

- **Heatmap**: Nature-style deep blue to red diverging colors
- **Radar Chart**: Viridis palette with performance-based ranking
- **Parallel Coordinates**: Enhanced gradient with 14-color progression

## Font & Style

- Unified font size: 14pt
- Arial font family
- Publication-ready formatting with proper axis styling
