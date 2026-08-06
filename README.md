# FutureCISI — Thesis code

Code for my MSc thesis.

All input data is stored locally and not included in this repository.

---

## Run order

1. `clip_resize_data.ipynb` — clips raw input rasters to the EU27 0.1° domain
2. `fix_data_pop_gdp.ipynb` — aligns GDP and population rasters to the EU27 grid
3. `one_hot_encoding.ipynb` — converts land cover to one-hot encoded bands
4. `preprocess_ssp_inputs.ipynb` — converts SSP scenario inputs to normalized format
5. `CISI_analysis.ipynb` — analyses the historic CISI label data
6. `train_model_final.ipynb` — runs hyperparameter sweep and final model training (this is the most important file)
7. `evaluate_test_set.ipynb` — evaluates the model on the Italy test set
8. `error_analysis.ipynb` — spatial error analysis
9. `sweep_analysis.ipynb` — analyses sweep results and selects best hyperparameters
10. `projections.ipynb` — runs the model on all SSP scenarios and generates figures
11. `projections_delta.ipynb` — computes change relative to historic CISI
12. `plotting_data.ipynb` — input data summary figures

---

## Model

The final trained model weights (`best_sweep_final_model.pt`) are not included due to file size.
