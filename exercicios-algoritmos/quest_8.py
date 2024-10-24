# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores
# relativos em outras medidas.
# Ex:
# Digite uma distância em metros: 185.72
# A distância de 85.7m corresponde a:
# 1857.2dm
# 0.18572Km
# 18572.0cm
# 1.8572Hm
# 185720.0mm
# 18.572Dam

dist_m = float(input("Digite a distância em metros: "))
dist_dm = dist_m * 10
dist_km = dist_m * 0.001
dist_cm = dist_m * 100
dist_hm = dist_m * 0.01
dist_mm = dist_m * 1000
dist_dam = dist_m * 0.1

print(f"{dist_m} m = {dist_dm} dm.")
print(f"{dist_m} m = {dist_km} km.")
print(f"{dist_m} m = {dist_cm} cm.")
print(f"{dist_m} m = {dist_hm} hm.")
print(f"{dist_m} m = {dist_mm} mm.")
print(f"{dist_m} m = {dist_dam} dam.")