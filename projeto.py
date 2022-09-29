#Configurações Iniciais
from escpos.printer import Usb
p = Usb(0x0471, 0x0055)
import imgkit

imgkit.from_file('index.html', 'out.jpg')
# Textos
p.image("out.jpg")
p.cut()
