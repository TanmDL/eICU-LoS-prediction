Running the models
==================================

1) Once you have run the pre-processing steps you can run all the models in your terminal. Set the working directory to the eICU-LoS-prediction, and run the following:

    ```
    python -m models.run_tpc
    ```
    
    Note that your experiment can be customised by using command line arguments e.g.
    
    ```
    python -m models.run_tpc --model_type tpc --n_layers 4 --kernel_size 3 --no_temp_kernels 10 --point_size 10 --last_linear_size 20 --diagnosis_size 20 --batch_size 64 --learning_rate 0.001 --main_dropout_rate 0.3 --temp_dropout_rate 0.1 
    ```
    
    Each experiment you run will create a directory within models/experiments. The naming of the directory is based on 
    the date and time that you ran the experiment (to ensure that there are no name clashes). The experiments are saved 
    in the standard trixi format: https://trixi.readthedocs.io/en/latest/_api/trixi.experiment.html.
    
2) The hyperparameter searches can be replicated by running:

    ```
    python -m models.hyperparameter_scripts.tpc
    ```
 
    Trixi provides a useful way to visualise effects of the hyperparameters (after running the following command, navigate to http://localhost:8080 in your browser):
    
    ```
    python -m trixi.browser --port 8080 experiments/hyperparameters/TPC
    ```
    
    The final experiments for the paper are found in models/final_experiment_scripts:
    
    ```
    python -m models.final_experiment_scripts.tpc
    ```