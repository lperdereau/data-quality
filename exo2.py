# -*- coding: utf-8 -*-

from numpy import genfromtxt
from graph_ui import generate_ui

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

array_climat_si = genfromtxt('data/inputs/Climat - SI.csv', delimiter=';', dtype=float, skip_header=True)

generate_ui(months, array_climat_si)