from transport.client import Client
class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = [] # Список транспорта
        self.clients = []  # Список клиентов

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_client(self, client):
        self.clients.append(client)

    def list_clients(self):
        vip_clients = [client for client in self.clients if client.is_vip]
        regular_clients = [client for client in self.clients if not client.is_vip]
        return vip_clients, regular_clients
    
    def list_vehicles(self):
        return self.vehicles
    
    def optimize_cargo_distribution(self):
        vip_clients = [client for client in self.clients if client.is_vip]
        regular_clients = [client for client in self.clients if not client.is_vip]

        all_clients = vip_clients + regular_clients

        for client in all_clients:
            for vehicle in sorted(self.vehicles, key=lambda v: v.current_load):
                try:
                    vehicle.load_cargo(client)
                    break
                except ValueError:
                    continue