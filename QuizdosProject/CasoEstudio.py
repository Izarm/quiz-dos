



def calcular_liquidacion(Nombre, Dias, salario):
    # Cálculos
    prima = salario * Dias / 360
    cesantias = salario * dias / 360
    intereses_cesantias = cesantias * 0.12 / dias
    vacaciones = salario * dias / 720

    # Liquidación total
    liquidacion = prima + cesantias + intereses_cesantias + vacaciones

    # Resultados
    print(f"Señor {Nombre} para los {Dias} días laborados y salario ${salario}, su liquidación se compone así:")
    print(f"Prima: ${prima:.2f}")
    print(f"Cesantía: ${cesantias:.2f}")
    print(f"Intereses cesantías: ${intereses_cesantias:.2f}")
    print(f"Vacaciones: ${vacaciones:.2f}")
    print(f"Liquidación: ${liquidacion:.2f}")


# Datos de prueba
nombre = ("Luis Vejarano ")
dias = int(("7"))
salario = float(("785000"))

calcular_liquidacion(nombre, dias, salario)


