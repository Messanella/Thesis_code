# Model Performance Log

## Baseline Model (Run 1)
Date: [14/2]
Architecture: 3-layer CNN (9→16→32→64)
Loss: WeightedMSE (factor=10)
Data: Random 80/20 split

### Overall Performance:
- R² (full): 0.237
- R² (validation): 0.459
- MAE: 0.0211
- RMSE: 0.0369

### City Performance (CISI > 0.1):
- Count: 918 pixels (6.5%)
- City MAE: 0.0991 (6.63× worse than rural)
- Mean prediction: 0.050 (actual: 0.149)
- **Problem: Severe underprediction of cities**

### By CISI Level:
| Range | Count | MAE | Mean Actual | Mean Pred |
|-------|-------|-----|-------------|-----------|
| 0-0.05 | 9,332 | 0.011 | 0.019 | 0.021 |
| 0.05-0.1 | 2,259 | 0.031 | 0.070 | 0.040 |
| 0.1-0.15 | 612 | 0.072 | 0.120 | 0.049 |
| 0.15-0.2 | 167 | 0.117 | 0.170 | 0.053 |
| 0.2+ | 126 | 0.209 | 0.265 | 0.056 |

### Conclusion:
Model performs well on low CISI (rural) but fails on high CISI (cities/hotspots).
Data imbalance (81% rural vs 6.5% cities) causes model to optimize for majority class.


## Experiment 2: Oversampling Cities 10x
Date: [18/2/2026]

### Results:
- Overall R²: 0.873 (baseline: 0.237) - IMPROVEMENT: +268%
- Overall MAE: 0.017 (baseline: 0.021) - IMPROVEMENT: -19%
- Pred max: 0.245 (baseline: 0.178) - IMPROVEMENT: +38%
- City MAE: ? (baseline: 0.099)
- City bias: ? (baseline: -0.099)

