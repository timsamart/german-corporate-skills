# Beiträge

Verbessere einen konkreten Arbeitsablauf oder ein belegbares Fehlermuster. Ein guter Beitrag zeigt den Nutzerauftrag, eine synthetische oder zur Veröffentlichung bereinigte Eingabe, das beobachtete Problem und die erwartete Verbesserung.

## Änderungen an Skills

- Halte jeden Skill auf einen Auftrag fokussiert und einzeln installierbar.
- Bewahre Quellenstatus, Zusagen, offene Angaben und explizite Nutzerwünsche.
- Ergänze nur Anleitung, die das Verhalten tatsächlich verbessert.
- Verknüpfe ein neues Beispiel oder einen Testfall mit dem Fehler, den die Änderung behebt.
- Kennzeichne ausgedachte Daten, manuelle Referenzantworten und tatsächliche Modellläufe eindeutig.

Vermeide private Namen, vertrauliche Zahlen und nicht freigegebene Unternehmensunterlagen. Beachte Nutzungsrechte an beigefügten Dateien.

## Repository prüfen

Python 3.10 oder neuer:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

Der Check bestätigt strukturelle Konsistenz. Für eine Verhaltensänderung prüfe außerdem den betroffenen Fall nach [dem Evaluationsverfahren](docs/qualitaet.md) und dokumentiere Modell, Eingabe, Ausgabe und Urteil.

Der vollständige [Entstehungsprozess](docs/skill-lifecycle.md) verbindet Quellenprüfung, schlanke Instruktionen, Vergleich, reservierte Fälle und Veröffentlichung. Vorhandene Ergebnisse lassen sich deterministisch nachzählen:

```bash
python scripts/summarize_evals.py evals/results/v0.2.0
```

Dieser Befehl prüft gespeicherte Kriterien und Zählungen. Er startet keinen neuen Modelllauf und bewertet die Bedeutung der Antworten nicht erneut. Bereits öffentliche Transferfälle sind bei einer zukünftigen Überarbeitung Entwicklungsmaterial; ein neuer Transfernachweis benötigt neue, zuvor unbekannte Fälle.

Neue Skills sollten denselben Aufnahmekriterien wie die erste Version folgen: klarer Auftrag, wiederkehrender relevanter Fehler und überprüfbares Ergebnis. Öffne für einen größeren neuen Bereich zunächst ein Issue mit einem Beispiel.
