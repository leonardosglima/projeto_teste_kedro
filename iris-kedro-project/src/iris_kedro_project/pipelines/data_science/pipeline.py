# src/iris_kedro_project/pipelines/data_science/pipeline.py

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, train_model, predict, report_accuracy

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["iris_raw", "parameters"],  # <-- CORREÇÃO AQUI
                #inputs=['iris_raw', 'params:test_size', 'params:random_state', 'params:features', 'params:target_column'],
                outputs=['X_train', 'X_test', 'y_train', 'y_test'],
                name='split_data_node',
            ),
            node(
                func=train_model,
                inputs=['X_train', 'y_train'],
                outputs='model',
                name='train_model_node',
            ),
            node(
                func=predict,
                inputs=['model', 'X_test'],
                outputs='predictions',
                name='predict_node',
            ),
            node(
                func=report_accuracy,
                inputs=['predictions', 'y_test'],
                outputs=None, # Este nó não gera saída para o catálogo
                name='report_accuracy_node',
            ),
        ]
    )

