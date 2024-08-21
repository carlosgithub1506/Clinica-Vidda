
lista_pacientes = [
    {
        "ID": 1,
        "Nombre": "Alejandro",
        "Apellido": "Gonzalez",
        "Edad": 35,
        "Altura": 175,
        "Peso": 78.5,
        "DNI": "45678912",
        "Grupo Sanguíneo": "A+"
    },
    {
        "ID": 2,
        "Nombre": "Beatriz",
        "Apellido": "Rodriguez",
        "Edad": 28,
        "Altura": 160,
        "Peso": 62.2,
        "DNI": "56789012",
        "Grupo Sanguíneo": "B+"
    },
    {
        "ID": 3,
        "Nombre": "Carlos",
        "Apellido": "Perez",
        "Edad": 42,
        "Altura": 180,
        "Peso": 85.3,
        "DNI": "67890123",
        "Grupo Sanguíneo": "AB+"
    },
    {
        "ID": 4,
        "Nombre": "Diana",
        "Apellido": "Martinez",
        "Edad": 23,
        "Altura": 165,
        "Peso": 55.8,
        "DNI": "78901234",
        "Grupo Sanguíneo": "O-"
    },
    {
        "ID": 5,
        "Nombre": "Eduardo",
        "Apellido": "Garcia",
        "Edad": 37,
        "Altura": 170,
        "Peso": 70.1,
        "DNI": "89012345",
        "Grupo Sanguíneo": "A-"
    },
    {
        "ID": 6,
        "Nombre": "Fernanda",
        "Apellido": "Lopez",
        "Edad": 31,
        "Altura": 168,
        "Peso": 68.9,
        "DNI": "90123456",
        "Grupo Sanguíneo": "B-"
    },
    {
        "ID": 7,
        "Nombre": "Gustavo",
        "Apellido": "Sanchez",
        "Edad": 46,
        "Altura": 175,
        "Peso": 82.7,
        "DNI": "01234567",
        "Grupo Sanguíneo": "AB-"
    },
    {
        "ID": 8,
        "Nombre": "Helena",
        "Apellido": "Diaz",
        "Edad": 29,
        "Altura": 162,
        "Peso": 60.5,
        "DNI": "12345678",
        "Grupo Sanguíneo": "O+"
    },
    {
        "ID": 9,
        "Nombre": "Ignacio",
        "Apellido": "Fernandez",
        "Edad": 36,
        "Altura": 178,
        "Peso": 76.3,
        "DNI": "23456789",
        "Grupo Sanguíneo": "A+"
    },
    {
        "ID": 10,
        "Nombre": "Julia",
        "Apellido": "Ruiz",
        "Edad": 25,
        "Altura": 167,
        "Peso": 64.8,
        "DNI": "34567890",
        "Grupo Sanguíneo": "B-"
    },
    {
        "ID": 11,
        "Nombre": "Karla",
        "Apellido": "Moreno",
        "Edad": 33,
        "Altura": 170,
        "Peso": 72.0,
        "DNI": "45678901",
        "Grupo Sanguíneo": "AB+"
    },
    {
        "ID": 12,
        "Nombre": "Luis",
        "Apellido": "Muñoz",
        "Edad": 39,
        "Altura": 176,
        "Peso": 79.6,
        "DNI": "56789012",
        "Grupo Sanguíneo": "O-"
    },
    {
        "ID": 13,
        "Nombre": "Marta",
        "Apellido": "Alvarez",
        "Edad": 27,
        "Altura": 163,
        "Peso": 63.7,
        "DNI": "67890123",
        "Grupo Sanguíneo": "A-"
    },
    {
        "ID": 14,
        "Nombre": "Nicolas",
        "Apellido": "Romero",
        "Edad": 41,
        "Altura": 180,
        "Peso": 84.2,
        "DNI": "78901234",
        "Grupo Sanguíneo": "B-"
    },
    {
        "ID": 15,
        "Nombre": "Olga",
        "Apellido": "Gutierrez",
        "Edad": 30,
        "Altura": 165,
        "Peso": 66.5,
        "DNI": "89012345",
        "Grupo Sanguíneo": "AB-"
    },
    {
        "ID": 16,
        "Nombre": "Pablo",
        "Apellido": "Navarro",
        "Edad": 38,
        "Altura": 177,
        "Peso": 78.9,
        "DNI": "90123456",
        "Grupo Sanguíneo": "O+"
    },
    {
        "ID": 17,
        "Nombre": "Querida",
        "Apellido": "Ramos",
        "Edad": 32,
        "Altura": 170,
        "Peso": 71.3,
        "DNI": "01234567",
        "Grupo Sanguíneo": "A+"
    },
    {
        "ID": 18,
        "Nombre": "Rafael",
        "Apellido": "Gil",
        "Edad": 34,
        "Altura": 174,
        "Peso": 77.8,
        "DNI": "12345678",
        "Grupo Sanguíneo": "B+"
    }
]


lista_compatibilidad_sangre = [
    {
        "Tipo": "A+",
        "Donar": ["A+","AB+"],
        "Recibir": ["O+", "O", "A+", "A-"]
    },
    {
        "Tipo": "A-",
        "Donar": ["A+","A-","AB+","AB-"],
        "Recibir": ["A-","O-"]
    },
    {
        "Tipo": "B+",
        "Donar": ["B+","AB+"],
        "Recibir": ["O+","O-","B+","B-"]
    },
    {
        "Tipo": "B-",
        "Donar": ["B+","B-","AB+","AB-"],
        "Recibir": ["O-","B-"]
    },
    {
        "Tipo": "AB+",
        "Donar": ["AB+"],
        "Recibir": ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
    },
    {
        "Tipo": "AB-",
        "Donar": ["AB+","AB-"],
        "Recibir": ["AB-","O-","A-","B-"]
    },
    {
        "Tipo": "O+",
        "Donar": ["A+","B+","AB+","O+"],
        "Recibir": ["O+", "O-"]
    },
    {
        "Tipo": "O-",
        "Donar": ["A+","A-","B+","B-","AB+","AB-","O+","O-"],
        "Recibir": ["O-"]
    }
]

matriz_tipos_sanguineos = [
    ['A+', 0, 0],
    ['A-', 0, 0],
    ['B+', 0, 0],
    ['B-', 0, 0],
    ['AB+', 0, 0],
    ['AB-', 0, 0],
    ['O+', 0, 0],
    ['O-', 0, 0]
    ]
