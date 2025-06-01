class Recursos:
    def __init__(self, metal=2500, cristal=1000, prometium=0, energia=0):
        self.metal = metal
        self.cristal = cristal
        self.prometium = prometium
        self.energia = energia

    def __repr__(self):
        return f"<Recursos: Metal={self.metal}, Cristal={self.cristal}, Prometium={self.prometium}, Energia={self.energia}>"

    def deduzir(self, custo: dict):
        for recurso, valor in custo.items():
            if hasattr(self, recurso):
                setattr(self, recurso, getattr(self, recurso) - valor)