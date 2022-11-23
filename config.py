import os
import ProxyCloud

BOT_TOKEN = '5771140185:AAEXgz_lUQH9mxBYC2U7X3EMM0v_0ro1-iU' #Aqui va el token del bot
API_ID =  13233271 #Tu api id de telegram
API_HASH = 'e3ce8145aa657c2a4cc5cf0f7183e476' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','nautaii').split(';')

static_proxy = 'socks5h://KGGJJJYIJFLIFEYDJFLEKHYGCHDHRHHKCHHGCE'
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['nautaii','EleaGlez98'] = 0

