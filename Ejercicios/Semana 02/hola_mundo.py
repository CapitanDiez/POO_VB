class HolaMundo:

    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Método Uno")
    
    def metodoDos(self,variable_uno:int, variable_dos:float)->int:
        
        """"
        Éste método recibe 2 variables enteras, la suma y regresa
        el resultado de la suma.

        Args:

        variable_uno:int-Primer número entero
        variable_dos:int-Segundo número entero

        Return:

        suma:int - Sume de los dos números enteros.
        """
        suma = variable_uno+variable_dos
        return int (suma)
    def metodoTres(self,variable_tres:str)->None:
        print(f"Númer de carácteres: {len(variable_tres)}")

nombre_objeto = HolaMundo()
nombre_objeto.metodoUno()
