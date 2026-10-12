# Abschließende Evidenzprüfung für v0.3.0

Stand: 12. Oktober 2026. Separate Modellgegenprüfung der gespeicherten Evidenz. Dies ist weder ein menschliches Expertengremium noch eine Nutzbarkeitsbewertung durch Manager, Projektleitungen oder Consultants.

## Tatsächlich geprüfter Umfang

Die Gegenprüfung las zunächst sämtliche **21 Kandidatenausgaben** gegen die Originaleingaben, Aufträge und unveränderten Kriterien: sieben Entwicklungsfälle und 14 Transferfälle. Erst danach wurden gespeicherte `grading.json` gelesen. Die sieben später fertiggestellten Transferbewertungen wurden anschließend ebenfalls gegen ihre Originalmetadaten nachgezählt.

Entwicklung: `evals/v0.3.0/tasks.json`, alle sieben dort benannten Dateien unter `evals/v0.3.0/fixtures/` und jeweils `eval_metadata.json`, `new_skill/request.json`, `new_skill/outputs/output.md` und `new_skill/execution.md` unter `evals/results/v0.3.0/development/eval-*`.

| Entwicklungsfall | Geprüfte Quelle | Wörter / Grenze |
| --- | --- | ---: |
| 1 | deck-argument-und-lesesituation.md | 310 / 350 |
| 2 | nutzenpfad-und-doppelte-stunden.md | 275 / 330 |
| 3 | entscheidung-umfang-vor-anbieter.md | 277 / 330 |
| 4 | gremium-umsetzung-ohne-zustimmung.md | 279 / 300 |
| 5 | status-geteilte-spezialistin.md | 251 / 280 |
| 6 | protokoll-entscheidungsweg-und-nachtest.md | 191 / 300 |
| 7 | mail-sicht-und-ungeklaerte-eingaben.md | 108 / 150 |

Transfer: `evals/results/v0.3.0/transfer/source/manifest.json`, sämtliche 14 Originaldateien unter dessen `sources/` sowie jeweils `eval_metadata.json`, `new_skill/request.json`, `new_skill/outputs/output.md` und `new_skill/execution.md` unter `evals/results/v0.3.0/transfer/eval-*`.

| Transfer-ID | Geprüfte Originalquelle | Wörter / Grenze |
| --- | --- | ---: |
| v03-pr-01 | sources/v03-pr-01.md | 264 / 300 |
| v03-pr-02 | sources/v03-pr-02.md | 59 / 120 |
| v03-bc-01 | sources/v03-bc-01.md | 217 / 300 |
| v03-bc-02 | sources/v03-bc-02.md | 61 / 120 |
| v03-ev-01 | sources/v03-ev-01.md | 265 / 300 |
| v03-ev-02 | sources/v03-ev-02.md | 71 / 120 |
| v03-gv-01 | sources/v03-gv-01.md | 285 / 300 |
| v03-gv-02 | sources/v03-gv-02.md | 56 / 120 |
| v03-ps-01 | sources/v03-ps-01.md | 250 / 300 |
| v03-ps-02 | sources/v03-ps-02.md | 30 / 120 |
| v03-ep-01 | sources/v03-ep-01.md | 232 / 300 |
| v03-ep-02 | sources/v03-ep-02.md | 56 / 120 |
| v03-sk-01 | sources/v03-sk-01.md | 201 / 250 |
| v03-sk-02 | sources/v03-sk-02.md | 47 / 120 |

Die Wortzählung umfasst die vollständige jeweilige Ausgabedatei einschließlich Überschriften und Tabellen. Gezählt wurden durch Leerraum getrennte Tokens mit mindestens einem Unicode-Buchstaben oder einer Ziffer; reine Markdown- oder Interpunktionszeichen zählen nicht. Alle 21 Kandidatenausgaben liegen innerhalb ihrer ursprünglichen Grenze. Alle 21 Kandidatenaufträge stimmen mit den Originalaufgaben überein.

Zusätzlich geprüft: alle 21 Entwicklungsbewertungen der drei Vergleichsarme und alle 14 Transferbewertungen auf Kriterienidentität und konsistente Summen; die eingefrorenen Datei- und Quellenhashes; `docs/research/methods-v0.3.0.md` und die Zugriffsgrenzen der Methodenbeschreibung. Die 14 Entwicklungsantworten der Kontrollarme wurden für Wortzählungen verarbeitet, aber in dieser Gegenprüfung nicht nochmals vollständig inhaltlich gegen Quellen auditiert. Ihre Zählungen sind deshalb eine Nachzählung gespeicherter Modellurteile.

## Nachrechnung und fachliche Bindung

- **Entwicklungsdeck:** `(12 − 8,4) / 12 = 30 %`. Die Ausgabe behauptet weder gesicherte Kausalität noch Cash-Einsparung und schützt beide bestätigten Ausfälle. Ohne Renderings werden keine Layout- oder Achsenbeobachtungen behauptet.
- **Entwicklungs-Business-Case:** `12.000 × 4 / 60 = 800` Stunden; `800 × 60 = 48.000` Euro Kapazitätsäquivalent. Dieselben Stunden ergeben nicht zusätzlich 48.000 Euro Personaleinsparung. `48.000 − 12.000 = 36.000`; Jahr eins `48.000 − 30.000 − 12.000 = 6.000`. `30.000 / 36.000 = 0,83` Jahre beziehungsweise zehn Monate ist ausdrücklich ein vereinfachtes, annahmenabhängiges Kapazitätsmodell. Cash-Amortisation bleibt unbelegt.
- **Entwicklungsentscheidung und Briefing:** Die Prozessprüfung für 12.000 Euro und sechs Wochen bleibt im Prüfmandat bis 20.000 Euro. Anbieterverträge über 90.000 beziehungsweise 75.000 Euro bleiben spätere Entscheidungen. Das Briefing wahrt Pilotmandat im vorhandenen 30.000-Euro-Rahmen, gesonderte Geschäftsführungsentscheidung und den Unterschied zwischen 80 benötigten Stunden und 20 monatlich verfügbaren Stunden. Konsultation und Kalkulationsprüfung werden nicht zu Umsetzungszusagen oder Rolloutfreigaben.
- **Entwicklungsstatus:** `4 + 3 = 7` benötigte Tage bei fünf verfügbaren Tagen; mindestens zwei fehlen. A zuerst lässt einen Tag für B, B zuerst zwei für A. Die genehmigten Termine bleiben Soll; neue Termine werden nicht erfunden. Der vorgeschlagene Entscheidungstermin ist als Vorschlag bezeichnet.
- **Entwicklungsprotokoll und Mail:** Eva entscheidet nur Nord nach Beratung; Alex' Gegenposition bleibt erhalten. Tom übernimmt Lieferung am 16.10. bedingt durch Zugang bis 14.10.; Nachtestnachweis und gemeinsame Prüfung am 19.10. bleiben erhalten. Süd erhält keine erfundene Aufgabe. Die Mail erhält Anfrage vom 08.10., tatsächliche Antwort vom 09.10., fehlende Eingaben und offene Budgetentscheidung ohne neue Frist oder Zusage.
- **Transferdeck:** `14 + 12 = 26` Personentage bei 20 zugesagten Tagen; sechs fehlen. Der Pilot für 50.000 Euro ist innerhalb des 60.000-Euro-Mandats; 240.000 Euro Rollout bleiben beim Investitionsausschuss. Vier Pilotwünsche von sechs Befragten werden nicht zu nachgewiesener praktischer Akzeptanz.
- **Transfer-Business-Case:** Externe Auszahlungen `180.000 + 3 × (90.000 + 30.000) = 540.000` Euro. 130.000 Euro Personalkapazität jährlich erst ab 2028 ergeben 260.000 Euro Kapazitätswert für den Horizont, keine belegte Auszahlungseinsparung. Bedingte externe Einsparung `2 × 80.000 = 160.000`; Zahlungssaldo bei erfüllter Bedingung `−540.000 + 160.000 = −380.000`, derzeit ohne bestätigte Einsparung `−540.000`. Pilotquote 2,4 % überschreitet höchstens 2,0 %. Interne Arbeit `500 × 80 = 40.000` Euro ohne zusätzliche Auszahlung. Die Einrichtung wird entsprechend der expliziten Finanzvorgabe vollständig 2027 als Aufwand erfasst. Die zusätzlich gezeigte Ressourcenrechnung ergibt `260.000 + 160.000 − 540.000 − 40.000 = −160.000` und wird nicht als Zahlungsrückfluss ausgegeben.
- **Kleine Transferpreisprüfung:** A `1.280 + 200 = 1.480`, B `4 × 350 + 200 = 1.600` Euro netto für dasselbe eine Jahr; A ist um 120 Euro günstiger. Keine zusätzlichen Nutzenpositionen oder Bewertungsprogramme werden erfunden.
- **Transferarchitektur:** Das Board wählt B unter Bedingungen; es ersetzt weder Investitionsfreigabe von 60.000 Euro noch Datenschutz oder 0,5 zusätzliche Vollzeitäquivalente. Die Verlängerung A für 15.000 Euro bis 31. Januar bleibt Empfehlung an die befugte Projektleitung bis 31. Oktober. Übergang und Umsetzung zusammen `15.000 + 60.000 = 75.000`, zusätzliche Personalkosten offen. Rückmeldung am 1. November, Investitionsausschuss am 5. November und sechs Wochen Umsetzung ab freigegebenem Start bleiben erhalten.
- **Transfersitzung:** Originalentwurf `15 + 12 + 12 + 10 = 49` Minuten, vier Minuten zu lang. Nach reservierten 15 Minuten bleiben 30 statt benötigter 34. Ersatzagenda `15 + 10 + 8 + 9 + 3 = 45` Minuten ist korrekt. Tests `3 + 3 = 6` Personentage bei vier verfügbaren Tagen; Priorisierung A verwendet drei und lässt einen Reserve-Tag. Sechs protokollierte Tests werden von zwei ungetesteten Anbieterbestätigungen getrennt. Vertrag und Haftung bleiben Empfehlung an Finanzleitung/Recht vor 20. November, 17:00 Uhr.
- **Transferstatus:** `8 − 2 = 6` fehlende Personentage; Dienstleistung `6 × 1.200 = 7.200` Euro netto; zusätzlicher Bedarf `7.200 − 2.000 = 5.200`. Dieser überschreitet das Sponsorlimit von 5.000 um 200 Euro und benötigt Bereichsfreigabe. Rot folgt der gelieferten Definition; Bestellung bis 15.10., 12:00 Uhr, Zugang am 16.10. und Terminprognose bleiben bedingt. 10:00 Uhr ist ausdrücklich ein vorgeschlagener interner Entscheidungstermin.
- **Transferprotokoll und Kundenantwort:** Der 20. November bleibt internes Planungsziel; das behauptete Kundenversprechen für den 19. bleibt strittig. Security-Prüfung am 18.11. hängt von vollständigen Daten bis 16.11., 12:00 Uhr ab. Nur die abwesende Nora darf 12.000 Euro über dem 10.000-Euro-Mandat freigeben; ihr Antworttermin und Toms Klärungstermin bleiben offen. Die Kundenmail erhält beide Produktivstartbedingungen, `50.000 + 30.000 = 80.000` Euro netto für das erste Jahr, Ausschlüsse, bestehendes Update am 21.11. sowie eine belegte Demonstrationsoption am 1.12. ohne produktive Kundenaktenprüfung.

In diesen 21 gelesenen Kandidatenantworten wurde keine materielle erfundene Freigabe, Befugnis, Zuständigkeit, verbindliche Zusage, Cash-Einsparung oder visuelle Beobachtung gefunden. Dies ist eine Beobachtung der benannten Antworten, keine allgemeine Zuverlässigkeitsgarantie.

Die sieben kleinen Transferfälle `*-02` bleiben bei Raum-Anleitung, Preisnotiz, bestehendem Wiki-Entscheid, Informationszweck, zwei Teamchat-Sätzen, drei Protokollpunkten beziehungsweise Raummitteilung. Sie führen keine unnötige Gremienbefassung, erneute Freigabe, Risikoanalyse oder umfassende Planung ein. Die Entwurfskennzeichnung im kleinen Protokoll ist überflüssig, erzeugt aber kein formales Abnahmeverfahren.

## Erhaltene Fehlstellen und semantische Grenzen

1. **Entwicklungsdeck, Kriterium 3, nicht kritisch:** Die Ausgabe begründet die Verdichtung für die Vorabunterlage und erhält beide Ausfälle, erklärt jedoch nicht ausdrücklich den unterschiedlichen Bedarf gegenüber Monitoring. Das zusammengesetzte Kriterium bleibt mit 4/5 bewertet. Sein Maßstab ist mehrdeutig: Zweckgerechte Verdichtung kann bereits als Unterscheidung verstanden werden; der konservative Grader verlangt eine explizite inhaltliche Erläuterung. Weder Kriterium noch Antwort wurden geändert.
2. **Transfer v03-gv-01, Kriterium 1, kritisch:** Die neue Agenda passt korrekt in 45 Minuten, die originale Überziehung von 34 gegenüber 30 Minuten beziehungsweise vier Minuten wird in der Antwort jedoch nicht diagnostiziert. Diese bestätigte Auslassung muss im Qualitätsbericht bleiben. Ein korrekt reparierter Zeitplan beweist nicht, dass beide Teile des Kriteriums erfüllt wurden; 5/6 und 3/4 kritische Kriterien bleiben bestehen. Es ist keine falsche Dauerbehauptung.
3. **Transfer v03-sk-01, Kriterium 3, kritisch:** Die Mail bezeichnet 80.000 Euro als unverbindliche Schätzung, nennt Jahr eins, Netto, Integration/Lizenz, Ausschlüsse und das fehlende verbindliche Angebot. Sie sagt jedoch nicht ausdrücklich, dass die Schätzung selbst noch nicht freigegeben ist. Unter der eingefrorenen Prüfung aller Bestandteile bleibt dies eine Auslassung: 5/6 und 2/3 kritische Kriterien. Die semantische Grenze ist offenzulegen, da der Auftrag zugleich unnötige interne Details vermeiden soll und die Antwort die fehlende Verbindlichkeit klar mitteilt. Es liegt kein erfundener Endpreis und keine unbefugte verbindliche Zusage vor.

## Nachgezählte gespeicherte Modellurteile

Alle 35 Bewertungsdateien sind vorhanden. Kriterien stimmen mit den jeweiligen ursprünglichen Metadaten überein; gespeicherte Pass-/Fehl-/Gesamtsummen sind intern konsistent. Entwicklungsmetadaten stimmen mit `tasks.json`, Transfermetadaten mit dem eingefrorenen Originalmanifest überein.

| Teil / Konfiguration | Fälle | Alle Kriterien im Fall erfüllt | Einzelkriterien | Kritische Kriterien | Alle kritischen Kriterien im Fall erfüllt |
| --- | ---: | ---: | ---: | ---: | ---: |
| Entwicklung, v0.3.0 | 7 | 6/7 | 34/35 | 21/21 | 7/7 |
| Entwicklung, v0.2.0 | 7 | 5/7 | 33/35 | 21/21 | 7/7 |
| Entwicklung, ohne Corporate-Skill | 7 | 4/7 | 32/35 | 21/21 | 7/7 |
| Reservierter Transfer, nur v0.3.0 | 14 | 12/14 | 74/76 | 41/43 | 12/14 |

„Kritisch“ ist eine Kriterienmarkierung; ihre Nichterfüllung ist nicht automatisch eine falsche Tatsachenbehauptung. Die zwei kritischen Transferauslassungen dürfen weder als vollständig bestandener kritischer Transfer noch als zwei erfundene Zusagen beschrieben werden. Die Kontrollarmzahlen wurden hier nachgezählt, nicht vollständig neu inhaltlich bewertet. Ein zusätzlicher erfüllter Entwicklungspunkt gegenüber v0.2.0 belegt keine allgemeine Überlegenheit. Im Transfer fehlen Vergleichsarme.

## Integrität und Quellenzugriff

SHA-256 wurde gegen `evals/results/v0.3.0/freeze.json` geprüft. **28/28 aktuelle Skilldateien, 28/28 Kandidatenkopien, 21/21 v0.2.0-Baselinedateien und 8/8 Entwicklungsdateien** stimmen überein. Die tatsächlichen Inventare der drei Skillverzeichnisse haben exakt 28, 28 und 21 Dateien, ohne zusätzliche oder fehlende Einträge. Gegen den Transferfreeze stimmen **15/15 Originaldateien**: Manifest und 14 Quellen. Der Hash dieses Freeze-Dokuments entspricht dem im Kandidatenfreeze gespeicherten Wert. Der Transferfreeze vom 11.10.2026, 23:47:10 UTC liegt vor dem Kandidatenfreeze vom selben Tag, 23:49:23 UTC. Das belegt die erhaltene Dateifassung und zeitliche Reihenfolge der Aufzeichnungen; es beweist keine erzwungene Zugriffstrennung.

`python scripts/validate.py` wurde ausgeführt und meldete sieben Skills, lokale Referenzen und 16 validierte Evaluationsspezifikationen. Das ist Strukturprüfung und führt keine Modelltests aus. Die Zahl 16 wird nicht als Umfang der 21 neuen Kandidatenläufe interpretiert.

`docs/research/methods-v0.3.0.md` behauptet keine vollständige Buchlektüre. Es benennt öffentliche HTML-Erklärungen, Kapitelzusammenfassungen, Glossar, zwei Seiten einer adaptierten Contracting-Checkliste und Leseproben. Der fehlgeschlagene Wiederabruf von Ward/Daniel Kapitel 4 am 12.10. wird ausdrücklich genannt. Redaktionelle Anwendung, fiktive Beispiele und Methodenbezug werden von Wirksamkeitsbeweis getrennt. Diese Gegenprüfung überprüft diese **Zugriffsbehauptungen und ihre Begrenzung im Dokument**; sie hat die Webabrufe oder kompletten Bücher nicht wiederholt.

## Enges Veröffentlichungsurteil und Grenzen

Die gelesenen Antworten und erhaltenen Hashes tragen eine begrenzte, transparente Veröffentlichung dieser Fassung mit den oben genannten Fehlstellen. Ein Anspruch auf vollständiges Bestehen aller kritischen Transferbedingungen wird nicht getragen. Der Kandidat wurde nicht verändert; Kriterien und Ausgaben wurden nicht repariert, um die Zählung zu verbessern.

Alle Fälle sind synthetisch; ein Lauf je Konfiguration ist keine Wiederholungs- oder Häufigkeitsstudie. Separate Modellkontexte bleiben Modellurteile. Die gelesenen Zugriffslisten sind Selbstberichte in gemeinsamer Dateiumgebung, keine vollständigen Tooltraces oder erzwungene OS-Isolation. Exakter Modellbezeichner, Sampling, Tokens und Laufzeit sind im Freeze als unbekannt aufgeführt und wurden nicht ergänzt. Automatische Skillauswahl, native Officeformate, echte Unternehmensarbeit und menschliche Nutzbarkeit werden aus diesem Audit nicht abgeleitet. GitHub-Veröffentlichung oder Installation einer öffentlichen v0.3.0-Fassung wurde in diesem Audit nicht durchgeführt.

## Abgleich der öffentlichen Evidenz

Nach Fertigstellung wurden `docs/qualitaet.md`, `evals/results/v0.3.0/README.md`, die öffentlichen Summen in `summary.json` und ein umgestellter Transferauftrag gelesen. **70/70 öffentliche Ausgaben- und Bewertungsdateien** stimmen per SHA-256 mit ihren privaten Originalen überein: je Ausgabe `outputs/output.md` und `grading.json` für alle 35 Läufe. Der öffentliche Auftrag verwendet ausdrücklich Repositorypfade statt lokaler Rechnerpfade; der vollständige Umstellungsprozess aller Zugriffslisten wurde hier nicht zusätzlich neu durchgeführt.

Die öffentliche Qualitätstabelle und `summary.json` entsprechen der unabhängigen Nachzählung: 34/35, 33/35 und 32/35 Entwicklungskriterien sowie 74/76 und 41/43 kritische Transferkriterien. Auch die 14 Entwicklungsantworten der Kontrollarme liegen innerhalb ihrer Wortgrenzen; damit ist die Angabe **35/35 Ausgaben innerhalb der Wortgrenze** durch die lokale Nachzählung gestützt.

Die Qualitätsprosa erhält Deckmehrdeutigkeit, ursprünglichen Zeitüberhang, fehlenden expliziten Freigabestatus der Kostenschätzung und dessen Spannung zum Kundenauftrag. Sie begrenzt die Aussage zur Gegenprüfung auf Modellurteile und die tatsächlich gelesenen Kandidatenantworten; sie behauptet keine Vollbuchlektüre, allgemeine Überlegenheit, menschliche Nutzbarkeitsfreigabe oder bereits erfolgte öffentliche v0.3.0-Installation. Die Downloadpaket- und Instruktionsreviewnachweise sind zusätzliche Arbeiten anderer Kontexte; sie wurden in diesem Audit nicht vollständig erneut ausgeführt.

Für die hier geprüften Quellen-, Ausgabe-, Bewertungs- und Integritätsaussagen besteht nach diesem Abgleich kein weiterer materieller Widerspruch. Das Veröffentlichungsurteil bleibt auf transparente Bereitstellung dieses synthetischen Materials mit seinen bestätigten Fehlstellen beschränkt.

Bei der Veröffentlichung wurden ausschließlich Arbeitspfade auf die entsprechenden öffentlichen Evidenzpfade umgestellt. Urteile, Zahlen und Befunde bleiben erhalten.
