# German Corporate Skills

**Sieben Agent Skills für bessere Präsentationen, Entscheidungen und Zusammenarbeit im deutschsprachigen Unternehmensalltag.**

Für Führungskräfte, Projektleitungen und Consultants, die mit KI an echten Arbeitsunterlagen arbeiten: Ein Deck braucht belastbare Aussagen. Eine Entscheidung braucht klare Optionen. Nach einer Sitzung muss erkennbar sein, wer was tatsächlich zugesagt hat.

Die Skills geben einem KI-Agenten konkrete Prüfkriterien, Arbeitsabläufe und Ausgabeformen. Jeder Skill enthält ein vollständig synthetisches, nachvollziehbares Beispiel und lässt sich einzeln verwenden.

[English overview](README.en.md) · [Beispiele und Testfälle](docs/qualitaet.md) · [MIT-Lizenz](LICENSE)

## Der schnellste Einstieg: ein Deck prüfen

Installiere den Skill und gib ihm dein Deck mit Zielgruppe und gewünschtem Ergebnis:

```text
$praesentations-review
Prüfe diese Präsentation für unseren Lenkungsausschuss.
Wir haben zehn Minuten und beantragen die Freigabe eines Piloten.
Nenne die entscheidenden Schwächen mit Foliennummer und konkreter Änderung.
```

Ein nützliches Review sieht beispielsweise so aus:

| Im fiktiven Deck | Was das Review feststellt |
| --- | --- |
| „40 % weniger Zeit“, von 12 auf 8,4 Minuten | Das sind 30 %. Die Aussage muss den Testumfang erhalten. |
| „450.000 Euro Einsparung jährlich“ | Die Eingaben ergeben 135.000 Euro potenzielles Kapazitätsäquivalent. Eine finanzielle Einsparung braucht einen Realisierungsmechanismus. |
| „Amortisation nach sechs Monaten“ | Das vereinfachte Kapazitätsmodell ergibt bei vollem Jahresnutzen 1,6 Jahre. Eine Anlaufphase verändert das Ergebnis. |
| „Freigabe erteilt“, in der Notiz „Prüfung offen“ | Der Status ist widersprüchlich und muss belegt werden. |
| „Loslegen“ als letzte Folie | Umfang, Mittel und Bedingungen des gewünschten Beschlusses fehlen. |

Das [vollständige Beispiel mit sechs Textfolien und Review](skills/praesentations-review/references/beispiel.md) zeigt Eingabe, Rechnung, priorisierte Befunde und eine vorgeschlagene Beschlussfolie.

## Die Sammlung

| Skill | Typischer Auftrag | Ergebnis |
| --- | --- | --- |
| [Präsentationsreview](skills/praesentations-review/SKILL.md) | „Kann dieses Deck die gewünschte Entscheidung tragen?“ | Priorisierte Befunde, konkrete Folienänderungen, offene Nachweise |
| [Business Case prüfen](skills/business-case-pruefung/SKILL.md) | „Trägt diese Wirtschaftlichkeitsrechnung?“ | Überprüfbare Rechnung, Nutzenarten, kritische Annahmen und Sensitivitäten |
| [Entscheidungsvorlage](skills/entscheidungsvorlage/SKILL.md) | „Bereite eine belastbare Entscheidung vor.“ | Beschlusssatz, vergleichbare Optionen, Empfehlung und Bedingungen |
| [Gremienvorbereitung](skills/gremienvorbereitung/SKILL.md) | „Welche Fragen werden entscheidend und was kann ich beantworten?“ | Kurzer Einstieg, sachliche Einwände, Antworten mit Beleglage |
| [Projektstatus und Eskalation](skills/projektstatus/SKILL.md) | „Was muss das Management jetzt wissen oder entscheiden?“ | Soll/Ist/Prognose, Auswirkungen und konkrete Bitte um Unterstützung |
| [Ergebnisprotokoll](skills/ergebnisprotokoll/SKILL.md) | „Was wurde beschlossen und wer hat was zugesagt?“ | Beschlüsse, bestätigte Maßnahmen und offene Vorschläge |
| [Stakeholder-Kommunikation](skills/stakeholder-kommunikation/SKILL.md) | „Formuliere diese Nachricht klar und diplomatisch.“ | Verwendbarer Entwurf mit präziser Bitte und unverändertem Sachverhalt |

Die Skills folgen einer Arbeitskette: prüfen, entscheiden, besprechen und nachhalten. Wähle den Skill für das aktuelle Ergebnis. Du kannst beispielsweise erst den Business Case prüfen und die korrigierte Grundlage anschließend in eine Entscheidungsvorlage überführen.

„German“ bezeichnet hier Sprache und Arbeitsartefakte: Vorstand, Geschäftsführung, Lenkungsausschuss, Fachbereich und Projektarbeit. Unternehmensvorlagen und tatsächliche Entscheidungswege haben Vorrang. Die Kriterien sind redaktionelle und praktische Arbeitskonventionen dieser Sammlung.

## Installation

Die Ordner verwenden das offene [Agent Skills Format](https://agentskills.io/specification). Installation und Aufruf richten sich nach dem Agenten.

### Mit der Skills CLI

Mit Node.js und der [Skills CLI von Vercel](https://github.com/vercel-labs/skills):

```bash
# Verfügbare Skills ansehen
npx skills add timsamart/german-corporate-skills --list

# Einen Skill für Codex installieren
npx skills add timsamart/german-corporate-skills --skill praesentations-review --agent codex

# Auswahl für deinen Agenten interaktiv installieren
npx skills add timsamart/german-corporate-skills
```

Die CLI ist ein externes Installationswerkzeug. Die Skills selbst benötigen keine projektspezifischen Zugangsdaten, Pakete oder Dienste.

### Direkt in Codex

```text
$skill-installer Installiere den Skill aus
https://github.com/timsamart/german-corporate-skills/tree/main/skills/praesentations-review
```

Alternativ klone das Repository und kopiere die gewünschten **vollständigen Skillordner** in `.agents/skills/` deines Arbeitsprojekts oder in `~/.agents/skills/`. Aufruf: `$praesentations-review`. Details stehen in der [Codex-Dokumentation](https://learn.chatgpt.com/docs/build-skills).

### Claude Code und weitere Agenten

Für Claude Code kopiere einen vollständigen Skillordner in `.claude/skills/` oder `~/.claude/skills/`. Aufruf: `/praesentations-review`. Siehe die [Claude-Code-Dokumentation](https://code.claude.com/docs/en/skills).

Andere Agenten mit Unterstützung für das Agent Skills Format können die Ordner nach ihren eigenen Installationsregeln verwenden. Die Paketstruktur ist standardbasiert; das Verhalten in einem konkreten Agenten hängt von dessen Modell und Werkzeugen ab.

## Was ein guter Einsatz braucht

Gib dem Agenten die relevanten Unterlagen, Zielgruppe und gewünschte Handlung. Die Standardsprache der Ergebnisse ist Deutsch; eine ausdrücklich gewünschte andere Sprache hat Vorrang.

Für PPTX/PDF braucht dein Agent passende Lese- und gegebenenfalls Renderwerkzeuge. Ein Textextrakt reicht für ein Inhaltsreview. Ein visuelles Review braucht Zugriff auf die gerenderten Folien. Die Skills benennen die tatsächliche Prüfgrundlage und behandeln fehlende Nachweise als offen.

Verwende Unternehmensunterlagen in einer dafür zugelassenen Umgebung. Nachrichten bleiben Entwürfe, solange kein Versand beauftragt wurde.

## Qualität und Weiterentwicklung

Version **0.1.0** enthält sieben Skills, sieben ausgearbeitete Beispiele und 16 verhaltensbezogene Testfälle. Der Repositorycheck prüft Paketstruktur, Metadaten, lokale Verweise und Testfalldaten. Die Beispiele sind redaktionelle Referenzen. Ein unabhängiger Benchmark verschiedener Modelle ist noch offen. Der Prüfstatus und das Vorgehen stehen in [Qualität und Evaluation](docs/qualitaet.md).

Beiträge sind willkommen, insbesondere reale, anonymisierte Fehlermuster und dokumentierte Verbesserungen. Lies [CONTRIBUTING.md](CONTRIBUTING.md). Bitte keine vertraulichen Unternehmensunterlagen in öffentliche Issues oder Pull Requests aufnehmen.

Erstellt von [Timotheos Samartzidis](https://github.com/timsamart). Frei verwendbar und anpassbar unter der [MIT-Lizenz](LICENSE).
