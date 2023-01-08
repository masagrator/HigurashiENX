# HigurashiENX

English translation mod for Nintendo Switch version of "Higurashi no Naku Koro ni Hou" (ひぐらしのなく頃に奉).

1.2.0 update is required.

Mod is partially using machine translation.

---

# Download and installation

1. Download mod from Releases
2. Copy `atmosphere` folder to root of sdcard used in your Switch
3. Run game.

---

# Compiling and installing mod manually

Repo is targeting Windows 10 with WSL Ubuntu installed. All tools and scripts are compatible with linux distros like Ubuntu, but because I don't know anything about shell files, I'm focusing on Windows only.

Requirements:
- Python 3 (and `numpy` library) 

Instructions:
1. Download repo with all submodules,
2. Compile `ShinDataUtil` (for example with `Microsoft Visual Studio 2019`),
3. Extract `data.rom` and `patch.rom` from romfs of game. You can use [NXDumpTool](https://github.com/DarkMatterCore/nxdumptool/releases) for that. Put those files to `ROMs` folder in downloaded repo,
4. Run `0.1.unpack-rom-files.cmd` without Administrator privileges,
5. Run `0.2.replace-images.cmd` without Administrator privileges,
6. Run `0.3.create-images.cmd` without Administrator privileges,
7. Run `0.4.create-mod.cmd` without Administrator privileges,
8. Copy `atmosphere` folder to the root of sdcard used in your Switch,
9. Run game.

---

# Notes
- Project started at 4th January 2021, first release was in 29th June 2021
- This project is practically in infinite beta. Expect bugs like not playing audio files, weird break lines, crashing related to broken tags, etc.
- We are providing support only for Nintendo Switch users with Atmosphere. Any other way of using this mod (different CFW or emulators) are not supported by us, but this doesn't mean it won't work on them.
- This project was not made with purpose to make easier to translate to other languages. JSON files are containing texts only for sending corrections and translation updates. They don't have any readable way to understand how SELECT is forcing jumps and sets flags.
- Script supports mainly Shift-JIS, so implementing any other language needs additional effort. PC release is not bothered by this limiation.
- Game doesn't support italics, they are changed so word is between `*`
- Mod is using special patch that not only translates strings stored in executable, but also allows for loading third ROM file on top of data.rom and patch.rom. This allows us to share ROM with only those files that are necessary for this mod (thanks for DCNick3 for that).
- We won't work on porting this mod to PS4 version of game.
- Mod translated only required minimum of images. We are not bothered by images that are using japanese and english texts at the same time (except for wrongly translated images).
- Mod is using `shindatautil` layouting function for automatic injection of break lines. Game itself is breaking lines by any last fitting character, not by last fitting space only.
- This mod is also compatible with the physical edition "EG THE BEST" without any change required.
- `Oyashiro Shock` is in work as plugin which won't be compatible with any emulator to date.
- Hirukowashi has an option to mark it as finished without playing it at the beginning of chapter, because finishing it is required to play next chapters.

---

# Translation Status

Okinomiya Police Station Report:
- Prologue 100% (0% Machine Translation)
- Common Route 100% (9.4% Machine Translation)
- Rena Route 100% (100% Machine Translation)
- Mion Route 100% (20.8% Machine Translation)
- Satoko Route 100% (3.8% Machine Translation)
- Natsumi Route 100% (30% Machine Translation)
- Onikakushi 100% (0% Machine Translation)
- Onikakushi Afterparty 100% (3.9% Machine Translation)
- Watanagashi 100% (0.03% Machine Translation)
- Watanagashi Afterparty 100% (1 line Machine Translated)
- Tatarigoroshi 100% (1.1% Machine Translation)
- Tatarigoroshi Afterparty 100% (7.4% Machine Translation)
- Tsukiotoshi 100% (1 line Machine Translated)
- Taraimawashi 100% (0% Machine Translation)
- Taraimawashi Afterparty 100% (0% Machine Translation)
- Someutsushi 100% (0% Machine Translation)
- Sometsushi Afterparty 100% (0% Machine Translation)
- Epilogue 100% (0% Machine Translation)

Metropolitan Public Security 7th Room Case File:
- Prologue 100% (0% Machine Translation)
- Himatsubushi 100% (0.07% Machine Translation)
- Himatsubushi Afterparty 100% (6.6% Machine Translation)
- Meakashi 100% (0.05% Machine Translation)
- Hirukowashi 100% (0% Machine Translation)
- Kageboushi 100% (0% Machine Translation)
- Epilogue 100% (0% Machine Translation)

National Police Agency Administrative Document:
- Prologue 100% (0% Machine Translation)
- Tsumihoroboshi 100% (1.6% Machine Translation)
- Yoigoshi 100% (0% Machine Translation)
- Minagoroshi 100% (1.3% Machine Translation)
- Tokihogushi 100% (0% Machine Translation)
- Epilogue 100% (0% Machine Translation)

World of Fragments:
- Everlasting Dream 100% (6.6% Machine Translation)
- Prologue 100% (0% Machine Translation)
- Spinning Fragments 100% (0.08% Machine Translation)
- Matsuribayashi 100% (1% Machine Translation)
- Miotsukushi Omote 100% (3 lines Machine Translated)
- Miotsukushi Ura 100% (0% Machine Translation)
- Saikoroshi 100% (0% Machine Translation)
- Kotohogushi 100% (0% Machine Translation)
- Hajisarashi 100% (0% Machine Translation)
- Epilogue 100% (0% Machine Translation)

Gift:
- Higurashi Outbreak 100% (100% Machine Translation)
- Kamikashimashi 100% (100% Machine Translation)
- Hinamizawa Bus Stop 100% (100% Machine Translation)
- Batsukoishi 100% (1 line Machine Translated)
- "Gift" Afterparty 100% (0% Machine Translation)

TIPS: 169/188

---

# Plans

- Replace all machine translated parts with real translation
- Polish style matching of images from the same group

---

# Sources
Here I will provide names/links to all tools, files and sites I have used while working on this mod:

Tools:
- https://github.com/DCNick3/ShinDataUtil
- https://github.com/07th-mod/enter_extractor
- https://gitlab.com/Neurochitin/kaleido/-/tree/saku

Texts:
- https://github.com/07th-mod/higurashi-console-arcs
- https://github.com/07th-mod/tsumihoroboshi
- https://github.com/07th-mod/matsuribayashi
- https://github.com/07th-mod/minagoroshi
- https://github.com/07th-mod/tatarigoroshi
- https://github.com/07th-mod/meakashi
- https://github.com/07th-mod/himatsubushi
- https://github.com/07th-mod/watanagashi
- https://github.com/07th-mod/onikakushi
- https://github.com/07th-mod/higurashi-rei
- https://twitter.com/furudejinja/status/1330012660377686017

Other:
- https://www.youtube.com/channel/UCCgK9pgiq0Bt73ESMjQfARg
- https://github.com/DCNick3/higu-switch-patches
- https://whentheycry.fandom.com/wiki/Higurashi_no_Naku_Koro_Ni_Wiki
- Google Sheets
- Python 3
- Notepad++
- GIMP 2
- Adobe Photoshop 2020

---

# Thanks to
- MangaGamer for releasing 8 main chapters in English (not directly involved with this project). Official Steam release available here: https://store.steampowered.com/bundle/709/Higurashi_When_They_Cry_Hou/
- [07th mod](https://07th-mod.com/home/) for tremendous work put to translations of console exclusive chapters and help with understanding some technical things about game engine (not directly involved with this project)
- xPearse Scanlations - for providing machine translations for Hou chapters (not directly involved with this project)
- [DCNick3](https://github.com/DCNick3) for ShinDataUtil, mainly for scenario decompiler/compiler. Without it this project wouldn't even start.
- [Neurochitin](https://gitlab.com/Neurochitin) for providing scripts that helped finish this project faster.
- ~Xanu for help with translating and proofreading some parts of game
- ~LeatherCupcake for testing
- ~DestockJapan for help with translating some lines
- ~loonelywolf for help with proofreading some images

And everybody I forgot to list here.

---

# Gallery

<img src="https://i.imgur.com/PKN5SND.jpg" width="540"><br>
<img src="https://i.imgur.com/BuxOVLH.jpg" width="540"><br>
<img src="https://i.imgur.com/Tn8GCi7.jpg" width="540"><br>
<img src="https://i.imgur.com/poClDuB.jpg" width="540"><br>
<img src="https://i.imgur.com/mdtsycg.jpg" width="540"><br>
<img src="https://i.imgur.com/D7JE22Q.jpg" width="540"><br>
<img src="https://i.imgur.com/bj6GmjF.jpg" width="540">
