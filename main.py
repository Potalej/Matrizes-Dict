class MatrizDict:
  """
    O tipo `MatrizDict` demanda menos memória para armazenar e operar com matrizes
    esparsas que os tipos tradicionais, pois utiliza `dicts` em vez de `lists`.
  """
  def __init__(self, matriz_base=[], lins=1, cols=1, colunas=[]):
    """
      Para inicializar, é importante informar o tamanho da matriz para operações
      futuras. Elementos podem ser adicionados à posteriori (NÃO RECOMENDÁVEL), mas manter
      uma estrutura fixa é importante.
      Se desejado, é possível informar uma matriz no formato de lista para que
      seja feita a conversão através do parâmetro `matriz_base`. Caso seja passado um
      vetor, este será convertido para uma matriz coluna.
      Pode receber também uma lista de vetores colunas do tipo `MatrizDict` e os
      converte numa só matriz, mas nesse caso é preciso informar o número de linhas.
    """
    # define tamanho
    self.lins = lins
    self.cols = cols
    # onde é armazenada a matriz
    self.matriz = dict()
    
    # verifica se foi informada alguma matriz de base
    if len(matriz_base) > 0:
      # caso seja, é preciso verificar se foi passado um vetor ou uma matriz
      try: matriz_base[0][0]
      except: self.cols = 1 # caso seja um vetor, a quantidade de colunas é 1
      else: self.cols = len(matriz_base[0]) # caso seja uma matriz, a quantidade de colunas é padrão
 
      # a quantidade de linhas é essa daí mesmo
      self.lins = len(matriz_base)
      # e faz a conversão
      self.__converter(matriz_base, False if self.cols == 1 else True)
    
    # verifica se a lista de colunas tem algo
    elif len(colunas) > 0:
      # seta a quantidade de colunas da matriz
      self.cols = len(colunas)
      # percorre os vetores
      for col,v in enumerate(colunas):
        # percorre os componentes de cada coluna e vai adicionando
        # como a quantidade de linhas será a mesma de A, é necessário te-la passado
        for i in range(self.lins): if v[i,0] != 0: self.matriz[i, col] = v[i,0]
            

  def __converter(self, matrizBase, matriz=True):
    """
      Aqui pode ser feita a conversão de uma matriz da forma de lista para uma
      do tipo `MatrizDict` durante o instanciamento da classe.
    """
    # se for uma matriz, tem que percorrer também as colunas
    if matriz:
      # percorre as linhas
      for i in range(self.lins):
        for j in range(self.cols): 
          # se não for nulo, adiciona
          if matrizBase[i][j] != 0: self[i,j] = matrizBase[i][j]
    # se não for, pode adicionar direto percorrendo as linhas
    else:
      for i in range(self.lins):
        # caso não seja nulo, evidentemente
        if matrizBase[i]: self[i,0] = matrizBase[i]
          
  # exibição da matriz
  def __str__(self):
    """Função que deixa a matriz bonitinha na hora do print.""" 
    str_final = '['+'{:4}]\n['.format("").join([''.join(['{:5}'.format(self[coluna,linha]) for coluna in range(self.cols)]) 
      for linha in self.lins])+"{:4}]".format("")
    return str_final
  
  # funcionalidades básicas de uma matriz
  def __getitem__(self, indice):
    """Capturar elementos da matriz é o mínimo."""
    # verifica se o índice está na lista de chaves do dicionário
    if indice in self.matriz.keys(): return self.matriz[indice]
    # se não for o caso mas o índice estiver no escopo da matriz, retorna 0
    elif 0 <= indice[0] < self.lins and 0 <= indice[1] < self.cols: return 0
    # se não for o caso novamente, então o índice não faz parte da matriz
    else: raise Exception("O índice informado não faz parte da matriz.")
  
  def __setitem__(self, indice, valor):
    """Ser capaz de alterar um valor da matriz também é básico."""
    # caso o valor seja nulo
    if valor == 0: return
    # verifica se o índice está compreendido na matriz, e se estiver atribui
    elif 0 <= indice[0] < self.lins and 0 <= indice[1] < self.cols: self.matriz[indice] = valor
    # caso não, dá erro
    else: raise Exception("O índice informado não faz parte da matriz.")

  # algumas operações unárias a seguir
  def T(self):
    """
      Retorna a transposta da matriz.
    """
    # cria uma nova matriz
    transposta = MatrizDict(lins=self.cols, cols=self.lins)
    # a transposta vai ser a troca de índices
    for i in range(self.lins):
      for j in range(self.cols):
        if self[i,j] != 0:
          transposta[j,i] = self[i,j]
    return transposta
