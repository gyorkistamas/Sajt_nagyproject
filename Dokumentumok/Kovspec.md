# 1.Áttekintés
<h3>Funkcionális elemek:</h3>
A rendszer alapvető funkciói a következők:

Felhasználói regisztráció és bejelentkezés: A felhasználók saját fiókot hozhatnak létre, amelyhez egyedi azonosítóval, e-mail címmel és jelszóval férhetnek hozzá.

Termékek böngészése és szűrése: A felhasználók kategóriák alapján kereshetnek termékeket, valamint szűrhetnek ár, elérhetőség, és egyéb paraméterek alapján.

Kosár és rendeléskezelés: A felhasználók termékeket helyezhetnek a kosárba, majd leadhatják rendeléseiket különböző fizetési módokkal.

Adminisztrátori funkciók: Az adminisztrátorok kezelhetik a termékeket, kategóriákat, felhasználókat, és megtekinthetik a leadott rendeléseket.


<h3>Nem funkcionális követelmények:</h3>
A rendszernek biztosítania kell a következőket:

Biztonság: Az adatbiztonság kiemelten fontos a felhasználói adatok, fizetési adatok, és a termékek biztonságos kezelése szempontjából. A jelszavakat biztonságos titkosítással kell tárolni.

Teljesítmény: A webshopnak képesnek kell lennie nagy mennyiségű termékek gyors kezelésére, és folyamatosan biztosítani kell a gyors oldalbetöltést.

Karbantarthatóság: A rendszernek modulárisnak és könnyen bővíthetőnek kell lennie, hogy az új funkciók és frissítések egyszerűen hozzáadhatók legyenek.


<h3>Adatbázis követelmények:</h3>
Az adatbázis a webshop különböző funkcióit kiszolgáló táblákat fog tartalmazni. A főbb táblák a következők:

Felhasználók táblája: Tárolja a regisztrált felhasználók adatait (azonosító, név, e-mail cím, jelszó).

Termékek táblája: Minden terméket azonosít, amely tartalmazza a termék nevét, árát, leírását, készlet információit és kategóriáját.

Rendelések táblája: Tárolja a felhasználók által leadott rendeléseket, beleértve a termékeket, az összeget, a fizetési módot és a rendelés állapotát.

Kategóriák táblája: A termékek kategorizálására szolgáló tábla, amely lehetővé teszi a termékek böngészését különböző csoportok alapján.
# 2.Jelenlegi helyzet

A jelenlegi webshop rendszer egyszerű online termékértékesítési platformként működik, azonban számos olyan funkció és struktúra hiányzik belőle, amely a felhasználói élmény javításához, az adminisztráció hatékonyságának növeléséhez, valamint a biztonságos és skálázható adatkezeléshez szükséges.
<h3>Felhasználói fiók kezelés</h3>
<ul>
<li>Jelenleg a felhasználók fiók nélkül is böngészhetiok a termékeket, azonban a vásárláshoz regisztrációra van szükség. A regisztrációs folyamat alapvető információkat kér, de nincs lehetőség például jelszó-visszaállitásra vagy többféle belépési lehetőségre (pl. közösségi média fiókkal való belépés).</li>
<li>A felhasználói adatok biztonsága nem megfelelő, mivel a jelszavak nem titkosítottak, és nincs kétfaktoros hitelesítési (2FA) lehetőség.</li>
</ul>
<h3>Termékkatalógus és keresési funkciók</h3>
<ul>
<li>A termékkatalógus egyszerű felépétísű, azonban a termékek kategorizálása és szűrése korlátozott. Jelenleg nincs több lehetőség több kritérium szerinti szűrésre (pl. ár, értékelések, készlet elérhetőség).</li>
<li>Az adminisztrátorok számára nincs megfelelő felület a termékek egyszerű kezelésére (pl. termékek tömeges importálása/exportálása), és az új termékek hozzáadása manuálisan történik.</li>
</ul>
<h3>Kosár és rendelési folyamat</h3>
<ul>
<li>A kosár funkció alapszinten működik, de nincs támogatva az elhagyott kosarak visszakeresése vagy a visszatérő vásárlók automatikus kosárba helyezése.</li>
<li>A rendelési folyamat csak korlátozott fizetési lehetőségeket támogat (pl. kizárólag banki átutalás), és nincs integrált fizetési megoldás, mint például bankkártyás fizetés vagy PayPal.</li>
</ul>

<h3>Adminisztrációs felület</h3>
<ul>
<li>Az adminisztrációs felület jelenleg nem teszi lehetővé a részletes riportok készítését a rendelések állapotáról, a forgalom elemzásáről, vagy a legkeresettebb termékekről.</li>
<li>Hiányzik egy fejlett felhasználókezelő rendszer, amely lehetővé tenné az adminisztrátorok számára, hogy különböző jogosoltsági szinteket állítsanak be.</li>
</ul>

<h3>Adatbázis struktúra</h3>
A webshop adatbázisának jelenlegi felépítése nem skálázható, és nem optimalizált a rendszer növekvő igényeihez. Az adatbázis struktúrájának jelenlegi jellemzői a következők:
<br>
<ul>
<li>Felhasználók tábla: Alapvető adatokat tartalmaz (név,email,jelszó), de nincsenek bővített profil inormációk (pl. több szállítási cím, rendelési előzmények).</li>
<li>Termékek tábla: A termékek tábla egyszerű információkat tárol (terméknév,ár, leírás), de hiányzik a készlet kezelése, valamint az értékelések és vélemények tárolása.</li>
<li>Rendelések tábla: Tárolja az egyes rendelések alapadatait, de nincs nyomon követési funkció, amely megmutatná a rendelés aktuális állapotát (pl. feldolgozás alatt, szállítás alatt, lezárva).</li>
<li>Kategóriák tábla: A termékek kategorizálására szolgáló rendszer alapvető szintű, azonban nincs lehetőség több szintű kategorizálásra vagy attribútum alapú szűrésre.</li>
</ul>

# 3.Vágyálom rendszer

# 4.Jelenlegi üzleti folyamatok modellje


# 5.Igényelt üzleti folyamatok modellje

# 6.Követelménylista

# 7.Fogalomtár