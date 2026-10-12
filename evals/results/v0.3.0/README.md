# Arbeitsfälle für v0.3.0

Stand: 12. Oktober 2026. Alle Materialien sind vollständig synthetisch. Dieses Paket bewahrt die tatsächlichen Aufgabenausgaben, Quellen, Kriterien und Bewertungen. Ergebnisse und Grenzen stehen im [Qualitätsbericht](../../../docs/qualitaet.md).

## Aufbau

| Teil | Umfang | Aussagegrenze |
| --- | --- | --- |
| Entwicklung | Sieben Aufgaben × v0.3.0, v0.2.0 und gewöhnliches Prompting | Einzelne Vergleichsantworten auf dieselben Quellen und Aufträge |
| Reservierter Transfer | 14 Aufgaben × v0.3.0 | Je Skill ein komplexer und ein kleiner Gegenfall; keine Vergleichsarme |

Das sind 21 unterschiedliche Aufgaben und 35 Ausgaben, ein Lauf pro Konfiguration. Die Transferquellen und ihr Manifest wurden von einem separaten Autor ohne Lesen des Kandidaten, der Buchrecherche oder vorheriger Evaluationen erstellt und eingefroren. Der Kandidat wurde anschließend vor allen Ausführungen eingefroren. Zeitstempel und Hashes stehen in [freeze.json](freeze.json) und dem [Original-Transferfreeze](transfer/source/freeze.json). Beide verwenden UTC, die Berichte das lokale Datum in Europe/Berlin.

## Nachweise

- [Entwicklungsaufträge und vorab festgelegte Kriterien](../../v0.3.0/tasks.json); Quellen in demselben Ordner.
- [Unveränderte Transferquellen und Kriterien](transfer/source/manifest.json); alle ursprünglichen Eingabebytes bleiben erhalten.
- [Ausgewerteter Kandidat](candidate/skills/) und [v0.2.0-Baseline](baseline/skills/): vollständige Skillordner mit eingefrorenen Hashes.
- `development/eval-*` und `transfer/eval-*`: tatsächliches Ergebnis, Selbstbericht der Datei-/Werkzeugzugriffe, Ausführungsauftrag und Einzelurteile. Rechnerpfade in Aufträgen und Zugriffslisten wurden auf Repositorypfade umgestellt; Quellen, Skilldateien und Kriterien bleiben bytegenau erhalten.
- [summary.json](summary.json): deterministische Nachzählung der gespeicherten Urteile, Wortgrenzen und Datenhashes. Die Nachzählung führt keinen Agenten aus.
- [benchmark.json](benchmark.json): ausschließlich die sieben Vergleichsaufgaben, gleich je Aufgabe gewichtet; kein allgemeiner Erfolgsprozentsatz. Transfer bleibt getrennt.
- [viewer.html](viewer.html): lokal zu öffnende Ansicht der Vergleichsantworten mit Bewertungen. Erzeugt mit dem skill-creator-Viewer; [Lizenzhinweis](../../../THIRD_PARTY_NOTICES.md).
- [grader-feedback/](grader-feedback/): ursprüngliche Kriterienkritik und abschließender Quellen-/Integritätsaudit.

## Verfahren und Grenzen

Jede Ausführung verwendet einen frischen Gesprächskontext mit derselben geerbten aktiven Codex-Konfiguration und denselben verfügbaren Werkzeugen. Eine Anweisung begrenzt das Lesen auf Auftrag, Quelle und gegebenenfalls Skill samt relevanten Referenzen. Die Dateiumgebung ist gemeinsam zugänglich; es gibt keine erzwungene OS-Isolation. Zugriffsnachweise sind Selbstberichte, keine vollständigen Tooltraces.

Die Entwicklungsantworten wurden für zwei getrennte Grader als A/B/C pro Fall rotiert. Versionszuordnung, Skills und Zugriffsprotokolle gehörten nicht zu ihrem Lesebereich. Zwei weitere Grader bewerteten den Transfer. Kriterien beurteilen die gesamte geforderte Leistung anhand der bereitgestellten Quellen, nicht bestimmte Überschriften oder eine bevorzugte Formulierung. „Kritisch“ kennzeichnet besonders relevante erforderliche Kriterien; eine Auslassung kann eines verfehlen, ohne eine falsche Tatsachenbehauptung zu sein. Kein Kriterium wurde nachträglich geändert; Kritik an zusammengesetzten oder semantisch unklaren Kriterien bleibt neben den ursprünglichen Urteilen erhalten.

Exakter Modellbezeichner, Sampling, Laufzeiten, Tokens und vollständige Tooltraces wurden vom Harness nicht offengelegt und nicht geschätzt. Es gibt keine Aussage über automatische Skillladung, verschiedene Officehosts oder reale Nutzerwirksamkeit. Nach Veröffentlichung sind die Transferfälle bekannte Regressionen. Tatsächliche Praktikerbeurteilung und Wiederholungsstabilität bleiben offen.
