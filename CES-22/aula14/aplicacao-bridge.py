

# classe abstrata que serve de interface
class texto_estilizado:
    def escreve_texto(self, texto):
        raise NotImplemented()

# diferente implementação
class textoReverso(texto_estilizado):
    def escreve_texto(self, texto):
        texto_reverso = "".join(reversed(texto))
        print(texto_reverso)

# diferente implementação
class textoNormal(texto_estilizado):
    def escreve_texto(self, texto):
        print(texto)

# diferente implementação
class textoMaiuscula(texto_estilizado):
    def escreve_texto(self, texto):
        print(texto.upper())

# interface concreta
class textWriter:
    def __init__(self, estilo):
        self.estilo = estilo

    def escreve_frase(self, frase):
        self.estilo.escreve_texto(frase)

if __name__ == '__main__':
    escritor1 = textWriter(textoReverso())
    escritor2 = textWriter(textoNormal())
    escritor3 = textWriter(textoMaiuscula())
    escritor1.escreve_frase("essa frase deve ser escrita reversa")
    escritor2.escreve_frase("essa frase deve ser escrita normal")
    escritor3.escreve_frase("essa frase deve ser escrita maisucula")
