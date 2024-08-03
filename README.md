## README

### ATIVIDADE 1 - ARIEL LIMA ABADE BANDEIRA: How do I print to console in pytest?

**REPOSITÓRIO DO PROJETO:** [https://github.com/arielzz66/Teste_Software_2024_BANDEIRA_ARIEL](https://github.com/arielzz66/Teste_Software_2024_BANDEIRA_ARIEL)

**Problema**

Este projeto aborda a dificuldade de imprimir logs do sistema (saídas da função `print()`) durante a execução de testes com o Pytest em Python. A visualização desses logs é crucial para entender o fluxo de execução dos testes e identificar possíveis falhas.

O problema original, publicado no Stack Overflow, envolvia um cenário de testes em uma classe `Blogger` que herda de `Site`, buscando verificar a correta recuperação de posts e links associados a um usuário específico. No entanto, a execução padrão do Pytest não exibia as mensagens de log desejadas.

**Objetivos dos Testes**

1. Confirmar se a classe `Blogger` é uma subclasse de `Site`.
2. Verificar se a chamada ao dono do blog retorna corretamente os posts associados ao usuário "alice".
3. Imprimir o nome do usuário e seus links associados para validação visual.

**Solução**

A solução encontrada foi executar o Pytest com a opção `-s` (shortcut para `--capture=no`):

```bash
pytest test_blogger.py -s
```

Essa opção desativa a captura padrão de saída do Pytest, permitindo que as mensagens de log sejam exibidas no console durante a execução dos testes.


**Estrutura do Projeto**

* **`myapplication.py`:** Contém o código da aplicação principal a ser testada. ([Link para myapplication.py](https://github.com/arielzz66/Teste_Software_2024_BANDEIRA_ARIEL/blob/master/tests/myapplication.py))
* **`test_blogger.py`:** Contém os testes unitários utilizando o Pytest. ([Link para test_blogger.py](https://github.com/arielzz66/Teste_Software_2024_BANDEIRA_ARIEL/blob/master/tests/test_blogger.py))

