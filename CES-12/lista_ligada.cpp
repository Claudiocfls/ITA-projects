#include <stdio.h>

class noh{
public:
	int valor;
	noh* proximo_noh;
	noh(int valor){
		this->valor = valor;
		this->proximo_noh = NULL;
	}
	noh(){
		this->proximo_noh = NULL;
		this->valor = -1;
	}
};

class lista_ligada{
public:
	int tamanho;
	noh* ultimo;
	noh* add;
	noh noh_cabeca;
	lista_ligada(){
		this->ultimo = &this->noh_cabeca;
		this->tamanho = 0;
	}
	void adiciona(int valor){
		this->add = new noh(valor);
		this->ultimo->proximo_noh = add;
		this->ultimo = add;
		this->add = NULL;
		this->tamanho++;
	}
	int top(){
		if (tamanho > 0){
			return noh_cabeca.proximo_noh->valor;
		}
		return -1;
	}
	void pop(){
		if (tamanho > 0){
			noh* remove = noh_cabeca.proximo_noh;
			noh_cabeca.proximo_noh = noh_cabeca.proximo_noh->proximo_noh;
			if (ultimo == remove){
				ultimo = &noh_cabeca;
			}
			delete remove;
			tamanho--;
		}
	}

};

int main(){
	return 0;
}