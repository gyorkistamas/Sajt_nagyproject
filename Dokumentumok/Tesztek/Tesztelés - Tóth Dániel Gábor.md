### Bejelentkezés / regisztráció tesztelése

**Tesztelő:** Tóth Dániel Gábor

**Tesztelés dátuma:** 2022.12.08


| Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| TDG_001 | Bejelentkezés esetén hiányos mezők. | Az oldal hibás közli hogy a megadott adatok hibásak. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |
| TDG_002 | Bejelentkezés esetén rossz felhasználónév. | Az oldal hibás közli hogy a megadott felhasználó nem található. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |
| TDG_003 | Bejelentkezés esetén rossz jelszó. | Az oldal hibás közli hogy a megadott jelszó nem egyezik. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |
| TDG_004 | Regisztráció esetén már létező felhasználónév. | Az oldal hibás közli hogy a megadott felhasználó már létezik. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |
| TDG_005 | Regisztráció esetén már létező email. | Az oldal hibás közli hogy a megadott email cím már létezik. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |
| TDG_006 | Regisztráció esetén már hibás jelszó ellenőrzés. | Az oldal hibás közli hogy a megadott jelszavak nem egyeznek. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |
| TDG_007 | Regisztráció esetén már létező google fiók. | Az oldal bejelentkeztet a létező felhasználóba, annak módosítása nélkül. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |
| TDG_008 | Regisztráció mgé nem létező google fiók. | Az oldal bejelentkeztet a létező felhasználóba, létrehozza a szükséges háttér adatokat és elküldi a szükséges cookie-kat. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |
| TDG_009 | Bejelentkezés google felhasználóval. | Az oldal megfelelőnen bejelentkeztet az oldalra, viszont néha callback hibát dob. | Megegyzik a várt eredménnyel, a hibát feltételezem hogy a google szerverei miatt van. | Nem találtam hibát, a feltüntetten kívül. |
| TDG_010 | Bejelentkezés helyes adatokkal. | Az oldal bejelentkeztet és betölti a szükséges cookie-kat. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |

### Áru megjelenítés tesztelése

**Tesztelő:** Tóth Dániel Gábor

**Tesztelés dátuma:** 2022.12.09


| Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| TDG_001 | Termék hozzáadása oldalra navigálás bejelentkezés nélkül. | Az oldal visszairányít a bejelentkezésre. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |
| TDG_002 | Kosár fül megnyitása bejelentkezés nélkül. | Az oldal visszairányít a bejelentkezésre. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |
| TDG_003 | Termék hozzáadása oldalra navigálás bejelentkezés nélkül. | Az oldal visszairányít a bejelentkezésre. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |

### Admin panel tesztelése

**Tesztelő:** Tóth Dániel Gábor

**Tesztelés dátuma:** 2022.12.09


| Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| TDG_001 | Felhasználó szintjének módosítása | Az oldal módosítja a kiválasztott felhasználó elérési szintjét ha az nem a sajátja. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |
| TDG_002 | Admin panel megnyitása a megfelelő jogosultság nélkül. | Az oldal visszairányít az indexre. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |
| TDG_003 | Felhasználó neveinek módosítása. | Az oldal módosítja a kiválasztott felhasználó adatait ha az nem a sajátja. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |
| TDG_004 | Felhasználó email címének módosítása. | Az oldal módosítja a kiválasztott felhasználó email címét ha az nem a sajátja. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |
| TDG_005 | Felhasználó törlése. | Az oldal törli a kiválasztott felhasználót. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |