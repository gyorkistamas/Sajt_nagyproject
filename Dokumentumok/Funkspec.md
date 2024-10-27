# Funkcionális Specifikáció

## 1. Jelenlegi helyzet

A jelenlegi webshop rendszer egy alapvető online termékértékesítési platform, amely lehetővé teszi a termékek online megjelenítését és értékesítését. Azonban a jelenlegi struktúra és funkciók korlátozottak, ami akadályozza a felhasználói élmény és az adminisztráció hatékonyságának növelését, valamint a biztonságos és skálázható adatkezelést.

### Felhasználói Fiók Integráció

- Jelenlegi helyzet: A felhasználók nem tudnak sikeresen bejelentkezni vagy új fiókot regisztrálni. Ennek következtében a személyre szabott funkciók, mint a termékek mentése és az értesítések, nem érhetők el.

### Termékek Hozzáadása és Kosár

- Jelenlegi helyzet: A termékek "Hozzáadás" gombja jelenleg nem működik, így a felhasználók nem tudják termékeket hozzáadni a listájukhoz. Az oldal nem reagál a termékválasztásra, és nem jelenik meg semmilyen információ a kiválasztott termékekről.

- Jelenlegi helyzet: A kosár funkció jelenleg inaktív. A felhasználók nem tudják megtekinteni vagy kezelni a hozzáadott termékeiket, így nem módosíthatják a mennyiséget, és nem indíthatják el a vásárlási folyamatot.

### Technikai Megvalósítás Jelenlegi Állapota

#### Adatbázis

- Jelenlegi helyzet: Bár a termékek és felhasználói adatok adatbázis struktúrája kialakításra került, a vágyalom funkcióhoz szükséges adatokat kezelő tábla nem működik megfelelően, ami akadályozza a gyors keresést és az adatok kezelését.

#### Frontend

- Jelenlegi helyzet: A vágyalom funkció, valamint a felhasználói fiókok kezeléséhez szükséges frontend elemek nem reagálnak megfelelően. Hiányoznak az alapvető interaktív elemek, és a felhasználók nem tudják elérni a kívánt funkciókat.

#### Backend

- Jelenlegi helyzet: A szerveroldali logika jelenleg nem képes kezelni a termékek hozzáadását, eltávolítását vagy a felhasználói értesítéseket.

## 2. Vágyálom rendszer

A vágyalom rendszer célja, hogy javítsa a vásárlói élményt azáltal, hogy lehetőséget biztosít a felhasználók számára, hogy kedvenc termékeiket egyszerűen nyomon követhessék és később megvásárolhassák. Ez a funkció elősegíti a vásárlói hűséget és a visszatérő látogatásokat.

### Rendszer Felépítése

Felhasználói Fiók Integráció: - A funkciók csak bejelentkezett felhasználók számára érhető el, amely biztosítja a termékek mentését és a személyre szabott élményt. - A felhasználóknak lehetőségük van a fiókjukba való bejelentkezés után termékeket hozzáadni és vásárolni.
Termékek Hozzáadása: - A felhasználók a termékoldalon található "Hozzáadás" gombra kattintva egyszerűen hozzáadhatják a kiválasztott termékeket a listájukhoz. - A termékek képe, neve, ára és egyéb fontos információk megjelennek a listán.
Kosár: - A Kosár könnyen elérhető a felhasználói fiókból, ahol a felhasználók megtekinthetik a hozzáadott termékeket. - A lista tartalmazhat funkciókat, mint például a termékek eltávolítása, a mennyiség módosítása vagy a vásárlás megkezdése.
Értesítések: - A rendszer értesítéseket küld a felhasználóknak, ha a kívánt termékek ára csökken, vagy ha az adott termék készleten van. - E-mail értesítések is elérhetők a felhasználók számára, hogy emlékeztessék őket a kívánt termékeikről.

### Technikai Megvalósítás

Adatbázis: - A vágyalom adatai (termék ID, felhasználó ID, időbélyeg) egy külön táblában tárolódnak az adatbázisban, biztosítva a gyors keresést és az egyszerű kezelést.
Frontend: - A vágyalom funkciót HTML, CSS és JavaScript segítségével valósítjuk meg, lehetővé téve a felhasználók számára, hogy könnyedén navigáljanak és interakcióba lépjenek a rendszerrel.
Backend: - A vágyalom kezeléséhez szükséges logika a szerveroldalon fut, amely biztosítja a termékek hozzáadását, eltávolítását és a felhasználói értesítések kezelését.

## 3. Jelenlegi üzleti folyamatok modellje

## 4. Igényelt üzleti folyamatok modellje

## 5. Követelménylista

| Kép | Áruház neve | Termék neve | Leírás | Ár | db |

Felhasználói Fiók:

- Regisztrációs és bejelentkezési funkciók (e-mail, jelszó)
- Jelszó visszaállítás lehetősége
- Felhasználói profil kezelés (személyes adatok, rendelési előzmények)
  Termékkezelés

Termékek listázása és kategorizálása:

- Részletes termékleírások, képek, árak
- Termékek keresése és szűrése
- Termékek hozzáadása a vágyalomhoz
- Kosár és Vásárlás

Kosár funkció:

- Termékek hozzáadása, eltávolítás, mennyiség módosítás
- Vásárlási folyamat (kosár áttekintése, szállítási és fizetési adatok megadása)
- Fizetési Módok

Többféle online fizetési lehetőség:

- bankkártya, PayPal, banki átutalás
- Biztonságos tranzakciók garantálása

Szállítási lehetőségek és költségek megjelenítése:

- Várható érkezés

E-mail értesítések:

- rendelés megerősítése, szállítási értesítések
- Árváltozásokról és akciókról szóló értesítések

## 6. Használati esetek

## 7. Megfeleltetés, hogyan fedik le a használati eseteket a követelményeket

| ID  | Leírás |
| --- | ------ |

## 8. Képernyőtervek

### Korai látványterv

![korai_látványterv](../Img/memulatoralphfa.jpg)

## 9. Forgatókönyvek

## 10. Funkció - követelmény megfeleltetése

| Id  | Követelmény | Funkció |
| :-: | ----------- | ------- |

## 11. Fogalomszótár
