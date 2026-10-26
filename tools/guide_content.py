# Útmutató tartalma (magyar + angol). A tools/build-guide.py ebből készít PDF-et és Markdownt.
REPO = "https://github.com/zoltan-234/coospace5-egyedi-temak-szte"
REL = REPO + "/releases/latest"

# Képernyőképek: id -> (magyar felirat, angol felirat, mit kell lefotózni [magyarul])
SHOTS = {
 "GH-01": ("A GitHub Releases oldal: itt tölthető le a két fájl", "The GitHub Releases page: the two downloadable files",
           "A repó Releases oldala (…/releases/latest), a lenti 'Assets' lista látszódjon: a .xpi és a -chromium.zip fájl. Jelöld be (pl. piros keret) a két fájlt."),
 "GH-02": ("A kicsomagolt mappa: közvetlenül benne van a manifest.json", "The extracted folder: manifest.json is directly inside",
           "A Fájlkezelőben a kicsomagolt mappa tartalma, jól látható a manifest.json fájl és a content, popup, themes mappák. A címsorban látszódjon a mappa neve."),
 "FF-01": ("Firefox: a telepítés megerősítése (Hozzáadás gomb)", "Firefox: confirming the installation (Add button)",
           "A Firefoxban a letöltött .xpi megnyitása után felugró ablak 'Hozzáadja a(z) Unics Themes kiegészítőt?' – a Hozzáadás gombbal együtt."),
 "FF-02": ("Firefox: a bővítmény a kiegészítők listájában", "Firefox: the add-on in the add-ons list",
           "about:addons oldal, a Bővítmények között az Unics Themes látszódjon, bekapcsolt állapotban."),
 "FF-03": ("Firefox: az Engedélyezés gomb a popupban", "Firefox: the Allow button in the popup",
           "Az Unics oldalon (unics.szte.hu) a bővítmény ikonjára kattintva megnyíló popup, a sárga 'Engedélyezés' dobozzal együtt (még az engedélyezés ELŐTT)."),
 "FF-04": ("Firefox: a bővítmény kitűzése az eszköztárra", "Firefox: pinning the add-on to the toolbar",
           "A Firefox eszköztárán a puzzle (Bővítmények) menü megnyitva, az Unics Themes mellett a 'Kitűzés az eszköztárra' lehetőség látszódjon."),
 "FF-05": ("Firefox: az Unics oldal egy kiválasztott témával", "Firefox: the Unics site with a theme applied",
           "Az Unics főoldala (Áttekintés) egy látványos témával és stílussal – szebb legyen, mint az eredeti."),
 "FF-06": ("Firefox: a bővítmény eltávolítása", "Firefox: removing the add-on",
           "about:addons, az Unics Themes melletti három pontos (…) menü megnyitva, az 'Eltávolítás' sor látszódjon."),
 "CH-01": ("Chrome: a bővítménykezelő, bekapcsolt fejlesztői móddal", "Chrome: the extensions page with Developer mode on",
           "chrome://extensions oldal, jobb felül a 'Fejlesztői mód' kapcsoló BEkapcsolva, jelöld be."),
 "CH-02": ("Chrome: a „Kicsomagolt bővítmény betöltése” gomb", "Chrome: the “Load unpacked” button",
           "Ugyanez az oldal a fejlesztői mód bekapcsolása után: bal felül a 'Kicsomagolt bővítmény betöltése' gomb, jelöld be."),
 "CH-03": ("Chrome: a mappa kiválasztása", "Chrome: choosing the folder",
           "A mappaválasztó ablak, kijelölve a kicsomagolt mappa (amiben a manifest.json van)."),
 "CH-04": ("Chrome: a betöltött bővítmény kártyája", "Chrome: the loaded extension card",
           "A bővítménykezelőben az Unics Themes kártya, hibajelzés (piros) nélkül."),
 "CH-05": ("Chrome: kitűzés az eszköztárra", "Chrome: pinning to the toolbar",
           "A puzzle ikon menüje megnyitva, az Unics Themes mellett a kitűző (tűzőcsap) ikon, jelöld be."),
 "CH-06": ("Chrome: a bővítmény eltávolítása", "Chrome: removing the extension",
           "chrome://extensions, az Unics Themes kártyán az 'Eltávolítás' gomb, jelöld be."),
 "ED-01": ("Edge: a bővítménykezelő, bekapcsolt fejlesztői móddal", "Edge: the extensions page with Developer mode on",
           "edge://extensions oldal; a bal oldali menüben a 'Fejlesztői mód' kapcsoló BEkapcsolva, jelöld be."),
 "ED-02": ("Edge: a „Kicsomagolt betöltése” gomb", "Edge: the “Load unpacked” button",
           "Ugyanez az oldal fejlesztői móddal: a 'Kicsomagolt betöltése' gomb, jelöld be."),
 "ED-03": ("Edge: a mappa kiválasztása", "Edge: choosing the folder",
           "A mappaválasztó ablak, kijelölve a kicsomagolt mappa."),
 "ED-04": ("Edge: a betöltött bővítmény kártyája", "Edge: the loaded extension card",
           "Az Unics Themes kártya az edge://extensions oldalon, hibajelzés nélkül."),
 "ED-05": ("Edge: kitűzés az eszköztárra", "Edge: pinning to the toolbar",
           "A Bővítmények (puzzle) menü megnyitva, az Unics Themes mellett a szem/kitűző ikon, jelöld be."),
 "ED-06": ("Edge: a bővítmény eltávolítása", "Edge: removing the extension",
           "edge://extensions, az Unics Themes kártyán az 'Eltávolítás' gomb."),
 "BR-01": ("Brave: a bővítménykezelő, bekapcsolt fejlesztői móddal", "Brave: the extensions page with Developer mode on",
           "brave://extensions oldal; a 'Fejlesztői mód' kapcsoló BEkapcsolva, jelöld be."),
 "BR-02": ("Brave: a „Kicsomagolt bővítmény betöltése” gomb", "Brave: the “Load unpacked” button",
           "Ugyanez az oldal fejlesztői móddal: a 'Kicsomagolt bővítmény betöltése' gomb, jelöld be."),
 "BR-03": ("Brave: a mappa kiválasztása", "Brave: choosing the folder",
           "A mappaválasztó ablak, kijelölve a kicsomagolt mappa."),
 "BR-04": ("Brave: a betöltött bővítmény kártyája", "Brave: the loaded extension card",
           "Az Unics Themes kártya a brave://extensions oldalon, hibajelzés nélkül."),
 "BR-05": ("Brave: kitűzés az eszköztárra", "Brave: pinning to the toolbar",
           "A Bővítmények (puzzle) menü megnyitva, az Unics Themes mellett a kitűző ikon, jelöld be."),
 "BR-06": ("Brave: a bővítmény eltávolítása", "Brave: removing the extension",
           "brave://extensions, az Unics Themes kártyán az 'Eltávolítás' gomb."),
 "US-01": ("A popup: színtémák", "The popup: colour themes",
           "A bővítmény popupja nyitva az Unics oldalon, a 'Színek' rész teteje látszódjon (Világos, Többszínű csoportok)."),
 "US-02": ("A popup: stílusok", "The popup: styles",
           "Ugyanaz a popup legörgetve a 'Stílus' részhez: Klasszikus, Modern, Üveg, Szigetek, Brutalista."),
 "US-03": ("Példa: Modern stílus, világos téma", "Example: Modern style, light theme",
           "Az Unics Színterek oldala Modern stílussal és egy világos témával (pl. Világos modern vagy Pasztell). Személyes adat (név) legyen kitakarva, ha kell."),
 "US-04": ("Példa: Üveg stílus, sötét téma", "Example: Glass style, dark theme",
           "Az Unics Áttekintés oldala Üveg stílussal és az Aurora témával."),
 "US-05": ("Példa: Brutalista stílus", "Example: Brutalist style",
           "Az Unics Színterek oldala Brutalista stílussal és pl. a Rózsakert vagy Dracula témával."),
}

def browser(code, name, addr, devmode_hu, devmode_en):
    """Chromium-alapú böngésző fejezete (a három ugyanolyan)."""
    return code, name, addr, devmode_hu, devmode_en

CHAPTERS_HU = [
 ("h1", "mi", "1. Mi ez, és mire jó?"),
 ("p", "Az <b>Unics Themes</b> egy kis böngészőbővítmény az SZTE <b>Unics (CooSpace)</b> felületéhez. Segítségével kiválaszthatod, hogyan nézzen ki az oldal: 18 színtéma (világos, színes, rózsaszín, sötét) és 5 stílus (Klasszikus, Modern, Üveg, Szigetek, Brutalista) közül, és tetszőlegesen kombinálhatod őket."),
 ("list", ["A választásod <b>megmarad</b> frissítés (F5) és a böngésző újraindítása után is.", "Egy kattintással váltasz: a bővítmény ikonjára kattintva megnyílik a választó ablak.", "Ingyenes, és bármikor kikapcsolható vagy eltávolítható."]),
 ("note", "ok", "Nem kell aggódnod: ez csak a kinézetet változtatja", "A bővítmény <b>kizárólag az oldal megjelenését</b> módosítja (színek, formák, animációk). Biztonságos, mert:"),
 ("list", [
   "<b>Csak az unics.szte.hu oldalon fut</b>, más weboldalhoz nem fér hozzá.",
   "<b>Nem küld el semmit sehova</b>: nincs szervere, nincs követés, nincs statisztika. A választott téma csak a saját böngésződben tárolódik.",
   "<b>Nem módosítja az Unics adatait</b>: nem ír, nem küld be semmit, nem érinti a jegyeidet, üzeneteidet vagy beadandóidat. Ha kikapcsolod, minden pontosan olyan, mint előtte.",
   "<b>Nem kér jelszót</b>, és nem fér hozzá a böngésződ jelszavaihoz, előzményeihez vagy más füleihez.",
   "<b>Nyílt a forráskód</b>: a teljes kód megtekinthető a GitHubon, bárki ellenőrizheti.",
   "<b>Nem hivatalos</b> projekt, nem áll kapcsolatban az SZTE-vel vagy az Unics fejlesztőivel."]),
 ("p", "Technikai pontosság kedvéért: a bővítménynek az Unics oldalon futnia kell, hogy átszínezhesse azt. Ezt a böngésző külön engedélyhez köti (lásd a telepítési részt). Az oldal tartalmát nem olvassa ki és nem továbbítja, csak a megjelenést (színeket, méreteket) állítja."),

 ("h1", "melyik", "2. Melyik böngészőt használod?"),
 ("p", "A telepítés böngészőnként kicsit más. Keresd meg a sajátodat a táblázatban, majd ugorj a hozzá tartozó fejezetre."),
 ("table", ["Böngésző", "Telepítés módja", "Marad újraindítás után?", "Automatikus frissítés"], [
   ["<b>Firefox</b>", "Aláírt .xpi fájl, egy kattintás", "Igen", "Igen (naponta)"],
   ["<b>Chrome</b>", "Kicsomagolt mappa betöltése", "Igen, ha a mappa a helyén marad", "Nem, kézzel"],
   ["<b>Edge</b>", "Kicsomagolt mappa betöltése", "Igen, ha a mappa a helyén marad", "Nem, kézzel"],
   ["<b>Brave</b>", "Kicsomagolt mappa betöltése", "Igen, ha a mappa a helyén marad", "Nem, kézzel"]]),
 ("note", "info", "Telefonon és tableten", "Androidos Chrome, Edge és Brave nem támogat bővítményeket, ezért ott nem használható. Az Android-Firefoxon nem teszteltük, nem ajánlott. A bővítmény asztali gépre (Windows, macOS, Linux) készült."),

 ("h1", "letoltes", "3. A fájl letöltése"),
 ("p", "Minden kiadás a GitHub <b>Releases</b> oldalán található: <code>%s</code>" % REL),
 ("steps", [
   ("Nyisd meg a fenti oldalt. Az <b>Assets</b> (Fájlok) listában két fájlt látsz.", ["GH-01"]),
   ("<b>Firefoxhoz</b> az <code>.xpi</code> végű fájlt töltsd le (pl. <code>unics-themes-0.5.8.xpi</code>).", []),
   ("<b>Chrome-hoz, Edge-hez és Brave-hez</b> a <code>…-chromium.zip</code> fájlt töltsd le.", [])]),

 ("h1", "firefox", "4. Telepítés Firefoxban"),
 ("note", "ok", "Ez a legkényelmesebb", "A Firefox-verzió a Mozilla által <b>aláírt</b>, ezért egyszerűen telepíthető, tartósan megmarad, és magától frissül."),
 ("steps", [
   ("Töltsd le az <code>.xpi</code> fájlt a Releases oldalról (lásd a 3. fejezetet).", []),
   ("Nyisd meg a letöltött fájlt, vagy húzd rá a Firefox ablakára. Megjelenik egy kérdés: kattints a <b>Hozzáadás</b> gombra.", ["FF-01"]),
   ("Ellenőrizd: a <code>about:addons</code> oldalon az <b>Unics Themes</b> a bővítmények között látszik.", ["FF-02"]),
   ("Nyisd meg az Unics oldalt (<code>unics.szte.hu</code>), és kattints a bővítmény ikonjára. Firefoxban az oldalhoz való hozzáférést külön meg kell adni: nyomd meg a sárga dobozban az <b>Engedélyezés</b> gombot. Ez egyszeri lépés.", ["FF-03"]),
   ("Opcionális: tűzd ki az ikont az eszköztárra, hogy mindig kéznél legyen (puzzle ikon, majd <b>Kitűzés az eszköztárra</b>).", ["FF-04"]),
   ("Válassz színt és stílust a popupban. A változás azonnal látszik.", ["FF-05"])]),
 ("note", "info", "Frissítés", "A Firefox naponta egyszer ellenőrzi, van-e újabb verzió, és magától frissít. Azonnali kereséshez: <code>about:addons</code> → fogaskerék → <b>Bővítmények frissítéseinek keresése</b>."),

 ("h1", "chrome", "5. Telepítés Chrome-ban"),
 ("note", "warn", "Fontos: a mappa a bővítmény helye", "A Chrome a letöltött mappából olvassa a fájlokat, nem másolja át. Ezért a mappát <b>ne töröld és ne helyezd át</b>, különben a bővítmény leáll."),
 ("steps", [
   ("Töltsd le a <code>…-chromium.zip</code> fájlt (3. fejezet), és <b>csomagold ki egy állandó helyre</b>, pl. <code>Dokumentumok\\unics-themes</code>. Jobb klikk → <b>Összes kibontása</b>.", []),
   ("Nyisd meg a kicsomagolt mappát: közvetlenül benne kell lennie a <code>manifest.json</code> fájlnak.", ["GH-02"]),
   ("Írd be a címsorba: <code>chrome://extensions</code>, és kapcsold be jobb felül a <b>Fejlesztői módot</b>.", ["CH-01"]),
   ("Kattints a <b>Kicsomagolt bővítmény betöltése</b> gombra.", ["CH-02"]),
   ("Válaszd ki azt a mappát, amiben a <code>manifest.json</code> van, és kattints a <b>Mappa kiválasztása</b> gombra.", ["CH-03"]),
   ("Az <b>Unics Themes</b> megjelenik a listában, hibajelzés nélkül.", ["CH-04"]),
   ("Tűzd ki az ikont: puzzle ikon → az Unics Themes melletti tűzőcsap.", ["CH-05"]),
   ("Nyisd meg az Unics oldalt, kattints az ikonra, és válassz témát (lásd a 8. fejezetet).", [])]),
 ("note", "info", "Nem kell az „Engedélyezés” gomb", "Chrome-ban, Edge-ben és Bravében az oldalhoz való hozzáférés telepítéskor már megvan, a Firefoxtól eltérően."),

 ("h1", "edge", "6. Telepítés Edge-ben"),
 ("note", "warn", "Fontos: a mappa a bővítmény helye", "Az Edge is a kicsomagolt mappából olvassa a fájlokat. A mappát <b>ne töröld és ne helyezd át</b>."),
 ("steps", [
   ("Töltsd le a <code>…-chromium.zip</code> fájlt (3. fejezet), és csomagold ki egy állandó helyre.", ["GH-02"]),
   ("Írd be a címsorba: <code>edge://extensions</code>, és kapcsold be a bal oldali menüben a <b>Fejlesztői módot</b>.", ["ED-01"]),
   ("Kattints a <b>Kicsomagolt betöltése</b> gombra.", ["ED-02"]),
   ("Válaszd ki a mappát, amiben a <code>manifest.json</code> van.", ["ED-03"]),
   ("Az <b>Unics Themes</b> megjelenik a listában, hibajelzés nélkül.", ["ED-04"]),
   ("Tűzd ki az ikont az eszköztárra (Bővítmények menü → szem ikon az Unics Themes mellett).", ["ED-05"]),
   ("Nyisd meg az Unics oldalt, és válassz témát (8. fejezet).", [])]),

 ("h1", "brave", "7. Telepítés Bravében"),
 ("note", "warn", "Fontos: a mappa a bővítmény helye", "A Brave is a kicsomagolt mappából olvassa a fájlokat. A mappát <b>ne töröld és ne helyezd át</b>."),
 ("steps", [
   ("Töltsd le a <code>…-chromium.zip</code> fájlt (3. fejezet), és csomagold ki egy állandó helyre.", ["GH-02"]),
   ("Írd be a címsorba: <code>brave://extensions</code>, és kapcsold be a <b>Fejlesztői módot</b>.", ["BR-01"]),
   ("Kattints a <b>Kicsomagolt bővítmény betöltése</b> gombra.", ["BR-02"]),
   ("Válaszd ki a mappát, amiben a <code>manifest.json</code> van.", ["BR-03"]),
   ("Az <b>Unics Themes</b> megjelenik a listában, hibajelzés nélkül.", ["BR-04"]),
   ("Tűzd ki az ikont az eszköztárra (puzzle ikon → kitűzés).", ["BR-05"]),
   ("Nyisd meg az Unics oldalt, és válassz témát (8. fejezet).", [])]),
 ("note", "info", "Vivaldi, Opera és más Chromium-böngészők", "Ezekben ugyanígy működik a kicsomagolt betöltés (a cím <code>vivaldi://extensions</code>, ill. <code>opera://extensions</code>). Ezeket nem teszteltük."),

 ("h1", "hasznalat", "8. Használat"),
 ("steps", [
   ("Nyisd meg az Unics oldalt, és kattints a bővítmény ikonjára.", []),
   ("<b>Színek:</b> válassz a témák közül (Világos, Többszínű, Rózsaszín, Sötét). A kis előnézet mutatja a színeket.", ["US-01"]),
   ("<b>Stílus:</b> legörgetve válassz formát: Klasszikus (az eredeti), Modern, Üveg, Szigetek vagy Brutalista.", ["US-02"]),
   ("A kettő szabadon kombinálható, a változás azonnal látszik, és a böngésző bezárása után is megmarad.", [])]),
 ("h2", "Példák"),
 ("shot", "US-03"), ("shot", "US-04"), ("shot", "US-05"),
 ("note", "info", "Vissza az eredetihez", "Válaszd a <b>Világos → Eredeti</b> színt és a <b>Klasszikus</b> stílust: az oldal pontosan úgy néz ki, mint a bővítmény nélkül."),

 ("h1", "figyelj", "9. Amikre figyelj"),
 ("list", [
   "<b>Chrome, Edge, Brave:</b> a kicsomagolt mappát <b>ne töröld, ne nevezd át és ne helyezd át</b>. Ha mégis, a bővítmény hibával kikapcsol; tedd vissza, vagy töltsd be újra.",
   "<b>Ne csomagold a Letöltések mappába</b>, mert ott könnyen kitörlődik. Állandó helyet válassz.",
   "<b>Chrome/Edge figyelmeztetés:</b> indításkor megjelenhet egy üzenet a „fejlesztői módú bővítményekről”. Ez normális, bezárhatod, a bővítmény működik.",
   "<b>Firefox:</b> az Engedélyezés gombot egyszer kell megnyomni. Utána minden Unics-oldalon működik.",
   "<b>Frissítés kézzel</b> (Chrome, Edge, Brave): lásd a következő fejezetet.",
   "Csak a <b>unics.szte.hu</b> oldalon látszik a hatása. Más weboldalakat nem változtat."]),

 ("h1", "frissites", "10. Frissítés"),
 ("p", "<b>Firefox:</b> automatikus, nem kell tenned semmit."),
 ("p", "<b>Chrome, Edge, Brave:</b>"),
 ("steps", [
   ("Töltsd le az új <code>…-chromium.zip</code> fájlt a Releases oldalról.", []),
   ("Csomagold ki <b>ugyanabba a mappába</b>, a régi fájlok fölé (felülírás).", []),
   ("Nyisd meg a bővítménykezelőt, és kattints az Unics Themes kártyán az <b>Újratöltés</b> (⟳) gombra.", []),
   ("Az Unics oldalon nyomj egy F5-öt.", [])]),

 ("h1", "hiba", "11. Hibaelhárítás"),
 ("table", ["Mi a gond?", "Megoldás"], [
   ["Nem változik az oldal kinézete", "Firefoxban nyomd meg a popupban az <b>Engedélyezés</b> gombot. Nyomj F5-öt. Ellenőrizd, hogy a <code>unics.szte.hu</code> oldalon vagy-e."],
   ["Az Engedélyezés gomb nem tűnik el (Firefox)", "Kattints rá újra, és a böngésző kérdésére válaszolj <b>Engedélyezés</b>-sel. Ha így sem megy, indítsd újra a Firefoxot."],
   ["Újraindítás után eltűnt a bővítmény (Chrome/Edge/Brave)", "Valószínűleg a kicsomagolt mappa törlődött vagy elmozdult. Csomagold ki újra egy állandó helyre, és töltsd be."],
   ["Hibajelzés a bővítménykártyán", "Nyisd meg a Hibák gombot, és küldd el a szöveget a GitHub Issues oldalon. Próbáld meg az Újratöltés gombot is."],
   ["Valami rosszul néz ki (olvashatatlan szöveg, fehér doboz)", "Készíts képernyőképet, és írd meg, melyik téma és stílus. Addig válts másik témára."],
   ["Lassú az oldal", "Az Üveg stílus (elmosás) gyengébb gépen terhelőbb lehet. Válts Modern vagy Klasszikus stílusra."]]),

 ("h1", "eltavolitas", "12. Eltávolítás"),
 ("p", "Az eltávolítás után az oldal visszaáll az eredeti kinézetre, és a bővítmény minden adata törlődik a böngésződből."),
 ("steps", [
   ("<b>Firefox:</b> <code>about:addons</code> → az Unics Themes melletti <b>…</b> → <b>Eltávolítás</b>.", ["FF-06"]),
   ("<b>Chrome:</b> <code>chrome://extensions</code> → az Unics Themes kártyán <b>Eltávolítás</b>.", ["CH-06"]),
   ("<b>Edge:</b> <code>edge://extensions</code> → <b>Eltávolítás</b>.", ["ED-06"]),
   ("<b>Brave:</b> <code>brave://extensions</code> → <b>Eltávolítás</b>.", ["BR-06"]),
   ("Chrome/Edge/Brave esetén ezután a kicsomagolt mappát is törölheted.", [])]),

 ("h1", "licenc", "13. Licenc, hibabejelentés"),
 ("list", [
   "<b>Licenc:</b> PolyForm Noncommercial 1.0.0. Szabadon használható, másolható és módosítható <b>nem kereskedelmi célra</b>, de pénzt keresni vele nem lehet. A betűtípusok (Inter, Manrope) az SIL OFL licenc alatt állnak.",
   "<b>Nem hivatalos</b> projekt, nem áll kapcsolatban az SZTE-vel vagy az Unics / CooSpace fejlesztőivel.",
   "<b>Hibát találtál, vagy ötleted van?</b> Írj a GitHub <b>Issues</b> oldalon: <code>%s/issues</code>. Képernyőképet is csatolhatsz." % REPO,
   "A kód nyilvános: <code>%s</code>" % REPO]),
]

CHAPTERS_EN = [
 ("h1", "mi", "1. What is this?"),
 ("p", "<b>Unics Themes</b> is a small browser extension for the University of Szeged's <b>Unics (CooSpace)</b> site. It lets you choose how the site looks: 18 colour themes (light, colourful, pink, dark) and 5 styles (Classic, Modern, Glass, Islands, Brutalist), freely combined."),
 ("list", ["Your choice <b>is kept</b> after a refresh (F5) and after restarting the browser.", "Switch with one click: click the extension icon and the picker opens.", "Free, and can be turned off or removed at any time."]),
 ("note", "ok", "Nothing to worry about: it only changes the looks", "The extension changes <b>only how the page looks</b> (colours, shapes, animations). It is safe because:"),
 ("list", [
   "<b>It runs only on unics.szte.hu</b> and has no access to any other website.",
   "<b>It sends nothing anywhere</b>: no server, no tracking, no analytics. Your chosen theme is stored only in your own browser.",
   "<b>It does not change any Unics data</b>: it submits nothing and does not touch your grades, messages or assignments. Turn it off and everything is exactly as before.",
   "<b>It never asks for a password</b> and has no access to your saved passwords, history or other tabs.",
   "<b>The source code is open</b>: the full code is on GitHub for anyone to inspect.",
   "It is an <b>unofficial</b> project, not affiliated with the University of Szeged or the Unics developers."]),
 ("p", "To be technically precise: the extension has to run on the Unics page in order to recolour it, which the browser gates behind a separate permission (see the install chapters). It does not read out or forward the page's content; it only adjusts the appearance (colours, sizes)."),

 ("h1", "melyik", "2. Which browser do you use?"),
 ("p", "Installation differs slightly per browser. Find yours in the table, then jump to its chapter."),
 ("table", ["Browser", "How to install", "Stays after restart?", "Automatic updates"], [
   ["<b>Firefox</b>", "Signed .xpi file, one click", "Yes", "Yes (daily)"],
   ["<b>Chrome</b>", "Load an unpacked folder", "Yes, as long as the folder stays put", "No, manual"],
   ["<b>Edge</b>", "Load an unpacked folder", "Yes, as long as the folder stays put", "No, manual"],
   ["<b>Brave</b>", "Load an unpacked folder", "Yes, as long as the folder stays put", "No, manual"]]),
 ("note", "info", "Phones and tablets", "Chrome, Edge and Brave on Android do not support extensions, so it cannot be used there. We have not tested Firefox for Android, so it is not recommended. The extension is made for desktop computers (Windows, macOS, Linux)."),

 ("h1", "letoltes", "3. Downloading the file"),
 ("p", "Every release is on the GitHub <b>Releases</b> page: <code>%s</code>" % REL),
 ("steps", [
   ("Open the page above. In the <b>Assets</b> list you will see two files.", ["GH-01"]),
   ("<b>For Firefox</b> download the file ending in <code>.xpi</code> (e.g. <code>unics-themes-0.5.8.xpi</code>).", []),
   ("<b>For Chrome, Edge and Brave</b> download the <code>…-chromium.zip</code> file.", [])]),

 ("h1", "firefox", "4. Installing in Firefox"),
 ("note", "ok", "This is the easiest one", "The Firefox version is <b>signed</b> by Mozilla, so it installs simply, stays permanently and updates itself."),
 ("steps", [
   ("Download the <code>.xpi</code> file from the Releases page (chapter 3).", []),
   ("Open the downloaded file, or drag it onto the Firefox window. A prompt appears: click <b>Add</b>.", ["FF-01"]),
   ("Check: on <code>about:addons</code> the <b>Unics Themes</b> is listed among your extensions.", ["FF-02"]),
   ("Open the Unics site (<code>unics.szte.hu</code>) and click the extension icon. In Firefox, access to the site must be granted separately: press the <b>Allow</b> button in the yellow box. This is a one-time step.", ["FF-03"]),
   ("Optional: pin the icon to the toolbar so it is always at hand (puzzle icon, then <b>Pin to Toolbar</b>).", ["FF-04"]),
   ("Choose a colour and a style in the popup. The change is instant.", ["FF-05"])]),
 ("note", "info", "Updates", "Firefox checks once a day for a newer version and updates itself. To check right away: <code>about:addons</code> → gear icon → <b>Check for Updates</b>."),

 ("h1", "chrome", "5. Installing in Chrome"),
 ("note", "warn", "Important: the folder is the extension's home", "Chrome reads the files from the downloaded folder instead of copying them. So <b>do not delete or move</b> the folder, otherwise the extension stops."),
 ("steps", [
   ("Download the <code>…-chromium.zip</code> file (chapter 3) and <b>extract it to a permanent place</b>, e.g. <code>Documents\\unics-themes</code>. Right-click → <b>Extract All</b>.", []),
   ("Open the extracted folder: <code>manifest.json</code> must be directly inside it.", ["GH-02"]),
   ("Type <code>chrome://extensions</code> into the address bar and switch on <b>Developer mode</b> in the top right.", ["CH-01"]),
   ("Click <b>Load unpacked</b>.", ["CH-02"]),
   ("Select the folder that contains <code>manifest.json</code> and click <b>Select Folder</b>.", ["CH-03"]),
   ("<b>Unics Themes</b> appears in the list, with no error.", ["CH-04"]),
   ("Pin the icon: puzzle icon → the pin next to Unics Themes.", ["CH-05"]),
   ("Open the Unics site, click the icon and choose a theme (chapter 8).", [])]),
 ("note", "info", "No “Allow” button needed", "In Chrome, Edge and Brave, access to the site is already granted on install, unlike Firefox."),

 ("h1", "edge", "6. Installing in Edge"),
 ("note", "warn", "Important: the folder is the extension's home", "Edge also reads the files from the extracted folder. <b>Do not delete or move</b> the folder."),
 ("steps", [
   ("Download the <code>…-chromium.zip</code> file (chapter 3) and extract it to a permanent place.", ["GH-02"]),
   ("Type <code>edge://extensions</code> into the address bar and switch on <b>Developer mode</b> in the left menu.", ["ED-01"]),
   ("Click <b>Load unpacked</b>.", ["ED-02"]),
   ("Select the folder that contains <code>manifest.json</code>.", ["ED-03"]),
   ("<b>Unics Themes</b> appears in the list, with no error.", ["ED-04"]),
   ("Pin the icon to the toolbar (Extensions menu → eye icon next to Unics Themes).", ["ED-05"]),
   ("Open the Unics site and choose a theme (chapter 8).", [])]),

 ("h1", "brave", "7. Installing in Brave"),
 ("note", "warn", "Important: the folder is the extension's home", "Brave also reads the files from the extracted folder. <b>Do not delete or move</b> the folder."),
 ("steps", [
   ("Download the <code>…-chromium.zip</code> file (chapter 3) and extract it to a permanent place.", ["GH-02"]),
   ("Type <code>brave://extensions</code> into the address bar and switch on <b>Developer mode</b>.", ["BR-01"]),
   ("Click <b>Load unpacked</b>.", ["BR-02"]),
   ("Select the folder that contains <code>manifest.json</code>.", ["BR-03"]),
   ("<b>Unics Themes</b> appears in the list, with no error.", ["BR-04"]),
   ("Pin the icon to the toolbar (puzzle icon → pin).", ["BR-05"]),
   ("Open the Unics site and choose a theme (chapter 8).", [])]),
 ("note", "info", "Vivaldi, Opera and other Chromium browsers", "Loading unpacked works the same way there (address <code>vivaldi://extensions</code> or <code>opera://extensions</code>). We have not tested these."),

 ("h1", "hasznalat", "8. Using it"),
 ("steps", [
   ("Open the Unics site and click the extension icon.", []),
   ("<b>Colours:</b> pick a theme (Light, Colourful, Pink, Dark). The small preview shows the colours.", ["US-01"]),
   ("<b>Style:</b> scroll down and pick a shape: Classic (the original), Modern, Glass, Islands or Brutalist.", ["US-02"]),
   ("The two combine freely, the change is instant, and it survives closing the browser.", [])]),
 ("h2", "Examples"),
 ("shot", "US-03"), ("shot", "US-04"), ("shot", "US-05"),
 ("note", "info", "Back to the original", "Choose <b>Light → Eredeti</b> as the colour and <b>Klasszikus</b> as the style: the page looks exactly as it does without the extension."),

 ("h1", "figyelj", "9. Things to watch out for"),
 ("list", [
   "<b>Chrome, Edge, Brave:</b> <b>do not delete, rename or move</b> the extracted folder. If you do, the extension switches off with an error; put it back or load it again.",
   "<b>Do not extract into the Downloads folder</b>, where it is easily deleted. Pick a permanent place.",
   "<b>Chrome/Edge warning:</b> at startup a message about “developer mode extensions” may appear. This is normal; close it, the extension works.",
   "<b>Firefox:</b> the Allow button is pressed once. After that it works on every Unics page.",
   "<b>Manual updates</b> (Chrome, Edge, Brave): see the next chapter.",
   "The effect is visible only on <b>unics.szte.hu</b>. It changes no other website."]),

 ("h1", "frissites", "10. Updating"),
 ("p", "<b>Firefox:</b> automatic, nothing to do."),
 ("p", "<b>Chrome, Edge, Brave:</b>"),
 ("steps", [
   ("Download the new <code>…-chromium.zip</code> from the Releases page.", []),
   ("Extract it <b>into the same folder</b>, over the old files (overwrite).", []),
   ("Open the extensions page and click <b>Reload</b> (⟳) on the Unics Themes card.", []),
   ("Press F5 on the Unics site.", [])]),

 ("h1", "hiba", "11. Troubleshooting"),
 ("table", ["What is wrong?", "Fix"], [
   ["The page does not change", "In Firefox press <b>Allow</b> in the popup. Press F5. Check that you are on <code>unics.szte.hu</code>."],
   ["The Allow button does not go away (Firefox)", "Click it again and answer the browser prompt with <b>Allow</b>. If it still fails, restart Firefox."],
   ["The extension vanished after a restart (Chrome/Edge/Brave)", "The extracted folder was probably deleted or moved. Extract it again to a permanent place and load it."],
   ["Error on the extension card", "Open the Errors button and send the text via GitHub Issues. Also try the Reload button."],
   ["Something looks wrong (unreadable text, white box)", "Take a screenshot and tell us which theme and style. Switch to another theme meanwhile."],
   ["The page feels slow", "The Glass style (blur) can be heavier on weaker machines. Switch to Modern or Classic."]]),

 ("h1", "eltavolitas", "12. Removing it"),
 ("p", "After removal the page returns to its original look and all extension data is deleted from your browser."),
 ("steps", [
   ("<b>Firefox:</b> <code>about:addons</code> → the <b>…</b> next to Unics Themes → <b>Remove</b>.", ["FF-06"]),
   ("<b>Chrome:</b> <code>chrome://extensions</code> → <b>Remove</b> on the Unics Themes card.", ["CH-06"]),
   ("<b>Edge:</b> <code>edge://extensions</code> → <b>Remove</b>.", ["ED-06"]),
   ("<b>Brave:</b> <code>brave://extensions</code> → <b>Remove</b>.", ["BR-06"]),
   ("For Chrome/Edge/Brave you can then delete the extracted folder too.", [])]),

 ("h1", "licenc", "13. Licence, reporting issues"),
 ("list", [
   "<b>Licence:</b> PolyForm Noncommercial 1.0.0. Free to use, copy and modify for <b>non-commercial purposes</b>; it may not be used to make money. The fonts (Inter, Manrope) are under the SIL OFL licence.",
   "<b>Unofficial</b> project, not affiliated with the University of Szeged or the Unics / CooSpace developers.",
   "<b>Found a bug or have an idea?</b> Write on the GitHub <b>Issues</b> page: <code>%s/issues</code>. You can attach a screenshot." % REPO,
   "The code is public: <code>%s</code>" % REPO]),
]

META = {
 "hu": dict(file="utmutato-hu", title="Unics Themes – telepítési útmutató", sub="Egyedi témák az SZTE Unics (CooSpace) felületéhez",
            ver="Verzió", toc="Tartalom", guide="Útmutató", footer="Nem hivatalos projekt · nem kereskedelmi licenc", missing="Ide kerül a képernyőkép", other="English version: GUIDE.md"),
 "en": dict(file="guide-en", title="Unics Themes – installation guide", sub="Custom themes for the University of Szeged's Unics (CooSpace)",
            ver="Version", toc="Contents", guide="Guide", footer="Unofficial project · non-commercial licence", missing="Screenshot goes here", other="Magyar verzió: UTMUTATO.md"),
}
