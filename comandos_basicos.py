from whatsapp_api.whatsapp_api import WhatsApp

wp = WhatsApp()
wp.search_contact('Aprendizagens 3')
print('phone numbers' + wp.get_group_numbers().__str__)