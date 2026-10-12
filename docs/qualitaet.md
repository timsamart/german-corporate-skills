# Qualität und Evaluation

Stand: 12. Oktober 2026. Version 0.3.0 ergänzt sieben eigenständige Skills um gezielte Arbeitsweisen aus tatsächlich eingesehenen öffentlichen Erklärungen, Zusammenfassungen und Leseproben. Die [Methodennachweise](research/methods-v0.3.0.md), [Buchanalyse](research/books-for-next-version.md) und [Entstehungsschritte](skill-lifecycle.md) dokumentieren Grundlage und Grenzen. Die vollständigen Bücher wurden nicht gelesen.

Die [historische v0.2.0-Prüfung](qualitaet-v0.2.0.md) bleibt erhalten. Ihre visuellen PDF- und Auswahltests wurden in diesem Durchgang nicht wiederholt.

## Was ausgeführt wurde

| Prüfung | Nachweis |
| --- | --- |
| Instruktionen | Separate Gegenprüfung aller sieben Skillordner; konkrete Korrekturen vor dem Freeze; [Review](review.md) |
| Vergleich | Sieben neue Aufgaben mit identischen Quellen, jeweils v0.3.0, unveränderter v0.2.0 und gewöhnlichem Prompting: 21 tatsächliche Ausgaben |
| Reservierter Transfer | 14 separat erstellte Aufgaben ohne Einsicht in Kandidat oder Vorarbeiten; pro Skill ein komplexer und ein kleiner Gegenfall |
| Bewertung | Zwei separate Grader für anonymisierte Vergleichsausgaben, zwei weitere für Transfer; Quellenbelege zu jedem Einzelurteil |
| Integrität | 28 Kandidaten- und 21 Baseline-Dateien sowie originale Eingaben und Kriterien per SHA-256 eingefroren und nachgeprüft |
| Umfang | Alle 35 Ausgaben innerhalb ihres jeweiligen Wortlimits; alle sieben kleinen Transferaufträge bleiben kompakt |
| Downloadpakete | Sieben einzelne Skill-ZIPs und ein Gesamt-ZIP; archivierte Dateien stimmen bytegenau mit den ausgewerteten Skills überein; wiederholte Builds lieferten identische Hashes |

## Ergebnisse

Die [vollständigen Nachweise](../evals/results/v0.3.0/README.md) enthalten Quellen, Aufträge, Ausgaben, Zugriffslisten, Urteile und eingefrorene Skillordner. [summary.json](../evals/results/v0.3.0/summary.json) zählt die gespeicherten Urteile nach.

| Teil / Konfiguration | Alle Kriterien im Fall erfüllt | Erfüllte Einzelkriterien | Erfüllte kritische Kriterien |
| --- | ---: | ---: | ---: |
| Entwicklung, v0.3.0 | 6/7 | 34/35 | 21/21 |
| Entwicklung, v0.2.0 | 5/7 | 33/35 | 21/21 |
| Entwicklung, ohne Corporate-Skill | 4/7 | 32/35 | 21/21 |
| Reservierter Transfer, nur v0.3.0 | 12/14 | 74/76 | 41/43 |

„Kritisch“ bezeichnet vorab markierte erforderliche Kriterien. Eine Auslassung kann ein solches Kriterium verfehlen, ohne eine falsche Tatsache zu behaupten. Die Zahlen zählen Kriterienurteile dieser Antworten; sie sind keine allgemeine Erfolgswahrscheinlichkeit.

## Beobachtete Unterschiede und Auslassungen

**Auftragsklärung:** Im Gremienvergleich stellt v0.3.0 eine echte Frage, die einen engeren Piloten, keinen Start oder einen kleineren Vorbereitungsschritt zulässt. v0.2.0 und gewöhnliches Prompting fragen nach der Umsetzung des bereits festgelegten Vorhabens. Das ist der einzige zusätzliche erfüllte Vergleichspunkt gegenüber v0.2.0. Gewöhnliches Prompting lässt außerdem Entwurfskennzeichnung und Fundstellen des Protokolls aus. Alle drei Konfigurationen erfüllen sämtliche kritischen Entwicklungskriterien.

**Zusammengesetztes Deckkriterium:** Alle drei Antworten verdichten die Vorabunterlage sinnvoll, erhalten beide Ausfälle und benennen den fehlenden Bildzugriff. Sie erklären jedoch nicht ausdrücklich den anderen Informationsbedarf eines Monitorings. Dafür verfehlt jede Antwort das gesamte zusammengesetzte Kriterium. Der Grader bezeichnet die semantische Schwelle als unklar. Originalkriterium und ursprüngliche Urteile bleiben erhalten; daraus wird kein belegter Mangel der vorgeschlagenen Darstellung abgeleitet.

**Transfer, Sitzungszeit:** Die Kandidatenantwort liefert eine gültige 45-Minuten-Agenda mit den festen 15 Minuten Datenschutzinformation. Sie nennt nicht, dass der ursprüngliche Entwurf weitere 34 Minuten bei nur 30 verfügbaren Minuten verlangt. Das kritische Kriterium verbindet Reparatur und ausdrückliche Diagnose; es scheitert an der ausgelassenen Diagnose.

**Transfer, Kostenschätzung:** Die Antwort kennzeichnet 80.000 Euro netto für das erste Jahr als unverbindliche Schätzung und nennt Umfang, Ausschlüsse sowie das fehlende verbindliche Angebot. Sie sagt nicht ausdrücklich, dass die Schätzung intern noch nicht freigegeben ist. Das vorab festgelegte kritische Kriterium verlangt diese Angabe und bleibt deshalb verfehlt. Der Grader weist auf die Unterscheidung von kundenseitiger Unverbindlichkeit und internem Freigabestatus hin. Der Auftrag verlangt zugleich eine Nachricht ohne unnötige interne Details; diese Spannung bleibt als Kriterienkritik dokumentiert. Es wurde keine Freigabe oder Preiszusage erfunden.

Die [Graderkritik](../evals/results/v0.3.0/grader-feedback/) bleibt neben den Urteilen zugänglich. Kein Kriterium und keine Skillinstruktion wurde nach den reservierten Ergebnissen angepasst. Diese beiden Transferfälle sind künftig bekannte Regressionen.

## Abschließende Gegenprüfung

Ein weiterer frischer Modellkontext prüfte alle sieben Kandidaten-Vergleichsausgaben und alle 14 Kandidaten-Transferausgaben zuerst gegen ihre Quellen. Anschließend kontrollierte er Bewertungen, wesentliche Rechnungen, Verbindlichkeit, kleine Aufträge und eingefrorene Dateien. In diesem Material fand er keine materiell erfundene Entscheidungsbefugnis, Zusage, Cash-Einsparung oder Rechnung. Die beiden Transferauslassungen und die Kritik am Deckkriterium bleiben bestehen.

Der [Auditnachweis](../evals/results/v0.3.0/grader-feedback/final-audit.md) nennt den tatsächlichen Lesebereich und die Grenzen. Diese Gegenprüfung ist ein Modellurteil, keine menschliche Expertenempfehlung und keine vollständige Wiederholung der externen Quellenabrufe.

## Grenzen

- **Synthetisch und klein:** 21 unterschiedliche Aufgaben, ein Lauf je Konfiguration; keine Wiederholungsstabilität oder statistisch belastbare Allgemeinquote.
- **Starke Vergleichsarme:** v0.2.0 und gewöhnliches Prompting leisten bereits viel. Ein zusätzlicher erfüllter Vergleichspunkt belegt keinen allgemeinen Qualitätsvorsprung.
- **Transfer ohne Vergleich:** Nur der Kandidat wurde auf den 14 reservierten Fällen ausgeführt. Daraus folgt keine vergleichende Verbesserung.
- **Modellurteile:** Separate Gesprächskontexte stammen aus demselben Ausführungsrahmen. Systematische Nutzbarkeitsprüfung durch echte Manager, Projektleitungen und Consultants steht aus.
- **Isolation:** Frische Kontexte und Leseanweisungen; gemeinsame Dateiumgebung ohne erzwungene OS-Trennung. Zugriffslisten sind Selbstberichte.
- **Unbekannte Konfiguration:** Exakter Modellbezeichner, Sampling, Tokens, Laufzeiten und vollständige Tooltraces wurden nicht offengelegt und nicht erfunden.
- **Kriterien:** Mehrere Kriterien bündeln unterschiedliche Verhaltensmerkmale. Die Kritik ist dokumentiert; binäre Urteile liefern keine Teilpunkte. Mündliche Nutzbarkeit wurde am Text, nicht durch gemessene Vorträge beurteilt.
- **Quellen:** Öffentliche Artikel, Erklärungen, Zusammenfassungen und Leseproben; keine Vollbuchlektüre. Die Übertragung in Arbeitsregeln ist eigene redaktionelle Synthese.
- **Werkzeuge und Auswahl:** Dieser Durchgang nutzt Textquellen. Native PPTX-Notizen, Excel-Neuberechnung und weitere Officehosts wurden nicht getestet. Beschreibungen sind unverändert; keine neue tatsächliche automatische Hostauswahl wurde geprüft.

## Nachzählen und weiterentwickeln

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python scripts/summarize_evals.py evals/results/v0.2.0
python scripts/summarize_work_practice.py evals/results/v0.3.0
python scripts/package_release.py
```

Diese Befehle prüfen Struktur, lokale Verweise, Originalhashes, Kriterienvollständigkeit, gespeicherte Urteile und ZIP-Inhalte. Sie führen keine neuen Modelltests aus. Git bewahrt die eingefrorenen Skill- und Eingabebytes ohne Zeilenendennormalisierung. Die [Ansicht der Vergleichsausgaben](../evals/results/v0.3.0/viewer.html) lässt sich lokal im Browser öffnen.

Der nächste belastbare Schritt sind autorisierte, anonymisierte Unterlagen aus echten Arbeitsabläufen sowie Praktikerfeedback zu Entscheidung, Handlungsbedarf und unnötiger Leserarbeit. Substantielle Änderungen benötigen neue Tests und neue reservierte Fälle.
