# Impressora Termica USB com Raspberry Pi + Python
Códigos utilizados para o uso de uma impressora térmica USB comum,(comprada no mercado livre) junto com Raspberry Pi + Python </br>
# Automatizando impressão por horário:
Entrar no crontab para programar o horário:
```
sudo crontab -e
```
Código utilizado:
```
5 16 * * * python3 /home/pi/test.py
```
