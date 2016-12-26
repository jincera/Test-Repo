#!/usr/bin/python
#
# Toma datos de la entrada <key\tval> y los procesa
# Como val solo es "1" para la ocurrencia de un candidato,
# el procesamiento simplemente es un acumulador
# 
# Recuerde que los datos ya llegan ordenados, por lo que
# al detectar cambio de candidato, se despliega el resultado

import sys

Acumulados = 0
candidatoAnt = None

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        # Hay algo raro, ignora esta linea
        continue

    esteCandidato, esteValor  = DataIn

    if candidatoAnt and candidatoAnt != esteCandidato:
        print candidatoAnt, "\t", Acumulados
        candidatoAnt = esteCandidato;
        Acumulados = 0

    candidatoAnt = esteCandidato
    Acumulados += 1

if candidatoAnt != None:
    print candidatoAnt, "\t", Acumulados

