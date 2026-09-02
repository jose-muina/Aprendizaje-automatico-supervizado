datos = [
    {"usuario": "user01", "accion": "Combate", "duracion": 120, "resultado": "Victoria"},
    {"usuario": "user02", "accion": "Exploracion", "duracion": 300, "resultado": "Descubrimiento"},
    {"usuario": "user03", "accion": "Interaccion social", "duracion": 180, "resultado": "Mensaje enviado"},
    {"usuario": "user04", "accion": "Combate", "duracion": 90, "resultado": "Derrota"},
    {"usuario": "user05", "accion": "Exploracion", "duracion": 240, "resultado": "Sin hallazgos"}
]

def clasificar_accion(registro):
    accion = registro["accion"]
    resultado = registro["resultado"]
    
    if accion == "Combate" and resultado == "Victoria":
        return "Combate Ganado"
    elif accion == "Combate" and resultado == "Derrota":
        return "Combate Perdido"
    elif accion == "Exploracion" and resultado == "Descubrimiento":
        return "Exploracion Exitosa"
    elif accion == "Exploracion" and resultado == "Sin hallazgos":
        return "Exploracion Improductiva"
    elif accion == "Interaccion social":
        return "Actividad Social"
    else:
        return "Accion No Clasificada"

for registro in datos:
    clasificacion = clasificar_accion(registro)
    print(f"Usuario: {registro['usuario']} | Acción: {registro['accion']} -> Clasificación: {clasificacion}")