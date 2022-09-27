from typing import List, Dict
import random

import statistics
import operator

from config import IGV_TOTAL, CURRENCY_SYMBOL


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
        'name': 'Lima - Cusco',
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

    # Se inicializa la variable all_cheap_tickets que almacenará los precios de pasaje económico
    all_cheap_tickets: List[float] = []

    # Se inicializa la variable all_premium_tickets que almacenará los precios de pasaje premium
    all_premium_tickets: List[float] = []
    
    # Se inicializa la variable all_flights que almacenará los  vuelos programados
    all_flights: List[Dict[str, str | float]] = []

    # Se inicializa la variable tickets_sold que almacenará los pasajes vendidos
    tickets_sold = {}

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

        # Destino y cantidad de pasajes vendidos (económicos y premium)
        destination_of_tickets_sold = {
            flight['name']: total_ticket
        }

        # Se agrega todos los pasajes vendidos con su destino al diccionario tickets_sold
        tickets_sold.update(destination_of_tickets_sold)

        # Se se agrega a la lista tickets_sold el objeto destino y total de pasaje vendido
        # tickets_sold.append(destination_and_total_tickets)

        # Se imprime la cantidad de pasajes por cada vuelo
        # Pregunta 1
        print(
            f"El total de pasajes vendidos por el vuelo {flight['code']} fueron {total_ticket}")

        # Iteración por cada asiento económico de cada vuelo
        for i in range(economic_ticket):

            # Se inicializa el precio del pasaje económico sin IGV
            economic_ticket_cost: float = (
                float(flight['base_price']) + float(flight['economy_seat']))

            # Se agrega a la lista all_cheap_tickets el precio de un pasaje con asiento económico
            all_cheap_tickets.append(economic_ticket_cost)

            # Se inicializa el precio total del pasaje económico con IGV
            total_economic_ticket_cost: float = economic_ticket_cost + \
                economic_ticket_cost * (IGV_TOTAL / 100)

            # Se va sumando el impuesto de cada pasaje económico del vuelo
            total_IGV += economic_ticket_cost * (IGV_TOTAL / 100)

            # Se va sumando el precio total del pasaje económico del vuelo
            total_economic_tickets_sales += total_economic_ticket_cost

        # Iteración por cada asiento premium de cada vuelo
        for i in range(premium_ticket):

            # Se inicializa el precio del pasaje premium sin IGV
            premium_ticket_cost: float = (
                float(flight['base_price']) + float(flight['premium_seat']))

            # Se agrega a la lista all_premium_tickets el precio de un pasaje con asiento premium
            all_premium_tickets.append(premium_ticket_cost)

            # Se inicializa el precio total del pasaje premium con IGV
            total_premium_ticket_cost: float = premium_ticket_cost + \
                premium_ticket_cost * (IGV_TOTAL / 100)

            # Se va sumando el impuesto de cada pasaje premium del vuelo
            total_IGV += premium_ticket_cost * (IGV_TOTAL / 100)

            # Se va sumando el precio total del pasaje premium del vuelo
            total_premium_tickets_sales += total_premium_ticket_cost
        total_ticket_sales = round(
            total_premium_tickets_sales + total_premium_tickets_sales, 2)
        
        # Creamos el diccionario para los vuelos programados
        flight: Dict[str, list] = {
            "route": flight["name"],
            "airplane": flight["airplane"],
            "total_tickets_sales": total_ticket_sales,
            "passengers": total_ticket,

        }
        all_flights.append(flight)

    print("-" * 50)

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
    print("-" * 50)

    # Pregunta 5
    # Se imprime el valor promedio del pasaje económico
    average_economic_ticket_cost: float = statistics.mean(all_cheap_tickets)
    print(
        f"El valor promedio del pasaje económico es: {round(average_economic_ticket_cost,2)}")

    # Aplicando formato de moneda a la variable average_economic_ticket_cost
    average_formatted_economy_ticket: str = "{}{:,.2f}".format(
        CURRENCY_SYMBOL, average_economic_ticket_cost)
    print(
        f"El valor promedio formateado del pasaje económico es: {average_formatted_economy_ticket}")
    print("-" * 50)

    # Pregunta 6
    # Se imprime el valor promedio del pasaje premium
    average_premium_ticket_cost: float = statistics.mean(all_premium_tickets)
    print(
        f"El valor promedio del pasaje premium es: {round(average_premium_ticket_cost,2)}")

    # Aplicando formato de moneda a la variable average_economic_ticket_cost
    average_formatted_premium_ticket: str = "{}{:,.2f}".format(
        CURRENCY_SYMBOL, average_premium_ticket_cost)
    print(
        f"El valor promedio formateado del pasaje premium es: {average_formatted_premium_ticket}")
    print("-" * 50)

    # Pregunta 7
    # Se imprime los pasajes vendidos con su destino

    # Se obtiene el maximo de pasajeros a traves de los pasajes vendidos
    max_passengers_destination = max(
        tickets_sold.items(), key=operator.itemgetter(1))[0]
    max_passengers = max(tickets_sold.items(), key=operator.itemgetter(1))[1]
    print(
        f"El vuelo con la mayor cantidad de pasajeros es: {max_passengers_destination} con una cantidad de {max_passengers}")

    # Pregunta 8
    # Ordenemos lista de vuelos según el número de pasajeros (de menor a mayor)
    sorted_passengers = sorted(all_flights, key=lambda x: x["passengers"])
    print("-" * 50)

    print(
        f"El vuelo con la menor cantidad de pasajeros es: {sorted_passengers[0]['route']} con una cantidad de {sorted_passengers[0]['passengers']}")
    print("-" * 50)

    # Pregunta 9
    # Ordenemos lista de vuelos según los ingresos por la venta de asientos (de mayor a menor)
    order_total_tickets_sales = sorted(
        all_flights, key=lambda x: x["total_tickets_sales"], reverse=True)

    # Iteramos los 3 veces la lista ordeana de vuelos 
    for i in range(3):
        print(
            f"El {i+1}° vuelo con con mayor ingresos es: {order_total_tickets_sales[i]['route']} con un total de {CURRENCY_SYMBOL}{order_total_tickets_sales[i]['total_tickets_sales']}")

    print("-" * 50)
    # Pregunta 10
    print(
        f"El avión que transportó mas pasajeros es: {sorted_passengers[0]['airplane']}")
    print("-" * 50)


if __name__ == "__main__":
    main()
