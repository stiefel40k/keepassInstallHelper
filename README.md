## Telepites

1. Toltsd le az aktualis verziot (2.XX) [innen](http://keepass.info/download.html)
  * Ha mas gepen, ahol nincs telepitve Keepass is szeretned hasznalni az adatbazisodat,
    akkor toltsd le mar most a portable verziot is, ha mar ugyis ott vagy.
    Reszletek lentebb.
1. Telepitsd a programot
  * az autoupdate NEM tolt le es telepit semmit sem, csak szol, h van uj verzio
3. Inditsd el a frissen telepitett Keepass-t

## Uj adatbazis
1. Valaszd ki a __Select -> New__ (Ures feher lap az ikonja)
2. Valaszd ki a nevet, es hogy hol legyen az adatbazis
3. Ezek utan add meg a mesterjelszot
  * Ezzel a jelszoval fogod tudni feloldani az osszes tobbi jelszavadat.
    Mivel ezek utan lenyegen csak ezt az egy jelszot kell majd megjegyezned, es ez a jelszo fogja az __OSSZES__ tobbi jelszavadat vedeni
    erdemes egy eros jelszot valasztani (mondjuk 20+ karakter, kis-nagy betu, szam, specialis karakter)
  * Opcionalis: Keyfile keszitese:
    * A keyfile egy masodik faktorkent szolgal.
      Hasznalhatod a jelszo *helyett* vagy *vele egyutt*.
      A lenyeg csak annyi, hogy sok random legyen benne.
    * Valaszhatsz, hogy generaljon neked a Keepass egy keyfilet,
      vagy pedig egy mar letezo filet (Word dokumentum vagy egy JPG, vagy barmi mas) legyen a keyfile 
4. Adatbazis beallitasok:
  * A legtobb magatol erthetodo, szoval nem nagyon mennek bele.

## Pluginek
1. A keepass rengeteg pluginnal rendelkezik. ([lasd itt](https://keepass.info/plugins.html))
2. En lenyegeben csak a [KeePassHttp](https://keepass.info/plugins.html#keepasshttp) plugint hasznalom,
   az osszes tobbirol gozom nincs, hogy mint csinal.
  * Mire jo?
    * Engedelyezi a kommunikaciot a browsered (Chrome, Safari, Firefox) es a Keepass kozott,
      ezaltal, ha fel van rakva a megfelelo plugin a browserben, mukodik az autocomplete.
  * Hogyan rakjam fel?
    * [Olvasd el ezt](https://github.com/pfn/keepasshttp/#non-windows--manual-windows-installation)
    * TL;DR:
      * Letoltod [ezt](https://github.com/pfn/keepasshttp/raw/master/KeePassHttp.plgx) es bemasolod a `<keepass_install_dir>\\Plugins` mappaba
  * Hogyan frissitsem?
    * Mivel lusta vagyok irtam egy updater scriptet, ami megcsinalja az updatet
    * Leirast last lentebb
3. Browser extensions:
  * [Chrome](https://chrome.google.com/webstore/detail/chromeipass/ompiailgknfdndiefoaoiligalphfdae=)
  * [Firefox](https://addons.mozilla.org/en-US/firefox/addon/passifox/)
  * [Safari](https://github.com/mmichaa/passafari.safariextension) (ezt sosem hasznaltam meg, szoval nem tudok rola semmit)
4. Cloud sync
  * en nem hasznalom, szoval sokat nem tudok rola, de itt van par link:
    * [Google Drive](https://sourceforge.net/projects/kp-googlesync/)
    * [One Drive](https://github.com/KoenZomers/KeePassOneDriveSync)
    * Lasd meg a `Backup & Synchronization & IO` bejegyzes alatt [itt](https://keepass.info/plugins.html)
  * __FONTOS:__ ebben az esetben mindenkeppen ajanlanam a keyfile hasznalatat mint extra security
    * __MEG FONTOSABB: A KEYFILET NE TOLTSD FEL A CLOUDRA, MERT AKKOR ELVESZTI AZ ERTELMET!!!1!__ 

## Jelszavak
__FONTOS:__ az hogy a jelszavad a Keepassban van, meg nem jelenti azt, hogy tenylegesen az a jelszavad mondjuk facebookon.
Elso korben minden jelszavadat meg kell valtoztatnod egyesevel.
Tudom, ez szar, meg unalmas, de hidd el megeri.
1. Az add entry gombbal tudsz uj jelszot megadni.
2. Adatok:
  * Title: mi legyen a jelszo/acc neve (pl Gmail, Facebook) ez csak arra van, hogy konnyebben megtalald a megfelelo acc-ot
  * User name: evidens
  * Password:
    * Van ket gomb az egyik, harom potty, ez megjeleniti az adott jelszot.
    * A masik, egy kulcs, a jelszogenerator, ha rakattintasz general neked uj jelszavakat.
      Csinalhatsz sajat jelszo generatorokat, ahol el tudod menteni a beallitasokat.
      (Peldaul ha egy oldal nem enged bizonyos karaktereket, akkor megadhatod, hogy melyek legyenek kizarva stb.)
    * URL: milyen URL alatt legyen ervenyes az acc (hasznos ha hasznalod a KeepassHttp plugint)
    * Expires: megadhatod, hogy meddig legyen ervenyes a jelszo
      * __FONTOS:__ ez nem jelenti azt, hogy a jelszavad torlodne, ha lejart, csak vizualisan jelzi neked (pirosan at van huzva), hogy lejard a jelszo
3. Miutan generaltal uj jelszot valtoztasd meg a jelszavadat az ujra az adott szolgaltatonal (Gmail, Facebook stb.)
4. Az elonye az egesz dolognak, hogy
  1. Nem kell megjegyezned a jelszot
  2. Minden acc-odnak lehet kulonbozo jelszava

## Android App
Androidra az Keepass2Android App-et tudom ajanlani.
Letoltheto [innen](https://play.google.com/store/apps/details?id=keepass2android.keepass2android&hl=hu)

## Hordozhato verzio
1. Toltsd le a hordozhato verziot [innen](http://keepass.info/download.html)
2. Csomagold ki a ZIP-et egy pendrivera, vagy amire szeretned.
3. Kesz

Megjegyzes:
En szemely szerint meg a kovetkezot csinaltam, mivel se a pendrive-om se a windows particiom nincs titkositva
(tudom, shame on me, tervben van), ezert a keyfilet meg beraktam egy veracrypt kontenerbe.
Lepesek:
1. Toltsd le a veracrypt programot [innen](https://veracrypt.codeplex.com/wikipage?title=Downloads#Title)
2. Telepitsd
  * Ha ezt is szeretned hordozhato verzioban a pendriveodon tartani, hiszen maskepp nem fersz hozza a keyfilehoz,
    akkor a telepites kozben az `Install` opcio helyett valaszd az `Extract` opciot. Add meg az utvonalat es kesz.
3. Keszits egy containert
  1. Create an encrypted file container
  2. Standard veracrypt container
  3. Add meg a container helyet
  4. En szemely szerint az AES-t hasznalom, de mindenkinek megvan a maga kedvenc titkositasi algoritmusa, szoval amit akarsz :)
  5. SHA-512 megfelelo szemely szerint
  6. Add meg a meretet (mivel csak a keyfile lesz benne par MB-nel tobbre valszeg nem lesz szukseg)
  7. Jelszo: NE a Keepassodban tarold, hacsak nem tudod kivulrol, mert a Keepass feloldasahoz kelleni fog a keyfile, a keyfile-hoz meg kelleni fogy a Keepass...
  8. Valassz fajlrendszert (NTFS/FAT windows eseteben) aztan mozgasd az egeredet amig zold nem lesz a csik
4. Oldd fel a containert a jelszoval
5. Masold be a containerbe a keyfile-t (a container mint external drive van jelen a gepeden)
6. Zard be a containert (Unmount)
7. Masold a container fajlt a pendrive-ra

__FONTOS:__ Ha az USB-rol inditod el a VeraCrypt-et, akkor minden alkalommal kerni fog rendszergazdai jogokat.
Ha ez nincs megadva neki, akkor nem fog mukodni.

## KeepassHttp Updater
Mi kell hozza?
* Python 3.6+ (letolheto [innen](https://www.python.org/downloads/))
* A ket letoltott file a `C:\bat\scripts` mappban van. (Ha ez neked nem szimpatikus a bat fileban atirhatod az eleresi utvonalat)

Futtasd az `update_starter.bat` scriptet rendszergazdakent, a tobbit bizd a pythonra ;)
