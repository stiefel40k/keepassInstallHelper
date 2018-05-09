## Telepítés

1. Töltsd le az aktuális verziót (2.XX) [innen](http://keepass.info/download.html)
    * Ha más gépén, ahol nincs telepítve KeePass is szeretnéd használni az adatbázisodat,
      akkor töltsd le már most a hordozható verziót is, ha már úgyis ott vagy.
      Részletek lentebb.
1. Telepítsd a programot
    * az autoupdate NEM tölt le és telepít semmit sem, csak szól, hogy van új verzió
3. Indítsd el a frissen telepített KeePass-t

## Új adatbázis
1. Válaszd ki a __Select -> New__ (Üres fehér lap az ikonja)
2. Válaszd ki a nevet, és hogy hol legyen az adatbázis
3. Ezek után add meg a mesterjelszót
    * Ezzel a jelszóval fogod tudni feloldani az összes többi jelszavadat.
      Mivel ezek után lényegében csak ezt az egy jelszót kell majd megjegyezned, és ez a jelszó fogja az __ÖSSZES__ többi jelszavadat védeni
      érdemes egy erős jelszót választani (mondjuk 20+ karakter, kis-nagy betű, szám, speciális karakter)
    * Opcionális: Keyfile készítése:
        * A keyfile egy második faktorként szolgál.
          Hasznalhatod a jelszó *helyett* vagy *vele együtt*.
          A lényeg csak annyi, hogy sok random legyen benne.
        * Választhatsz, hogy generáljon neked a KeePass egy keyfile-t,
          vagy pedig egy már létező fájl (Word dokumentum vagy egy JPG, vagy bármi más) legyen a keyfile 
4. Adatbázis beállítások:
    * A legtöbb magától értetődő, szóval nem nagyon mennék bele.

## Plugin-ek
1. A KeePass rengeteg plugin-nal rendelkezik. ([lásd itt](https://keepass.info/plugins.html))
2. Én lényegében csak a [KeePassHttp](https://keepass.info/plugins.html#keepasshttp) plugin-t használom,
   az összes többiről gőzöm nincs, hogy mit csinál.
    * Mire jó?
        * Engedélyezi a kommunikációt a browser-ed (Chrome, Safari, Firefox) és a KeePass között,
          ezáltal, ha fel van rakva a megfelelő plugin a browser-ben, működik az autocomplete.
    * Hogyan rakjam fel?
        * [Olvasd el ezt](https://github.com/pfn/keepasshttp/#non-windows--manual-windows-installation)
        * TL;DR:
            * Letöltöd [ezt](https://github.com/pfn/keepasshttp/raw/master/KeePassHttp.plgx) és bemásolod a `<keepass_install_dir>\\Plugins` mappába
    * Hogyan frissítsem?
        * Mivel lusta vagyok írtam egy updater script-et, ami megcsinálja az update-t
        * Leírást lásd lentebb
3. Browser extensions:
    * [Chrome](https://chrome.google.com/webstore/detail/chromeipass/ompiailgknfdndiefoaoiligalphfdae=)
    * [Firefox](https://addons.mozilla.org/en-US/firefox/addon/passifox/)
    * [Safari](https://github.com/mmichaa/passafari.safariextension) (ezt sosem használtam még, szóval nem tudok róla semmit)
4. Cloud sync
    * én nem használom, szóval sokat nem tudok róla, de itt van pár link:
        * [Google Drive](https://sourceforge.net/projects/kp-googlesync/)
        * [One Drive](https://github.com/KoenZomers/KeePassOneDriveSync)
        * Lásd még a `Backup & Synchronization & IO` bejegyzés alatt [itt](https://keepass.info/plugins.html)
    * __FONTOS:__ ebben az esetben mindenképpen ajánlanám a keyfile használatát mint extra security
        * __MÉG FONTOSABB: A KEYFILE-T NE TÖLTSD FEL A CLOUDRA, MERT AKKOR ELVESZTI AZ ÉRTELMÉT!!!4!__ 

## Jelszavak
__FONTOS:__ az hogy a jelszavad a KeePass-ban van, még nem jelenti azt, hogy ténylegesen az a jelszavad mondjuk facebook-on.
Első körben minden jelszavadat meg kell változtatnod egyesével.
Tudom, ez szar, meg unalmas, de hidd el megéri.
1. Az add entry gombbal tudsz új jelszót megadni.
2. Adatok:
    * Title: mi legyen a jelszó/acc neve (pl. Gmail, Facebook) ez csak arra van, hogy könnyebben megtaláld a megfelelő acc-ot
    * User name: evidens
    * Password:
        * Van két gomb, az egyiken három pötty látható, ez megjeleníti az adott jelszót.
        * A másik, egy kulcs, a jelszó generátor, ha rákattintasz generál neked új jelszavakat.
          Csinálhatsz saját jelszó generátorokat, ahol el tudod menteni a beállítasokat.
          (Példaul ha egy oldal nem enged bizonyos karaktereket, akkor megadhatod, hogy melyek legyenek kizárva stb.)
    * URL: milyen URL alatt legyen érvényes az acc (hasznos ha használod a KeePassHttp plugin-t)
    * Expires: megadhatod, hogy meddig legyen érvényes a jelszó
        * __FONTOS:__ ez nem jelenti azt, hogy a jelszavad törlődne, ha lejárt, csak vizuálisan jelzi neked (pirosan át van húzva), hogy lejárt a jelszó
3. Miután generáltál új jelszót, változtasd meg a jelszavadat az újra az adott szolgáltatónál (Gmail, Facebook stb.)
4. Az előnye az egész dolognak, hogy
    1. Nem kell megjegyezned a jelszót
    2. Minden acc-odnak lehet különböző jelszava

## Android App
Androidra a KeePass2Android App-et tudom ajánlani.
Letölthető [innen](https://play.google.com/store/apps/details?id=keepass2android.keepass2android&hl=hu)

## Hordozható verzió
1. Töltsd le a hordozható verziót [innen](http://keepass.info/download.html)
2. Csomagold ki a ZIP-et egy pendrive-ra, vagy amire szeretnéd.
3. Kész

Megjegyzés:
Én személy szerint még a következőt csináltam, mivel se a pendrive-om se a Windows partícióm nincs titkosítva
(tudom, shame on me, tervben van), ezért a keyfile-t még beraktam egy veracrypt konténerbe.
Lepések:
1. Töltsd le a veracrypt programot [innen](https://veracrypt.codeplex.com/wikipage?title=Downloads#Title)
2. Telepítsd
    * Ha ezt is szeretnéd hordozható verzióban a pendrive-odon tartani, hiszen másképp nem férsz hozzá a keyfile-hoz,
      akkor a telepítés közben az `Install` opció helyett válaszd az `Extract` opciót. Add meg az útvonalat és kész.
3. Készíts egy konténert
    1. Create an encrypted file konténer
    2. Standard veracrypt konténer
    3. Add meg a konténer helyét
    4. Én személy szerint az AES-t használom, de mindenkinek megvan a maga kedvenc titkosítási algoritmusa, szóval amit akarsz :)
    5. SHA-512 megfelelő
    6. Add meg a méretet (mivel csak a keyfile lesz benne pár MB-nél többre valszeg nem lesz szükség)
    7. Jelszó: NE a KeePass-odban tárold, hacsak nem tudod kívülről, mert a KeePass feloldásához kelleni fog a keyfile, a keyfile-hoz meg kelleni fog a KeePass...
    8. Válassz fájlrendszert (NTFS/FAT Windows esetében) aztán mozgasd az egeredet amíg zöld nem lesz a csík
4. Oldd fel a konténert a jelszóval
5. Másold be a konténerbe a keyfile-t (a konténer mint external drive van jelen a gépeden)
6. Zárd be a konténert (Unmount)
7. Másold a konténer fájlt a pendrive-ra

__FONTOS:__ Ha az USB-ről indítod el a VeraCrypt-et, akkor minden alkalommal kérni fog rendszergazdai jogokat.
Ha ez nincs megadva neki, akkor nem fog működni.

## KeePassHttp Updater
Mi kell hozzá?
* Python 3.6+ (letölthető [innen](https://www.python.org/downloads/))
* A két letöltött fájl a `C:\bat\scripts` mappában van. (Ha ez neked nem szimpatikus a `update_starter.bat` fájlban átírhatod az elérési útvonalat)

A fájlokat a scripts mappában találod.

Futtasd az `update_starter.bat` scriptet rendszergazdaként, a többit bízd a python-ra ;)
