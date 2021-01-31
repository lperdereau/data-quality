# -*- coding: utf-8 -*-

import argparse
from numpy import genfromtxt
from graph_ui import generate_ui


parser = argparse.ArgumentParser()
parser.add_argument("--csv", help="Path to the csv file")
args = parser.parse_args()

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

array_climat_si = genfromtxt(args.csv, delimiter=';', dtype=float, skip_header=True)

generate_ui(months, array_climat_si)