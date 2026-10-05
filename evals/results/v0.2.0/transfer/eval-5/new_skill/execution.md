# Ausführungsnachweis

## Auftrag und verwendete Eingaben

- Auftrag: `.publication/skill-evals/heldout/request-5.txt`
- Fachlicher Input: `evals/results/v0.2.0/transfer/source/T05-input.md`
- Berichtsstichtag laut Input: 21.05.2027; synthetischer Fall.

## Verwendeter Skill

- `.publication/skill-evals/candidate-v0.2.0/skills/projektstatus/SKILL.md`
- Gelesene Referenz: `.publication/skill-evals/candidate-v0.2.0/skills/projektstatus/references/beispiel.md`
- Die Referenz wurde wegen der unbegründeten grünen Bewertung im vorhandenen Entwurf und des überfälligen Kranmeilensteins herangezogen.

## Werkzeuge und Bearbeitung

- `functions.exec` zur Ausführung der Werkzeugaufrufe.
- `exec_command` mit PowerShell `Get-Content -LiteralPath ... -Raw` zum Lesen der vier oben genannten Dateien.
- `apply_patch` zum Schreiben von `outputs/output.md` und dieses Ausführungsnachweises.
- `exec_command` mit PowerShell `Get-Content` zur anschließenden Sichtprüfung der beiden geschriebenen Dateien.
- Fachliche Überarbeitung und arithmetische Ableitungen erfolgten im Modell: 14.000 / 210.000 × 100 = rund 6,7 %; 224.000 − 39.000 = 185.000 Euro. Datumsabweichungen sind in Kalendertagen angegeben.

## Grenzen und Kennzeichnung

- Verwendet wurden ausschließlich der reservierte Auftrag, dessen fachlicher Input und die genannten Dateien des erlaubten Skill-Ordners.
- Keine anderen Aufgaben, Ausgaben, Manifest-, Freeze-, Metadaten- oder Assertionsdateien wurden gelesen. Keine externe Recherche, keine Rückfragen und keine externen Schreibaktionen wurden vorgenommen.
- Die Kostenbewertung verwendet allein die vorgegebene Kostenampel. Eine Termin- oder Gesamtampel wurde nicht eingeführt.
- Abrechnungen und offene Beauftragungen wurden als unterschiedliche Kategorien ausgewiesen; vollständige Istkosten sind im Input nicht angegeben.
- Die Abschlussprognose wurde mit ihrer unbestätigten Kranabhängigkeit gekennzeichnet. Der vorgeschlagene neue Abschlusstermin wurde nicht als genehmigte Ausgangsplanung dargestellt.
- Die Frist 24.05.2027 für die Kranentscheidung stammt aus dem Input. Dieselbe Frist für die finanzielle Deckung ist ausdrücklich ein neuer Vorschlag, keine bestehende Zusage.
- Die Sichtprüfung betrifft die Übereinstimmung des Berichts mit den gelesenen Angaben und seine verständliche Darstellung. Keine unabhängige Prüfung der Quelldaten oder tatsächlichen Projektlage und keine empirische Wirkungsmessung erfolgten.

## Ergebnis

- `.publication/skill-evals/heldout/eval-5/new_skill/outputs/output.md`
- `.publication/skill-evals/heldout/eval-5/new_skill/execution.md`
