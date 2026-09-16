 Pesquisa sobre a biblioteca Pandas

 1. O que é o Pandas

Pandas é uma biblioteca da linguagem Python utilizada para trabalhar e analisar dados de forma organizada.

 2. Principais estruturas de dados

 DataFrame

DataFrame é uma estrutura de dados bidimensional, semelhante a uma planilha ou a uma tabela de banco de dados.

 Series

Series é uma estrutura de dados unidimensional, formada por valores e índices.

 3. Como criar uma Series

Uma Series pode ser criada utilizando `pd.Series()`.

Os principais parâmetros são:

- `data`: representa os valores que serão armazenados na Series.
- `index`: representa os rótulos ou índices associados a cada valor.
- `dtype`: define o tipo dos dados da Series.
- `name`: permite dar um nome à Series.
- `copy`: controla a cópia dos dados de entrada.

### Exemplo

```python
import pandas as pd

s = pd.Series([16, 26, 67], index=["Rayssa", "Gael", "Davi"])

print(s)

Resultado:

Rayssa    16
Gael      26
Davi      67

Nesse exemplo, 16, 26 e 67 são os dados da Series, enquanto Rayssa, Gael e Davi são os índices.

Também é possível acessar um valor utilizando seu índice:

print(s["Gael"])

Resultado:

26

## 4. Exemplos de uso

O Pandas permite realizar operações e análises nos dados de uma forma simples.

#Exemplo
import pandas as pd

dados = {
    "nome": ["Rayssa", "Gael", "Davi"],
    "idade": [20, 25, 19]
}

tabela = pd.DataFrame(dados)

print(tabela["idade"].mean())
print(tabela["idade"].max())
print(tabela["idade"].min())

Os métodos utilizados são:

.mean() → calcula a média dos valores.
.max() → encontra o maior valor.
.min() → encontra o menor valor.

Resultados:

21.333333333333332
25
19
Nesse exemplo, a média das idades de Rayssa, Gael e Davi é aproximadamente 21,33, o maior valor é 25 e o menor é 19.


## 5. Estrutura interna do Pandas

No arquivo pandas/core/frame.py, o DataFrame é implementado como uma classe chamada DataFrame.

class DataFrame(NDFrame, OpsMixin):

Isso mostra que DataFrame é uma classe e que ela herda de NDFrame e OpsMixin.

#Parâmetros do DataFrame

Na construção de um DataFrame, os principais parâmetros são:

data: dados que serão utilizados para construir o DataFrame.
index: índices das linhas.
columns: rótulos ou nomes das colunas.
dtype: tipo dos dados.
copy: controla a cópia dos dados.

O parâmetro columns representa os rótulos ou nomes das colunas do DataFrame.

No nosso exemplo, as colunas são nome e idade. Os nomes de Rayssa, Gael e Davi são os dados armazenados dentro da coluna nome.

dados = {
    "nome": ["Rayssa", "Gael", "Davi"],
    "idade": [20, 25, 19]
}


##Estrutura do projeto

O Pandas é dividido em diferentes pastas e arquivos que organizam suas funcionalidades.

A pasta core contém partes centrais da biblioteca, incluindo os arquivos series.py, relacionado à estrutura Series, e frame.py, relacionado ao DataFrame.

A pasta io está relacionada às funcionalidades de entrada e saída de dados.


#Método __init__

O método __init__ é usado para inicializar o objeto DataFrame.

Ele recebe os dados e outros parâmetros e, durante a construção do DataFrame, verifica o tipo de dado recebido para decidir como esses dados serão processados.

No código-fonte, o __init__ recebe data, index, columns, dtype e copy e trata diferentes tipos de entrada, como dicionários, arrays e Series.


#Funcionamento interno

Quando um DataFrame é criado, o método __init__ recebe os dados.

Quando o parâmetro data é um dicionário, o código identifica esse tipo de entrada e chama a função dict_to_mgr(), localizada em pandas/core/internals/construction.py.

Isso mostra que a construção do DataFrame é dividida em diferentes etapas e funções internas do Pandas.

O processo pode ser representado assim:

pd.DataFrame(dados)
        ↓
classe DataFrame
        ↓
método __init__()
        ↓
verificação do tipo de data
        ↓
dict_to_mgr()
        ↓
continuação da construção do DataFrame


## 6. Conclusão

O Pandas é uma biblioteca Python voltada para o trabalho e a análise de dados.

Durante a pesquisa, foi possível entender suas principais estruturas, como DataFrame e Series, além de observar como elas são implementadas no código-fonte.

Os testes realizados também mostraram que o Pandas permite organizar e analisar dados de maneira prática, utilizando recursos como mean(), max() e min().

A pesquisa também permitiu observar que o funcionamento do Pandas é dividido em diferentes classes, métodos, arquivos e funções internas que trabalham em conjunto para processar os dados.


## 7. Referências
Documentação oficial do Pandas: https://pandas.pydata.org/docs/
Código-fonte do Pandas no GitHub: https://github.com/pandas-dev/pandas
Arquivo frame.py: https://github.com/pandas-dev/pandas/blob/v3.0.5/pandas/core/frame.py
Arquivo construction.py: https://github.com/pandas-dev/pandas/blob/v3.0.5/pandas/core/internals/construction.py
Documentação 3.0.5 Pandas: https://pandas.pydata.org/docs/reference/api/pandas.Series.htm
