### Bejelentkezés / regisztráció tesztelése

**Tesztelő:** Teszt Elek

**Tesztelés dátuma:** 2022.10.09


| Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| ASD_001 | Regisztráció esetén mezők hiányos kitöltése. | Az oldal figyelmeztet a hiányosságokra. | Megegyzik a várt eredménnyel. | Nem találtam hibát. |

&nbsp;

### Termék hozzáadása tesztelése

**Tesztelő:** Teszt Elek

**Tesztelés dátuma:** 2022.10.09


| Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| ASD_010 | Termék hozzáadása oldalra navigálás bejelentkezés nélkül. | Az oldal visszairányít a bejelentkezésre. | Megegyezik az elvárt eredménnyel. | Nem találtam hibát. |


### Vásárlói visszajelzés funkció tesztelése
**Tesztelő:** Kiss Péter
**Tesztelés dátuma:** 2024.12.04.
 | Teszt szám | Teszt eset | Várt eredmény | Tényleges Eredmény | Megjegyzés |
|------------|------------|---------------|--------------------|------------|
| FB_001 | A visszajelzés beküldése mezők kitöltése nélkül. | A rendszer figyelmeztetést ad, hogy minden mezőt ki kell tölteni. | A rendszer nem ellenőrizte a mezők kitöltését. | Hiányzik az űrlap validálása.|
| FB_002 | Értékelés és visszajelzés kitöltése után a „Küldés” gombra kattintás. | Az értékelés és a visszajelzés elmentésre kerül, sikerüzenet jelenik meg. | Megegyezik a várt eredménnyel. | Sikerült a visszajelzés beküldése. |