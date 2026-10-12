# Wie diese Skills entstehen

Ein Skill hält wiederkehrende Arbeitsurteile fest: was zu prüfen ist, welche Aussagen ein Beleg trägt und welches Ergebnis der Nutzer braucht. Ein langer Prompt und ein Quellenverzeichnis allein beantworten noch nicht, ob er funktioniert.

## 1. Auftrag und Portfolio

Zielgruppe sind Führungskräfte, Projektleitungen und Consultants im deutschsprachigen Unternehmensalltag. Die sieben Jobs bilden eine Arbeitskette: Unterlagen prüfen, wirtschaftliche Aussagen kontrollieren, eine Entscheidung formulieren, die Sitzung vorbereiten, Fortschritt berichten, Ergebnisse festhalten und Beteiligte verständlich ansprechen.

Das gewünschte Artefakt trennt die Skills. Ein Foliensatz, eine Beschlussvorlage und ein gesprochenes Briefing können dasselbe Thema behandeln und benötigen trotzdem unterschiedliche Arbeit. Regulatorische Fachprüfungen, automatischer Versand und organisationsspezifische Geschäftsordnungen sind eigene Aufgaben.

## 2. Recherchieren und Grenzen prüfen

Die [Rechercheberichte](research/README.md) enthalten datierte Primärquellen, tatsächlich eingesehene Materialien, Gegenargumente und Zugriffsgrenzen. Verwaltungsmethoden, Lernstudien und Darstellungsempfehlungen haben jeweils ihren eigenen Geltungsbereich. Eine Übertragung auf Unternehmensarbeit wird als Designentscheidung behandelt.

Beispiel eines entscheidenden Konflikts: Einfacher Stil kann das Entfernen von Modalwörtern nahelegen. „Wir könnten liefern, falls …“ enthält aber eine Bedingung und Unsicherheit. Die Überarbeitung muss diese Bedeutung erhalten. Ebenso kann freie Arbeitszeit wertvoll sein, ohne eine zahlungswirksame Einsparung zu ergeben.

## 3. Schlank entwerfen

Jeder Ordner ist eigenständig installierbar. Die Beschreibung nennt Job und Auswahlgrenzen. SKILL.md enthält die wesentlichen Arbeitsregeln. Vertiefung, ein durchgerechnetes Beispiel und Quellen stehen in bedarfsgerecht verlinkten Referenzen. Unternehmensvorgaben und der konkrete Nutzerauftrag bestimmen Form und Umfang.

Die Änderungen gegenüber v0.1.0 behandeln plausible Fehlermuster aus der Quellen- und Instruktionsanalyse. Das sind zunächst Hypothesen über besseres Verhalten, keine bereits beobachteten Modellverbesserungen.

## 4. Fälle und Bewertungsregeln festlegen

Die [Entwicklungsaufträge](../evals/tasks.json) enthalten vollständige synthetische Eingaben, begründbare Sollmerkmale und kritische Fehlertypen. Vor der Ausführung werden Eingaben, Kandidat und Ausgangsversion per SHA-256 eingefroren. Eine zweite Person oder ein separater Modellkontext sollte Zahlen und Bewertungsregeln prüfen.

Kritische Fehler sind etwa eine erfundene Freigabe, eine neue Lieferzusage, ein falscher Nettoeffekt oder das Übergehen einer Bedingung. Gute Überschriften gleichen sie nicht aus. Ein striktes Wortlimit wird als Nutzbarkeitsmerkmal separat beurteilt.

## 5. Frisch ausführen und vergleichen

Ausgangsversion und Kandidat bearbeiten identische Aufträge mit denselben Eingaben und verfügbaren Werkzeugen. Die ausführenden Kontexte erhalten weder Bewertungsantworten noch frühere Ergebnisse. Das explizite Laden eines Skills testet dessen Anwendung. Es beweist keine automatische Auswahl durch einen bestimmten Agenten.

Separate Auswahltests mit allen Beschreibungen sind eine Annäherung an Routing. Erst ein beobachteter Hostlauf kann zeigen, welcher Skill tatsächlich geladen wurde. Ein Vergleich mit v0.1.0 beantwortet außerdem nicht, ob ein Skill besser als derselbe Auftrag ganz ohne Corporate-Skill ist.

## 6. Ausgaben prüfen und überarbeiten

Prüfe Kriterien semantisch und belege jedes Urteil mit der Ausgabe. Ein separater Grader darf eine besonders ausführliche Antwort nicht allein wegen ihrer Länge bevorzugen. Kontrolliere entscheidende Rechnungen zusätzlich deterministisch. Bei Fehlern unterscheide Skillregel, Werkzeuggrenze, unklare Eingabe und fehlerhafte Bewertung.

Der Review zeigt tatsächliche Ausgaben. Modelldiagnosen sind keine Nutzerinterviews oder Zustimmung von Fachleuten. Praxisfeedback von echten Vertretern der Zielgruppe bleibt eine eigene Evidenzquelle.

## 7. Reservierte Transferfälle

Neue Fälle werden von einem separaten Autor erstellt und bleiben bis zur Kandidatenfixierung unbekannt. Ihre Ergebnisse dürfen nicht zur stillen Anpassung desselben Kandidaten dienen. Werden daraufhin Änderungen vorgenommen, wandern diese Fälle in die Entwicklungssuite und für einen neuen Transfernachweis werden neue Fälle benötigt.

## 8. Öffentlich dokumentieren und pflegen

Veröffentliche Version, Eingaben, Ausgaben, begründete Bewertungen und verbleibende Fehler. Berichte kleine synthetische Stichproben mit ihren tatsächlichen Fallzahlen; daraus folgt keine allgemeine Erfolgsquote. Paketprüfung, Installation, Verhaltensprüfung, Auswahl und Praxistauglichkeit bleiben getrennte Nachweise.

Der [Qualitätsbericht](qualitaet.md) dokumentiert, welche Schritte tatsächlich ausgeführt wurden. Neue reale Fehlermuster kommen als autorisierte, anonymisierte Regressionen hinzu. Eine Änderung wird erst nach den für sie relevanten Prüfungen veröffentlicht.

## Vertiefung in v0.3.0

Die [Buchanalyse](research/books-for-next-version.md) führte zu [sieben gezielten Arbeitsweisen](research/methods-v0.3.0.md). In die Instruktionen wurden nur redaktionelle Anwendungen tatsächlich eingesehener Erklärungen, Artikel, Zusammenfassungen und Leseproben übernommen. Vollständige Bücher und unzugängliche Vorlagen wurden nicht als gelesen ausgegeben.

Die Instruktionsgegenprüfung korrigierte vier konkrete Punkte vor dem Einfrieren: gezielte Deckaufträge bleiben gezielt; ein Kapazitätsunterschied allein beweist keine ungeeignete Investition; Aufgaben können unter belegtem Mandat wirksam zugewiesen werden; ein Statusbeispiel bewahrt Möglichkeit statt einer neuen Zusage. Eine sprachliche Entwurfskorrektur wurde ebenfalls aufgenommen.

Der Vergleich nutzt die unveränderte v0.2.0-Fassung, den eingefrorenen Kandidaten und identische Aufträge ohne Corporate-Skill. Pro Skill kamen zwei separat erstellte reservierte Fälle hinzu, darunter ein kleiner Auftrag als Gegenprobe gegen unnötige Verfahren. Die [Nachweise](../evals/results/v0.3.0/README.md) trennen ausgeführte Antworten, Bewertungen und noch offene Praxisvalidierung.
