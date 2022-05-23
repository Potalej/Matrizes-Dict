# Matrizes-Dict

Quando se trabalha com matrizes no Python, geralmente se as constrói com listas dentro de listas, à depender da ocasião e aplicação para definir qual é linha e qual é coluna.

Ocorre, no entanto, que quando se tem matrizes grandes e esparsas, há um desnecessário consumo de memória para a armazenar e um custo de processamento demasiado gasto com operações com estes zeros. Daí a necessidade de se pensar em outra forma de utilizar matrizes no Python.

Poderá se observar, porém, que não haverá forma possível de se superar determinados limites com as mudanças que serão propostas. O pacote NumPy (https://github.com/numpy/numpy), por exemplo, oferecerá melhores resultados independente do quão bem feita e otimizada estiver a estrutura das matrizes aqui realizadas (talvez com algumas raras exceções), pois sua superioridade em desempenho se deve não só à forma de indexação dos valores, mas em questões de baixo nível, às quais esse repositório não tange. Como forma alternativa bruta, criada para aprendizado, porém, a estrutura daqui oferece resultados interessantes.

<h2> Listas e Dicionários </h2>

As variáveis do tipo `list` no Python são literalmente listas e listas ordenadas, ou seja, possuem uma indexação bem definida pela ordem de chegada dos elementos. Assim, se tem-se uma lista `A = ["a", "b"]`, adicionar à A a string "c" (pelo método padrão) define automaticamente que `A[2]="c"`. Em muitas ocasiões, isto é positivo, mas não nesse caso.

Outras formas de se ter listas no Python podem ser pelos tipos `dict` e `set`, ambos não ordenados, mas com o primeiro sendo indexado e o segundo não. Isso significa que um dicionário `D = {0: "a", 1: "b"}` pode receber "c" em qualquer índice que for, podendo ser inclusive uma string, um int ou até uma tupla, enquanto que um conjunto `S = {"a", "b"}` pode receber "c" e será verdadeiro que `"c" in S`, mas não será possível encontrar esta string através da aplicação de um índice sobre `S`.

O fato do tipo `dict` ser indexável e, ainda, com tuplas, nos é bastante útil.

<h2>Estrutura básica e instanciamento</h2>

Quando se pensa na definição de uma matriz em abstrato, a única informação que se necessita é sua dimensão. Em muitos casos, não é exatamente importante se uma matriz tem entradas reais, complexas ou além, mas é sempre importante saber suas medidas, já que estas não podem (ou não deveriam) ser mutáveis.

Dessa forma, o tipo proposto aqui recebe, de uma forma ou de outra, o tamanho da matriz que se busca utilizar.

```python
M = MatrizDict(lins = qntd_linhas, cols = qntd_colunas)
```

Os outros dois parâmetros que podem ser passados são `matrizBase` e `colunas`, ambos do tipo `list`:

- `matrizBase`: A forma em listas já citada anteriormente é bastante mais intuitiva visualmente, e em muitos casos é mais simples desenvolve-la a priori e apenas depois trabalhar com esta em sua forma de dicionário. Por isso, pode-se passar uma matriz escrita desta forma através desse parâmetro e se a terá em forma um pouco mais otimizada, quando possível;
- `colunas`: É bastante recorrente a representação de conjuntos de vetores como matrizes-colunas de uma matriz maior, então caso se tenha uma lista de vetores (de tipo `MatrizDict`!) e se queira construir uma matriz a partir dela, pode-se utilizar esse parâmetro.
