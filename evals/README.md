# Evaluationsmaterial

Alle Fälle sind vollständig synthetisch. Es werden keine echten Unternehmensunterlagen veröffentlicht.

- [cases.json](cases.json): 16 kompakte Regressionen, zunächst Verhaltensspezifikationen. Ihre Existenz bedeutet nicht, dass sie ausgeführt wurden.
- [tasks.json](tasks.json): sieben vollständige Entwicklungsaufträge mit Eingabedateien. Die ursprünglichen Kriterien wurden vor der Ausführung festgelegt; eine unabhängige Prüfung präzisierte vor der Bewertung drei Begriffe in vier Kriterien. [Original und Änderung](results/v0.2.0/assertion-amendment.json) sind dokumentiert.
- [fixtures/](fixtures/): vollständige Quellen der Entwicklungsaufträge. Das Deck liegt als Text, sechsseitige PDF und Bild der Diagrammfolie vor. Der irreführende Balkenvergleich ist ein absichtlicher Testfehler.
- [results/](results/): zur Veröffentlichung bereinigte Eingaben, Ausgaben und Bewertungen tatsächlich ausgeführter Läufe. Der [Qualitätsbericht](../docs/qualitaet.md) erläutert Ergebnisse und Grenzen.

## Ausführung

1. Lade nur den ausgewählten vollständigen Skillordner und den gewünschten Auftrag samt Eingaben. Für einen Vergleich ohne Corporate-Skill lasse diese Instruktionen weg; die Werkzeuge bleiben gleich.
2. Gib der ausführenden Sitzung keine Bewertungsregeln oder Referenzantworten. Starte jeden Auftrag in einem neuen Kontext.
3. Speichere die tatsächliche Ausgabe sowie beobachtbare Quellen-/Werkzeugnutzung. Nicht verfügbare Metriken bleiben unbekannt.
4. Prüfe alle Kriterien gegen die Quellen und die Ausgabe. Jeder Fehler braucht einen Beleg. Kritische Falschaussagen werden getrennt von Nutzbarkeit gezählt.
5. Vergleiche identische Aufgaben. Bewahre Gleichstände, Fehler und fehlende Prüfungen. Ein Quellenverzeichnis oder eine Installation ist kein Verhaltenstest.

Ein allgemeiner Testaufruf für Modellläufe ist bewusst nicht vorgetäuscht: Modelle und Hosts haben unterschiedliche APIs, Konfigurationen und Werkzeuge. Die gespeicherten Aufträge sind portabel; der Ausführungsrahmen muss die tatsächlich verwendete Umgebung dokumentieren.

## Übertragbarkeit

Synthetische Fälle zeigen konkrete Fähigkeit oder Fehlverhalten. Ein Lauf pro Fall prüft keine Wiederholungsstabilität. Ein unbekannter Transferfall prüft eine weitere Situation; ohne entsprechende Vergleichsarme zeigt er keine Verbesserung gegenüber anderen Instruktionen. Auswahl anhand der Beschreibungen ist eine Routingannäherung und keine beobachtete automatische Hostauswahl.

Die sinnvolle Weiterentwicklung besteht aus echten, autorisierten und anonymisierten Fehlermustern, unabhängiger menschlicher Prüfung und den dafür relevanten Wiederholungen. Veröffentliche nur tatsächlich vorhandene Evidenz.
