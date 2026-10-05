# Ausgeführte Evaluation: v0.2.0

Datum: 5. Oktober 2026. Vollständig synthetische Daten. Der [Qualitätsbericht](../../../docs/qualitaet.md) erläutert die Ergebnisse; [summary.json](summary.json) zählt die gespeicherten Bewertungen nach.

## Versuchsaufbau

| Teil | Umfang | Aussage |
| --- | --- | --- |
| Entwicklung | 7 Aufgaben × 3 Konfigurationen = 21 Ausgaben | Vergleich von v0.1.0, eingefrorenem Kandidaten und gleichem Prompt ohne Corporate-Skill |
| Reservierter Transfer | 7 neue Aufgaben × Kandidat = 7 Ausgaben | Weitere Anwendung auf beim Einfrieren unbekannte Fälle; kein vergleichender Transfernachweis |
| Auswahl | 28 Prompts × 2 Beschreibungssätze | Modellbasierte Annäherung an Skillauswahl; keine tatsächliche automatische Hostauswahl |
| Graderkontrollen | 3 einfache Paare mit insgesamt 6 semantischen Urteilen; ein Paar in zwei Reihenfolgen verglichen | Erkennen verlorener Bedingungen, falscher Freigabe und überflüssiger Wiederholung; keine menschliche Kalibrierung |

Die 28 Aufgabenausgaben bearbeiten **14 unterschiedliche Aufträge**, jeweils einmal pro Konfiguration. Es gab keine Wiederholungen zur Messung von Stabilität. [benchmark.json](benchmark.json) enthält ausschließlich die Entwicklungsergebnisse; Transferfälle werden getrennt gezählt. Der dortige Mittelwert gewichtet Aufgaben gleich und ist keine allgemeine Erfolgsquote.

## Konfigurationen

- `old_skill`: vollständiger Skillordner aus [v0.1.0](https://github.com/timsamart/german-corporate-skills/releases/tag/v0.1.0), Commit `6b982909e758d820cae87c703de49b0df8c9cd8c`. Alle 14 Dateien wurden vor dem Vergleich bytegenau gegen diesen Commit geprüft.
- `new_skill`: eingefrorener v0.2.0-Kandidat mit 21 Dateien. Die Hashes stehen in [freeze.json](freeze.json). Die veröffentlichte Skillfassung entspricht diesen Dateien.
- `without_corporate`: identischer Auftrag und Eingaben mit den gleichen verfügbaren Werkzeugen, ohne Lesen dieser Corporate-Skillinstruktionen.

Ausführung: Codex-Kollaboration mit frischen Subagentkontexten pro Aufgabe, geerbter aktiver Modellkonfiguration, denselben verfügbaren PowerShell-/Python-/Bildwerkzeugen. Der genaue Modellbezeichner und Samplingparameter wurden vom Harness nicht offengelegt. Es wurden keine Werte dafür erfunden. Die Leseregel gestattet nur Auftrag, zugehörige Eingaben und gegebenenfalls den ausgewählten Skill samt Referenzen.

Das ist eine Gesprächskontextgrenze und eine per Anweisung umgesetzte Dateigrenze. Die Dateien liegen in einer gemeinsamen Umgebung. Eine durch Betriebssystemrechte erzwungene Trennung wurde nicht eingerichtet. Die ausführenden Agenten dokumentieren ihre tatsächlichen Quellen und Werkzeuge in `execution.md`; diese selbst berichteten Listen ersetzen keine vollständigen Tooltraces.

## Bewertung und Kontrolle

Entwicklungsausgaben wurden für separate Grader als A/B/C beschriftet, mit pro Aufgabe rotierter Reihenfolge. Die Grader erhielten Kriterien und Quellen, ohne die Zuordnung zu Ausgangs- und Kandidatenversion. Die gespeicherten Ergebnisse tragen zur Nachvollziehbarkeit wieder die ursprünglichen Konfigurationsnamen. Transferbewertungen stammen aus einem separaten Graderkontext.

Jedes Urteil enthält Kriterium, Pass/Fail und Beleg. Kriterien werden semantisch geprüft. Zusätzliche Graderkritik bleibt erhalten. Keine Bewertung wurde wegen eines ungünstigen Ergebnisses gelöscht.

Eine unabhängige Eingabenprüfung präzisierte vor der Bewertung drei Begriffe in vier Kriterien: Kapazitätsmodell statt Cashflow, Testverantwortung statt Betriebsowner, Startprognose statt Startempfehlung. Einige Ausgaben lagen zu diesem Zeitpunkt bereits vor. Der Prüfer hatte weder diese Ausgaben noch den Kandidaten gelesen. [Originalkriterien](tasks-before-amendment.json), [Änderung und Hashes](assertion-amendment.json) bleiben erhalten. Eingaben, Ausführungsaufträge und Kandidat wurden dabei nicht geändert.

Der deterministische Nachzählbefehl prüft Vollständigkeit und Bewertungsarithmetik:

```bash
python scripts/summarize_evals.py evals/results/v0.2.0
```

Das ist kein neuer Modelllauf. Fehlende Laufzeit, Tokenzahlen und vollständige Tooltraces werden als unbekannt behandelt. Wortzahlen zählen durch Leerraum getrennte Elemente mit Buchstaben oder Ziffern; reine Markdownzeichen zählen nicht.

## Dateien

- [development/](development/): Aufträge, 21 Antworten, Zugriffslisten und Kriterienurteile.
- [transfer/](transfer/): reservierte Eingaben, deren Erstellungs-/Fixierungsnachweis und 7 Antworten samt Urteilen. Nach Veröffentlichung sind diese Fälle öffentliches Entwicklungsmaterial.
- [selection/](selection/): 28 vorab zugeordnete Auswahlprompts, beide Beschreibungssätze, tatsächliche Entscheidungen und Nachzählung.
- [grader-calibration-request.json](grader-calibration-request.json) und [grader-calibration.json](grader-calibration.json): einfache Kontrollpaare und tatsächliche Urteile.
- [viewer.html](viewer.html): mit dem skill-creator-Tool erzeugte Ansicht der Antworten. Zum interaktiven Lesen lokal im Browser öffnen. Der Template-Lizenzhinweis steht in [THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md).

Bei Veröffentlichung wurden absolute Rechnerpfade in den Zugriffslisten und Metadaten zu Repositorypfaden verkürzt. Der Antwortinhalt und die Kriterienurteile wurden nicht inhaltlich überarbeitet. Die sechs gerenderten Deckseiten sind ebenfalls enthalten; [rendered-pages.json](rendered-pages.json) verzeichnet ihre Veröffentlichungshashes.

Der Transfer-Fixierungsnachweis dokumentiert den Erstellungszustand vor der Ausführung (`tests_executed: 0`). [publication.json](transfer/source/publication.json) stellt ursprüngliche Fixierungshashes und veröffentlichte Hashes gegenüber, damit eine Pfadbereinigung nicht mit einer Eingabenänderung verwechselt wird.
