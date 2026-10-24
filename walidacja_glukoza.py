# mmol/l -> 3.9-5.6
# mg/dl -> 70-100
# 1. wprowadzić wartość do programu 
# 2. decyzja -> jaka jednostka? wartość graniczna: 30
# 3. Podać wynik walidacji

podana_wartosc = input('Proszę podać wartość stężenia glukozy: ')
print(podana_wartosc)
podana_wartosc = float(podana_wartosc)
# print(type(podana_wartosc))

if podana_wartosc > 30:
    jedn = 'mg/dl'
    dolna_granica = 70
    gorna_granica = 100
else:
    jedn = 'mmol/l'
    dolna_granica = 3.9
    gorna_granica = 5.6
