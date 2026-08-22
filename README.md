# FutureCISI — Thesis code
All input data is stored locally and not included in this repository as it is multiple Gb of data.

---

## Run order

1. `clip_resize_data.ipynb` — Clips raw input rasters to the EU27 0.1 degree domain
2. `fix_data_pop_gdp.ipynb` — Aligns GDP and population rasters to the EU27 grid
3. `one_hot_encoding.ipynb` — Converts land cover to one-hot encoded bands
4. `preprocess_ssp_inputs.ipynb` — Converts SSP scenario inputs to normalized format
5. `CISI_analysis.ipynb` — Analyses the historic CISI label data
6. `train_model_final.ipynb` — Runs hyperparameter sweep and final model training. This is by far the most used and important file. Entire blocks are commented out or used, depending on the specific application. This file was used for model training and for the W&B sweep.
7. `evaluate_test_set.ipynb` — Evaluates the model on the Italy test set
8. `error_analysis.ipynb` — Spatial error analysis
9. `sweep_analysis.ipynb` — Analyses sweep results and selects best hyperparameters
10. `projections.ipynb` — Runs the model on all SSP scenarios and generates figures
11. `projections_delta.ipynb` — Computes change relative to historic CISI
12. `plotting_data.ipynb` — Input data figures

---

## Model

The final trained model weights (`best_sweep_final_model.pt`) are not included due to file size.
