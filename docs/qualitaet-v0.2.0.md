# Qualität und Evaluation

Stand: 5. Oktober 2026. Version 0.2.0 verbindet Quellenrecherche, gezielte Überarbeitung und tatsächliche Modellläufe. Die [Entstehungsschritte](skill-lifecycle.md) und [Research-Dossiers](research/README.md) dokumentieren die Grundlage.

## Was ausgeführt wurde

| Prüfung | Nachweis |
| --- | --- |
| Paket und Metadaten | Sieben eigenständige Skills; System-Skillvalidator und Repositoryvalidator ausgeführt |
| Öffentliche Installation | Skills CLI kopierte alle sieben Skills aus GitHub in ein isoliertes Windows-Testprojekt; alle 21 Dateien stimmen bytegenau mit dem ausgewerteten Kandidaten überein; [Nachweis](../evals/results/v0.2.0/installation.json) |
| Quellen und Gegenargumente | Drei Dossiers mit Primärquellen, Datum, Geltungsbereich und Zugriffsgrenzen; kurze Grundlagen in jedem Skill |
| Getrennte Reviewperspektiven | Fünf Modellkontexte, gezielte Gegenprüfung und dokumentierte Begrenzung der Regeln; [Review](review.md) |
| Vollständige Entwicklungseingaben | Sieben Aufgaben, darunter ein sechsseitiges gerendertes PDF mit absichtlich irreführendem Diagramm |
| Vergleichsausgaben | 21 frische Ausführungen: sieben identische Aufgaben jeweils mit v0.1.0, Kandidat und ohne Corporate-Skill |
| Reservierte Transferfälle | Sieben weitere Kandidatenläufe; Fälle von separatem Autor, beim Einfrieren unbekannt |
| Auswahlannäherung | 28 Prompts anhand aller Beschreibungen, jeweils für v0.1.0 und Kandidat |
| Bewertung | Separate Grader mit Quellen und belegten Einzelurteilen; sechs einfache semantische Kontrollurteile korrekt |
| Nachvollziehbarkeit | Eingaben, 28 Ausgaben, Zugriffslisten, Urteile und Hashes unter [evals/results/v0.2.0](../evals/results/v0.2.0/README.md) |

Die ursprünglichen [16 Kurzfälle](../evals/cases.json) bleiben ergänzende Regressionstestspezifikationen. Sie wurden in diesem Durchgang nicht zusätzlich als Modellläufe ausgeführt. Zwei zuvor fehlende Anhänge wurden durch vollständige Inlinequellen ersetzt.

## Ergebnisse

Die endgültige Nachzählung steht in [summary.json](../evals/results/v0.2.0/summary.json).

| Teil / Konfiguration | Alle Kriterien im Fall erfüllt | Erfüllte Einzelkriterien | Erfüllte kritische Kriterien |
| --- | ---: | ---: | ---: |
| Entwicklung, v0.2.0 | 7/7 | 35/35 | 25/25 |
| Entwicklung, v0.1.0 | 7/7 | 35/35 | 25/25 |
| Entwicklung, ohne Corporate-Skill | 5/7 | 32/35 | 23/25 |
| Reservierter Transfer, nur v0.2.0 | 7/7 | 56/56 | 35/35 |

„Kritisch“ bezeichnet vorab als besonders relevant markierte Kriterien. Ein verfehltes Kriterium kann eine ausgelassene erforderliche Angabe sein; es bedeutet nicht automatisch eine falsche Tatsachenbehauptung. Es werden Kriterienurteile gezählt, keine allgemeine Erfolgswahrscheinlichkeit.

## Was die Unterschiede bedeuten

In den Entwicklungsaufgaben liefern auch v0.1.0 und gewöhnliches Prompting überwiegend korrekte Arbeit. Die gefundenen Unterschiede betreffen konkrete Vollständigkeit und Nachvollziehbarkeit. Die gewöhnliche Deckprüfung lässt die zweijährige vereinfachte Modellamortisation aus. Das gewöhnliche Protokoll nennt den richtigen aktuellen Termin, dokumentiert aber dessen Korrektur vom Freitag und die Fundstellen nicht.

Diese Auslassungen bleiben in den Bewertungen sichtbar. Sie erlauben eine Aussage über die geprüften Antworten. Ein allgemeiner Vorteil der neuen Instruktionen gegenüber v0.1.0 oder über alle Unternehmensaufgaben wird daraus nicht abgeleitet.

## Grenzen

- **Synthetisch:** 14 unterschiedliche Aufgaben, ein Lauf je Konfiguration; keine Häufigkeitsstudie, Wiederholungsstabilität oder statistisch belastbare Allgemeinquote.
- **Modellbewertung:** Separate Kontexte bleiben Modellurteile aus demselben Ausführungsrahmen. Echte Manager, Projektleitungen und Consultants haben die Ausgaben noch nicht systematisch auf Nutzbarkeit geprüft.
- **Modellkonfiguration:** Die aktive Codex-Konfiguration wurde vererbt. Exakter Modellbezeichner, Sampling, Tokens, vollständige Tooltraces und Laufzeit wurden vom Harness nicht offengelegt.
- **Isolation:** Neue Gesprächskontexte und eine Leseanweisung; gemeinsame Dateiumgebung ohne erzwungene Zugriffstrennung. Die Zugriffslisten sind Selbstberichte.
- **Transfer:** Kandidatenläufe ohne Vergleichsarme. Nach Veröffentlichung sind die Fälle bekannt und eignen sich künftig als Regressionen.
- **Auswahl:** Beide Beschreibungssätze erfüllen die erwartete Zuordnung bei 28/28 Proxyprompts, einschließlich 7/7 negativer Fälle. Das prüft keine tatsächliche automatische Skillladung in Codex oder anderen Hosts.
- **Kriterien:** Drei Begriffe in vier Entwicklungskriterien wurden nach unabhängiger Eingabenprüfung vor der Bewertung präzisiert. Original und Änderung sind erhalten; Eingaben, Aufträge und Kandidat blieben gleich.
- **Graderkritik:** Ein Transferkriterium zum nicht erstattbaren Deposit ist durch „falls thematisiert“ zu schwach formuliert. Die geprüfte Antwort enthält den Betrag und die Konsequenz korrekt. Für zukünftige Regressionen sollte seine Nennung verbindlich geprüft werden; der ursprüngliche Fall und das Graderfeedback bleiben unverändert erhalten.
- **Werkzeuge:** Der visuelle Fall ist eine PDF. Native PPTX-Notizen, Excel-Neuberechnung und unterschiedliche Office-/Agentenhosts wurden hier nicht getestet.

## Abschließende Gegenprüfung

Ein weiterer separater Modellkontext las alle 14 Kandidatenausgaben und alle sieben Antworten ohne Corporate-Skill gegen ihre Quellen. Er zählte alle 28 gespeicherten Bewertungen nach, prüfte die 21 eingefrorenen Skilldateien sowie die dokumentierte Kriterienänderung und kontrollierte entscheidende Rechnungen. Dabei fand er keine materiell erfundene Freigabe, Zuständigkeit oder Zusage. Das ist eine Beobachtung dieser Ausgaben, keine allgemeine Zuverlässigkeitsgarantie.

| Prüflinse | Abschluss und Grenze |
| --- | --- |
| Evidenz | Zählungen, Hashes und dokumentierte Auslassungen stimmen mit den gespeicherten Nachweisen überein. |
| Logik | Gleichstand mit v0.1.0 und fehlende Vergleichsarme im Transfer bleiben sichtbar. |
| Fachliche Gültigkeit | Entscheidende Rechnungen und Verbindlichkeitsunterschiede sind in den geprüften Antworten erhalten. |
| Strategische Passung | Sieben einzeln nutzbare Arbeitsartefakte passen zur erklärten Zielgruppe. |
| Umsetzbarkeit | Eingaben, Ausgaben, Urteile und Viewer sind vorhanden; automatische Hostauswahl und weitere Officeformate bleiben ungeprüft. |
| Governance | Keine materielle erfundene Verbindlichkeit in den gelesenen Kandidatenausgaben; die gemeinsame Dateiumgebung wird offengelegt. |
| Verständlichkeit | Kriterienabdeckung und Tatsachenfehler werden unterschieden; echte Leser haben die Nutzbarkeit noch nicht bewertet. |

Alle sieben Prüflinsen unterstützen diese begrenzte Veröffentlichung, mit **mittlerer qualitativer Zuversicht**. Die Gegenprüfung war keine vollständige Wiederholung aller Quellenabrufe. Ihre konkrete Kritik am Deposit-Kriterium bleibt oben dokumentiert. Repositoryprüfung und deterministische Nachzählung sind zusätzliche Releasebedingungen.

## Nachzählen und weiterentwickeln

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python scripts/summarize_evals.py evals/results/v0.2.0
```

Diese Befehle prüfen Paket, eingefrorene Skill- und Eingabehashes sowie gespeicherte Bewertungsdaten. Git bewahrt die ausgewerteten Dateien ohne Zeilenendennormalisierung. Neue Modellläufe benötigen einen konfigurierten Agenten mit passenden Dokumentwerkzeugen. Das [Evaluationsmaterial](../evals/README.md) erklärt die Ausführung.

Der nächste belastbare Schritt sind autorisierte, anonymisierte Unterlagen aus echten Arbeitsabläufen und Feedback der Zielgruppe zu Entscheidung, Handlungsbedarf und unnötiger Leserarbeit. Daraus entstehen neue Regressionen und bei substantiellen Änderungen neue reservierte Transferfälle.
