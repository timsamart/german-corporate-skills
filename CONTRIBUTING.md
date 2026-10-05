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

Neue Skills sollten denselben Aufnahmekriterien wie die erste Version folgen: klarer Auftrag, wiederkehrender relevanter Fehler und überprüfbares Ergebnis. Öffne für einen größeren neuen Bereich zunächst ein Issue mit einem Beispiel.
