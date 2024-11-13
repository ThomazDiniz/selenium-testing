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

Ferramentas para pesquisar:
1. https://grafana.com/
2. https://streamlit.io/
3. https://plotly.com/
