class Professor:

    #Metoodo Inicializador:
    def __init__(self, nome, especialidade, funcao, formacao, idade, genero, trabalhando):
        self.setNome(nome)
        self._especialidade = especialidade
        self._funcao = funcao
        self._formacao = formacao
        self._idade = idade
        self._genero = genero
        self._trabalhando = trabalhando


    #Metoodo para visualizar dados:
    def relatorio(self):
        print("")
        print("#"*50)

        print(f"Nome: {self.getNome()}")
        print(f"Especialidade: {self.getEspecialiade()}")
        print(f"Formação: {self.getFormacao()}")
        print(f"Idade: {self.getIdade()}")
        print(f"Gênero: {self.getGenero()}")
        print(f"Trabalhando: {self.getTrabalhando()}")

        print("#"*50)

    #Metodos especiais:
    def ensinar():
        print("O professor esta ensinado.")
    
    def avaliar():
        print("O professor está avaliando.")
    
    def gerenciapessoas():
        print("O professor está administrando a turma.")

    def trabalhar():
        print("O professor esta trabalhando.")

    #Metodos acessores:

    @property
    def getNome(self):
        return self._nome   

    @property
    def getEspecialiade(self):
        return self._especialidade

    @property
    def getFuncao(self):
        return self._funcao
        
    @property
    def getFormacao(self):
        return self._formacao
    
    @property
    def getIdade(self):
        return self._idade

    @property
    def getGenero(self):
        return self._genero

    @property
    def getTrabalhando(self):
        return self._trabalhando


    @_nome.setter
    def setNome(self, nome):
        if(type(nome) == type(str())):
            self._nome = nome
        else:
            print("Campo nome Inválido!")

    @_especialidade.setter
    def setEspecialidade(self, especialidade):
        if(type(especialidade)) == type((str)):
            self._especialidade = especialidade

        
