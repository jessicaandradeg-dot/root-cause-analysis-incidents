# 🔍 Root Cause Analysis (RCA) & Incident Recommendation Engine

Projeto de análise de causa raiz para incidentes em sistemas distribuídos, com foco em recomendação automatizada de suspeitas prioritárias para suporte e operação.

Este repositório apresenta uma solução analítica em Python para Análise de Causa Raiz (RCA) e diagnósticos de falhas em sistemas distribuídos e microsserviços. O motor combina análise de eventos em janelas temporais com sistemas de ranqueamento probabilístico para acelerar o diagnóstico de incidentes críticos.

---

## 📌 Problema de negócio

Em ambientes de alta disponibilidade, falhas críticas raramente aparecem isoladamente. Elas são normalmente precedidas por sinais fracos e espalhados em diferentes serviços: latência de banco, saturação de memória, timeouts em autenticação, erros de rede e picos de carga.

A investigação manual desses eventos consome tempo, aumenta o MTTR (Mean Time to Resolution) e prejudica SLA, disponibilidade e experiência do cliente. Em cenários de e-commerce, pagamentos, fintechs e plataformas digitais, o custo de uma análise lenta pode ser alto tanto em operação quanto em reputação.

Este projeto automatiza a etapa inicial de triagem: identifica os componentes mais prováveis de terem causado o incidente usando correlação temporal e ranking probabilístico.

---

## 🛠️ O que foi construído

- Segmentação por janela temporal antes do evento crítico
- Tratamento de eventos correlacionados e de baixa severidade
- Cálculo de score por frequência, severidade e proximidade temporal
- Geração de recomendações Top-1 e Top-3
- Métricas de avaliação de qualidade do ranking
- Estrutura modular pronta para extensão para logs reais e observabilidade

### Funcionalidades principais e arquitetura

* Correlação temporal por janela deslizante $(T - \Delta t)$: filtra e isola os eventos e anomalias de baixa gravidade que antecederam o incidente principal em um intervalo de tempo parametrizável.
* Sistema de ranqueamento Top-K: aplica um modelo de pontuação baseado na frequência de ocorrência, severidade do evento e proximidade temporal do incidente, gerando recomendações diretas (Top-1 e Top-3) para o time de suporte.
* Simulação estocástica e ingestão de logs: pipeline preparado para aquisição de arquivos de log contendo `timestamp`, `service_id`, `event_type` e `severity_level` (`INFO`, `WARN`, `ERROR`, `CRITICAL`).
* Estrutura modular e testável: desenvolvido com arquitetura limpa em Python, pronto para integração com pipelines de observabilidade (ex.: Prometheus, Grafana, OpenTelemetry).
* Métricas de avaliação de ranking Top-K (`src/evaluation_metrics.py`): módulo para validação quantitativa das recomendações do motor de RCA usando métricas formais de sistemas de recomendação e recuperação de informação.
  * Precision@1 (Top-1 Accuracy): acurácia direta da causa raiz prevista na primeira posição.
  * Precision@3 (Top-3 Recall): taxa de cobertura da causa raiz entre os 3 principais suspeitos.
  * MAP@K (Mean Average Precision): média da precisão ponderada pela posição da causa raiz no ranking.

---

## 📐 Metodologia

A lógica segue uma abordagem simples e interpretável:

1. Seleciona o evento alvo de falha, como `Payment_Gateway_500`.
2. Define uma janela histórica anterior ao incidente.
3. Extrai eventos de outros componentes dentro desse intervalo.
4. Conta sua frequência e calcula um score de probabilidade.
5. Ordena os componentes e devolve os mais prováveis candidatos a causa raiz.

A implementação principal está em `calcular_rca_top_k`, que combina:

- janela móvel de tempo
- filtro de eventos diferentes do incidente alvo
- contagem de ocorrência por componente
- ranking de prioridade

A avaliação de qualidade usa `Precision@K` e `MAP@K`, medidas comuns em sistemas de recomendação e ranking.

---

## 📊 Resultados esperados e KPI

O objetivo do sistema é maximizar a chance de o incidente real aparecer nas primeiras posições do ranking.

### Métricas implementadas

- Precision@1: chance de a causa correta aparecer no topo
- Precision@3: chance de a causa correta aparecer entre os 3 primeiros
- MAP@3: qualidade geral do ranking em múltiplos incidentes

### Exemplo ilustrativo

| Métrica | Valor | Interpretação |
|---|---:|---|
| Precision@1 | 66.7% | boa capacidade de priorizar a causa correta no topo |
| Precision@3 | 100.0% | cobertura forte entre os 3 primeiros candidatos |
| MAP@3 | 0.7778 | ranking consistente e útil para suporte operacional |

Essas métricas transformam o problema em um caso de recomendação orientada a decisão, e não apenas em análise exploratória.

---

## 🧪 Benchmark comparativo de políticas

Uma boa evolução para o projeto é comparar políticas de priorização:

- frequências puras
- peso por severidade
- peso por proximidade temporal
- score híbrido combinando todos os fatores

### Exemplo de benchmark recomendado

| Política | Top-1 | Top-3 | Observação |
|---|---:|---:|---|
| Frequência simples | 40% | 80% | fácil de interpretar |
| Severidade ponderada | 55% | 85% | favorece eventos críticos |
| Tempo + frequência | 60% | 90% | melhor para cascatas temporais |
| Híbrida | 67% | 100% | melhor equilíbrio operacional |

Esse tipo de comparação mostra maturidade analítica e é especialmente valioso para recrutadores, porque demonstra pensamento de produto, impacto real em operações e capacidade de tomada de decisão orientada por dados.

---

## 🧰 Stack

- Python
- Pandas
- NumPy
- Jupyter / notebooks de análise
- Métricas de ranking e avaliação
- Estrutura modular para expansão com logs e dados reais

---

## 📁 Estrutura do projeto

- `rca_engine.py`: motor principal de análise e ranking
- `src/evaluation_metrics.py`: métricas de avaliação Precision@K e MAP@K
- `README.md`: documentação do projeto e contexto de negócio

---

## 📈 Exemplo de saída

```python
--- TOP-3 CAUSAS RAIZES IDENTIFICADAS ---
      componente_causa  score_probabilidade
0    DB_Timeout           0.31
1    High_CPU_Redis       0.27
2    Network_Latency      0.22
```

Esse resultado ilustra como o algoritmo transforma um histórico de eventos em uma recomendação acionável para o time de operação.

---

## 🎯 Relevância para vagas de dados e ML

Este projeto comunica bem uma narrativa de negócio e engenharia aplicada:

- resolve um problema operacional real
- usa dados de eventos e correlação temporal
- cria um mecanismo de recomendação acionável
- mede qualidade de ranking com indicadores objetivos
- demonstra capacidade de transformar dados em decisão

É um bom exemplo de perfil para vagas envolvendo:

- Data Science
- ML Operations
- Analytics Engineering
- SRE / observabilidade
- incident response
- causal analysis
- decision support

---

## 🚀 Próximos passos recomendados

- integrar logs reais de produção
- adicionar feature engineering por janela e serialização temporal
- comparar modelos de score e regras heurísticas
- gerar dashboards de incidentes e ranking
- anexar benchmark em tabela ou notebook público
- publicar artigo de metodologia e resultado em markdown ou README

---

## 🔗 Link para artigo / benchmark / tabela

Se o projeto for expandido para público ou apresentação, este é o espaço ideal para adicionar:

- link para notebook de benchmark
- link para dashboard ou report em PDF
- link para artigo técnico ou resumo executivo
- tabela comparando políticas e resultados por cenário

Exemplo de estrutura sugerida:

- [Benchmark notebook](#)
- [Relatório executivo](#)
- [Artigo técnico](#)

---

## 🧾 Mensagem para recrutadores

Este projeto combina analítica operacional, priorização de risco e sistemas de recomendação. Em vez de focar apenas em modelagem preditiva, a solução foi pensada para apoiar decisões reais em ambientes críticos, com foco em velocidade de diagnóstico, rastreabilidade e qualidade da recomendação.

A proposta é resolver um problema de negócio concreto: reduzir o tempo de investigação em incidentes críticos, melhorar o MTTR e oferecer recomendações úteis para time de suporte e operação.

Esse tipo de projeto comunica bem visão de produto, impacto em negócio e capacidade de transformar dados em ação.

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/jessicaandradeg-dot/root-cause-analysis-incidents.git
cd root-cause-analysis-incidents
```

### 2. Executar o motor de RCA

```bash
python rca_engine.py
```

### 3. Visualizar métricas de avaliação

```bash
python src/evaluation_metrics.py
```

---

## ✅ Resumo executivo

Este projeto demonstra capacidade de:

- trabalhar com dados de eventos em produção
- construir pipelines analíticos orientados a decisão
- aplicar ranking e recomendação em contextos operacionais
- comparar estratégias por métricas quantitativas
- comunicar valor de negócio em linguagem clara e objetiva

Esse perfil é muito relevante para vagas de ciência de dados, ML, análise operacional, suporte analítico e engenharia de dados aplicada a decisão.
