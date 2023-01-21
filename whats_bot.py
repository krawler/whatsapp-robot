from time import sleep
from whatsapp_api.whatsapp_api import WhatsApp

wp = WhatsApp()

sleep(10)
input("Pressione enter apos escanear o QRCode")
wp.search_contact('Olivia')

sleep(5)
print(wp.get_last_message())

sleep(10)
wp.driver.close()