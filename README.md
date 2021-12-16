# Codes for Prompt-Based Event Extraction

## Trigger Extraction
    python3 detect/cli.py --method pet --pattern_ids 0 1 2 --data_dir ./data --model_type roberta --model_name_or_path roberta-base --task_name trigger --output_dir ./output_arg_ex --do_train --do_eval --no_distillation

## Argument Existence Detection
To run training script for argument existence detection, you need

    python3 detect/cli.py --method pet --pattern_ids 0 1 2 --data_dir ./data --model_type roberta --model_name_or_path roberta-base --task_name event_argument_existence --output_dir ./output_arg_ex --do_train --do_eval --no_distillation

## Argument identification
To run traininng script for argument identification, you need

    bash gen-arg/gen-arg/src/genie/train_kairos.sh

For testing, run

    bash gen-arg/src/genie/test_kairos.sh 
 
Our customized event templates with role description is here: bartgen/gen-arg/event_role_KAIROS.json
