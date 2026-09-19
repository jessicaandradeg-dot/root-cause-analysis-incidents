import numpy as np
from typing import List

def precision_at_k(actual_root_cause: str, recommended_top_k: List[str], k: int = 1) -> float:
    """Calcula Precision@K para a recomendação de causa raiz."""
    truncated_recommendations = recommended_top_k[:k]
    return 1.0 if actual_root_cause in truncated_recommendations else 0.0

def mean_average_precision_at_k(actual_root_causes: List[str], recommendations_list: List[List[str]], k: int = 3) -> float:
    """
    Calcula a Média da Precisão Média (MAP@K) sobre um conjunto de incidentes.
    
    Mede a capacidade do algoritmo de posicionar a verdadeira causa raiz nas
    primeiras posições do ranking de suporte.
    """
    aps = []
    for actual, recs in zip(actual_root_causes, recommendations_list):
        truncated = recs[:k]
        if actual in truncated:
            rank = truncated.index(actual) + 1
            ap = 1.0 / rank  # Reciprocal Rank para causa raiz única
        else:
            ap = 0.0
        aps.append(ap)
        
    return float(np.mean(aps))

if __name__ == "__main__":
    # Exemplo de avaliação do motor de RCA
    true_incidents = ["db_connection_timeout", "redis_oom", "auth_service_500"]
    model_predictions = [
        ["db_connection_timeout", "gateway_latency", "cpu_spike"], # Acertou em Top-1
        ["network_drop", "redis_oom", "disk_full"],               # Acertou em Top-2
        ["payment_api_error", "gateway_latency", "auth_service_500"] # Acertou em Top-3
    ]
    
    p1 = np.mean([precision_at_k(t, p, k=1) for t, p in zip(true_incidents, model_predictions)])
    p3 = np.mean([precision_at_k(t, p, k=3) for t, p in zip(true_incidents, model_predictions)])
    map3 = mean_average_precision_at_k(true_incidents, model_predictions, k=3)
    
    print("=== INCIDENT RECOMMENDATION EVALUATION ===")
    print(f"Precision@1 (Top-1 Accuracy): {p1 * 100:.1f}%")
    print(f"Precision@3 (Top-3 Recall):   {p3 * 100:.1f}%")
    print(f"MAP@3 (Mean Avg Precision):   {map3:.4f}")