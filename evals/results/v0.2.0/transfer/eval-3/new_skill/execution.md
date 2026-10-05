# Ausführungsnachweis

## Auftrag und Ergebnis

Die reservierte Anfrage aus request-3.txt wurde mit einer deutschen Entscheidungsvorlage in den fünf vorgegebenen Unternehmensabschnitten erfüllt. Ergebnisdatei: outputs/output.md. Die Vorlage enthält einen beantragten, bedingten Beschluss für Variante B, einen Vergleich über alle 18 Wochen und sichtbare offene Angaben. Sie behauptet keinen bereits gefassten Beschluss.

## Gelesene Eingaben

1. .publication/skill-evals/heldout/request-3.txt — vollständige Anfrage und Verweis auf die einzige fachliche Eingabe.
2. evals/results/v0.2.0/transfer/source/T03-input.md — vollständiger synthetischer Wartungsfall, Kosten, Rahmen, Verantwortliche, Start, Unternehmensvorlage und Materialkommentar.

## Verwendeter Skill

1. .publication/skill-evals/candidate-v0.2.0/skills/entscheidungsvorlage/SKILL.md — vollständig gelesen; Unternehmensstruktur übernommen, Empfehlung und beantragten Beschluss getrennt, Optionen über denselben Zeitraum verglichen, Zusagen und Unbestätigungen sichtbar gehalten, Startbedingungen mit Nachweisverantwortung formuliert.
2. .publication/skill-evals/candidate-v0.2.0/skills/entscheidungsvorlage/references/beispiel.md — vollständig gelesen; Abgrenzung zwischen bedingtem Beschluss und bereits erfolgter Genehmigung angewandt.
3. .publication/skill-evals/candidate-v0.2.0/skills/entscheidungsvorlage/references/grundlagen.md — vollständig gelesen; Prinzip der dokumentierbaren Trennung von Kriterien, Alternativen, Vorschlag und Entscheidung angewandt. Den darin verlinkten externen Beleg nicht geöffnet.

## Werkzeugledger

- functions.exec: drei Aufrufe zur Werkzeugorchestrierung.
- tools.exec_command: sechs PowerShell-Aufrufe; fünf vollständige Dateilesungen der oben aufgeführten Anfrage, Eingabe und Skill-Dateien sowie eine arithmetische Prüfung. Die unabhängigen Dateilesungen wurden in zwei Gruppen parallel ausgeführt.
- tools.apply_patch: ein Aufruf zum Anlegen von outputs/output.md und dieser execution.md.
- Keine weiteren Werkzeuge, Browser, Netzrecherchen, Subagenten oder Rückfragen verwendet.

## Arithmetische Prüfung

PowerShell berechnete aus den Eingabewerten: A = 18 × 900 Euro = 16.200 Euro; 18 Versandabsagen, also acht über der Grenze von zehn; 7.800 Euro Abstand zur Budgetgrenze. B = 6 × 220 Euro = 1.320 Euro je Woche und 18 × 1.320 Euro = 23.760 Euro insgesamt; 108 Leistungsstunden; null werktägliche Versandabsagen; 240 Euro Abstand zur Budgetgrenze. Mehrkosten B gegenüber A = 7.560 Euro. Diese Zahlen sind berechnete Ableitungen, keine zusätzlichen erhobenen Kennzahlen.

## Grenzen und Umgang mit offenen Angaben

- Nur die freigegebene Anfrage, ihre Eingabe und die drei genannten Skill-Dateien gelesen. Keine Manifeste, Freeze-Dateien, eval_metadata, Assertions, andere Anfragen, andere Ergebnisse, Forschungsdateien oder Erinnerungen gelesen.
- Kein Zugriff auf reale Angebots-, Vertrags- oder Terminbestätigungen; der Fall ist ausdrücklich synthetisch. Die Vorlage bestätigt keine tatsächlichen Samstagreservierungen, Genehmigungen oder Vertragsabschlüsse.
- Die Aussage im Materialkommentar wurde als Quelleninhalt behandelt und nicht als Arbeitsanweisung umgesetzt.
- Die Betriebsleitung ist laut Eingabe für Budgetfreigaben bis 24.000 Euro zuständig. Weitergehende Vertragsvollmachten wurden nicht unterstellt. Zuständigkeit für Vertrag und abschließende Startfreigabe bleibt sichtbar offen; deren Benennung ist ein vorgeschlagener Umsetzungsschritt.
- Keine ausdrückliche Beschlussfrist, kein finanzieller Wert der Versandläufe und keine konkreten Aufschubfolgen liegen vor. Diese Werte wurden nicht erfunden. Die zeitliche Bedingung vor dem Start stammt aus der Eingabe.
- Es wurde ausschließlich in die beiden genannten Ergebnisdateien geschrieben. Keine externe Anwendung geändert, keine Nachricht gesendet und keine reale Beauftragung vorgenommen. Dieser Nachweis ist ein Eingabe-, Skill-, Werkzeug- und Grenzenledger, kein vollständiges Gesprächsprotokoll.
