#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mod_t9.py
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

# Função cria e preenche
def criaPreenche(dados):

	# Declaração de variáveis
	carroU = list() # modelo do carro (str), preço de venda do carro ao consumidor (float) e o ano de fabricação do veículo (int)
	cadastroCU = list()
	modeloC = str()
	precoV = float()
	anoFabric = int()
	quantidade = int()

	# Processamento de leitura de arquivos 
	linha = dados.readline()
	quantidade = int(linha)

	# Entrada de dados
	for i in range(quantidade):
		linha = dados.readline()
		modeloC = str(linha)
		modeloC = modeloC[0:-1] #EAI?

		linha = dados.readline()
		precoV = float(linha)
		
		linha = dados.readline()
		anoFabric = int(linha)
	
		carroU = [modeloC, precoV, anoFabric]
		cadastroCU.append(carroU)
		
	return cadastroCU

def desconto(anoFabric):
	descontinho = (2021 - anoFabric) * 10.00
	return descontinho

def ordena_lista(cadastroCU):	# Declaração de variáveis
	descontoA1 = float(0.0)
	descontoA2 = float(0.0)
	auxiliar = list() # Lista para auxiliar as trocas
	trocas = 1
	
	while trocas != 0:
		trocas = 0
		
		#carroU = [modeloC, precoV, anoFabric]
		for i in range(len(cadastroCU)-1):
			precoT1 = cadastroCU[i][1] - desconto(cadastroCU[i][2]) 
			precoT2 = cadastroCU[i + 1][1] - desconto(cadastroCU[i + 1][2]) 
			
			if precoT1 < precoT2: 
				auxiliar = cadastroCU[i] 
				cadastroCU[i] = cadastroCU[i + 1]
				cadastroCU[i + 1] = auxiliar
				trocas = trocas + 1

def imprima(cadastroCU, escrita):
	
	# Declaração de variáveis
	lucroTotal = float(0.0) 
	c = float(0.0) 
	precoDesconto = float(0.0)
	ano = int(0)
	
	for i in cadastroCU:
		precoOriginal = i[1]
		precoDesconto = desconto(i[2])
		
		# Entrada de dados 
		c = (precoOriginal - precoDesconto) # preço original - desconto
		lucroTotal = c  + lucroTotal
		
		# Saída
		print(f'Modelo: {i[0]}') # Nome do produto
		print(f'Preco final: {(c):.2f}') # Preço final
		
	print(f'Total em vendas: {lucroTotal}')
