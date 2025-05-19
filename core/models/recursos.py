class Recursos:
    def __init__(self, metal=0, cristal=0, prometium=0, energia=0):
        self.metal = metal
        self.cristal = cristal
        self.prometium = prometium
        self.energia = energia

    def __repr__(self):
        return f"<Recursos: Metal={self.metal}, Cristal={self.cristal}, Prometium={self.prometium}, Energia={self.energia}>"