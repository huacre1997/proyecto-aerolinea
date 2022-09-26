from typing import List, Dict
import random

from config import IGV_TOTAL


def main():

    # Se inicializa la variable 'flights'
    flights: List[Dict[str, str | float | int]] = [{
        'code': 'LIM-AYA',
        'name': 'Lima - Ayacucho',
        'base_price': 55.19,
        'economy_seat': 8,
        'premium_seat': 16,
        'airplane': 'A001',
        'ticket_sale_economy_min_range': 120,
        'ticket_sale_economy_max_range': 130,
        'ticket_sale_premium_min_range': 10,
        'ticket_sale_premium_max_range': 20
    }, {
        'code': 'LIM-CUS',
        'name': 'LLima - Cusco',
        'base_price': 136.51,
        'economy_seat': 8,
        'premium_seat': 16,
        'airplane': 'A002',
        'ticket_sale_economy_min_range': 130,
        'ticket_sale_economy_max_range': 144,
        'ticket_sale_premium_min_range': 15,
        'ticket_sale_premium_max_range': 24
    }, {
        'code': 'LIM-ARE',
        'name': 'Lima - Arequipa',
        'base_price': 90.29,
        'economy_seat': 8,
        'premium_seat': 16,
        'airplane': 'A003',
        'ticket_sale_economy_min_range': 115,
        'ticket_sale_economy_max_range': 138,
        'ticket_sale_premium_min_range': 16,
        'ticket_sale_premium_max_range': 22
    }, {
        'code': 'LIM-TAR',
        'name': 'Lima - Tarapoto',
        'base_price': 71.89,
        'economy_seat': 8,
        'premium_seat': 16,
        'airplane': 'A004',
        'ticket_sale_economy_min_range': 100,
        'ticket_sale_economy_max_range': 120,
        'ticket_sale_premium_min_range': 12,
        'ticket_sale_premium_max_range': 18
    }, {
        'code': 'AYA-LIM',
        'name': 'Ayacucho - Lima',
        'base_price': 40.42,
        'economy_seat': 7,
        'premium_seat': 16,
        'airplane': 'A001',
        'ticket_sale_economy_min_range': 100,
        'ticket_sale_economy_max_range': 115,
        'ticket_sale_premium_min_range': 10,
        'ticket_sale_premium_max_range': 15
    }, {
        'code': 'CUS-LIM',
        'name': 'Cusco - Lima',
        'base_price': 124.32,
        'economy_seat': 7,
        'premium_seat': 16,
        'airplane': 'A002',
        'ticket_sale_economy_min_range': 105,
        'ticket_sale_economy_max_range': 120,
        'ticket_sale_premium_min_range': 14,
        'ticket_sale_premium_max_range': 20
    }, {
        'code': 'ARE-LIM',
        'name': 'Arequipa - Lima',
        'base_price': 86.59,
        'economy_seat': 7,
        'premium_seat': 16,
        'airplane': 'A003',
        'ticket_sale_economy_min_range': 100,
        'ticket_sale_economy_max_range': 110,
        'ticket_sale_premium_min_range': 13,
        'ticket_sale_premium_max_range': 18
    }, {
        'code': 'TAR-LIM',
        'name': 'Tarapoto - Lima',
        'base_price': 68.42,
        'economy_seat': 7,
        'premium_seat': 16,
        'airplane': 'A004',
        'ticket_sale_economy_min_range': 90,
        'ticket_sale_economy_max_range': 105,
        'ticket_sale_premium_min_range': 10,
        'ticket_sale_premium_max_range': 15
    }]

    # Se inicializa la variable que almacenará la venta total de los pasajes económicos
    total_economic_tickets_sales: float = 0

    # Se inicializa la variable que almacenará la venta total de los pasajes premium
    total_premium_tickets_sales: float = 0

    # Se inicializa la variable que almacenará el total de IGV
    total_IGV: float = 0

    # Iteración para cada vuelo
    for key, flight in enumerate(flights):

        # Se inicializa la variable que almacenará el total de pasajes económicos vendidos
        economic_ticket: int = random.randint(int(flight['ticket_sale_economy_min_range']), int(
            flight['ticket_sale_economy_max_range']))

        # Se inicializa la variable que almacenará el total de pasajes premium vendidos
        premium_ticket: int = random.randint(int(flight['ticket_sale_premium_min_range']), int(
            flight['ticket_sale_premium_max_range']))

        # Se inicializa la variable que almacenará el total de pasajes vendidos
        total_ticket: int = economic_ticket + premium_ticket

        # Se imprime la cantidad de pasajes por cada vuelo
        # Pregunta 1
        print(
            f"El total de pasajes vendidos por el vuelo {flight['code']} fueron {total_ticket}")

        # Iteración por cada asiento económico de cada vuelo
        for i in range(economic_ticket):

            # Se inicializa el precio del pasaje económico sin IGV
            economic_ticket_cost: float = (
                float(flight['base_price']) + float(flight['economy_seat']))

            # Se inicializa el precio total del pasaje económico con IGV
            total_economic_ticket_cost: float = economic_ticket_cost + \
                economic_ticket_cost * (IGV_TOTAL/100)

            # Se va sumando el impuesto de cada pasaje económico del vuelo
            total_IGV += economic_ticket_cost * (IGV_TOTAL/100)

            # Se va sumando el precio total del pasaje económico del vuelo
            total_economic_tickets_sales += total_economic_ticket_cost

        # Iteración por cada asiento premium de cada vuelo
        for i in range(premium_ticket):

            # Se inicializa el precio del pasaje premium sin IGV
            premium_ticket_cost: float = (
                float(flight['base_price']) + float(flight['premium_seat']))

            # Se inicializa el precio total del pasaje premium con IGV
            total_premium_ticket_cost: float = premium_ticket_cost + \
                premium_ticket_cost * (IGV_TOTAL/100)

            # Se va sumando el impuesto de cada pasaje premium del vuelo
            total_IGV += premium_ticket_cost * (IGV_TOTAL/100)

            # Se va sumando el precio total del pasaje premium del vuelo
            total_premium_tickets_sales += total_premium_ticket_cost

    print("-"*50)

    # Se imprime el total de pasajes económicos que se han vendido
    # Pregunta 2
    print(
        f"Se ingresó un total de $ {round(total_economic_tickets_sales,2)} en pasajes económicos")

    # Se imprime el total de pasajes premium que se han vendido
    # Pregunta 3
    print(
        f"Se ingresó un total de $ {round(total_premium_tickets_sales,2)} en pasajes premium")

    # Se imprime el total IGV que se ha cobrado
    # Pregunta 4
    print(f"Se cobró un total de $ {round(total_IGV,2)} en IGV")
    print("-"*50)


if __name__ == "__main__":
    main()
