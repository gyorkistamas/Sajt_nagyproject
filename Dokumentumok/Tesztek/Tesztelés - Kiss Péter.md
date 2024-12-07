### Bejelentkezés tesztelése

**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.05


| Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| LOGIN_001 | Login oldal betöltése | Az oldal helyesen betöltődik, a design és a mezők megjelennek. | Megegyzik a várt eredménnyel. | Az oldal minden elem helyesen látható. |
| LOGIN_002 | Hibás felhasználónév és jelszó megadása | A "Helytelen felhasználónév vagy jelszó" hibaüzenet jelenik meg. | Megegyezik a várt eredménnyel. | A hibaüzenet megfelelően megjelenik. |



### Vásárlói visszajelzés funkció tesztelése
**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.04.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| FB_001 | A visszajelzés beküldése mezők kitöltése nélkül. | A rendszer figyelmeztetést ad, hogy minden mezőt ki kell tölteni. | A rendszer nem ellenőrizte a mezők kitöltését. | Hiányzik az űrlap validálása.|
| FB_002 | Értékelés és visszajelzés kitöltése után a „Küldés” gombra kattintás. | Az értékelés és a visszajelzés elmentésre kerül, sikerüzenet jelenik meg. | Megegyezik a várt eredménnyel. | Sikerült a visszajelzés beküldése. |


### Profil tesztelés
**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.04.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| PRF_001 | Felhasználói fiók adatainak megjelenítése. | A felhasználó adatai (felhasználónév, email, telefonszám, cím) helyesen jelennek meg. | Megegyezik a várt eredménnyel. | Az összes adat helyesen jelenik meg.|


### Kedvencek tesztelés
**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.04.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| KEDV_001 | Kedvencek oldal betöltése | A "Kedvenc Sajtok" cím jelenik meg a böngésző fülén. | Megegyezik a várt eredménnyel. | Az oldal betöltődött, a cím megfelelően megjelenik.|

### Fizetés tesztelés
**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.05.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| PAY_001 | Fizetési oldalra navigálás bejelentkezés nélkül. | Az oldal visszairányít a bejelentkezésre. | Megegyezik a várt eredménnyel. | Nem találtam hibát.|

### Elfelejtett Jelszó  tesztelés
**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.05.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| TC_001 | Üres mezők kitöltése nélkül a "Küldés" gombra kattintás. | Hibaüzenet: "Minden mezőt ki kell tölteni." | Megegyezik a várt eredménnyel. | Nem találtam hibát.|


### Rendelések  tesztelés
**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.06.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| ORD_001 | Egy termék részleteinek megtekintése. | A "Részletek" gombra kattintás a megfelelő termék részletes oldalára navigál. | Megegyezik a várt eredménnyel. | Nem találtam hibát.|
| ORD_002 | Több termék képeinek helyes megjelenítése. | Az összes kép megfelelően jelenik meg a megadott méretben és elrendezésben. | Megegyezik a várt eredménnyel. | Nem találtam hibát.|


### Regisztráció tesztelés
**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.07.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| REG_001 | Üres felhasználónév mező | Hibaüzenet: "Felhasználónév megadása kötelező." | Megegyezik a várt eredménnyel. | Nem találtam hibát.|
| REG_002 | Helytelen email-formátum (email: "rosszformátum") | Hibaüzenet: "Az email cím érvénytelen." | Megegyezik a várt eredménnyel. | Nem találtam hibát.|


### Navbar tesztelés
**Tesztelő:** Kiss Péter

**Tesztelés dátuma:** 2024.12.07.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| NAV_001 | Navigációs menü megjelenítése bejelentkezett felhasználóval | Minden menüpont elérhető (Főoldal, Áruk, Kosár, Rendeléseim, Rólunk, Kapcsolat, Fiókom) | Megegyezik a várt eredménnyel. | Nem találtam hibát.|
| NAV_002 | Navigációs menü megjelenítése be nem jelentkezett felhasználóval | Minden menüpont elérhető (Főoldal, Áruk, Rólunk, Kapcsolat, Bejelentkezés, Regisztráció) | Megegyezik a várt eredménnyel. | Nem találtam hibát.|

