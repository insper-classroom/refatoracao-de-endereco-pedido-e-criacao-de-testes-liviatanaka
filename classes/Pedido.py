#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re



class Pedido:
    EM_ABERTO = 1
    PAGO = 2
    
    def __init__(self, conta_pessoa: PessoaFisica, carrinho: Carrinho):
        self.pessoa = conta_pessoa
        self.carrinho = carrinho
        self.endereco_entrega = None
        self.endereco_faturamento = None
        self.status = Pedido.EM_ABERTO
    
    
    def __str__(self) :
        return f'Cliente: {self.pessoa.nome}\n Endereços: {self.endereco_entrega} e {self.endereco_faturamento}\n Produtos: {self.carrinho.get_itens()}'
    