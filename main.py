import dataset
miBase = dataset.connect("sqlite:///datos.db")
tabla = miBase["Productos"]


def listar():
    print("*********** Listado de productos *****************")
    for cada_item in tabla:
        print(f'ID: {cada_item["id"]} | Producto: {cada_item["Nombre"]} | Precio: {cada_item["Precio"]} | Categoria: {cada_item["Categoria"]} ')
    

while True: 
    opciones = input("\nID - Remover por ID\nS - Salir\nA - Agregar\nL - Listar\n")
    
    match opciones:
        case "S":
            break
        
        case "A":
            agregarProducto = input("\nProducto a agregar: ").strip()
            precioAgregar = float(input("\nPrecio producto: ").strip())
            agregarCategoria = input("\nCategoria producto: ").strip()

            agregar = {"Nombre":agregarProducto,"Precio":precioAgregar,"Categoria":agregarCategoria}
            
            tabla.insert(agregar)
            listar()

        case "L":
            listar()
           
        case "ID":
            quitar = int(input("\nID de producto a quitar: ").strip())
            tabla.delete(id=quitar)
            
            print(f"El producto en ID {quitar} se eliminó exitosamente!\n")
            
            listar()
            
