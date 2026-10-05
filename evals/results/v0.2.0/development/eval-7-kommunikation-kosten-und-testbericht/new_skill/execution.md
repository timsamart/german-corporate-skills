# Ausführungsdokumentation

## Quellen

- Auftrag: `iteration-1/eval-7-kommunikation-kosten-und-testbericht/request.txt`, vollständig gelesen. Gefordert: zuerst eine verwendbare Mail an Herrn Berger in Sie-Form, maximal 160 Wörter, Kostenklärung und Testbericht vor dem 08.10.2026, keine neuen Zusagen oder Drohungen.
- Eingabe: `evals/fixtures/stakeholder-kommunikation.md`, vollständig gelesen. Verwendet wurden Gesamtbudget von 100.000 Euro, Gesamtkostenprognose von 112.000 Euro, Differenz von 12.000 Euro, fehlendes Freigabemandat, fehlender vorheriger Testbericht und die daraus folgende Unsicherheit der Startprognose.

## Skill

- `candidate-v0.2.0/skills/stakeholder-kommunikation/SKILL.md`, vollständig gelesen und angewendet: konkrete Bitte und vorhandene Frist, stabile Sachinformationen, sichtbare Unsicherheit, keine erfundene Schuldzuweisung oder Eskalationsdrohung; verwendbare Nachricht zuerst.
- Optionale Referenzen wurden nicht benötigt und nicht gelesen.

## Werkzeuge und Prüfung

- `exec_command` / PowerShell: erlaubte Auftrag-, Skill- und Eingabedateien gelesen.
- `apply_patch`: Mail und diese Ausführungsdokumentation lokal gespeichert.
- `exec_command` / PowerShell: Wortzahl der gespeicherten Mail geprüft. Ergebnis: 111 durch Leerraum getrennte Wörter einschließlich Betreff, Anrede, Gruß und Namensplatzhalter; die Grenze von 160 Wörtern ist eingehalten.
- Inhaltlich geprüft: Zahlen und Termin entsprechen der Eingabe; die Mandatsgrenze und die fehlende belastbare Startprognose bleiben erhalten. Die Vorwürfe und Drohung des Rohentwurfs wurden entfernt. Keine zusätzliche Zusage oder neue Frist ergänzt.

## Grenzen

- Grundlage ist ausschließlich der fiktive, bereitgestellte Sachverhalt; keine externe Verifikation.
- Keine weiteren Skills, Metadaten, Assertions, Recherchedateien oder fremden Ergebnisse gelesen.
- Kein Versand und keine externen Schreibzugriffe. Der Namensplatzhalter ist vor einem Versand zu ersetzen.
