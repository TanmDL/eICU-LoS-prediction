from eICU_preprocessing.split_train_test import create_folder
from models.run_tpc import TPC
import numpy as np
import random
from models.initialise_arguments import initialise_tpc_arguments


if __name__=='__main__':

    c = initialise_tpc_arguments()
    c['mode'] = 'train'
    c['exp_name'] = 'TempWeightShare'
    c['model_type'] = 'temp_only'
    c['share_weights'] = True

    temp_kernels_choice = list(int(x) for x in np.logspace(np.log2(16), np.log2(64), base=2, num=9))
    c['temp_kernels'] = [random.choice(temp_kernels_choice)]*c['n_layers']

    log_folder_path = create_folder('models/experiments/hyperparameters', c.exp_name)
    temp_weight_share = TPC(config=c,
                            n_epochs=c.n_epochs,
                            name=c.exp_name,
                            base_dir=log_folder_path,
                            explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
    temp_weight_share.run()