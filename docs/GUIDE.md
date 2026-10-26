# Unics Themes – installation guide

Custom themes for the University of Szeged's Unics (CooSpace)  
Version 0.5.8 · Magyar verzió: UTMUTATO.md

## Contents

1. [What is this?](#1-what-is-this)
2. [Which browser do you use?](#2-which-browser-do-you-use)
3. [Downloading the file](#3-downloading-the-file)
4. [Installing in Firefox](#4-installing-in-firefox)
5. [Installing in Chrome](#5-installing-in-chrome)
6. [Installing in Edge](#6-installing-in-edge)
7. [Installing in Brave](#7-installing-in-brave)
8. [Using it](#8-using-it)
9. [Things to watch out for](#9-things-to-watch-out-for)
10. [Updating](#10-updating)
11. [Troubleshooting](#11-troubleshooting)
12. [Removing it](#12-removing-it)
13. [Licence, reporting issues](#13-licence-reporting-issues)


## 1. What is this?

**Unics Themes** is a small browser extension for the University of Szeged's **Unics (CooSpace)** site. It lets you choose how the site looks: 18 colour themes (light, colourful, pink, dark) and 5 styles (Classic, Modern, Glass, Islands, Brutalist), freely combined.

- Your choice **is kept** after a refresh (F5) and after restarting the browser.
- Switch with one click: click the extension icon and the picker opens.
- Free, and can be turned off or removed at any time.

> ✅ **Nothing to worry about: it only changes the looks**  
> The extension changes **only how the page looks** (colours, shapes, animations). It is safe because:

- **It runs only on unics.szte.hu** and has no access to any other website.
- **It sends nothing anywhere**: no server, no tracking, no analytics. Your chosen theme is stored only in your own browser.
- **It does not change any Unics data**: it submits nothing and does not touch your grades, messages or assignments. Turn it off and everything is exactly as before.
- **It never asks for a password** and has no access to your saved passwords, history or other tabs.
- **The source code is open**: the full code is on GitHub for anyone to inspect.
- It is an **unofficial** project, not affiliated with the University of Szeged or the Unics developers.

To be technically precise: the extension has to run on the Unics page in order to recolour it, which the browser gates behind a separate permission (see the install chapters). It does not read out or forward the page's content; it only adjusts the appearance (colours, sizes).


## 2. Which browser do you use?

Installation differs slightly per browser. Find yours in the table, then jump to its chapter.

| Browser | How to install | Stays after restart? | Automatic updates |
|---|---|---|---|
| **Firefox** | Signed .xpi file, one click | Yes | Yes (daily) |
| **Chrome** | Load an unpacked folder | Yes, as long as the folder stays put | No, manual |
| **Edge** | Load an unpacked folder | Yes, as long as the folder stays put | No, manual |
| **Brave** | Load an unpacked folder | Yes, as long as the folder stays put | No, manual |

> ℹ️ **Phones and tablets**  
> Chrome, Edge and Brave on Android do not support extensions, so it cannot be used there. We have not tested Firefox for Android, so it is not recommended. The extension is made for desktop computers (Windows, macOS, Linux).


## 3. Downloading the file

Every release is on the GitHub **Releases** page: `https://github.com/zoltan-234/coospace5-egyedi-temak-szte/releases/latest`

1. Open the page above. In the **Assets** list you will see two files.

   > 🖼️ *[GH-01] The GitHub Releases page: the two downloadable files*
   
2. **For Firefox** download the file ending in `.xpi` (e.g. `unics-themes-0.5.8.xpi`).
3. **For Chrome, Edge and Brave** download the `…-chromium.zip` file.


## 4. Installing in Firefox

> ✅ **This is the easiest one**  
> The Firefox version is **signed** by Mozilla, so it installs simply, stays permanently and updates itself.

1. Download the `.xpi` file from the Releases page (chapter 3).
2. Open the downloaded file, or drag it onto the Firefox window. A prompt appears: click **Add**.

   > 🖼️ *[FF-01] Firefox: confirming the installation (Add button)*
   
3. Check: on `about:addons` the **Unics Themes** is listed among your extensions.

   > 🖼️ *[FF-02] Firefox: the add-on in the add-ons list*
   
4. Open the Unics site (`unics.szte.hu`) and click the extension icon. In Firefox, access to the site must be granted separately: press the **Allow** button in the yellow box. This is a one-time step.

   > 🖼️ *[FF-03] Firefox: the Allow button in the popup*
   
5. Optional: pin the icon to the toolbar so it is always at hand (puzzle icon, then **Pin to Toolbar**).

   > 🖼️ *[FF-04] Firefox: pinning the add-on to the toolbar*
   
6. Choose a colour and a style in the popup. The change is instant.

   > 🖼️ *[FF-05] Firefox: the Unics site with a theme applied*
   

> ℹ️ **Updates**  
> Firefox checks once a day for a newer version and updates itself. To check right away: `about:addons` → gear icon → **Check for Updates**.


## 5. Installing in Chrome

> ⚠️ **Important: the folder is the extension's home**  
> Chrome reads the files from the downloaded folder instead of copying them. So **do not delete or move** the folder, otherwise the extension stops.

1. Download the `…-chromium.zip` file (chapter 3) and **extract it to a permanent place**, e.g. `Documents\unics-themes`. Right-click → **Extract All**.
2. Open the extracted folder: `manifest.json` must be directly inside it.

   > 🖼️ *[GH-02] The extracted folder: manifest.json is directly inside*
   
3. Type `chrome://extensions` into the address bar and switch on **Developer mode** in the top right.

   > 🖼️ *[CH-01] Chrome: the extensions page with Developer mode on*
   
4. Click **Load unpacked**.

   > 🖼️ *[CH-02] Chrome: the “Load unpacked” button*
   
5. Select the folder that contains `manifest.json` and click **Select Folder**.

   > 🖼️ *[CH-03] Chrome: choosing the folder*
   
6. **Unics Themes** appears in the list, with no error.

   > 🖼️ *[CH-04] Chrome: the loaded extension card*
   
7. Pin the icon: puzzle icon → the pin next to Unics Themes.

   > 🖼️ *[CH-05] Chrome: pinning to the toolbar*
   
8. Open the Unics site, click the icon and choose a theme (chapter 8).

> ℹ️ **No “Allow” button needed**  
> In Chrome, Edge and Brave, access to the site is already granted on install, unlike Firefox.


## 6. Installing in Edge

> ⚠️ **Important: the folder is the extension's home**  
> Edge also reads the files from the extracted folder. **Do not delete or move** the folder.

1. Download the `…-chromium.zip` file (chapter 3) and extract it to a permanent place.

   > 🖼️ *[GH-02] The extracted folder: manifest.json is directly inside*
   
2. Type `edge://extensions` into the address bar and switch on **Developer mode** in the left menu.

   > 🖼️ *[ED-01] Edge: the extensions page with Developer mode on*
   
3. Click **Load unpacked**.

   > 🖼️ *[ED-02] Edge: the “Load unpacked” button*
   
4. Select the folder that contains `manifest.json`.

   > 🖼️ *[ED-03] Edge: choosing the folder*
   
5. **Unics Themes** appears in the list, with no error.

   > 🖼️ *[ED-04] Edge: the loaded extension card*
   
6. Pin the icon to the toolbar (Extensions menu → eye icon next to Unics Themes).

   > 🖼️ *[ED-05] Edge: pinning to the toolbar*
   
7. Open the Unics site and choose a theme (chapter 8).


## 7. Installing in Brave

> ⚠️ **Important: the folder is the extension's home**  
> Brave also reads the files from the extracted folder. **Do not delete or move** the folder.

1. Download the `…-chromium.zip` file (chapter 3) and extract it to a permanent place.

   > 🖼️ *[GH-02] The extracted folder: manifest.json is directly inside*
   
2. Type `brave://extensions` into the address bar and switch on **Developer mode**.

   > 🖼️ *[BR-01] Brave: the extensions page with Developer mode on*
   
3. Click **Load unpacked**.

   > 🖼️ *[BR-02] Brave: the “Load unpacked” button*
   
4. Select the folder that contains `manifest.json`.

   > 🖼️ *[BR-03] Brave: choosing the folder*
   
5. **Unics Themes** appears in the list, with no error.

   > 🖼️ *[BR-04] Brave: the loaded extension card*
   
6. Pin the icon to the toolbar (puzzle icon → pin).

   > 🖼️ *[BR-05] Brave: pinning to the toolbar*
   
7. Open the Unics site and choose a theme (chapter 8).

> ℹ️ **Vivaldi, Opera and other Chromium browsers**  
> Loading unpacked works the same way there (address `vivaldi://extensions` or `opera://extensions`). We have not tested these.


## 8. Using it

1. Open the Unics site and click the extension icon.
2. **Colours:** pick a theme (Light, Colourful, Pink, Dark). The small preview shows the colours.

   > 🖼️ *[US-01] The popup: colour themes*
   
3. **Style:** scroll down and pick a shape: Classic (the original), Modern, Glass, Islands or Brutalist.

   > 🖼️ *[US-02] The popup: styles*
   
4. The two combine freely, the change is instant, and it survives closing the browser.


### Examples


> 🖼️ *[US-03] Example: Modern style, light theme*


> 🖼️ *[US-04] Example: Glass style, dark theme*


> 🖼️ *[US-05] Example: Brutalist style*

> ℹ️ **Back to the original**  
> Choose **Light → Eredeti** as the colour and **Klasszikus** as the style: the page looks exactly as it does without the extension.


## 9. Things to watch out for

- **Chrome, Edge, Brave:** **do not delete, rename or move** the extracted folder. If you do, the extension switches off with an error; put it back or load it again.
- **Do not extract into the Downloads folder**, where it is easily deleted. Pick a permanent place.
- **Chrome/Edge warning:** at startup a message about “developer mode extensions” may appear. This is normal; close it, the extension works.
- **Firefox:** the Allow button is pressed once. After that it works on every Unics page.
- **Manual updates** (Chrome, Edge, Brave): see the next chapter.
- The effect is visible only on **unics.szte.hu**. It changes no other website.


## 10. Updating

**Firefox:** automatic, nothing to do.

**Chrome, Edge, Brave:**

1. Download the new `…-chromium.zip` from the Releases page.
2. Extract it **into the same folder**, over the old files (overwrite).
3. Open the extensions page and click **Reload** (⟳) on the Unics Themes card.
4. Press F5 on the Unics site.


## 11. Troubleshooting

| What is wrong? | Fix |
|---|---|
| The page does not change | In Firefox press **Allow** in the popup. Press F5. Check that you are on `unics.szte.hu`. |
| The Allow button does not go away (Firefox) | Click it again and answer the browser prompt with **Allow**. If it still fails, restart Firefox. |
| The extension vanished after a restart (Chrome/Edge/Brave) | The extracted folder was probably deleted or moved. Extract it again to a permanent place and load it. |
| Error on the extension card | Open the Errors button and send the text via GitHub Issues. Also try the Reload button. |
| Something looks wrong (unreadable text, white box) | Take a screenshot and tell us which theme and style. Switch to another theme meanwhile. |
| The page feels slow | The Glass style (blur) can be heavier on weaker machines. Switch to Modern or Classic. |


## 12. Removing it

After removal the page returns to its original look and all extension data is deleted from your browser.

1. **Firefox:** `about:addons` → the **…** next to Unics Themes → **Remove**.

   > 🖼️ *[FF-06] Firefox: removing the add-on*
   
2. **Chrome:** `chrome://extensions` → **Remove** on the Unics Themes card.

   > 🖼️ *[CH-06] Chrome: removing the extension*
   
3. **Edge:** `edge://extensions` → **Remove**.

   > 🖼️ *[ED-06] Edge: removing the extension*
   
4. **Brave:** `brave://extensions` → **Remove**.

   > 🖼️ *[BR-06] Brave: removing the extension*
   
5. For Chrome/Edge/Brave you can then delete the extracted folder too.


## 13. Licence, reporting issues

- **Licence:** PolyForm Noncommercial 1.0.0. Free to use, copy and modify for **non-commercial purposes**; it may not be used to make money. The fonts (Inter, Manrope) are under the SIL OFL licence.
- **Unofficial** project, not affiliated with the University of Szeged or the Unics / CooSpace developers.
- **Found a bug or have an idea?** Write on the GitHub **Issues** page: `https://github.com/zoltan-234/coospace5-egyedi-temak-szte/issues`. You can attach a screenshot.
- The code is public: `https://github.com/zoltan-234/coospace5-egyedi-temak-szte`

