class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    def get_alto(self):
        return self._alto

    def set_alto(self, alto):
        self._alto = alto

    def get_ancho(self):
        return self._ancho

    def set_ancho(self,ancho):
        self._ancho = ancho

    def __str__(self):
        return f'alto: {self._alto}, ancho: {self._ancho}'