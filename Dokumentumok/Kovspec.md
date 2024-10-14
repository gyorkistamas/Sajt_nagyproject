# 1.Áttekintés
### Funkcionális elemek:
A rendszer alapvető funkciói a következők:

Felhasználói regisztráció és bejelentkezés: A felhasználók saját fiókot hozhatnak létre, amelyhez egyedi azonosítóval, e-mail címmel és jelszóval férhetnek hozzá.

Termékek böngészése és szűrése: A felhasználók kategóriák alapján kereshetnek termékeket, valamint szűrhetnek ár, elérhetőség, és egyéb paraméterek alapján.

Kosár és rendeléskezelés: A felhasználók termékeket helyezhetnek a kosárba, majd leadhatják rendeléseiket különböző fizetési módokkal.

Adminisztrátori funkciók: Az adminisztrátorok kezelhetik a termékeket, kategóriákat, felhasználókat, és megtekinthetik a leadott rendeléseket.


### Nem funkcionális követelmények:
A rendszernek biztosítania kell a következőket:

Biztonság: Az adatbiztonság kiemelten fontos a felhasználói adatok, fizetési adatok, és a termékek biztonságos kezelése szempontjából. A jelszavakat biztonságos titkosítással kell tárolni.

Teljesítmény: A webshopnak képesnek kell lennie nagy mennyiségű termékek gyors kezelésére, és folyamatosan biztosítani kell a gyors oldalbetöltést.

Karbantarthatóság: A rendszernek modulárisnak és könnyen bővíthetőnek kell lennie, hogy az új funkciók és frissítések egyszerűen hozzáadhatók legyenek.


### Adatbázis követelmények:
Az adatbázis a webshop különböző funkcióit kiszolgáló táblákat fog tartalmazni. A főbb táblák a következők:

Felhasználók táblája: Tárolja a regisztrált felhasználók adatait (azonosító, név, e-mail cím, jelszó).

Termékek táblája: Minden terméket azonosít, amely tartalmazza a termék nevét, árát, leírását, készlet információit és kategóriáját.

Rendelések táblája: Tárolja a felhasználók által leadott rendeléseket, beleértve a termékeket, az összeget, a fizetési módot és a rendelés állapotát.

Kategóriák táblája: A termékek kategorizálására szolgáló tábla, amely lehetővé teszi a termékek böngészését különböző csoportok alapján.
# 2.Jelenlegi helyzet

A jelenlegi webshop rendszer egyszerű online termékértékesítési platformként működik, azonban számos olyan funkció és struktúra hiányzik belőle, amely a felhasználói élmény javításához, az adminisztráció hatékonyságának növeléséhez, valamint a biztonságos és skálázható adatkezeléshez szükséges.
## Felhasználói fiók kezelés

- Jelenleg a felhasználók fiók nélkül is böngészhetiok a termékeket, azonban a vásárláshoz regisztrációra van szükség. A regisztrációs folyamat alapvető információkat kér, de nincs lehetőség például jelszó-visszaállitásra vagy többféle belépési lehetőségre (pl. közösségi média fiókkal való belépés).
- A felhasználói adatok biztonsága nem megfelelő, mivel a jelszavak nem titkosítottak, és nincs kétfaktoros hitelesítési (2FA) lehetőség.

## Termékkatalógus és keresési funkciók

- A termékkatalógus egyszerű felépétísű, azonban a termékek kategorizálása és szűrése korlátozott. Jelenleg nincs több lehetőség több kritérium szerinti szűrésre (pl. ár, értékelések, készlet elérhetőség).
- Az adminisztrátorok számára nincs megfelelő felület a termékek egyszerű kezelésére (pl. termékek tömeges importálása/exportálása), és az új termékek hozzáadása manuálisan történik.

### Kosár és rendelési folyamat

- A kosár funkció alapszinten működik, de nincs támogatva az elhagyott kosarak visszakeresése vagy a visszatérő vásárlók automatikus kosárba helyezése.
- A rendelési folyamat csak korlátozott fizetési lehetőségeket támogat (pl. kizárólag banki átutalás), és nincs integrált fizetési megoldás, mint például bankkártyás fizetés vagy PayPal.


### Adminisztrációs felület

- Az adminisztrációs felület jelenleg nem teszi lehetővé a részletes riportok készítését a rendelések állapotáról, a forgalom elemzásáről, vagy a legkeresettebb termékekről.
- Hiányzik egy fejlett felhasználókezelő rendszer, amely lehetővé tenné az adminisztrátorok számára, hogy különböző jogosoltsági szinteket állítsanak be.


### Adatbázis struktúra
A webshop adatbázisának jelenlegi felépítése nem skálázható, és nem optimalizált a rendszer növekvő igényeihez. Az adatbázis struktúrájának jelenlegi jellemzői a következők:


- Felhasználók tábla: Alapvető adatokat tartalmaz (név,email,jelszó), de nincsenek bővített profil inormációk (pl. több szállítási cím, rendelési előzmények).
- Termékek tábla: A termékek tábla egyszerű információkat tárol (terméknév,ár, leírás), de hiányzik a készlet kezelése, valamint az értékelések és vélemények tárolása.
- Rendelések tábla: Tárolja az egyes rendelések alapadatait, de nincs nyomon követési funkció, amely megmutatná a rendelés aktuális állapotát (pl. feldolgozás alatt, szállítás alatt, lezárva).
- Kategóriák tábla: A termékek kategorizálására szolgáló rendszer alapvető szintű, azonban nincs lehetőség több szintű kategorizálásra vagy attribútum alapú szűrésre.


# 3.Vágyálom rendszer
A webshop célja, hogy felhasználóbarát környezetet biztosítson, ahol a felhasználók könnyen kereshetnek és vásárolhatnak különböző termékek.

### Célok

- Felhasználói élmény javítása
- Termékek egyszerű kereshetősége
- Zökkenőmentes vásárlási folyamat biztosítása
- Hatékony ügyfélszolgálat

### Funkcionális követelmények
#### Felhasználói regisztráció és bejelentkezés

- Regisztrációs űrlap a felhasználói adatok megadásához
- Bejelentkezési lehetőség e-mail cím és jelszó alapján
- Jelszó helyreállítási funkció

#### Termékkezelés

- Termékek hozzáadása, módosítása és törlése
- Termékkategóriák létrehozása és kezelése
- Termékek keresése szűrők segítségével (ár, népszerűség, értékelés)

#### Kosár és vásárlás

- Termékek kosárba helyezésének lehetősége
- Kosár tartalmának megtekintése és módosítása
- Vásárlási folyamat lépései (szállítási adatok, fizetési mód választása)

#### Fizetési lehetőségek
 
 - Különböző fizetési módok támogatása (bankkártya, Paypal, átutalás)
 - Biztonságos tranzakciók biztosítása
 
#### Ügyfélszolgálat

-Kapcsolati űrlap és élő chat lehetőség
-Gyakran ismételt kérdések (GYIK) szekció

### Nem funkcionális követelmények
#### Teljesítmény

- A webshopnak 3 másodpercen belül kell betöltődnie


#### Biztonság

- Adatok titkosítása és biztonságos tárolása
- Rendszeres biztonsági frissítések


#### Skalabilitás

- A rendszernek képesnek kell lennie a felhasználók és termékek számának növekedésére

### Képességek és technológiák

- Webfejlesztési keretrendszerek (pl. Laravel, React, DJango)
- Adatbázis-kezelés (pl. sqllite)
- Felhő alapú tárolás és hosztolás



# 4.Jelenlegi üzleti folyamatok modellje

Célunk a folyamatok optimalizálása és a hatékonyság növelése.
### Jelenlegi üzleti folyamatok
#### Termékkezelés

- Termékek hozzáadása: Az adminisztrátorok manuálisan töltik fel a termékadatokat (név, leírás, ár, kép)
- Készletkezelés: A termékek elérhetősége nyomon követhető, és automatikusan frissül, ha a vásárlások során változik

#### Vásárlási folyamat

- Kosár: A felhasználók termékeket helyeznek a kosárba. A kosár tartalma ideiglenesen tárolódik az adatbázisban
- Pénztár: A felhasználók megadják szállítási és számlázási adataikat, majd választhatnak a különböző fizetési módok közül

#### Megrendelés feldolgozása

- Megrendelések tárolása: Az adatbázisban minden megrendelés rögzítésre kerül, beleértve a vásárló adatait, a kiválasztott termékek , és a tranzakciós részleteket
- Visszaigazolás: A vásárlók e-mailben kapják meg a megrendelés visszaigazolását

### Adatbázis modell
#### Adatbázis struktúra






# 5.Igényelt üzleti folyamatok modellje

# 6.Követelménylista

# 7.Fogalomtár