import pandas as pd
import geopandas as gpd
from shapely.geometry import box

data = {
    "Nazwa_warstwy": [],
    "Rodzaj_geometrii": [],
    "Ilosc_obiektow": [],
    "Srednia_powierzchnia_obiektow": [],
    "Srednia_dlugosc_obiektow": [],
    "Srednia_zlozonosc_linii": [],
    "Srednie_wypelnienie_przestrzeni": []
}

df = pd.DataFrame(data)

adja_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_ADJA_A.shp")
adms_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_ADMS_A.shp")
adms_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_ADMS_P.shp")
bubd_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUBD_A.shp")
buhd_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUHD_L.shp")
buib_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUIB_A.shp")
buib_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUIB_L.shp")
buin_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUIN_L.shp")
buit_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUIT_A.shp")
buit_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUIT_P.shp")
busp_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUSP_A.shp")
busp_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUSP_L.shp")
butr_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUTR_L.shp")
buuo_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUUO_L.shp")
buwt_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUWT_P.shp")
buzm_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUZM_L.shp")
buzt_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUZT_A.shp")
buzt_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_BUZT_P.shp")
kuho_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUHO_A.shp")
kuhu_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUHU_A.shp")
kuko_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUKO_A.shp")
kuko_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUKO_P.shp")
kumn_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUMN_A.shp")
kuos_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUOS_A.shp")
kuoz_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUOZ_A.shp")
kupg_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUPG_A.shp")
kupg_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUPG_P.shp")
kusc_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUSC_A.shp")
kusk_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUSK_A.shp")
kuza_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_KUZA_A.shp")
oikm_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_OIKM_A.shp")
oikm_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_OIKM_P.shp")
oimk_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_OIMK_A.shp")
oior_a = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_OIOR_A.shp")
oior_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_OIOR_L.shp")
oior_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_OIOR_P.shp")
oipr_l = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_OIPR_L.shp")
oipr_p = gpd.read_file("3024_SHP/PL.PZGiK.308.BDOT10k.3024__OT_OIPR_P.shp")

lista_warstw_poligonowych = (adja_a, adms_a, bubd_a, buib_a, buit_a, busp_a, buzt_a, kuho_a, kuhu_a, kuko_a, kumn_a, kuos_a, kuoz_a, kupg_a, kusc_a, kusk_a, kuza_a, oikm_a, oimk_a, oior_a)
lista_warstw_liniowych = (buhd_l, buib_l, buin_l, busp_l, butr_l, buuo_l, buzm_l, oior_l, oipr_l)
lista_warstw_punktowych = (adms_p, buit_p, buwt_p, buzt_p, kuko_p, kupg_p, oikm_p, oior_p, oipr_p)

lista_nazw = []
lista_geometrii = []
lista_ilosci = []
lista_powierzchni = []
lista_dlugosci = []
lista_linii = []
lista_wypelnien = []

for i in lista_warstw_poligonowych:
    lista_geometrii.append("Poligon")
    lista_ilosci.append(len(i))
    i["powierzchnia"] = i.geometry.area
    lista_powierzchni.append(sum(i["powierzchnia"]) / len(i))
    lista_dlugosci.append("brak")

for i in lista_warstw_liniowych:
    lista_geometrii.append("Linia")
    lista_ilosci.append(len(i))
    i["dlugosc"] = i.geometry.length
    lista_powierzchni.append("brak")
    lista_dlugosci.append(sum(i["dlugosc"]) / len(i))

for i in lista_warstw_punktowych:
    lista_geometrii.append("Punkt")
    lista_ilosci.append(len(i))
    lista_powierzchni.append("brak")
    lista_dlugosci.append("brak")

df["Nazwa_warstwy"] = lista_nazw
df["Rodzaj_geometrii"] = lista_geometrii
df["Ilosc_obiektow"] = lista_ilosci
df["Srednia_powierzchnia_obiektow"] = lista_powierzchni
df["Srednia_dlugosc_obiektow"] = lista_dlugosci

print(df)