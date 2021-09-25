from escpos.printer import Usb
from datetime import datetime
now = datetime.now()
p = Usb(0x0471, 0x0055)

ano= 2021       #formato AAAA
mes=  12         #usar numeros
dia= 13
import datetime

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

if datapadrao > hoje:
    delta = datapadrao - hoje

elif datapadrao <= hoje:
    delta = hoje - datapadrao

restante = delta.days
restante = str(restante)


dt_string = now.strftime("%d/%m/%Y")
p.set(align='center')
p.text('\n')
p.text('Bom dia!' + '\n')
p.text(dt_string + '\n')
p.text('\n')

p.text(restante + ' Dias' + '\n')
p.text('Para o fim do semestre' + '\n')
p.cut()