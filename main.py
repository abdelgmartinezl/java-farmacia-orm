from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///farmacia.db', echo=False, future=True)
Session = sessionmaker(bind=engine, autoflush=False, future=True)

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)

class Transaccion(Base):
    __tablename__ = 'transaccion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cantidad = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    metodo_pago = Column(String, nullable=False)

class Medicina(Base):
    __tablename__ = 'medicinas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    receta = Column(String, nullable=False)
    dosis = Column(String, nullable=False)

Base.metadata.create_all(engine)

def crear_cliente(nombre, edad):
    with Session() as session:
        nuevo_cliente = Cliente(nombre=nombre, edad=edad)
        session.add(nuevo_cliente)
        session.commit()

def leer_clientes():
    with Session() as session:
        return session.query(Cliente).all()

def actualizar_cliente(id, nombre, edad):
    with Session() as session:
        cliente = session.get(Cliente, id)
        if cliente:
            cliente.nombre = nombre
            cliente.edad = edad
            session.commit()

def eliminar_cliente(id):
    with Session() as session:
        cliente = session.get(Cliente, id)
        if cliente:
            session.delete(cliente)
            session.commit()

def crear_transaccion(monto, fecha, metodo_pago):
    with Session() as session:
        nueva_transaccion = Transaccion(monto=monto, fecha=fecha, metodo_pago=metodo_pago)
        session.add(nueva_transaccion)
        session.commit()

def leer_transacciones():
    with Session() as session:
        return session.query(Transaccion).all()

def actualizar_transaccion(id, monto, fecha, metodo_pago):
    with Session() as session:
        transaccion = session.query(Transaccion, id)
        if transaccion:
            transaccion.monto = monto
            transaccion.fecha = fecha
            transaccion.metodo_pago = metodo_pago
            session.commit()

def eliminar_transaccion(id):
    with Session() as session:
        transaccion = session.query(Transaccion, id)
        if transaccion:
            session.delete(transaccion)
            session.commit()

def crear_medicina(nombre, receta, dosis):
    with Session() as session:
        nueva_medicina = Transaccion(nombre=nombre, receta=receta, dosis=dosis)
        session.add(nueva_medicina)
        session.commit()

def leer_medicinas():
    with Session() as session:
        return session.query(Medicina).all()

def actualizar_medicinas(id, nombre, receta, dosis):
    with Session() as session:
        medicina = session.query(Medicina, id)
        if medicina:
            medicina.nombre = nombre
            medicina.receta = receta
            medicina.dosis = dosis
            session.commit()

def eliminar_medicina(id):
    with Session() as session:
        medicina = session.query(Medicina, id)
        if medicina:
            session.delete(medicina)
            session.commit()

def cliente_menu():
    while True:
        print("\nMenu de Cliente")
        print("1. Crear Cliente")
        print("2. Ver Cliente")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver a Menu Principal")
        opcion = input("OPCION :: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            crear_cliente(nombre, edad)
            print("Cliente agregado!")
        elif opcion == '2':
            clientes = leer_clientes()
            for cliente in clientes:
                print(cliente.id, cliente.nombre, cliente.edad)
        elif opcion == '3':
            id = int(input("ID del Cliente: "))
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            actualizar_cliente(id, nombre, edad)
            print("Cliente actualizado!")
        elif opcion == "4":
            id = int(input("ID del Cliente: "))
            eliminar_cliente(id)
            print("Cliente eliminado!")
        elif opcion == "5":
            break
        else:
            print("ERR:: Opcion invalida")


def transaccion_menu():
    while True:
        print("\nMenu de Transaccion")
        print("1. Crear Transaccion")
        print("2. Ver Transaccion")
        print("3. Actualizar Transaccion")
        print("4. Eliminar Transaccion")
        print("5. Volver a Menu Principal")
        opcion = input("OPCION :: ")

        if opcion == '1':
            monto = float(input("Monto: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            metodo_pago = input("Metodo de Pago: ")
            crear_transaccion(monto, fecha, metodo_pago)
            print("Transaccion agregada!")
        elif opcion == '2':
            transacciones = leer_transacciones()
            for transaccion in transacciones:
                print(transaccion.id, transaccion.monto, transaccion.fecha, transaccion.metodo_pago)
        elif opcion == '3':
            id = int(input("ID de Transaccion: "))
            monto = float(input("Monto: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            metodo_pago = input("Metodo de Pago: ")
            actualizar_transaccion(id, monto, fecha, metodo_pago)
            print("Cliente actualizado!")
        elif opcion == "4":
            id = int(input("ID de Transaccion: "))
            eliminar_transaccion(id)
            print("Transaccion eliminada!")
        elif opcion == "5":
            break
        else:
            print("ERR:: Opcion invalida")

def medicina_menu():
    while True:
        print("\nMenu de Medicina")
        print("1. Crear Medicina")
        print("2. Ver Medicina")
        print("3. Actualizar Medicina")
        print("4. Eliminar Medicina")
        print("5. Volver a Menu Principal")
        opcion = input("OPCION :: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            receta = input("Receta: ")
            dosis = input("Dosis: ")
            crear_medicina(nombre, receta, dosis)
            print("Medicina agregada!")
        elif opcion == '2':
            medicinas = leer_medicinas()
            for medicina in medicinas:
                print(medicina.id, medicina.nombre, medicina.receta, medicina.dosis)
        elif opcion == '3':
            id = int(input("ID de Medicina: "))
            nombre = input("Nombre: ")
            receta = input("Receta: ")
            dosis = input("Dosis: ")
            actualizar_medicinas(id, nombre, receta, dosis)
            print("Medicina actualizada!")
        elif opcion == "4":
            id = int(input("ID de Medicina: "))
            eliminar_medicina(id)
            print("Medicina eliminada!")
        elif opcion == "5":
            break
        else:
            print("ERR:: Opcion invalida")

def menu_principal():
    while True:
        print("\n Menu Principal")
        print("1. Menu de Clientes")
        print("2. Menu de Transaccion")
        print("3. Menu de Medicinas")
        opcion = input("OPCION :: ")

        if opcion == "1":
            cliente_menu()
        elif opcion == "2":
            transaccion_menu()
        elif opcion == "3":
            medicina_menu()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("OPCION INVALIDA.")

if __name__ == "__main__":
    menu_principal()