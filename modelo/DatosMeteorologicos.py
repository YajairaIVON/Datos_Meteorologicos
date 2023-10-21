from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, archivo_datos: str):
        self.archivo_datos = archivo_datos
        self.temperaturas = []
        self.humedades = []
        self.presiones = []
        self.velocidades_viento = []
        self.direcciones_viento = []

# El archivo se lee y crea en el programa
    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open("archivo_datos.txt", "r") as archivo:
            lines = archivo.readlines()

# Son leidos los renglones del archivo que estan escritos de la siguiente manera
        for line in lines:
            if line.strip():
                key, value = line.strip().split(": ")
                if key == "Temperatura":
                    self.temperaturas.append(float(value))
                elif key == "Humedad":
                    self.humedades.append(float(value))
                elif key == "Presion":
                    self.presiones.append(float(value))
                elif key == "Viento":
                    velocidad, direccion = value.split(",")
                    self.velocidades_viento.append(float(velocidad))
                    self.direcciones_viento.append(direccion)

        # Son Calculadas las estadísticas de las operaciones 
        temperatura_promedio = sum(self.temperaturas) / len(self.temperaturas)
        humedad_promedio     = sum(self.humedades) / len(self.humedades)
        presion_promedio     = sum(self.presiones) / len(self.presiones)
        velocidad_promedio_viento     = sum(self.velocidades_viento) / len(self.velocidades_viento)
        direccion_predominante_viento = self.calcular_direccion_predominante(self.direcciones_viento)

        return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio_viento, direccion_predominante_viento

    def calcular_direccion_predominante(self, direcciones):
        direcciones_grados = {
            "N": 0,   "NNE": 22.5,  "NE": 45,  "ENE": 67.5,
            "E": 90,  "ESE": 112.5, "SE": 135, "SSE": 157.5,
            "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
            "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }

        grados = [direcciones_grados[d] for d in direcciones]
        direccion_promedio_grados = sum(grados) / len(grados)

        # Se calcula la dirección más cercana en grados de la siguiente forma:
        direccion_cercana = min(direcciones_grados, key=lambda x: abs(direcciones_grados[x] - direccion_promedio_grados))
        return direccion_cercana


nombre_archivo = "datos_meteorologicos.txt"
datos = DatosMeteorologicos(nombre_archivo)
temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio_viento, direccion_predominante_viento =datos.procesar_datos()

#Impresion de los calculos 
print(f"El promedio de la temperatura es: {temperatura_promedio} °C")
print(f"El promedio de la humedad es:     {humedad_promedio} %")
print(f"El promedio de la presión es:     {presion_promedio} hPa")
print(f"El promedio de la velocidad del viento es: {velocidad_promedio_viento} km/h")
print(f"La dirección predominante del viento es:   {direccion_predominante_viento}")
