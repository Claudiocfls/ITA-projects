
class Reader:
    def __init__(self, mediador):
        raise NotImplemented()

    def enviar_mensagem(self, texto):
        print("%s diz: %s " % (self.nome,texto))
        self.mediador.enviar(self.nome, texto)

    def receber_mensagem(self, texto):
        print("%s recebeu %s " % (self.nome,texto))

# objeto que só consegue se comunicar com uppercase
class upperReader(Reader):
    def __init__(self,mediador):
        self.mediador = mediador
        self.nome = 'Arnaldo'
        self.protocolo = 'upperReader'

# objeto que só consegue se comunicar em lowercase
class lowerReader(Reader):
    def __init__(self,mediador):
        self.mediador = mediador
        self.nome = 'Bernaldo'
        self.protocolo = 'lowerReader'

class Mediador:
    def __init__(self):
        self.nodes = []

    def adiciona_node(self, node):
        self.nodes.append(node)

    def enviar(self, nome, texto):

        for node in self.nodes:
            if node.protocolo == 'lowerReader' and node.nome != nome:
                mensagem = texto.lower()
                node.receber_mensagem(mensagem)
            elif node.protocolo == 'upperReader' and node.nome != nome:
                mensagem = texto.upper()
                node.receber_mensagem(mensagem)

if __name__=="__main__":

    mediador = Mediador()
    contato1 = upperReader(mediador)
    contato2 = lowerReader(mediador)

    mediador.adiciona_node(contato1)
    mediador.adiciona_node(contato2)


    contato1.enviar_mensagem("TEXTO MAISCULO")
    contato2.enviar_mensagem("frase minuscula")
