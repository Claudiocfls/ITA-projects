

class estado_do_copo:
    def cair(self):
        raise NotImplemented()
    def encher(self):
        raise NotImplemented()
    def esvaziar(self):
        raise NotImplemented()

class copo_cheio(estado_do_copo):
    def cair(self):
        print("copo quebrado")
        copo = copo_quebrado()
        return copo
    def encher(self):
        print("copo cheio")
        copo = copo_cheio()
        return copo
    def esvaziar(self):
        print("copo vazio")
        copo = copo_vazio()
        return copo

class copo_vazio(estado_do_copo):
    def cair(self):
        print("copo quebrado")
        copo = copo_quebrado()
        return copo
    def encher(self):
        print("copo cheio")
        copo = copo_cheio()
        return copo
    def esvaziar(self):
        print("copo vazio")
        copo = copo_vazio()
        return copo

class copo_quebrado(estado_do_copo):
    def cair(self):
        print("copo quebrado")
        copo = copo_quebrado()
        return copo
    def encher(self):
        print("copo quebrado")
        copo = copo_quebrado()
        return copo
    def esvaziar(self):
        print("copo quebrado")
        copo = copo_quebrado()
        return copo

class copo(estado_do_copo):
    def __init__(self):
        self.estado = copo_vazio()

    def copo_cair(self):
        self.estado =  self.estado.cair()
    def copo_encher(self):
        self.estado =  self.estado.encher()
    def copo_esvaziar(self):
        self.estado =  self.estado.esvaziar()

if __name__=='__main__':
    copo = copo()
    copo.copo_encher()
    copo.copo_esvaziar()
    copo.copo_encher()
    copo.copo_esvaziar()
    copo.copo_cair()
    copo.copo_encher()
    copo.copo_esvaziar()

