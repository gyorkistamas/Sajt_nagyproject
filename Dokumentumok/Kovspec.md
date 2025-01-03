# 1.Áttekintés

### A rendszer alapvető funkciói a következők:

- Felhasználói regisztráció és bejelentkezés: A felhasználók saját fiókot hozhatnak létre, amelyhez egyedi azonosítóval, e-mail címmel és jelszóval férhetnek hozzá.
- Termékek böngészése és szűrése: A felhasználók kategóriák alapján kereshetnek termékeket, valamint szűrhetnek ár, elérhetőség, és egyéb paraméterek alapján.
- Kosár és rendeléskezelés: A felhasználók termékeket helyezhetnek a kosárba, majd leadhatják rendeléseiket különböző fizetési módokkal.
- Biztonság: Az adatbiztonság kiemelten fontos a felhasználói adatok, fizetési adatok, és a termékek biztonságos kezelése szempontjából. A jelszavakat biztonságos titkosítással kell tárolni.
- Teljesítmény: A webshopnak képesnek kell lennie nagy mennyiségű termékek gyors kezelésére, és folyamatosan biztosítani kell a gyors oldalbetöltést.
- Karbantarthatóság: A rendszernek modulárisnak és könnyen bővíthetőnek kell lennie, hogy az új funkciók és frissítések egyszerűen hozzáadhatók legyenek.

# 2.Jelenlegi helyzet

A jelenlegi webshop rendszer egyszerű online termékértékesítési platformként működik, azonban számos olyan funkció és struktúra hiányzik belőle, amely a felhasználói élmény javításához, az adminisztráció hatékonyságának növeléséhez, valamint a biztonságos és skálázható adatkezeléshez szükséges.
### Felhasználói fiók kezelés

- Jelenleg a felhasználók fiók nélkül is böngészhetiok a termékeket, azonban a vásárláshoz regisztrációra van szükség. A regisztrációs folyamat alapvető információkat kér, de nincs lehetőség például jelszó-visszaállitásra vagy többféle belépési lehetőségre (pl. közösségi média fiókkal való belépés).
- A felhasználói adatok biztonsága nem megfelelő, mivel a jelszavak nem titkosítottak, és nincs kétfaktoros hitelesítési (2FA) lehetőség.

### Termékkatalógus és keresési funkciók

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

##### Rendelkezésre állás:

- A webshop rendelkezésre állása éves szinten legalább 99,9% kell legyen.

- Karbantartási ablakokat megfelelően kell ütemezni, és ezek időtartama nem haladhatja meg az összes leállási idő 0,1%-át.

##### Terheléses tesztelés:

- A rendszer teljesítményét rendszeresen kell tesztelni különböző terhelési szinteken, és az eredményeket dokumentálni kell a fejlesztési iterációk során.

##### Hálózati teljesítmény:

- A webshop minimális sávszélesség-igénye ne haladja meg a 2 Mbps-ot egyetlen felhasználóra nézve, normál használat mellett.

#### Biztonság

- Adatok titkosítása és biztonságos tárolása
- Rendszeres biztonsági frissítések


#### Skalabilitás

- A rendszernek képesnek kell lennie a felhasználók és termékek számának növekedésére

### Képességek és technológiák

- Webfejlesztési keretrendszerek (pl. Laravel, React, DJango)
- Adatbázis-kezelés (pl. sqlite)
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








# 5.Igényelt üzleti folyamatok modellje
A webshop célja egy felhasználóbarát online kereskedelmi platform biztosítása, ahol a vásárlók könnyedén böngészhetnek termékek között, vásárlásokat bonyolíthatnak le, és nyomon követhetik megrendeléseiket. 
A rendszer adatbázissal rendelkezik, amely a termékek, vásárlók és tranzakciók adatait kezeli.

### Funkcionális követelmények
#### Felhasználói fiókok
- Regisztráció: A felhasználók e-mail címük és jelszavuk megadásával regisztrálhatnak a webshopba.
- Bejelentkezés: A regisztrált felhasználók biztonságos bejelentkezési lehetőséggel rendelkeznek.
- Felhasználói profil kezelése: A felhasználók módosíthatják személyes adataikat (név, cím, elérhetőségek).
#### Termékek kezelése
- Terméklistázás: A webshopban minden termék kategóriákba sorolva jelenik meg, keresési és szűrési lehetőséggel.
- Termékadatok megjelenítése: Minden termékhez részletes adatokat kell megadni (név, ár, leírás, elérhetőség, képek).
- Kosár funkció: A felhasználók a kiválasztott termékeket kosárba helyezhetik.
#### Rendelések kezelése
- Vásárlási folyamat: A felhasználó kiválaszthatja a fizetési módot (online bankkártyás fizetés, utánvét) és szállítási lehetőségeket (háztól házig, csomagpontra).
- Megrendelés követése: A felhasználók rendeléseik állapotát követhetik a felhasználói fiókjukban.
### Adatbázis követelmények
- Terméktáblázat: A termékek adatai (ID, név, leírás, ár, elérhetőség, kategória).
- Felhasználók táblázat: A regisztrált felhasználók adatai (ID, név, e-mail, jelszó).
- Rendelések táblázat: A leadott rendelésekkel kapcsolatos adatok (ID, felhasználó ID, termékek, rendelési dátum, összeg).
- Szállítás és fizetés: A szállítási címek és fizetési adatok kezelésére külön táblák (felhasználóhoz és rendeléshez kapcsolva).

### Nem funkcionális követelmények
#### Teljesítmény
- A webshopnak gyors válaszidőkkel kell működnie, különösen a keresési funkció és a kosár frissítése esetén.
#### Biztonság
- Minden adatátvitel biztonságos csatornákon (HTTPS) keresztül történik.
- A felhasználói jelszavak titkosítva tárolódnak az adatbázisban.
#### Skálázhatóság
- Az adatbázis és az alkalmazás szerver képes legyen nagy felhasználószám kezelésére és nagy termékválaszték kezelésére.
### Felhasználói szerepkörök
- Adminisztrátor: Az adminisztrátorok hozzáférhetnek a teljes adatbázishoz, kezelhetik a termékeket, felhasználókat, valamint a rendelések állapotát.
- Felhasználó: A regisztrált vásárlók böngészhetik a termékeket, vásárlásokat bonyolíthatnak, és követhetik rendeléseiket.

### Üzleti folyamatok modellje
Az üzleti folyamatok a következő lépésekre bonthatók:

- Felhasználói regisztráció: A felhasználó létrehoz egy fiókot a webshopban.
- Termékek böngészése: A felhasználó keres a webshop termékei között.
- Vásárlási folyamat: A felhasználó a fizetési és szállítási információk megadásával véglegesíti a vásárlást.
- Rendelés feldolgozása: Az adminisztrátor a háttérrendszeren keresztül kezeli a rendeléseket és szállítást.
- Megrendelés követése: A felhasználó nyomon követi a rendelése állapotát.

# 6.Követelménylista
### Felhasználói követelmények
#### Regisztráció és bejelentkezés:

- A felhasználóknak lehetősége kell legyen regisztrálni, illetve bejelentkezni a webshopba.
- A regisztráció során kötelező mezők: felhasználónév, jelszó, e-mail cím, szállítási cím.
- Bejelentkezés után a felhasználók hozzáférhetnek saját profiljukhoz és rendelési előzményeikhez.

#### Termékböngészés és keresés:

- A felhasználóknak lehetőségük kell legyen a termékek kategóriák szerinti böngészésére és keresésére.
- A keresési eredmények szűrhetők különböző paraméterek alapján, mint ár, népszerűség vagy értékelések.


#### Kosár és rendelés:

- A felhasználók hozzáadhatják a termékeket a kosárhoz.
- A kosárban lévő termékeket a felhasználók módosíthatják (törlés, mennyiség változtatása).
- A rendelés véglegesítésénél a felhasználóknak meg kell adniuk a szállítási és fizetési adatokat.

#### Értékelés és véleményezés:

- A felhasználók értékelhetik a vásárolt termékeket, és véleményt írhatnak róluk.

#### Profilkezelés:

- A felhasználók módosíthatják személyes adataikat (név, cím, jelszó, stb.).
- Megtekinthetik és nyomon követhetik korábbi rendeléseiket.


### Funkcionális követelmények
#### Termékkezelés:

- Az adminisztrátori felület lehetővé teszi a termékek hozzáadását, módosítását és törlését.
- Minden termékhez tartozó adatok: név, leírás, ár, kép, készlet mennyisége, kategória, értékelések.

#### Felhasználókezelés:

- Az adminisztrátorok kezelhetik a felhasználói fiókokat (pl. törlés, fiók felfüggesztése).

#### Rendeléskezelés:

- A rendszer automatikusan nyilvántartja a leadott rendeléseket, állapotukat (pl. folyamatban, teljesítve, törölve).
- Az adminisztrátorok frissíthetik a rendelés állapotát, valamint kezelhetik a visszatérítéseket.

#### Szállítási rendszer:

- A felhasználóknak különböző szállítási lehetőségeket kell kínálni (pl. standard, expressz).
- A rendszernek követnie kell a szállítási állapotokat, és értesítenie kell a felhasználót.

### Rendszerkövetelmények

#### Platform:
- A webshopnak futnia kell minden modern böngészőn (pl. Chrome, Firefox, Edge).
#### Adatbázis:
- A rendszerhez MySQL vagy SQLite adatbázist kell használni.
#### Szerver követelmények:
- A webshophoz PHP, Node.js vagy egyéb backend technológia szükséges.
- Szükséges minimum egy VPS vagy dedikált szerver, amely támogatja a skálázható infrastruktúrát.


# 7.Fogalomtár

- VPS: azaz virtuális dedikált szerver vagy virtuális privát szerver egy olyan virtuális számítógép, amelyet internetes tárhelyszolgáltatás részeként értékesítenek.
- Skálázható infrastruktúra: A skálázható infrastruktúra olyan informatikai rendszer, amely képes hatékonyan bővülni vagy zsugorodni a terhelés vagy igények változásának megfelelően, anélkül hogy jelentős teljesítményromlás vagy probléma lépne fel. 