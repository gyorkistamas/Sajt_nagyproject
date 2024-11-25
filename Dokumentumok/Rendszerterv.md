# 1. A Rendszer Célja
Egy olyan webes platform mely a különböző sajt fajták vásárlásának biztosít egy tökéletes alapot. Az oldalon számos különböző kategóriából válogathatnak a vásárlók, ezentúl különböző hivatásos sajtmesterek is hirdethetik a termékeiket

# 2. Projekt Terv
A weboldalon a felállított jogosultság rendszer és választékos menük szabályozzák a megjelenített tartalmat.
Jogosultságaink szerteágazóak, ebből kifolyólag pedig sok lehetőségünk van szabályozni az oldal felhasználóit. Ezen jogosultságok a következőek:
Adminisztrátor, Moderátor, Segítő, Megbízott eladó, Sajtmester, Eladó, Felhasználó, Tesztelő, Látogató
Ezen jogkörök bővebb leírása az 5.1-es pontban található a Rendszerszereplőknél. Terveink közé tartozik továbbá, hogy az oldal a reszponzivitást támogassa, ezáltal akár okostelefonon és tableten is használható legyen. Az oldalon közel azonnali segítséget kap a felhasználó az ügyintézőktől segítőktől, ha bármilyen kérdése akadna, akár a termékekkel akár a profiljával kapcsolatban. Illetve a profilját teljességgel modifikálni tudja, a megvásárolt termékek alatt megjegyzést hagyni, vagy azt egy 1-5 ig terjedő skálán értékelni. Az oldal tartalmaz egy blog felületet is, ahol a sajt fanatikusok böngészhetnek az oldal témájához kapcsolódó tartalmakat, vagy éppen az oldalon végzett újításokat olvashatják.

## 2.1 Projektszerepkörök, felelősségek
* Scrum master:
    -
* Product owner:
    - Sajt Non-profit
* Üzleti szereplő:
    - Megrendelő:
        - Györkis Tamás

## 2.2 Projektmunkások és felelősségek

* Frontend:
    - Kiszely Dávid
    - Kiss Péter
* Backend:
    - Tóth Dániel Gábor
* Tesztelés
    - Kiszely Dávid
    - Kiss Péter
    - Tóth Dániel Gábor

## 2.3 Ütemterv
W.I.P

## 2.4 Mérföldkövek
* 10.07. - Rendszerterv elkészítése
* 10.14. - Követelmény specifikáció elkészítése
* 10.21. - Funkcionális specifikáció elkészítése
* 11.08. - Front-end elkészítése
* 12.xx. - Előzetes tesztelések elkészítése
* 12.xx. - Back-end elkészítése
* 12.xx. - Prototípus elkészítése
* 12.09. - Prototípus prezentálása

# 3. Üzleti folyamatok modellje

## 3.1 Üzleti szereplők
W.I.P
   
## 3.2 Üzleti folyamatok
W.I.P

# 4. Követelmények

## Követelménytáblázat

 | Kép | Áruház neve | Termék neve | Leírás | Ár | db |
 | :---: | --- | --- | --- |

## Funkcionális
| ID | Név | Leírás |
| 

## Nem Funkcionális

# 5. Funkcionális terv
    
## 5.1 Rendszerszereplők

|Megnevezés					|Leírás						| 
|---------------------------|---------------------------|
|Adminisztrátor 			|Az oldalt felügyelik, fejlesztők                    |  
|Moderátor					|A webshop tisztaságát ellenőrzik, és moderálják a posztokat, ha valamilyen szabály elleneset találnak                    |
|Segítő          			|Az oldal működését segítő szereplők, valós időben válaszoló segítők (support)                    | 
|Megbízott eladó          	|Olyan eladók akik a megadott számú eladáson túl vannak, így megbízottnak tekintehetőek.  Esetlegesen a moderátorok munkájába segíthetnek, jelezhetnek nekik|
|Sajtmester      			|Az oldal sajtmester szekciójába posztolók kapják ezt a rangot, ha hivatalos sajtmesterek, ellenőrzés után kapható csak | 
|Eladó                  	|Olyan felhasználók akik a megadott számú eladáson még nincsenek túl. Felhasználó jogusultság illeti|
|Felhasználó              	|Általános felhasználó, regisztrálás után ebbe a jogusultságba kerül     |
|Tesztelő                  	|Speciális felhasználó. Az alap jogokon kívül tesztelői funkciókhoz fér hozzá   |
|Látogató                  	|Olyan felhasználó aki még nem rendelkezik profillal |
   
## 5.2 Menü-hierarchia:
### Sajtfanatikus Webshop Menü

#### Főoldal
Az otthona minden sajtkedvelőnek! Nézd meg legújabb sajtjainkat és ajánlatainkat.

#### Termékek
##### Kategóriák
- **Kézműves sajtok**
  - Érlelt sajtok
  - Friss sajtok
  - Krémsajtok
- **Fűszerezett sajtok**
  - Borsos
  - Fokhagymás
  - Fűszeres specialitások
- **Exkluzív sajtok**
  - Limitált kiadású sajtok
  - Különleges érlelési technikák
  - Sajtmesterek ajánlatai
- **Sajtkiegészítők**
  - Sajtgyalu
  - Sajttartók
  - Vágódeszkák
  - Kések

#### Újdonságok
Fedezd fel legújabb kézműves sajtjainkat, amelyeket csak nálunk találsz meg.

#### Akciók
Exkluzív kedvezmények hűséges sajtkedvelőknek:
- **Heti ajánlat**: Friss sajtok 20% kedvezménnyel!
- **Szezonális akció**: Téli érlelt sajtok kiárusítása.

#### Sajtbár (Blog)
Legújabb írásaink a sajt világából:
- **Sajtfajták és borpárosítások**
- **Interjúk sajtmesterekkel**
- **Sajt tárolás és érlelés otthon**

#### Vásárlói fiók
- **Profilom**
- **Megrendeléseim**
- **Kedvenc sajtjaim**
- **Kosár**
- **Kijelentkezés**

#### Kapcsolat
- **Ügyfélszolgálat**: Kérdéseidre válaszolunk!
- **GYIK**: Gyakran ismételt kérdések.
- **Rólunk**: Ismerd meg csapatunkat és filozófiánkat.

#### Lábléc
##### Információk
- **Szállítási feltételek**: Hogyan juttatjuk el hozzád sajtjainkat.
- **Fizetési módok**: Bankkártyás fizetés, utánvét, PayPal.

##### Jogi információk
- **Adatvédelmi szabályzat**
- **Általános szerződési feltételek**

##### Közösségi média
- **Facebook**: Kövess minket, és ne maradj le az újdonságokról!
- **Instagram**: Inspiráció és exkluzív sajt fotók.
- **YouTube**: Videók sajtkészítésről és -fogyasztásról.

# 6. Fizikai környezet

## Vásárolt szoftverkomponensek, valamint esetleges külső rendszerek
* Keretrendszer:
  - Django : 5.1.1

## Hardver topológia
 nincs

## Fizikai alrendszerek
 - Futtatható : Windows, Linux (olyan OP-ek amelyeken futtathó a python 3.10[+] verziója)
  - Futtatáshoz szükséges komponens(ek) : Django (5.1.1), Python(3.12.6)
  - Futtatáshoz szükséges erőforrások : >2GB RAM, virtualizációra alkalmas processzor

## Fejlesztő eszközök
 - Programozási nyelvek: JS, Python
 - Leíró nyelvek: Html, CSS
 - Adatbázis: SQLite
 - Fejlesztő környezet: Visual Studio Code
 - Tesztkörnyezet: Böngészők fejlesztői konzola

    
# 7. Architekturális terv

# 8. Adatbázis terv

## Felhasználói táblák 
| AUTH_USER |
|------------|------------|------------|
| id            | **INT**           | A felhasználó indexelése                        |
| password      | **varchar(128)**  | A felhasználó sha256-os kódolásba mentett jelszava |
| last_login    | **datetime**      | A felhasználó utolsó bejelentkezésének ideje    |
| is_superuser  | **bool**          | A felhasználó admin jogusultsága                |
| username      | **varchar(150)**  | A felhasználó felhasználóneve                   |
| email         | **varchar(254)**  | A felhasználó email címe                        |
| is_staff      | **bool**          | A felhasználó moderátori jogusultsága           |
| is_active     | **bool**          | A felhasználó fiókjának elérhetősége            |
| date_joined   | **datetime**      | A felhasználó fiókjának létrehozásának időpontja|

| AUTH_GROUP |
|------------|------------|------------|
| id            | **INT**           | A csoport indexe                                |
| name          | **varchar(150)**  | A csoport neve                                  |

| AUTH_USER_GROUPS |
|------------|------------|------------|
| id            | **INT**           | A felhasználó felhasználói csoportja            |
| group_id      | **INT**           | A csoport indexe                                |
| user_id       | **INT**           | A felhasználó indexe                            |

| AUTH_PERMISSION |
|------------|------------|------------|
| id            | **INT**           | A jog indexe                                    |
| content_type_id | **INT**         | A hozzáférés típusának indexe                   |
| name          | **varchar(255)**  | A hozzáférés megnevezése                        |

| AUTH_GROUP_PERMISSION |
|------------|------------|------------|
| id            | **INT**           | A hozzáférési csoport rekord indexe             |
| group_id      | **INT**           | A hozzáféréshez hozzárendelt csoport indexe     |
| permission_id | **INT**           | A hozzáférés szintjének az indexe               |

| DJANGO_SESSION |
|------------|------------|------------|
| session_key   | **varchar(40)**   | A felhasználó session kulcsa                    |
| session_data  | **text**          | A felhasználó adata                             |
| expire_date   | **datetime**      | A kulcs lejárásának időpontja                   |

## Termékek és fizetés

| **SAJTNAGY_CART** |
|------------|------------|------------|
| id            | **INT**           | A kosár indexe                                  |
| quantity      | **INT**           | Az adott termék darabszáma                      |
| created_at    | **datetime**      | A kosárhoz adás időpontja                       |
| updated_at    | **datetime**      | A frissítés időpontja                           |
| user_id       | **INT**           | A felhasználó indexe                            |
| product_id    | **INT**           | A hozzáadott termék indexe                      |

| **SAJTNAGY_PRODUCT** |
|------------|------------|------------|
| id            | **INT**           | A termék azonosítója                            |
| name          | **varchar(255)**  | A termék neve                                   |
| description   | **text**          | A termék leírása                                |
| price         | **INT**           | A termék ára                                    |
| stock         | **INT**           | A termék rendelkezésre álló darabszáma          |
| created_at    | **datetime**      | A termék létrehozásának időpontja               |
| updated_at    | **datetime**      | A termék frissítésének időpontja                |
| category_id   | **INT**           | A termék kategóriájának az azonosítója          |

| **SAJTNAGY_CATEGORY** |
|------------|------------|------------|
| id            | **INT**           | A kategória azonosítója                         |
| name          | **varchar(255)**  | A kategória neve                                |
| description   | **text**          | A kategória leírása                             |

| **SAJTNAGY_ORDER** |
|------------|------------|------------|
| id            | **INT**           | A rendelés azonosítója                          |
| total_price   | **INT**           | A rendelés összege                              |
| status        | **INT**           | A rendelés státusza                             |
| created_at    | **datetime**      | A rendelés létrehozásának időpontja             |
| updated_at    | **datetime**      | A rendelés módosításának időpontja              |
| user_id       | **INT**           | A rendelés létrehozójának az indexe             |
| address       | **varchar(255)**  | A rendelés létrehozójának címe                  |
| city          | **varchar(255)**  | A rendelés létrehozójának városa                |
| first_name    | **varchar(255)**  | A rendelés létrehozójának vezetékneve           |
| last_name     | **varchar(255)**  | A rendelés létrehozójának keresztneve           |
| payment_method | **INT**          | A fizetés típusa                                |
| state         | **varchar(100)**  | A rendelő megyéje                               |
| zipcode       | **varchar(10)**   | A rendelő irányítószáma                         |

| **SAJTNAGY_ORDERITEM** |
|------------|------------|------------|
| id            | **INT**           | A rendelésben szereplő termék rendelésének azonosítója |
| quantity      | **INT**           | A rendelésben szereplő termék rendelt mennyisége       |
| price         | **INT**           | A rendelésben szereplő termék ára                      |
| created_at    | **datetime**      | A rendelésben szereplő termék rendelésének dátuma      |
| updated_at    | **datetime**      | A rendelésben szereplő termék rendelésének frissítésének időpontja |
| order_id      | **INT**           | A rendelés azonosítója                                 |
| product_id    | **INT**           | A rendelt termék azonosítója                           |

| **SAJTNAGY_PAYMENT** |
|------------|------------|------------|
| id            | **INT**           | A rendelés fizetésének indexe                        |
| payment_method | **INT**          | A fizetés típusa                                     |
| payment_status | **INT**          | A fizetés státusza                                   |
| payment_date  | **datetime**      | A fizetés időpontja                                  |
| order_id      | **INT**           | A rendelés azonosítója                               |

| **SAJTNAGY_REVIEW** |
|------------|------------|------------|
| id            | **INT**           | A vélemény azonosítója                               |
| rating        | **INT**           | A termék értékelése                                  |
| comment       | **text**          | A vélemény tartalma                                  |
| created_at    | **datetime**      | A vélemény közlésének időpontja                      |
| product_id    | **INT**           | Az értékelt termék azonosítója                       |
| user_id       | **INT**           | A vélemény létrehozójának azonosítója                |

| **SAJTNAGY_PROMO** |
|------------|------------|------------|
| id                | **INT**           | A promóciós kód azonosítója                        |
| promo_code_sha256 | **varchar(64)**    | A promóciós kód sha256-os hash kódja               |
| expiry_date       | **datetime**       | A promóciós kód lejárásának időpontja              |
| discount          | **DECIMAL**        | A promócióval járó árlevonás mennyisége            |
| user_id           | **INT**            | Ha a promóciós kód csak egy felhasználónak érvényes, akkor neki az azonosítója |

# 9. Implementációs terv
 
    
# 10. Tesztterv


# 11. Telepítési terv
- Webszerver
  - Python 3.12.6
  - Django 5.1.1
    
# 12. Karbantartási terv
 - Termékek hozzáadása / frissítése
 - Piaci ár követése