import pandas as pd
import numpy as np

def calcular_rca_top_k(df_logs, evento_falha, janela_minutos=15, top_k=3):
    """
    Identifica potenciais causas raízes de falhas distribuídas com base em
    janelas temporais e frequências de ocorrência.
    """
    df_falhas = df_logs[df_logs['evento'] == evento_falha]
    causas_potenciais = []
    
    for idx, row in df_falhas.iterrows():
        inicio_janela = row['timestamp'] - pd.Timedelta(minutes=janela_minutos)
        ocorrencias = df_logs[
            (df_logs['timestamp'] >= inicio_janela) & 
            (df_logs['timestamp'] < row['timestamp']) &
            (df_logs['evento'] != evento_falha)
        ]
        causas_potenciais.extend(ocorrencias['evento'].tolist())
        
    if not causas_potenciais:
        return pd.DataFrame(columns=['componente_causa', 'score_probabilidade'])

    df_scores = pd.DataFrame(causas_potenciais, columns=['evento_causa'])
    ranking = df_scores['evento_causa'].value_counts(normalize=True).reset_index()
    ranking.columns = ['componente_causa', 'score_probabilidade']
    
    return ranking.head(top_k)

if __name__ == "__main__":
    # Simulação de Logs de Incidentes Distribuídos
    np.random.seed(42)
    data = {
        'timestamp': pd.date_range(start='2026-09-01', periods=100, freq='5min'),
        'evento': np.random.choice(['DB_Timeout', 'High_CPU_Redis', 'Network_Latency', 'Payment_Gateway_500'], 100),
        'severidade': np.random.choice(['CRITICAL', 'WARNING', 'INFO'], 100)
    }
    df_logs = pd.DataFrame(data)
    
    print("--- TOP-3 CAUSAS RAIZES IDENTIFICADAS ---")
    print(calcular_rca_top_k(df_logs, evento_falha='Payment_Gateway_500', top_k=3))