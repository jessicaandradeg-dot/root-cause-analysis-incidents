# 🔍 Root Cause Analysis (RCA) & Incident Recommendation Engine

Este repositório apresenta uma solução analítica em Python para **Análise de Causa Raiz (RCA)** de falhas e anomalias em ambientes e sistemas distribuídos, combinando análise temporal de eventos e sistemas de recomendação baseados em ranking.

---

## 📌 Contexto e Problema de Negócio

Em arquiteturas complexas de microsserviços, incidentes críticos (ex: erro 500 no Gateway de Pagamentos) são frequentemente precedidos por pequenos gargalos em serviços correlacionados (timeouts em banco de dados, spikes de CPU no cache, latência de rede). Identificar manualmente o componente que originou a falha exige tempo operacional elevado.

A solução automatiza essa investigação através da correlação temporal de logs e ranqueamento probabilístico das causas raízes.

---

## 🛠️ Funcionalidades Principais

* **Correlação Temporal por Janela Deslizante:** Filtra eventos e anomalias que ocorreram imediatamente antes da falha em uma janela temporal parametrizável ($T - \Delta t$).
* **Sistema de Ranking (Top-K Recommendations):** Calcula a pontuação e frequência de recorrência dos componentes suspeitos, gerando recomendações diretas para sustentação do ambiente (**Top-1** e **Top-3** recomendações).
* **Processamento de Logs de Incidentes:** Simulação estocástica de logs contendo timestamp, identificador do evento e nível de severidade.

---

## 🚀 Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/jessicaandradeg-dot/root-cause-analysis-incidents.git](https://github.com/jessicaandradeg-dot/root-cause-analysis-incidents.git)
   cd root-cause-analysis-incidents