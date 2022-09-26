from typing import List, Dict
import random

from config import IGV_TOTAL


def main():

    flights: List[Dict[str, str|float|int]] = [{
        'code': 'LIM-AYA',
        'name': 'Lima - Ayacucho',
        'base_price' : 55.19,
        'economy_seat' : 8,
        'premium_seat' : 16,
        'airplane' : 'A001',
        'ticket_sale_economy_min_range' : 120,
        'ticket_sale_economy_max_range' : 130,
        'ticket_sale_premium_min_range' : 10,
        'ticket_sale_premium_max_range' : 20
    }, {
        'code': 'LIM-CUS',
        'name': 'LLima - Cusco',
        'base_price' : 136.51,
        'economy_seat' : 8,
        'premium_seat' : 16,
        'airplane' : 'A002',
        'ticket_sale_economy_min_range' : 130,
        'ticket_sale_economy_max_range' : 144,
        'ticket_sale_premium_min_range' : 15,
        'ticket_sale_premium_max_range' : 24
    }, {
        'code': 'LIM-ARE',
        'name': 'Lima - Arequipa',
        'base_price' : 90.29,
        'economy_seat' : 8,
        'premium_seat' : 16,
        'airplane' : 'A003',
        'ticket_sale_economy_min_range' : 115,
        'ticket_sale_economy_max_range' : 138,
        'ticket_sale_premium_min_range' : 16,
        'ticket_sale_premium_max_range' : 22
    }, {
        'code': 'LIM-TAR',
        'name': 'Lima - Tarapoto',
        'base_price' : 71.89,
        'economy_seat' : 8,
        'premium_seat' : 16,
        'airplane' : 'A004',
        'ticket_sale_economy_min_range' : 100,
        'ticket_sale_economy_max_range' : 120,
        'ticket_sale_premium_min_range' : 12,
        'ticket_sale_premium_max_range' : 18
    }, {
        'code': 'AYA-LIM',
        'name': 'Ayacucho - Lima',
        'base_price' : 40.42,
        'economy_seat' : 7,
        'premium_seat' : 16,
        'airplane' : 'A001',
        'ticket_sale_economy_min_range' : 100,
        'ticket_sale_economy_max_range' : 115,
        'ticket_sale_premium_min_range' : 10,
        'ticket_sale_premium_max_range' : 15
    }, {
        'code': 'CUS-LIM',
        'name': 'Cusco - Lima',
        'base_price' : 124.32,
        'economy_seat' : 7,
        'premium_seat' : 16,
        'airplane' : 'A002',
        'ticket_sale_economy_min_range' : 105,
        'ticket_sale_economy_max_range' : 120,
        'ticket_sale_premium_min_range' : 14,
        'ticket_sale_premium_max_range' : 20
    }, {
        'code': 'ARE-LIM',
        'name': 'Arequipa - Lima',
        'base_price' : 86.59,
        'economy_seat' : 7,
        'premium_seat' : 16,
        'airplane' : 'A003',
        'ticket_sale_economy_min_range' : 100,
        'ticket_sale_economy_max_range' : 110,
        'ticket_sale_premium_min_range' : 13,
        'ticket_sale_premium_max_range' : 18
    }, {
        'code': 'TAR-LIM',
        'name': 'Tarapoto - Lima',
        'base_price' : 68.42,
        'economy_seat' : 7,
        'premium_seat' : 16,
        'airplane' : 'A004',
        'ticket_sale_economy_min_range' : 90,
        'ticket_sale_economy_max_range' : 105,
        'ticket_sale_premium_min_range' : 10,
        'ticket_sale_premium_max_range' : 15
    }]

    for key,flight in enumerate(flights):
        economic_ticket: int = random.randint(int(flight['ticket_sale_economy_min_range']),int(flight['ticket_sale_economy_max_range']))
        premium_ticket: int = random.randint(int(flight['ticket_sale_premium_min_range']),int(flight['ticket_sale_premium_max_range']))
        total_ticket: int = economic_ticket + premium_ticket
        print(f"El total de pasajes vendidos de la aerolinea {flight['code']} fueron {total_ticket}")
        
        total_economic_tickets_sales: float = 0

        for i in range(economic_ticket):
            economic_ticket_cost: float = (float(flight['base_price']) + float(flight['economy_seat'])) + (float(flight['base_price']) + float(flight['economy_seat'])) * (IGV_TOTAL/100)
            total_economic_tickets_sales += economic_ticket_cost

if __name__ == "__main__":
    main()
