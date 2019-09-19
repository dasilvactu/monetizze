# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:57:25 2019

@author: Marcus Vinicius
"""
from random import randint
class Loteria:
    __qtdDezenas = None # Número 1
    __resultado = None
    __totJogos = None
    __jogos = None
    def __init__(self, qtdDez, totJ): # numero 3
        if qtdDez<6 or qtdDez > 10:
            print("valor inválido")
            return
        else:
            self.__qtdDezenas = qtdDez
            self.__totJogos = totJ
    
    def getQtdDezenas(self): #número 2
        return self.__qtdDezenas
    def getResultado(self):
        return self.__resultado
    def getTotJogos(self):
        return self.__totJogos
    def getJogos(self):
        return self.__jogos
    
    def setQtdDezenas(self,val): # numero 2
        self.__qtdDezenas = val
    def setResultado(self,val):
        self.__resultado = val
    def setTotJogos(self,val):
        self.__totJogos = val
    def setJogos(self,val):
        self.__jogos = val
        
    def _retornaResult(self): # numero 4
        resultado = []
        while len(resultado) < self.__qtdDezenas:
            sorteado = randint(0,60)
            if sorteado in resultado:
                sorteado = randint(0,60)
            else:
                resultado.append(sorteado)
        resultado.sort()
        return resultado
    def preencheJogos(self): # Número 5
        qtd = self.__totJogos
        self.__jogos = []
        for i in range(qtd):
            self.__jogos.append(self._retornaResult())
    def sorteio(self): # numero 6
        result = []
        while len(result) < self.__qtdDezenas:
            sorteado = randint(0,60)
            if sorteado in result:
                sorteado = randint(0,60)
            else:
                result.append(sorteado)
        result.sort()
        self.__resultado = result
        
    ''' o que eu entendi dessa questão é que eu devo comparar o valor da variável 
    __resultado com todos os vetores da variável __jogos e contar a quantidade de 
    dezenas iguais que __resultado tem em cada posição de __jogos'''
    def confere(self):
        qtds = []
        for i in range(self.__totJogos):
            n = 0
            for j in range(self.__qtdDezenas):
                if self.__resultado[j] in self.__jogos[i]:
                    n = n+1
            qtds.append(n)
        tabela = ""
        tabela = tabela + "<html><head><title>Resultados Loteria</title></head><body>"
        tabela = tabela + "<table border = 1>"
        for i in range(self.__totJogos):
            tabela = tabela + "<tr>"
            tabela = tabela + "<td>" + str(self.__jogos[i]) + "</td>"
            tabela = tabela + "<td>" + str(qtds[i]) + "</td>"
            tabela = tabela + "</tr>"
        tabela = tabela + "</table></body></html>"
        return tabela.strip("[]")