# 🔍 Root Cause Analysis (RCA) & Incident Recommendation Engine

Este repositório apresenta uma solução analítica em Python para **Análise de Causa Raiz (RCA)** e diagnósticos de falhas em sistemas distribuídos e microsserviços. O motor combina análise de eventos em janelas temporais com sistemas de ranqueamento probabilístico para acelerar o diagnóstico de incidentes críticos.

---

## 📌 Contexto e Problema de Negócio

Em arquiteturas modernas de alta disponibilidade, incidentes críticos (ex: erro `500 Internal Server Error` no Gateway de Pagamentos) raramente ocorrem de forma isolada. Eles são precedidos por pequenas anomalias encadeadas em serviços correlacionados (como *timeouts* de banco de dados, saturação de memória ou latência em microsserviços de autenticação).

A investigação manual dessas falhas por equipes de Sustentação/SRE exige parsing extensivo de logs e gera um **MTTR (*Mean Time to Resolution*)** elevado, impactando diretamente o acordo de nível de serviço (SLA).

**Solução Proposta:** Automar a identificação de componentes críticos através de um algoritmo de **correlação temporal por janelas deslizantes** e um **sistema de ranqueamento Top-K**, priorizando os componentes com maior probabilidade de terem originado a falha.

---

## 🛠️ Funcionalidades Principais & Arquitetura

* **Correlação Temporal por Janela Deslizante ($T - \Delta t$):** Filtra e isola os eventos e anomalias de baixa severidade que antecederam o incidente principal em um intervalo de tempo parametrizável.
* **Sistema de Ranqueamento Top-K:** Aplica um modelo de pontuação (*score*) baseado na frequência de ocorrência, severidade do evento e proximidade temporal do incidente, gerando recomendações diretas (**Top-1** e **Top-3**) para o time de suporte.
* **Simulação Estocástica & Ingestão de Logs:** Pipeline preparado para ingestão de arquivos de log contendo `timestamp`, `service_id`, `event_type` e `severity_level` (INFO, WARN, ERROR, CRITICAL).
* **Estrutura Modular & Testável:** Desenvolvido com arquitetura limpa em Python, pronto para integração com pipelines de observabilidade (ex: Prometheus, Grafana, OpenTelemetry).

**Métricas de Avaliação de Ranking Top-K (`src/evaluation_metrics.py`):** Módulo para validação quantitativa das recomendações do motor de RCA utilizando métricas formais de sistemas de recomendação e recuperação de informação:
  * **Precision@1 (Top-1 Accuracy):** Acurácia direta da causa raiz prevista na primeira posição.
  * **Precision@3 (Top-3 Recall):** Taxa de cobertura da causa raiz entre os 3 principais suspeitos.
  * **MAP@K (Mean Average Precision):** Média da precisão ponderada pela posição da causa raiz no ranking.

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone [https://github.com/jessicaandradeg-dot/root-cause-analysis-incidents.git](https://github.com/jessicaandradeg-dot/root-cause-analysis-incidents.git)
cd root-cause-analysis-incidents
