class Client():
    def __init__(self, name, cargo_weight, is_vip=False):
        if name:
            self.name = name
        else:
            print("Имя должно быть указано!")
        try:
            cargo_weight = int(cargo_weight)
            self.cargo_weight = cargo_weight
        except:
            print("Вес груза должен быть обязательно указан числом")
        if not(isinstance(is_vip,bool)):
            print("Ошибка!")
        self.is_vip = bool(is_vip)
