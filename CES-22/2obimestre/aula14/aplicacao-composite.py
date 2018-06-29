
# classe abstrata
class arquivoComponent:
    def __init__(self):
        self.nome = None
        self.tipo = None

    # funções comuns a arquivos e pastas
    def getNomeArquivo(self):
        print("Nome do arquivo: %s",self.nome)
        return self.nome

    def getTipo(self):
        print("arquivo do tipo %s!" % self.tipo)

    # funções exclusivas de pastas
    def getArquivo(self, nome):
        print("impossivel obter o arquivo %s! (operação válida somente para pastas)" % nome)
        return None

    def addArquivo(self, nome):
        print("impossível adicionar o arquivo %s. (operação válida somente para pastas)" % nome)
        return None

    def removeArquivo(self, nome):
        print("impossível remover o arquivo! (operação válida somente para pastas)")
        return None

# classe concreta
class arquivoVideo(arquivoComponent):
    def __init__(self,nome):
        self.tipo = 'video'
        self.nome = nome

# classe concreta
class arquivoTexto(arquivoComponent):
    def __init__(self,nome):
        self.tipo = 'texto'
        self.nome = nome

# classe composita
class arquivoComposite(arquivoComponent):
    # define uma pasta
    def __init__(self, nome):
        self.nome = nome
        self.tipo = 'pasta'
        self.arquivos = {}

    # sobrescreve os arquivos
    def getArquivo(self, nome):
        return arquivos[nome]

    def getNomeArquivo(self):
        print("Nome da pasta: %s",self.nome)
        return self.nome

    def getArquivo(self, nome):
        if self.arquivos[nome]:
            print("arquivo existente na pasta")
            return nome
        else:
            print("arquivo inexistente na pasta")
            return None

    def addArquivo(self, nome):
        self.arquivos[nome] = nome
        print("arquivo %s adicionado na pasta %s!" % (nome, self.nome))
        return None

    def removeArquivo(self, nome):
        self.arquivos.pop(nome, None)
        print("arquivo deletado!")
        return None

    def listarArquivos(self):
        print(self.arquivos.keys())
        return None

if __name__ == '__main__':
    video = arquivoVideo('aula do possani')
    texto = arquivoTexto('lista de mat32')
    pasta = arquivoComposite('3 semestre')

    video.getTipo()
    texto.getTipo()
    pasta.getTipo()

    pasta.addArquivo('aula do possani')
    pasta.addArquivo('lista de mat32')
    video.addArquivo('aula do possani')
    video.removeArquivo('aula do possani')
    pasta.removeArquivo('aula do possani')
    pasta.listarArquivos()