#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    lista_pessoas = []

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista_pessoas.append(self)

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[apelido_endereco] = end
        return self.__enderecos[apelido_endereco]

    def remover_endereco(self, apelido_endereco):
        del self.__enderecos[apelido_endereco]
        return f'Endereço {apelido_endereco} deletado com sucesso!'

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[apelido_endereco]


    def listar_enderecos(self):
        return list(self.__enderecos.values())

    
    def __str__(self):
        return f'{self.nome}'
    
    @classmethod
    def busca_nome(cls, string):
        resultados = []
        string = string.capitalize()
        for pessoa in cls.lista_pessoas:
            nome_pessoa = pessoa.nome.capitalize()
            if string == nome_pessoa[:len(string)]:
                resultados.append(pessoa)
        return resultados

    