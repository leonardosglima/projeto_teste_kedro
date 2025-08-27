"""Project pipelines."""
from __future__ import annotations  # <--- Boa prática, mantida do código original
from typing import Dict
from kedro.pipeline import Pipeline

# Importação explícita do nosso pipeline (método do tutorial)
from iris_kedro_project.pipelines import data_science

def register_pipelines() -> dict[str, Pipeline]: # <- a anotação de tipo aqui beneficia do __future__
    """Register the project's pipelines."""
    
    # Criação e registo manual (método do tutorial)
    data_science_pipeline = data_science.create_pipeline()
    
    return {
        "__default__": data_science_pipeline,
        "ds": data_science_pipeline,
    }