# src/iris_kedro_project/pipelines/data_science/nodes.py

import pandas as pd
from typing import Dict, Tuple
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import logging

def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Divide os dados em features e target, e depois em treino e teste."""
    X = data[parameters["features"]]
    y = data[parameters["target_column"]]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    
    return X_train, X_test, y_train, y_test

def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LogisticRegression:
    """Treina um modelo de Regressão Logística."""
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def predict(model: LogisticRegression, X_test: pd.DataFrame) -> pd.Series:
    """Usa o modelo treinado para fazer previsões."""
    return model.predict(X_test)

def report_accuracy(predictions: pd.Series, y_test: pd.Series):
    """Calcula e loga a acurácia do modelo."""
    accuracy = accuracy_score(y_test, predictions)
    log = logging.getLogger(__name__)
    log.info(f"Acurácia do modelo: {accuracy:.3f}")