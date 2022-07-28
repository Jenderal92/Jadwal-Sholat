import requests as jadwal
import json
from colorama import Fore

print '{}\nJadwal Sholat | by muslimsalat.com\n'.format(Fore.YELLOW)

REGION = raw_input(Fore.WHITE + 'Input Nama Kota / Negara : ')

try:
	jadwaljadwal = jadwal.get('http://muslimsalat.com/'+REGION+'/false.json')
	bismillah = json.loads(jadwaljadwal.text)["items"][0]
	print(Fore.WHITE + '\nKota / Negara :\n' + Fore.GREEN + json.loads(jadwaljadwal.text)["title"] + Fore.WHITE)
	print(Fore.WHITE + 'Tanggal :' + Fore.YELLOW + bismillah["date_for"] + Fore.WHITE)
	print(Fore.WHITE + 'Fajr [subuh] :' +' '+ Fore.RED + bismillah["fajr"] + Fore.WHITE)
	print(Fore.RED + 'Shurooq [syuruq] :' +' '+ Fore.WHITE + bismillah["shurooq"] + Fore.WHITE)
	print(Fore.WHITE + 'Dhuhr [djuhur] :' +' '+ Fore.RED + bismillah["dhuhr"] + Fore.WHITE)
	print(Fore.WHITE + 'Asr [asar] :' +' '+ Fore.RED + bismillah["asr"] + Fore.WHITE)
	print(Fore.WHITE + 'Maghrib [maghrib] :' +' '+ Fore.RED + bismillah["maghrib"] + Fore.WHITE)
	print(Fore.WHITE + 'Isha [isha] :' +' '+ Fore.RED + bismillah["isha"] + Fore.WHITE)
except:
	pass
	