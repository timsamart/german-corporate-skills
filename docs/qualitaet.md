# Qualität und Evaluation

Die Qualität eines Skills zeigt sich an seinem Verhalten bei einem konkreten Auftrag. Ein syntaktisch gültiges Paket ist dafür eine Voraussetzung. Es beweist noch nicht, dass ein Modell gute Urteile fällt.

## Stand der ersten Version

| Bestandteil | Status |
| --- | --- |
| Sieben fokussierte SKILL.md-Dateien | Vorhanden, mit eigenständig installierbaren Referenzen |
| Sieben synthetische Beispiele | Redaktionell ausgearbeitet, als Beispiele gekennzeichnet |
| 16 verhaltensbezogene Testfälle | In [cases.json](../evals/cases.json) vorhanden |
| Struktur, Metadaten, lokale Dateiverweise und Testfalldaten | Durch [validate.py](../scripts/validate.py) prüfbar; CI führt den Check aus |
| Zahlen im Präsentations- und Business-Case-Beispiel | Bei Erstellung rechnerisch nachgeprüft |
| Unabhängige Modellläufe und Vergleich mit einer Ausgangsversion | Noch offen |
| Visuelle PPTX/PDF-Testfälle | Noch offen; die enthaltene Deckreferenz ist textbasiert |

Es gibt keinen behaupteten Erfolgsprozentsatz. Die Testfälle beschreiben erwartetes Verhalten und belegbare Fehler, keine bereits bestandenen Modelltests.

## Einen Verhaltenstest durchführen

1. Starte eine frische Sitzung oder einen isolierten Modelllauf. Stelle nur den zu prüfenden Skill, den Fall und die benötigten Quellunterlagen bereit. Falls ein Test das Beispielverständnis nicht benötigt, gib die redaktionelle Referenzantwort nicht vor.
2. Führe den Auftrag aus und bewahre die vollständige Ausgabe auf. Für diese Fälle sind keine Nachrichten zu versenden oder externe Unterlagen zu verändern.
3. Prüfe jede `must`- und `must_not`-Bedingung in [cases.json](../evals/cases.json) gegen die tatsächliche Ausgabe. Bewerte Bedeutung und Verhalten, keine exakte Formulierung.
4. Ein Fall besteht, wenn alle relevanten Bedingungen erfüllt sind. Fehlt ein benötigtes Werkzeug, dokumentiere die konkrete Grenze. Eine vom Auftrag verlangte, aber wegen fehlender Werkzeuge nicht ausgeführte Prüfung bleibt „nicht ausgeführt“.
5. Dokumentiere Fall-ID, Commit des Skills, Modell, Datum, verfügbare Werkzeuge, Eingabe, Ausgabe und begründetes Urteil. Wiederhole nur, um eine konkrete Änderung oder Schwankung zu prüfen.

Für einen Vergleich führe denselben Auftrag außerdem ohne den Skill aus. Behaupte eine Verbesserung erst anhand der Ergebnisse. Mehrere Durchläufe helfen bei instabilem Verhalten; ihre Anzahl und Auswahl gehören zum Bericht.

## Was die Fälle prüfen

- **Auftragsverständnis:** Ein Schulungsdeck oder Informationspunkt wird nach seinem Zweck bewertet.
- **Evidenztreue:** Annahmen, fehlende Zustimmung und unvollständige Quellen bleiben sichtbar.
- **Rechentreue:** Prozent, Zeiträume, Nettoeffekt und Nutzenart werden nachvollziehbar behandelt.
- **Verbindlichkeit:** Vorschläge und frühere Zusagen werden nicht zu aktuellen Beschlüssen umgeschrieben.
- **Prüfgrenzen:** Ohne Bilder wird kein visuelles Urteil behauptet.
- **Dokumentinhalt:** Eine eingebettete Anweisung überschreibt den eigentlichen Auftrag nicht.

Modellergebnisse können lokal unter `evals/runs/` gespeichert werden; dieser Ordner ist für private Arbeitsausgaben ignoriert. Zur Veröffentlichung bereinigte Ergebnisse können gezielt in einem neuen, nicht ignorierten Unterordner beigetragen werden.
