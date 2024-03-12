import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('copa_america.db')
cursor = conn.cursor()

# Equipos y jugadores de la Copa América
equipos = {
    'Argentina': [
        ('Lionel Messi', 34, 'Delantero'),
        ('Paulo Dybala', 27, 'Centrocampista'),
        ('Nicolas Otamendi', 33, 'Defensa'),
        ('Emiliano Martínez', 29, 'Portero')
    ],
    'Brasil': [
        ("Neymar Jr.", 30, "Delantero"),
        ("Alisson Becker", 29, "Portero"),
        ("Casemiro", 29, "Centrocampista"),
        ("Thiago Silva", 37, "Defensa")
    ],
    'Colombia': [
        ("James Rodríguez", 30, "Centrocampista"),
        ("David Ospina", 33, "Portero"),
        ("Juan Cuadrado", 33, "Centrocampista"),
        ("Davinson Sánchez", 25, "Defensa")
    ],
    'Ecuador': [
        ("Enner Valencia", 31, "Delantero"),
        ("Alexander Domínguez", 34, "Portero"),
        ("Moisés Caicedo", 20, "Centrocampista"),
        ("Robert Arboleda", 29, "Defensa")
    ],
    'Paraguay': [
        ("Ángel Romero", 30, "Delantero"),
        ("Antony Silva", 37, "Portero"),
        ("Miguel Almirón", 28, "Centrocampista"),
        ("Gustavo Gómez", 28, "Defensa")
    ],
    'Perú': [
        ("Paolo Guerrero", 38, "Delantero"),
        ("Pedro Gallese", 32, "Portero"),
        ("Christian Cueva", 30, "Centrocampista"),
        ("Miguel Trauco", 29, "Defensa")
    ],
    'Uruguay': [
        ("Luis Suárez", 35, "Delantero"),
        ("Fernando Muslera", 35, "Portero"),
        ("Federico Valverde", 23, "Centrocampista"),
        ("José Giménez", 27, "Defensa")
    ],
    'Venezuela': [
        ("Salomón Rondón", 32, "Delantero"),
        ("Wuilker Faríñez", 23, "Portero"),
        ("Tomás Rincón", 33, "Centrocampista"),
        ("Yordan Osorio", 26, "Defensa")
    ],
    'Bolivia': [
        ("Marcelo Martins Moreno", 34, "Delantero"),
        ("Carlos Lampe", 34, "Portero"),
        ("Henry Vaca", 23, "Centrocampista"),
        ("Jairo Quinteros", 20, "Defensa")
    ],
    'Estados_Unidos': [
        ("Christian Pulisic", 24, "Delantero"),
        ("Zack Steffen", 26, "Portero"),
        ("Weston McKennie", 23, "Centrocampista"),
        ("John Brooks", 29, "Defensa")
    ],
    'México': [
        ("Raúl Jiménez", 31, "Delantero"),
        ("Guillermo Ochoa", 36, "Portero"),
        ("Héctor Herrera", 31, "Centrocampista"),
        ("Diego Lainez", 21, "Defensa")
    ]
}

# Crear tablas e insertar datos para cada equipo
for equipo, jugadores in equipos.items():
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {equipo} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER,
        posicion TEXT
    );
    '''
    cursor.execute(create_table_query)

    insert_data_query = f'''
    INSERT INTO {equipo} (nombre, edad, posicion) VALUES (?, ?, ?);
    '''

    cursor.executemany(insert_data_query, jugadores)

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
