import pandas as pd
import os

class Limpieza:

    def Limpieza_matricula(self):
        # === RUTA DEL ARCHIVO DE ENTRADA ===
        archivo_entrada = "C:\\Users\\kenda\\OneDrive\\CUC\\Cuatri 4\\BD\\Progra_2\\Proyecto_final\\Proyecto_educacion\\data\\raw\\BD_Matrícula_Sector_Estatal_2021_2024.xlsx"

        # === LEER EL ARCHIVO EXCEL ===
        df = pd.read_excel(archivo_entrada, sheet_name="Archivo 2021-2024")

        # === SELECCIONAR SOLO LAS COLUMNAS POR ÍNDICE (0,2,6,7,8,16) ===
        columnas_deseadas = [0, 2, 6, 7, 8, 16]
        df_filtrado = df.iloc[:, columnas_deseadas]

        # === DEFINIR RUTA DE SALIDA ===
        carpeta_salida = "C:\\Users\\kenda\\OneDrive\\CUC\\Cuatri 4\\BD\\Progra_2\\Proyecto_final\\Proyecto_educacion\\data\\processed"
        archivo_salida = os.path.join(carpeta_salida, "Matriculas.csv")

        # === CREAR CARPETA SI NO EXISTE ===
        os.makedirs(carpeta_salida, exist_ok=True)

        # === GUARDAR EL RESULTADO EN CSV ===
        df_filtrado.to_csv(archivo_salida, index=False, encoding="utf-8-sig")
        print(f"Archivo guardado en: {archivo_salida}")

    def Limpieza_graduados(self):
        # === RUTA DEL ARCHIVO DE ENTRADA ===
        archivo_entrada = "C:\\Users\\kenda\\OneDrive\\CUC\\Cuatri 4\\BD\\Progra_2\\Proyecto_final\\Proyecto_educacion\\data\\raw\\BD_Diplomas_sector_estatal_y_privado_2021_2024.xlsx"

        # === LEER EL ARCHIVO EXCEL ===
        df = pd.read_excel(archivo_entrada, sheet_name="Diplomas 2021-2023")

        # === SELECCIONAR SOLO LAS COLUMNAS POR ÍNDICE (0,2,6,7,8,16) ===
        columnas_deseadas = [0,1,2,3,4,6,7,8,17,18,19,20,21]
        df_filtrado = df.iloc[:, columnas_deseadas]

        # === DEFINIR RUTA DE SALIDA ===
        carpeta_salida = "C:\\Users\\kenda\\OneDrive\\CUC\\Cuatri 4\\BD\\Progra_2\\Proyecto_final\\Proyecto_educacion\\data\\processed"
        archivo_salida = os.path.join(carpeta_salida, "Graduados.csv")

        # === CREAR CARPETA SI NO EXISTE ===
        os.makedirs(carpeta_salida, exist_ok=True)

        # === GUARDAR EL RESULTADO EN CSV ===
        df_filtrado.to_csv(archivo_salida, index=False, encoding="utf-8-sig")
        print(f"Archivo guardado en: {archivo_salida}")
