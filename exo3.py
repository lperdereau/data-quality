# -*- coding: utf-8 -*-
import argparse
import ntpath
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("--csv", help="Path to the csv file", required=True)
parser.add_argument("--fr", help="The file has temperature in Fahrenheit")
args = parser.parse_args()

def checkIsNumber(cell_value):
  try:
    float(cell_value)
    return True
  except:
    return False

def checkIsPossibleValue(std, cell_value_yesterday, cell_value):
  cell_range_min = cell_value_yesterday - (std * 3)
  cell_range_max = cell_value_yesterday + (std * 3)
  return cell_range_min < cell_value < cell_range_max

def patchArrayAsNumber(array):
  for i, month in enumerate(array, start=0):
    for j, day in enumerate(month, start=0):
      if not day == "" and not checkIsNumber(day):
        new_cell_value = np.nanmean([float(array[i][j-1]), float(array[i][j+1])])
        array[i][j] = float(new_cell_value)

def patchImpossibleValue(array):
  for i, month in enumerate(array, start=0):
    std_on_month = np.nanstd(month)
    for j, day in enumerate(month, start=0):
      if not np.isnan(day) and j!=0 and not checkIsPossibleValue(std_on_month, array[i][j-1], day):
       new_cell_value = np.nanmean([array[i][j-1], array[i][j+1]])
       array[i][j] = float(new_cell_value)

def fahrenheitToCelsius(value):
    return np.round((value - 32) / 1.8, 2)

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
array_climat_si = np.genfromtxt(args.csv, delimiter=';', dtype=str, skip_header=True)
array_climat_si = np.transpose(array_climat_si)
patchArrayAsNumber(array_climat_si)

if args.fr:
  for i, month in enumerate(array_climat_si, start=0):
    for j, day in enumerate(month, start=0):
      if array_climat_si[i][j] != '':
        array_climat_si[i][j] = fahrenheitToCelsius(float(array_climat_si[i][j]))

output_file = f"data/outputs/{ntpath.basename(args.csv)}"
np.savetxt(output_file, np.transpose(array_climat_si), delimiter=";", fmt="%s")
array_climat_si = np.genfromtxt(output_file, delimiter=';', dtype=float)
array_climat_si = np.transpose(array_climat_si)
patchImpossibleValue(array_climat_si)
np.savetxt(output_file, np.transpose(array_climat_si), header=";".join(months), delimiter=";", fmt="%.2f")

