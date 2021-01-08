# -*- coding: utf-8 -*-

from numpy import genfromtxt, nanmean, isnan, nanstd, nanmin, nanmax

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

array_climat_si = genfromtxt('data/inputs/Climat - SI.csv', delimiter=';', dtype=float, skip_header=True)

avg_on_months = nanmean(array_climat_si, axis=0)
print('Moyenne par mois:\n')
for i, avg_on_month in enumerate(avg_on_months, start=0):
    print(months[i] + " : " + str(avg_on_month))

std_on_months = nanstd(array_climat_si, axis=0)
print('\n\nEcart-type par mois:\n')
for i, std_on_months in enumerate(std_on_months, start=0):
    print(months[i] + " : " + str(std_on_months))

print('\n\nMin & Max par mois:\n')
for i, month in enumerate(months, start=0):
    print("\n{}".format(month))
    print("Min : " + str(nanmin(array_climat_si[:, i])))
    print("Max : " + str(nanmax(array_climat_si[:, i])))

year_climat_si = array_climat_si[~isnan(array_climat_si)]
print('\n')
print("Year Min : " + str(nanmin(year_climat_si)))
print("Year Max : " + str(nanmax(year_climat_si)))