# Video Download Status - Operation WAL-REQUIEM

## Video Quellen Identifiziert

### 1. Thilo Maack Video (tagesschau24)
- **URL:** https://www.tagesschau.de/video/video-1569826.html
- **Direkte MP4 URL:** https://tagesschau-progressive.ard-mcdn.de/video/2026/0328/TV-20260328-1359-1300.webxxl.h264.mp4
- **Titel:** "Thilo Maack, Meeresbiologe Greenpeace, zur Suche nach Buckelwal in der Ostsee"
- **Datum:** 28.03.2026, 13:00 Uhr
- **Dauer:** 6:58 Minuten
- **Qualität:** webxxl (1920x1080, Full HD)
- **Größe:** ~100 MB (geschätzt)
- **Format:** H.264 MP4

### 2. Hallo Niedersachsen Video (NDR)
- **URL:** https://www.ndr.de/fernsehen/sendungen/hallo_niedersachsen/befreiter-buckelwal-erneut-gestrandet,hallonds-6488.html
- **Titel:** "Befreiter Buckelwal erneut gestrandet"
- **Datum:** 28.03.2026, 19:30 Uhr
- **Type:** TV news segment
- **Status:** URL noch zu extrahieren

### 3. Drohnenaufnahmen (NDR)
- **URL:** https://www.ndr.de/radiomv/drohnenaufnahmen-zeigen-buckelwal-in-der-wismarer-bucht,buckelwal-178.html
- **Datum:** 28.03.2026, 18:00 Uhr
- **Content:** Drone footage
- **Status:** URL noch zu extrahieren

### 4. Robert Marc Lehmann Video (NDR)
- **URL:** https://www.ndr.de/fernsehen/sendungen/schleswig-holstein_magazin/Robert-Marc-Lehmann-ueber-Buckelwal-in-der-Ostsee,schleswig-holstein-magazin-648.html
- **Titel:** "Robert Marc Lehmann über Buckelwal in der Ostsee"
- **Datum:** 27.03.2026, 19:46 Uhr
- **Type:** TV news segment
- **Status:** ⏳ IN ARBEIT

---

## Download-Status

| Video | Status | Datei | Größe |
|-------|--------|-------|-------|
| Thilo Maack webxxl | ✅ ABGESCHLOSSEN (GETEILT) | TV-20260328-1359-1300_Thilo_Maack_webxxl_part1.mp4 (81.3 MB)<br>TV-20260328-1359-1300_Thilo_Maack_webxxl_part2.mp4 (87.9 MB) | 169,665,188 Bytes original (~162 MB) → 2 Teile je ~80 MB |
| Drohnenaufnahmen 1080 | ✅ ABGESCHLOSSEN | TV-20260328-1926-5400_Drohnenaufnahmen_1080.mp4 | 25,916,247 Bytes (~24.7 MB) |
| Hallo Niedersachsen 1080 | ✅ ABGESCHLOSSEN | TV-20260328-1939-1900_Hallo_Niedersachsen_1080.mp4 | 67,275,302 Bytes (~64.2 MB) |
| Robert Marc Lehmann wal-230 | ✅ ABGESCHLOSSEN | TV-20260326-1240-1300_Robert_Marc_Lehmann_1080.mp4 | 25,797,836 Bytes (~24.6 MB) |
| Buckelwal MV (RML) | ✅ ABGESCHLOSSEN | TV-20260327-1946-0500_Buckelwal_MV_1080.mp4 | 7,980,375 Bytes (~7.6 MB) |
| Wal befreit webxxl | ✅ ABGESCHLOSSEN (GETEILT) | TV-20260327-1837-5700_Wal_befreit_webxxl_part1.mp4 (86.9 MB)<br>TV-20260327-1837-5700_Wal_befreit_webxxl_part2.mp4 (73.9 MB) | 161,072,119 Bytes original (~153.6 MB) → 2 Teile je ~80 MB |

---

## Robert Marc Lehmann Videos (alle)

| # | Video | Datei | Größe | Datum | Status |
|---|-------|-------|-------|-------|--------|
| 1 | **Robert Marc Lehmann Interview (wal-230)** | TV-20260326-1240-1300_Robert_Marc_Lehmann_1080.mp4 | 24.6 MB | 26.03.2026, 12:40 | ✅ GESPEICHERT |
| 2 | **Buckelwal zuletzt vor MV** | TV-20260327-1946-0500_Buckelwal_MV_1080.mp4 | 7.6 MB | 27.03.2026, 19:46 | ✅ GESPEICHERT |

**Gesamtgröße Robert Marc Lehmann Videos:** 32.2 MB

**Details siehe:** `ROBERT_MARC_LEHMANN_VIDEOS.md`

---

## Technische Informationen

### Video-URL-Muster (ARD/tagesschau)
```
https://tagesschau-progressive.ard-mcdn.de/video/YYYY/MMDD/TV-YYYYMMDD-HHMM-XXXX.[QUALITÄT].h264.mp4
```

Verfügbare Qualitätsstufen:
- `webs` - 480px (SD)
- `webm` - 640px
- `webl` - 960px
- `webxl` - 1280px (HD)
- `webxxl` - 1920px (Full HD)

### M3U8 Stream URL
```
https://adaptive.tagesschau.de/i/video/2026/0328/TV-20260328-1359-1300,.webs.h264.mp4,.webl.h264.mp4,.webxl.h264.mp4,.webxxl.h264.mp4,.webm.h264.mp4,.csmil/master.m3u8
```

---

## Download-Befehle

### PowerShell (langsam, aber stabil)
```powershell
Invoke-WebRequest -Uri "https://tagesschau-progressive.ard-mcdn.de/video/2026/0328/TV-20260328-1359-1300.webxxl.h264.mp4" -OutFile "TV-20260328-1359-1300_Thilo_Maack_webxxl.mp4" -MaximumRedirection 10
```

### yt-dlp (empfohlen, falls verfügbar)
```bash
yt-dlp -o "TV-20260328-1359-1300_Thilo_Maack_%(height)s.%(ext)s" "https://www.tagesschau.de/video/video-1569826.html"
```

### FFmpeg (aus M3U8)
```bash
ffmpeg -i "https://adaptive.tagesschau.de/i/video/2026/0328/TV-20260328-1359-1300,.webs.h264.mp4,.webl.h264.mp4,.webxl.h264.mp4,.webxxl.h264.mp4,.webm.h264.mp4,.csmil/master.m3u8" -c copy "TV-20260328-1359-1300_Thilo_Maack.mp4"
```

---

## Metadaten (Thilo Maack Video)

- **Sendung:** tagesschau24
- **Datum:** 28.03.2026
- **Uhrzeit:** 13:00 Uhr (Video), 14:12 Uhr (Artikel-Stand)
- **Person:** Thilo Maack (Meeresbiologe, Greenpeace)
- **Thema:** Suche nach Buckelwal in der Ostsee
- **Format:** H.264 MP4
- **Auflösung:** 1920x1080 (webxxl)
- **Audio:** Deutsch, Stereo

---

## Verifikation

**Video-Hash (pending):**
- MD5: ` Berechnung nach Download `
- SHA256: ` Berechnung nach Download `

**Download-Integrität:**
- Dateigröße erwartet: ~100 MB
- Dateigröße aktuell: 0 Bytes (Download in Progress)
- Status: ⏳ Läuft

---

**Letzte Aktualisierung:** 28. März 2026, 23:55 Uhr  
**Investigator:** Fabian Schüßler
