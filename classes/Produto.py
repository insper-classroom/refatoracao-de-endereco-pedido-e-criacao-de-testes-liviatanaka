#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    lista_produtos = []

    def __init__(self, id_produto, nome, preco=''):
        self.__id = id_produto
        self.nome = nome
        self.preco = preco
        Produto.lista_produtos.append(self)

    # ID 
    def set_id(self, id_novo):
        self.__id = id_novo
    
    def get_id(self):
        return self.__id

    def to_dict(self):
        return {'Id':self.__id, 'Nome': self.nome}

    @classmethod
    def busca_nome(cls, string):
        resultados = []
        string = string.capitalize()
        for produto in cls.lista_produtos:
            nome = produto.nome.capitalize()
            if string == nome[:len(string)]:
                resultados.append(produto)
        return resultados
