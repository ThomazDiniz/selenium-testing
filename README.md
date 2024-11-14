# selenium-testing
O objetivo deste projeto é trazer um pouco de discussão referente a utilização de pytest + selenium para testes de maneira geral. Queremos investigar maneiras de utilizar o pytest para gerar relatórios 

# Instalação
+ python

Dependências:

      pip install pytest-json-report # ferramenta de extração mas podemos discutir outras estratégias
      pip install pytest-html
      pip install pytest-html-reporter #possivelmente essa sera a ferramenta de report de fato

# Rodando os testes

    python -m pytest --html=report.html --json-report --json-report-file=report.json
ou

    python -m pytest

O pytest por default roda todos os arquivos no formato test_*.py ou *_test.py


# Entendendo o Projeto
todo

# Ferramentas para pesquisar:
1. https://grafana.com/
2. https://streamlit.io/
3. https://plotly.com/

# Métricas relevantes a tentar adicionar
1. Quantidade de testes executados com sucesso
2. Quantidade de testes executados com falha
3. Quantidade de testes bloqueados
4. Tempo de execução Geral
5. Tempo de execução por teste
6. Testes Instáveis (Falsos positivos, falsos negativos)
7. Latency
8. Defect Leakage (Para verificar isso, seria necessário saber os defeitos que o teste capturou vs a quantidade de defeitos totais)
9. Cobertura de Código
10. Stack Trace
11. Linha de Erro
12. Densidade de defeitos (quantidade de defeitos por linha de código).

