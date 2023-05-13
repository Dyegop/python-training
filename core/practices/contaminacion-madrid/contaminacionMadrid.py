"""
Proceso para analizar datos relativos niveles de NO2 en Madrid
Descargar archivo zip de: https://datos.madrid.es/portal/site/egob Catálogo de datos > Calidad del
 aire. Datos horarios años 2001 a 2021
"""

import pandas as pd
import os
from typing import List
from zipfile import ZipFile, BadZipFile



DATA_EXTRACTED = "data/extracted"


def extracZip(source: str, destination: str):
    """Extrae archivo zip a la ruta indicada"""
    try:
        with ZipFile(source, 'r') as z:
            print("Extracting zip file")
            z.extractall(destination)
            print("Done")
    except BadZipFile:
        print("Error extracting zipfile")
        raise

def getDataframe(rute: str, filelist: List[str]):
    """Genera un dataframe en base a una serie de ficheros csv"""
    print("Creating dataframe")
    df_list = []
    for file in filelist:
        try:
            if ".csv" in file:
                df_list.append(pd.read_csv(f"{rute}/{file}", sep=";"))
        except FileExistsError:
            print(f"File {file} not found")
    print("Done")
    return pd.concat(df_list)




if __name__ == "__main__":
    # Extraemos el fichero zip
    extracZip("Anio201810.zip", "data")
    # Generamos un dataframe con los datos. En este caso, he elegido utilizar los datos de los csv
    df = getDataframe(DATA_EXTRACTED, os.listdir(DATA_EXTRACTED))
    # Filtramos valores para NO2 (campo magnitud == 8) y ordenamos por mes y día
    print("Filtering and cleaning data")
    df2 = df.loc[df["MAGNITUD"] == 8].sort_values(by=['MES', 'DIA'], ascending=[True, True])
    # Filtramos valores válidos
    # Se condieran validos aquellos valoros donde los valores de las columnas V01, V02 ... V24 sean "V"
    for i in [f"V{x:02}" for x in range(1, 25)]:
        df2 = df2[df2[i] == "V"]
    print("Exporting results to csv")
    # Exportamos datos a un csv con los resultados
    # De esta forma se pueden cargar rápidamente los valores con otra software para su visualización
    # En caso de necesitar su almacenamiento de manera prolongada, obtaría por programar su ingesta en una BBDD
    # Se podría utilizar cualquier conector python para la BBDD requerida y crear un proceso que automatice la carga
    df2.to_csv("results.csv", index=False, sep=";",
               columns=["PROVINCIA", "MUNICIPIO", "ESTACION", "MAGNITUD", "PUNTO_MUESTREO", "ANO", "MES", "DIA"] +
                       [f"H{x:02}" for x in range(1, 25)])
