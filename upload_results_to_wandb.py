"""
Uploads hyperparameter search results from CSV to Weights & Biases.
Run once after the search is complete.
"""

import csv
import wandb

CSV_FILES = {
    "search_v1_WeightedMSE_lam5-15": "hyperparameter_search_results.csv",
    "search_v2_WeightedMSE_lam15-30": "hyperparameter_search_results_v2.csv",
}

PROJECT = "cisi-cnn"

for run_group, csv_path in CSV_FILES.items():
    print(f"\nUploading {csv_path} → group '{run_group}'...")

    with open(csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row.get('lam')]  # skip empty last row

    for i, row in enumerate(rows):
        config = {
            'lam':     float(row['lam']),
            'lr':      float(row['lr']),
            'dropout': float(row['dropout']),
        }
        metrics = {
            'global_r2':              float(row['global_r2']),
            'global_mae':             float(row['global_mae']),
            'city_r2':                float(row['city_r2']),
            'city_mae':               float(row['city_mae']),
            'city_underprediction':   float(row['city_underprediction']),
            'city15_r2':              float(row.get('city15_r2', 0)),
            'city15_mae':             float(row.get('city15_mae', 0)),
            'city15_underprediction': float(row.get('city15_underprediction', 0)),
            'pred_max':               float(row['pred_max']),
        }

        run = wandb.init(
            project=PROJECT,
            group=run_group,
            config=config,
            reinit=True,
            name=f"{run_group}_run{i+1:02d}_lam{int(float(row['lam']))}",
        )
        wandb.log(metrics)
        run.finish()
        print(f"  Run {i+1}/{len(rows)} — lam={config['lam']}, city_underp={metrics['city_underprediction']:.1f}%")

print(f"\nDone. View at: https://wandb.ai/<your-username>/{PROJECT}")
