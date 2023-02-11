# Comandos bacanas

## Cobertura dos testes
pytest --cov

### Testes que não foram feitos
pytest --cov=arquivo pastaTestes/ --cov-report term-missing

### Relatório dos testes em html
pytest --cov=arquivo pastaTestes/ --cov-report html

### Gerar relatorio em xml
pytest --junitxml report.xml

### Gerar relatorio do coverage em xml
pytest --cov-report xml