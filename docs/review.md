# Review der Sammlung

Datum: 5. Oktober 2026. Fünf getrennte Modellkontexte prüften Instruktionen und Recherche vor der Verhaltensevaluation. Sie wurden mit unterschiedlichen fachlichen Fragen beauftragt. Das ist eine methodisch angeleitete Modellprüfung, keine Begutachtung oder Empfehlung der genannten Institutionen und kein Ersatz für echte Nutzer.

## Perspektiven

| Perspektive | Methodischer Bezug | Entscheidende Frage |
| --- | --- | --- |
| Fachliche Gültigkeit | IBCS, ONS, BMF AAWU | Passt die Regel zur Darstellung oder wirtschaftlichen Fragestellung? |
| Evidenz und Messung | OpenAI-/Anthropic-Evaluation, MT-Bench | Kann die Prüfung tatsächlich die behauptete Verbesserung zeigen? |
| Betrieb und Nutzung | V-Modell XT Bund, PM²-Artefaktinventar | Entsteht ein verwendbares Ergebnis im verlangten Umfang? |
| Leser und Beteiligte | BAköV, IDS grammis | Bleiben Handlungsbedarf, Bedingungen und Verbindlichkeit verständlich? |
| Gegenprüfung | Agent Skills Spezifikation, Judge-Bias-Forschung | Könnte das Paket professionell wirken, ohne bessere Arbeit zu erzeugen? |

Die [Recherche](research/README.md) dokumentiert Quellen und Geltungsgrenzen. Die institutionellen Methoden werden als überprüfbare Bezugspunkte verwendet, nicht als Rollenimitation.

## Konflikte und Änderungen

| Frage | Befund und Entscheidung |
| --- | --- |
| Braucht jeder Balken eine Nullbasis? | Nur wenn Länge einen Gesamtwert vergleicht. Bereichsbalken und Wasserfallsegmente haben eine andere Kodierung. Die Regel wurde eingegrenzt. |
| Ist ein Nutzen ohne Cash-Einsparung wertlos? | Nein. Kapazität, Qualität und Wartezeit können legitime Ziele sein. Die Nutzenklasse muss erhalten bleiben. |
| Braucht jede kleine Rechnung eine Herkunftstabelle? | Nein. Nachvollziehbarkeit bleibt erforderlich; Form und Aufwand richten sich nach dem Fall. |
| Belegt ein Vorteil gegenüber v0.1.0 den Wert eines Skills? | Dafür ist zusätzlich derselbe Auftrag ohne Corporate-Skill erforderlich. Die Entwicklungstests enthalten diese dritte Konfiguration. |
| Reicht ein frischer Agent für isolierte Evaluation? | Er trennt Gesprächskontext. Die gemeinsame Dateiumgebung bleibt zugänglich; eine Lesegrenze wird per Harnessanweisung umgesetzt, nicht durch OS-Berechtigungen erzwungen. |

Die Methodenperspektive prüfte die drei ersten Änderungen und die eingeschränkte Evaluationsaussage anschließend erneut. Sie akzeptierte eine begrenzte Veröffentlichung mit tatsächlich ausgeführten Tests und ehrlichem Zugriffsprotokoll. Bestehender Dissens: Ein Lauf pro Fall misst keine Zuverlässigkeit; Kandidatenläufe auf Transferfällen beweisen keine vergleichende Verbesserung; Nutzbarkeit für echte Leser bleibt offen.

## Sieben Prüflinsen

Evidenz, Logik, fachliche Gültigkeit, strategische Passung, Umsetzbarkeit, Governance und Verständlichkeit wurden getrennt geprüft. Die fachlichen und redaktionellen Korrekturen sind im Kandidaten enthalten. Aussagen über Wirksamkeit sind weiterhin an die dokumentierten Ergebnisse und Grenzen gebunden. Die anfängliche Modellbewertung war überwiegend „pass/revise“, mit mittlerer qualitativer Zuversicht; es wurde keine kalibrierte Erfolgswahrscheinlichkeit berechnet.

Ein separater Gegenprüfer hat die v0.2.0-Aussagen, Zählungen, Kandidatenhashes und Ausgaben anhand der gespeicherten Ergebnisse kontrolliert. Alle sieben Prüflinsen tragen diese begrenzte Veröffentlichung; die qualitative Zuversicht ist mittel. Der [historische Prüfstatus](qualitaet-v0.2.0.md#abschließende-gegenprüfung) nennt die Nachweise und verbleibenden Grenzen.

## Revision v0.3.0, 12. Oktober 2026

Ein frischer Modellkontext prüfte alle sieben Instruktionen und Referenzen, ohne Zugriff auf die reservierten Fälle oder Vergleichsausgaben. Die Korrekturen vor dem Freeze betrafen den beauftragten Deckumfang, konsistente Kapazitätsperioden und die Grenze von Investitionsurteilen, wirksame Aufgaben unter dokumentiertem Mandat sowie eine unbelegte Zusage im bisherigen Statusbeispiel. Eine Entwurfsformulierung wurde sprachlich korrigiert.

Diese Prüfung bestätigt Instruktionskonsistenz innerhalb des geprüften Materials. Sie ist keine neue menschliche Expertenrunde und keine vollständige Prüfung der zugrunde liegenden Bücher. Die Verhaltensergebnisse und der abschließende Veröffentlichungsstatus stehen im aktuellen [Qualitätsbericht](qualitaet.md).
