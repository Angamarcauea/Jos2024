# Datos de temperaturas
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 83},
            {"day": "Sábado", "temp": 81},
            {"day": "Domingo", "temp": 88}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 83},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 91}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 79},
            {"day": "Martes", "temp": 83},
            {"day": "Miércoles", "temp": 84},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 94},
            {"day": "Domingo", "temp": 91}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 90},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 93},
            {"day": "Domingo", "temp": 94}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 672},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 69}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 69},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 77},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 90}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 84},
            {"day": "Jueves", "temp": 86},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 90}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 95},
            {"day": "Miércoles", "temp": 96},
            {"day": "Jueves", "temp": 95},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 88}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 96},
            {"day": "Jueves", "temp": 88},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 88}
        ]
    ]
]
def calcular_promedio_temperaturas(ciudad):
    """
    Calcula y muestra los promedios de temperaturas por semana y el promedio total de una ciudad.
    """
    suma_total = 0  # Suma total de T° de la ciudad
    num_dias = 0  # Contador de días

    print(f"Ciudad {ciudad + 1}:")
    for j, semana in enumerate(temperaturas[ciudad]):
        suma_semana = 0
        for dia in semana:
            suma_semana += dia['temp']
        promedio_semana = suma_semana / len(semana)
        suma_total += suma_semana
        num_dias += len(semana)

    promedio_ciudad = suma_total / num_dias
    print(f"Promedio ciudad {ciudad + 1} = {promedio_ciudad:.2f}°F\n")
# Mostrar promedios de T° para cada ciudad
for i in range(len(temperaturas)):
    calcular_promedio_temperaturas(i)