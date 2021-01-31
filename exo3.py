# -*- coding: utf-8 -*-
import numpy as np

def checkIsNumber(cell_value):
  try:
    int(cell_value)
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
        new_cell_value = np.nanmean([int(array[i][j-1]), int(array[i][j+1])])
        array[i][j] = int(new_cell_value)

def patchImpossibleValue(array):
  for i, month in enumerate(array, start=0):
    std_on_month = np.nanstd(month)
    for j, day in enumerate(month, start=0):
      if not np.isnan(day) and j!=0 and not checkIsPossibleValue(std_on_month, array[i][j-1], day):
       new_cell_value = np.nanmean([array[i][j-1], array[i][j+1]])
       array[i][j] = int(new_cell_value)


months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
array_climat_si = np.genfromtxt('data/inputs/Climat - SI erreur.csv', delimiter=';', dtype=str, skip_header=True)
array_climat_si = np.transpose(array_climat_si)
patchArrayAsNumber(array_climat_si)
np.savetxt("data/outputs/Climat_SI_Erreur_Patch.csv", np.transpose(array_climat_si), delimiter=";", fmt="%s")
array_climat_si = np.genfromtxt('data/outputs/Climat_SI_Erreur_Patch.csv', delimiter=';', dtype=float)
array_climat_si = np.transpose(array_climat_si)
patchImpossibleValue(array_climat_si)
np.savetxt("data/outputs/Climat_SI_Erreur_Patch.csv", np.transpose(array_climat_si), delimiter=";", fmt="%.0f")

