#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app_t9.py
#  
#  Copyright 2021 Vitória <Vitória@DESKTOP-8NUNN4I>
#
#  Autora: Vitória Isabel Lemos de Mattos
#  Matricula: 20201tiimi0195
#
# Este programa: Cria, preenche, ordena e imprime um conjunto de dados por meio de manipulação de arquivos.

###########################
#Código fonte em Python 3
###########################

import mod_t1
def main():
	arqIn = input()
	arqOut = input()
	
	dados = open(arqIn, "r") # Arrumar nome dos arquivos
	escrita = open(arqOut, "w")
	
	cadastroCU =  mod_t1.criaPreenche(dados)
	mod_t1.ordena_lista(cadastroCU)
	mod_t1.imprima(cadastroCU, escrita)
	
	# Fechando os arquivos de entrada e saída
	dados.close()
	escrita.close()
if __name__ == "__main__":
	main()
