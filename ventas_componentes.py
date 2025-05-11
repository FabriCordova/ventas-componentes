class Componente:
    def especificacion(self):
        pass

class TarjetaVideo(Componente):
    def especificacion(self):
        return "Tarjeta de video NVIDIA RTX 4060"

class Procesador(Componente):
    def especificacion(self):
        return "Procesador AMD Ryzen 7 5800X"

class UnidadSSD(Componente):
    def especificacion(self):
        return "Unidad SSD NVMe 1TB"

class FabricaComponentes:
    def crear_componente(self, tipo):
        if tipo == "tarjeta":
            return TarjetaVideo()
        elif tipo == "procesador":
            return Procesador()
        elif tipo == "ssd":
            return UnidadSSD()
        else:
            raise ValueError("Tipo de componente no reconocido")

class DecoradorComponente(Componente):
    def __init__(self, componente):
        self.componente = componente

class GarantiaExtendida(DecoradorComponente):
    def especificacion(self):
        return self.componente.especificacion() + " + Garantía extendida (2 años)"

class ServicioInstalacion(DecoradorComponente):
    def especificacion(self):
        return self.componente.especificacion() + " + Servicio de instalación incluido"

class EstrategiaDescuento:
    def aplicar_descuento(self, precio):
        return precio

class SinDescuento(EstrategiaDescuento):
    def aplicar_descuento(self, precio):
        return precio

class DescuentoEstudiante(EstrategiaDescuento):
    def aplicar_descuento(self, precio):
        return precio * 0.90

class DescuentoVIP(EstrategiaDescuento):
    def aplicar_descuento(self, precio):
        return precio * 0.85

def main():
    print("🖥️ Bienvenido al sistema de venta de componentes de computadoras\n")

    fabrica = FabricaComponentes()
    componente = fabrica.crear_componente("tarjeta")

    componente_mejorado = GarantiaExtendida(componente)
    componente_final = ServicioInstalacion(componente_mejorado)

    print("🛒 Producto seleccionado: ", componente_final.especificacion())

    precio_base = 500.0
    estrategia_descuento = DescuentoEstudiante()
    precio_final = estrategia_descuento.aplicar_descuento(precio_base)

    print(f"\n💰 Precio base: ${precio_base}")
    print(f"💳 Precio con descuento aplicado: ${precio_final:.2f}")

if __name__ == "__main__":
    main()
