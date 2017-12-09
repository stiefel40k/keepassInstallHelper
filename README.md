## Telepites

1. Toltsd le az aktualis verziot (2.XX) [innen](http://keepass.info/download.html)
  * Ha mas gepen, ahol nincs telepitve Keepass is szeretned hasznalni az adatbazisodat,
    akkor toltsd le mar most a portable verziot is, ha mar ugyis ott vagy.
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

## KeepassHttp Updater
Mi kell hozza?
* Python 3.6+ (letolheto [innen](https://www.python.org/downloads/))
* A ket letoltott file a `C:\bat\scripts` mappban van. (Ha ez neked nem szimpatikus a bat fileban atirhatod az eleresi utvonalat)

Futtasd az `update_starter.bat` scriptet rendszergazdakent, a tobbit bizd a pythonra ;)
