import urllib.request
import ctypes
import sys
import os

if not ctypes.windll.shell32.IsUserAnAdmin():
	print('Please start the program as an Administrator')
	input("Press Enter to continue...")
	sys.exit(1)

temp_keepass = os.path.join(os.environ['temp'], "KeePassHttp.plgx")
urllib.request.urlretrieve("https://github.com/pfn/keepasshttp/raw/master/KeePassHttp.plgx", temp_keepass)

os.remove('C:\\Program Files (x86)\\KeePass Password Safe 2\\Plugins\\KeePassHttp.plgx')
os.rename(temp_keepass, 'C:\\Program Files (x86)\\KeePass Password Safe 2\\Plugins\\KeePassHttp.plgx')

input('Update done. Please press enter to continue...')
sys.exit(0)