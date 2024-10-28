# Funkcionális Specifikáció

## 1. Jelenlegi helyzet

A jelenlegi webshop rendszer egy alapvető online termékértékesítési platform, amely lehetővé teszi a termékek online megjelenítését és értékesítését. Azonban a jelenlegi struktúra és funkciók korlátozottak, ami akadályozza a felhasználói élmény és az adminisztráció hatékonyságának növelését, valamint a biztonságos és skálázható adatkezelést.

### Felhasználói Fiók Integráció
- Jelenlegi helyzet: A felhasználók nem tudnak sikeresen bejelentkezni vagy új fiókot regisztrálni. Ennek következtében a személyre szabott funkciók, mint a termékek mentése és az értesítések, nem érhetők el.

### Termékek Hozzáadása és Kosár
- Jelenlegi helyzet: A termékek "Hozzáadás" gombja jelenleg nem működik, így a felhasználók nem tudják termékeket hozzáadni a listájukhoz. Az oldal nem reagál a termékválasztásra, és nem jelenik meg semmilyen információ a kiválasztott termékekről.

- Jelenlegi helyzet: A kosár funkció jelenleg inaktív. A felhasználók nem tudják megtekinteni vagy kezelni a hozzáadott termékeiket, így nem módosíthatják a mennyiséget, és nem indíthatják el a vásárlási folyamatot.

#### Adatbázis
- Jelenlegi helyzet: Bár a termékek és felhasználói adatok adatbázis struktúrája kialakításra került, a vágyalom funkcióhoz szükséges adatokat kezelő tábla nem működik megfelelően, ami akadályozza a gyors keresést és az adatok kezelését.

#### Frontend
- Jelenlegi helyzet: A vágyalom funkció, valamint a felhasználói fiókok kezeléséhez szükséges frontend elemek nem reagálnak megfelelően. Hiányoznak az alapvető interaktív elemek, és a felhasználók nem tudják elérni a kívánt funkciókat.

#### Backend
- Jelenlegi helyzet: A szerveroldali logika jelenleg nem képes kezelni a termékek hozzáadását, eltávolítását vagy a felhasználói értesítéseket.

## 2. Vágyálom rendszer

A vágyalom rendszer célja, hogy javítsa a vásárlói élményt azáltal, hogy lehetőséget biztosít a felhasználók számára, hogy kedvenc termékeiket egyszerűen nyomon követhessék és később megvásárolhassák. Ez a funkció elősegíti a vásárlói hűséget és a visszatérő látogatásokat.

### Rendszer Felépítése
Felhasználói Fiók Integráció: 
- A funkciók csak bejelentkezett felhasználók számára érhető el, amely biztosítja a termékek mentését és a személyre szabott élményt. 
- A felhasználóknak lehetőségük van a fiókjukba való bejelentkezés után termékeket hozzáadni és vásárolni.
Termékek Hozzáadása: 
- A felhasználók a termékoldalon található "Hozzáadás" gombra kattintva egyszerűen hozzáadhatják a kiválasztott termékeket a listájukhoz. 
- A termékek képe, neve, ára és egyéb fontos információk megjelennek a listán.
Kosár: 
- A Kosár könnyen elérhető a felhasználói fiókból, ahol a felhasználók megtekinthetik a hozzáadott termékeket. 
- A lista tartalmazhat funkciókat, mint például a termékek eltávolítása, a mennyiség módosítása vagy a vásárlás megkezdése.
Értesítések: 
- A rendszer értesítéseket küld a felhasználóknak, ha a kívánt termékek ára csökken, vagy ha az adott termék készleten van. 
- E-mail értesítések is elérhetők a felhasználók számára, hogy emlékeztessék őket a kívánt termékeikről.

### Technikai Megvalósítás
Adatbázis: 
- A vágyalom adatai (termék ID, felhasználó ID, időbélyeg) egy külön táblában tárolódnak az adatbázisban, biztosítva a gyors keresést és az egyszerű kezelést.
Frontend: 
- A vágyalom funkciót HTML, CSS és JavaScript segítségével valósítjuk meg, lehetővé téve a felhasználók számára, hogy könnyedén navigáljanak és interakcióba lépjenek a rendszerrel.
Backend: 
- A vágyalom kezeléséhez szükséges logika a szerveroldalon fut, amely biztosítja a termékek hozzáadását, eltávolítását és a felhasználói értesítések kezelését.

## 3. Jelenlegi üzleti folyamatok modellje

#### Felhasználói Fiók Kezelés
- Jelenlegi állapot: Nincs megfelelő regisztrációs vagy bejelentkezési rendszer.

#### Vásárlási és Fizetési Folyamat
- Jelenlegi állapot: A vásárlási folyamat nem működik, mivel a kosár funkció és a fizetési rendszerek még nincsenek beállítva.

#### Rendelésfeldolgozás és Szállítási Automatizáció
- Jelenlegi állapot: A rendelésfeldolgozási folyamat nem létezik.

#### Kosárkezelés
- Jelenlegi állapot: A kosárfunkció nem működik.

#### Keresési Funkció
- Jelenlegi állapot: A Keresési funkció nem működik.

#### Termékkezelés és Készletkezelés
- Jelenlegi állapot: Nincs hatékony adminisztrációs felület a termékek kezelésére.

## 4. Igényelt üzleti folyamatok modellje

Az online weboldal jelenlegi üzleti folyamatai nem felelnek meg teljes mértékben a felhasználói elvárásoknak és az üzleti céloknak. Az igényelt üzleti folyamatok modellje bemutatja azokat a fejlesztési és bővítési lehetőségeket, amelyek szükségesek a felhasználói élmény javításához, az adminisztrációs hatékonyság növeléséhez, valamint az értékesítési folyamatok optimalizálásához.

#### Fejlett Felhasználói Fiók Kezelés
- Könnyű regisztráció és bejelentkezési lehetőségek, több belépési mód támogatása (pl. közösségi média), biztonságos adatkezelés, valamint személyre szabott felhasználói profilok.

#### Vásárlási és Fizetési Folyamat
- Gyors és egyszerű vásárlási folyamat, amely minimális lépéseket igényel a felhasználótól, többféle fizetési opcióval (hitelkártya, digitális pénztárcák, banki átutalás).

#### Rendelésfeldolgozás és Szállítási
- Automatikus rendelésfeldolgozás, amely magában foglalja a rendelés visszaigazolását, a szállítási információk frissítését és a kézbesítés nyomon követését a vásárlók számára.

#### Kosárkezelés
- A felhasználók könnyen hozzáadhatják és eltávolíthatják a termékeket a kosárból, módosíthatják a mennyiséget, és egyértelműen láthatják a kosár tartalmát és a vásárlás összegét.

#### Keresési Funkció
- A felhasználók gyorsan és könnyedén megtalálhatják a kívánt termékeket a keresősáv segítségével. A keresésnek releváns és pontos találatokat kell adnia, figyelembe véve a kulcsszavakat és szinonimákat.

#### Továbbfejlesztett Termékkezelés és Készletkezelés
- Könnyen használható adminisztrációs felület a termékek gyors hozzáadásához, szerkesztéséhez és eltávolításához, valamint automatizált készletfrissítések a valós idejű készletkezelés érdekében.

#### Adatbázis Struktúra és Kezelés
- Hatékony és skálázható adatbázis, amely biztonságosan és gyorsan kezeli a felhasználói adatokat, termékeket, rendeléseket, készletinformációkat, és más üzleti adatokat. Biztosítja a pontos nyomon követést és az adatok könnyű elérhetőség

## 5. Követelménylista

| Kép | Áruház neve | Termék neve | Leírás | Ár | db |

#### Felhasználói Fiók:
- Regisztrációs és bejelentkezési funkciók (e-mail, jelszó)
- Jelszó visszaállítás lehetősége
- Felhasználói profil kezelés (személyes adatok, rendelési előzmények)
  Termékkezelés

#### Termékek listázása és kategorizálása:
- Részletes termékleírások, képek, árak
- Termékek keresése és szűrése
- Termékek hozzáadása a vágyalomhoz
- Kosár és Vásárlás

#### Kosár funkció:
- Termékek hozzáadása, eltávolítás, mennyiség módosítás
- Vásárlási folyamat (kosár áttekintése, szállítási és fizetési adatok megadása)
- Fizetési Módok

#### Többféle online fizetési lehetőség:
- bankkártya, PayPal, banki átutalás
- Biztonságos tranzakciók garantálása

#### Szállítási lehetőségek és költségek megjelenítése:
- Várható érkezés

#### E-mail értesítések:
- rendelés megerősítése, szállítási értesítések
- Árváltozásokról és akciókról szóló értesítések

## 6. Használati esetek

- Felhasználói Fiók Kezelése:
    A felhasználók regisztrálhatnak, bejelentkezhetnek, jelszót állíthatnak vissza, és kezelhetik a fiókadataikat.
- Termékkeresés:
    A felhasználók kulcsszavak segítségével kereshetnek termékeket az oldalon, és szűrőkkel szűkíthetik a találatokat.
- Kosár Kezelése:
    A felhasználók hozzáadhatnak termékeket a kosárhoz, módosíthatják a mennyiséget, eltávolíthatják a termékeket, és megtekinthetik a teljes rendelési összesítést.
- Vásárlási és Fizetési Folyamat:
    A felhasználók megrendelhetik a kiválasztott termékeket, kitölthetik a szállítási adatokat, kiválaszthatják a fizetési módot és véglegesíthetik a vásárlást.
- Termékek Kezelése:
    Az adminisztrátorok hozzáadhatnak, szerkeszthetnek és eltávolíthatnak termékeket, valamint kezelhetik a készletet.

## 7. Megfeleltetés, hogyan fedik le a használati eseteket a követelményeket

- Felhasználói Fiók Kezelése:
    Biztosítani a felhasználók számára, hogy személyre szabott élményt kapjanak és könnyen hozzáférjenek saját profiljukhoz.
- Termékkeresés:
    Megkönnyíteni a termékek gyors és egyszerű megtalálását.
- Kosár Kezelése:
    Lehetővé tenni a vásárlási folyamat megkezdését és a kosár tartalmának egyszerű kezelését.
- Vásárlási és Fizetési Folyamat:
    Zökkenőmentes és gyors vásárlási élményt biztosítani a felhasználók számára.
- Termékek Kezelése:
     Egyszerűsíteni a termékek kezelését és biztosítani a készletadatok pontosságát.


## 8. Képernyőtervek

### Korai látványterv

![korai_látványterv](../Img/memulatoralphfa.jpg)

## 9. Forgatókönyvek

## 10. Funkció - követelmény megfeleltetése

|         Követelmény        |                                  Funkció                                              |
| :------------------------- | :------------------------------------------------------------------------------------ |
| Felhasználói Fiók Kezelés	 | Felhasználóknak lehetőségük van regisztrálni, bejelentkezni és jelszót visszaállítani |
|           Keresés          | Keresési lehetőség kulcsszavakkal.                                                    |
|   Termékek Megtekintése    | Termékek részletes információjának megjelenítése (kép, név, ár, leírás).              |
|           Kosár            | A kosár tartalmának áttekinthetősége és termékek módosítása (mennyiség, eltávoltás)   |
|      Fizetési Folyamat     | Biztonságos online tranzakciós lehetőség                                              |
|  Adminisztrációs Funkciók  | Adminisztrátorok képesek termékek hozzáadására, szerkesztésére és törlésére.          |

## 11. Fogalomszótár

- Webshop: 
    Olyan online platform, ahol termékeket vagy szolgáltatásokat lehet vásárolni.
- Kosár: 
    Az a virtuális hely, ahol a vásárló az általuk kiválasztott termékeket összegyűjti a vásárlás során.
- Termék:
    Olyan áru vagy szolgáltatás, amelyet a webshop kínál, és amelyet a vásárlók megvásárolhatnak.
- Keresés: 
    Az a funkció, amely lehetővé teszi a vásárlók számára, hogy kulcsszavak vagy szűrők segítségével gyorsan megtalálják a kívánt termékeket a webshopban.
- Kategória: 
    Az a csoportosítás, amelybe a webshopban elérhető termékek besorolásra kerülnek, segítve a vásárlókat a böngészésben 
    (pl. Külföldi sajtok, Magyar sajtok).
- Vásárlási folyamat:
    Az a lépések sora, amelyet a vásárlók követnek a termék kiválasztásától a vásárlás befejezéséig.
- Fizetési mód:
    Az a lehetőség, amelyet a vásárlók választhatnak a vásárlás során (pl. bankkártya, PayPal, utánvét).
- Szállítási díj: 
    A költség, amelyet a vásárlónak a termék kiszállításáért kell fizetnie.
- Rendelés visszaigazolás:
    Az a nyugtázó üzenet vagy e-mail, amelyet a webshop küld a vásárlónak a rendelés sikeres lebonyolítása után.
- Felhasználói fiók: 
    Az a személyes profil, amelyet a vásárlók létrehozhatnak a webshopban, és amely lehetővé teszi számukra a rendeléseik nyomon követését, valamint személyre szabott ajánlatok elérését.
- Készlet: 
    A webshopban elérhető termékek mennyisége.
- Adatvédelem: 
    Az a gyakorlat, amely biztosítja, hogy a vásárlók személyes adatait biztonságban kezelik, és nem használják fel jogosulatlanul.
- Regisztráció: 
    A folyamat, amely során a felhasználók létrehozzák fiókjukat a webshopban, hogy vásárolhassanak vagy hozzáférhessenek speciális funkciókhoz.