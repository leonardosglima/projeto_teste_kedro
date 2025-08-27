"""Project pipelines."""
from __future__ import annotations
from typing import Dict
from kedro.pipeline import Pipeline

# --- INÍCIO DA CORREÇÃO ---
# Importamos a função create_pipeline DIRETAMENTE do módulo pipeline.py
from iris_kedro_project.pipelines.data_science.pipeline import create_pipeline as data_science_pipeline_func

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""
    
    # Chamamos a função diretamente
    data_science_pipeline = data_science_pipeline_func()
    # --- FIM DA CORREÇÃO ---
    
    return {
        "__default__": data_science_pipeline,
        "ds": data_science_pipeline,
    }