# Corporate workflow research for German Corporate Skills

> Historical research snapshot of v0.1.0, before revision and execution. Several proposed changes were subsequently incorporated. Current implementation and actual results are recorded in the quality report; the observations below are instruction/example gaps, not observed agent failures.

Research date: **5 October 2026**. Scope: `business-case-pruefung`, `entscheidungsvorlage`, `projektstatus`, `ergebnisprotokoll`, and `stakeholder-kommunikation`, including their five worked examples. This is research and an improvement proposal; the shipped skills were not edited in this pass.

## What the evidence supports

The strongest shared design is a small set of useful business artifacts that preserve the difference between a source fact, an estimate, a recommendation, a decision, and a commitment. The current skills already express that distinction well. Their next improvement should target observable mistakes at the boundaries: inconsistent appraisal horizons, inflated progress, ambiguous assignments, and edits that change the strength of a promise.

Official German sources provide useful methods and examples. Most concern public administration. They are cited here as **transferable editorial and analytical conventions**, with their original scope stated. They do not establish a universal German corporate standard. Company templates, mandates, status definitions, accounting policies, and the actual user request remain controlling context.

This is a source-grounded editorial assessment. It does not demonstrate that using the skills improves outcomes, establish a benchmark result, or certify an artifact's legal or financial validity.

## Source ledger

All entries were inspected on 5 October 2026. Dates below are document dates or explicit page updates, not search-engine crawl dates.

| ID | Primary source and date | Material actually inspected | Scope and limitation |
| --- | --- | --- | --- |
| C1 | [BMF, Arbeitsanleitung Einführung in Wirtschaftlichkeitsuntersuchungen (AAWU)](https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_13012026_IIA3H100500150006005DOKCOO7005100213785493.htm), circular **13 January 2026**, GMBl. 2026 4/5 p. 58 | Official HTML, especially B.II, B.V, B.VIII–IX, C.IV.1, C.VI and C.VII | Federal public expenditure appraisal. The method is useful; federal obligations and discount rates cannot be transplanted into a company. |
| C2 | [Government Finance Function / HM Treasury, Government Efficiency Framework](https://www.gov.uk/government/publications/the-government-efficiency-framework/the-government-efficiency-framework--2), updated **24 November 2025** | Sections 4.1–4.8 and 5 | UK central government definitions. Supplementary first-party method for classifying savings, not a German accounting standard. |
| C3 | [ITZBund, V-Modell XT Bund 2.4, full documentation](https://ftp.tu-clausthal.de/pub/institute/informatik/v-modell-xt/Releases/2.4-Bund/Dokumentation/V-Modell-XT-Bund-Gesamt.pdf), **2024 edition** | Actual primary PDF, especially C.1.2.1 pp. 68–69, C.1.8.1 pp. 94–95, C.1.8.3 pp. 96–97, and C.1.2.2.5 p. 72 | Federal system development projects; use documentation principles without imposing its whole process or role model. The publisher's [release announcement](https://weit-verein.de/v-modell-xt-und-v-modell-xt-bund-in-version-2-4-erschienen/) states publication on **24 May 2024**; announcement dated **5 June 2024**. |
| C4 | [Bundesarchiv, Handreichung Aktenrelevanz](https://www.bundesarchiv.de/assets/bundesarchiv/de/Downloads/Erklaerungen/2025_Handreichung_Aktenrelevanz.pdf), **January 2025** | Both PDF pages | Public records guidance. The questions help preserve rationale and responsibility; public recordkeeping obligations are outside the collection's promise. |
| C5 | [Federal Servicestandard, Verständlich schreiben mit Einfacher Sprache](https://servicestandard.gov.de/handbuch/anleitungen/verstaendlich-schreiben-mit-einfacher-sprache/), updated **2 September 2025** | Official page, context caveat and text/sentence/word guidance | Digital public services. Audience-sensitive language advice, not an automatic corporate style policy. |
| C6 | [BAköV, Selbstlernheft: Verständliches Schreiben – Mehr Erfolg durch gute Texte](https://www.bakoev.bund.de/SharedDocs/Publikationen/LG_2/Selbstlernheft_Verstaendliches_Schreiben.pdf?__blob=publicationFile&v=1), **September 2012, second edition** | Primary PDF: word choice and active verbs, especially printed pp. 16–21; imprint p. 46 | Older editorial training source; still directly hosted by BAköV. Its stylistic prescriptions must be filtered for meaning and current audience. |
| C7 | [Leibniz-Institut für Deutsche Sprache, grammis: Modalverb](https://grammis.ids-mannheim.de/sgt/2199), last changed **31 January 2024** | Definition, examples, explanations and date | Linguistic first-party reference. Establishes semantic functions, not a corporate writing style. |
| C8 | [Schwaber / Sutherland, Scrum Guide 2020, German translation](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-German.pdf), framework **November 2020**, translation glossary **15 June 2022, v3.5** | Sprint Review and Increment / Definition of Done, printed pp. 10 and 13 | Method creators' official distribution of a community German translation. Relevant only where Scrum is part of the user's context. |
| C9 | [European Commission DIGIT, PM² Artefacts](https://pm2.europa.eu/pm2-artefacts_en), landing page **10 August 2022**, v3.1 files dated **9 December 2025** | Landing page and artifact inventory only | Supports the existence and lifecycle placement of the listed artifacts. Download attempts failed; their detailed contents were **not** treated as inspected evidence. |

The ledger distinguishes the publication date from the version date. In particular, a current landing page can host an older document, and a search result's apparent publication age is insufficient to date a source.

## 1. Business case review

**Current strength.** The skill's distinction between freed hours, a monetary capacity equivalent, avoided future cost, and reduced spending is unusually valuable. Its example calculates the supplied model, calls out the wrong savings claim, and preserves the first-year ramp-up effect. It also distinguishes formula inspection from recalculated spreadsheet results.

**Narrow support.** AAWU distinguishes prospective payment appraisal from period-based cost accounting. It uses comparable horizons and explicit assumptions, discusses discounting and residual values, excludes already incurred payments that do not affect the current choice, and examines assumptions that can change the preferred option. Its nonmonetary scoring is distinct from monetary valuation. [C1](https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_13012026_IIA3H100500150006005DOKCOO7005100213785493.htm)

The UK framework explicitly separates monetisable benefits from direct spending reductions. Time saved can support more output at unchanged spending. It also distinguishes gross effects, delivery costs, and net effects, and warns against double counting and shifting costs between periods. [C2](https://www.gov.uk/government/publications/the-government-efficiency-framework/the-government-efficiency-framework--2)

**Observed gaps.** The skill discusses comparable periods but does not explicitly check residual/end-of-contract effects or isolate irrevocable past spending in a continue/stop decision. It has good sensitivity guidance, yet the single example tests only one changed percentage and a largely stable operating trajectory. There is no example for an irregular cash flow, alternative comparison, inconsistent price basis, or double-counted benefits.

**Proposed compact changes.** These are design recommendations from the assessment, not additional source requirements:

- In a new-versus-continue decision, report historical spend separately from the future costs changed by that decision. Do not discard termination obligations or future effects merely because the contract was signed earlier.
- When different horizons or payment timing can change the choice, use a period-by-period model. Include relevant disposal, migration, termination and remaining-value assumptions if supplied. Show omissions explicitly.
- Keep amounts, price basis and timing consistent; distinguish nominal and constant-price inputs when this materially matters. Ask for the applicable company rate rather than inventing a discount rate.
- For weighted scoring, show supplied criteria, weights, scales and rationale. Label invented weights as a proposal. Do not combine points with euros as if they had a common unit.
- Keep a small benefit-realisation entry when requested: claimed benefit, baseline, mechanism, measurement, owner and date. Preserve missing fields as open.

**Limits / counterevidence.** A discounted model is not needed for every small, short decision. A mandatory elaborate model would add work without a demonstrated benefit. Cost accounting can be the appropriate requested lens, and capacity is a legitimate business benefit even when spending remains unchanged. The skill should name the lens rather than reject it.

**Behavioral evaluation candidates.** Use synthetic inputs independent of the shipped example:

1. A continue/stop choice includes €200,000 already paid, €30,000 future cancellation cost, and €90,000 remaining delivery cost. Passing behavior keeps historical spend visible and compares the future choices; it does not call all contract-related cost “sunk.”
2. A supplier says 40% faster with 50% adoption; the analyst has already used the adopted volume and multiplies by 50% again. Passing behavior identifies the duplicate factor and shows the corrected equation.
3. Cash flows are strongly uneven, including a negative operating year. Passing behavior declines a steady annual payback shortcut and shows the supplied period flows.
4. A spreadsheet exports only cached values. Passing behavior reports that formulas/recalculation were unavailable and limits its conclusion accordingly.

## 2. Decision memo

**Current strength.** The skill creates a concrete proposed resolution, compares real alternatives, preserves an authentic status-quo option, distinguishes a pilot from a rollout, and refuses to invent decision authority. It follows an existing company template and makes a one-page format a preference, not a rule.

**Narrow support.** V-Modell XT Bund's formal decision artifact places criteria, alternatives, assessment method, evaluation, recommendation and the actual decision in the same documented process. That supports making a recommendation reviewable while retaining the eventual decision as a separate event. [C3, C.1.2.1.2](https://ftp.tu-clausthal.de/pub/institute/informatik/v-modell-xt/Releases/2.4-Bund/Dokumentation/V-Modell-XT-Bund-Gesamt.pdf)

**Observed gaps.** The compact skill says to use common criteria but has no explicit treatment of an existing scorecard whose weights or scores favor the recommended option. It says an owner must confirm conditions but does not distinguish advice, coordination and mandatory approval when source notes use vague words such as “abgestimmt.”

**Proposed compact changes.**

- Preserve the source's actual scope of consultation: informed, consulted, reviewed and approved need different evidence. A named reviewer is not necessarily an approver.
- If using a scorecard, retain criteria and weighting provenance. For missing weights, prefer an explanatory comparison or a visibly proposed method.
- Name the latest useful decision date and the consequence of deferral only when supplied or calculated from supplied dependencies. Do not manufacture urgency.
- Offer a choice among approve, approve with conditions, defer for a specified missing fact, or reject when that is the user's actual decision space. Do not force those four labels into every memo.
- Add a short unresolved-conditions table only when conditions are material: condition, verification, confirming role and deadline.

**Limits / counterevidence.** A simple operational choice may need only a short email. A formal Vorstand or shareholder resolution can require organization-specific processes beyond an editorial skill. More documentation does not create a mandate or a valid resolution.

**Behavioral evaluation candidates.**

1. Notes say “Finance reviewed the estimate”; the proposed resolution claims “budget approved.” Passing behavior retains review status and flags approval as missing.
2. A preferred supplier wins an invented scoring matrix. Passing behavior labels unsupported weights and scores rather than laundering them into objective evidence.
3. A board paper seeks a complete rollout although the evidence concerns a limited pilot. Passing behavior narrows the supported proposal and preserves the later decision.
4. The user requires their company's two-paragraph template. Passing behavior fits the content to that template rather than imposing six mandatory headings.

## 3. Project status and escalation

**Current strength.** The skill uses a reporting date, a baseline and a forecast. It distinguishes activities from outcomes, actual issues from prospective risks, proposed rebaselining from an approved change, and missing evidence from an automatic status color.

**Narrow support.** The current V-Modell status artifact includes results, quality, risks, deviations and the following period's plan. For overall progress it calls for a common reporting date across subprojects. [C3, C.1.8.3](https://ftp.tu-clausthal.de/pub/institute/informatik/v-modell-xt/Releases/2.4-Bund/Dokumentation/V-Modell-XT-Bund-Gesamt.pdf)

In Scrum, completion is tied to the agreed Definition of Done; a Sprint Review inspects outcomes with stakeholders and considers adaptation. It should be treated as a working event with decisions and learning. This limits using a polished status report as a substitute for evidence of delivered work. [C8](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-German.pdf)

**Observed gaps.** The skill has an explicit reporting date but no rule for a merged report whose component dates differ. It does not challenge an unsupported percent-complete claim or distinguish “developed,” “tested,” “accepted,” and “in use.” Its example concerns a missing integration dependency; budget forecasts and quality impacts remain unexercised.

**Proposed compact changes.**

- For combined reports, retain each material source's date and flag a mixed-date aggregate. A newer top-level date must not silently update older component facts.
- Preserve the company's definition of completion. Report distinct delivery states where that distinction changes the decision; do not invent a global definition.
- Challenge claimed completion percentages when no denominator or measurement basis exists. Do not average unlike indicators or traffic lights into an unsupported overall score.
- Separate actual cost to date from forecast remaining cost and forecast final cost when supplied. Missing actuals are not zero.
- Where a forecast depends on an unresolved external event, state the dependency and a supported range or scenario; a precise date should not imply confidence the material does not support.

**Limits / counterevidence.** Agile work can legitimately revise scope as learning occurs. The existing line about retaining an approved baseline should preserve comparison, not forbid adaptation. A management escalation may be unnecessary where the team already has authority and a viable recovery action. Enterprise status reporting and Scrum serve different purposes and can coexist.

**Behavioral evaluation candidates.**

1. Three subproject reports dated 1 September, 20 September and 5 October are summarized “Stand 5 October.” Passing behavior exposes the different dates.
2. “80% complete” is based on meetings held; testing and acceptance have not started. Passing behavior avoids presenting 80% as verified deliverable progress.
3. Costs to date are €60,000, remaining forecast €70,000, approved total €100,000. Passing behavior states a €130,000 forecast and €30,000 projected variance, with its assumptions.
4. A team can resolve an issue within its mandate. Passing behavior can prepare a status update without adding an invented escalation or managerial demand.

## 4. Meeting results and action log

**Current strength.** The skill carefully preserves discussion, proposal, decision and commitment. It handles later corrections, contradictory sources, identity uncertainty, partial transcripts, conditional commitments and relative dates. It keeps advice outside the historical record and does not infer permission to send minutes.

**Narrow support.** The Bundesarchiv's document uses questions about why a matter was handled, who participated and when, what alternatives were considered, and the decision's reasons. It also says document relevance depends on process and purpose. These questions can guide a concise corporate record without importing public archival obligations. [C4](https://www.bundesarchiv.de/assets/bundesarchiv/de/Downloads/Erklaerungen/2025_Handreichung_Aktenrelevanz.pdf)

V-Modell's meeting artifact includes participants and action-list entries, and envisages participants checking accuracy. The reusable element is a review step, not an automatic sending action. [C3, C.1.8.1.2](https://ftp.tu-clausthal.de/pub/institute/informatik/v-modell-xt/Releases/2.4-Bund/Dokumentation/V-Modell-XT-Bund-Gesamt.pdf)

**Observed gaps.** The current output is clearly for review, but it does not name a draft/confirmed state or distinguish an apparent transcript from a reliable recording. There is no exercised example for a misrecognized number, a changed decision, a conditionally accepted task, or an owner expressed through a pronoun with ambiguous reference.

**Proposed compact changes.**

- Name the output's review state when relevant: draft from supplied notes, reviewed by a named person if supported, or approved if supported. Do not imply confirmation from silence.
- Retain a decision's concise reason only when the material gives it and it matters to future interpretation; avoid turning an Ergebnisprotokoll into a verbatim transcript.
- Flag consequential numbers, dates and names when the recording/transcript is ambiguous. Do not silently fix a plausible transcription error without checking a supplied source.
- Distinguish an owner accepting a task from another participant assigning or suggesting it. Preserve the actual meeting rules where supplied.
- Preserve meaningful conditions on a task: “after access is available” cannot become an unconditional deadline.

**Limits / counterevidence.** Task commitments can be explicit without ceremonial words. “Ich schicke es morgen” can be a commitment in context. A skill that demands a formal motion for every action will miss normal workplace communication. “Approved minutes” still does not certify legal validity. Drafting minutes does not create a retention rule or authorize publication.

**Behavioral evaluation candidates.**

1. “I can deliver by Friday if access arrives Tuesday” becomes “deliver Friday.” Passing behavior retains the dependency and does not claim an unconditional commitment.
2. Earlier budget approval is expressly withdrawn later. Passing behavior preserves the final state and the change where relevant.
3. A transcript inconsistently recognizes €15,000 / €50,000. Passing behavior identifies the contradiction rather than selecting the convenient value.
4. “They will check it” has two possible antecedents. Passing behavior leaves responsibility open instead of choosing a named owner.

## 5. Stakeholder communication

**Current strength.** The skill leads with purpose and required response, preserves Du/Sie and the user's relationship context, removes empty phrases, and retains facts, uncertainty and commitments. It refuses to polish invented blame or threats into a professional-looking message.

**Narrow support and a useful conflict.** BAköV favors concrete wording, familiar words and active verbs, while warning through its review questions that a chosen synonym must still match the substance. [C6](https://www.bakoev.bund.de/SharedDocs/Publikationen/LG_2/Selbstlernheft_Verstaendliches_Schreiben.pdf?__blob=publicationFile&v=1)

Servicestandard likewise recommends clear structure and language suited to readers. It expressly acknowledges that context can prevent applying every simplification recommendation. Some individual suggestions are much stricter, including a 12-word sentence guideline and removing modal verbs. [C5](https://servicestandard.gov.de/handbuch/anleitungen/verstaendlich-schreiben-mit-einfacher-sprache/)

IDS explains that modal verbs can express wishes, possibility, permission, necessity or the speaker's view of an event. Removing them can therefore change content. [C7](https://grammis.ids-mannheim.de/sgt/2199)

**Observed gaps.** The current instruction to preserve meaning is sound but broad. The example tests a difficult disagreement, not subtle changes introduced while shortening an ordinary update. “Wir könnten am Freitag liefern” can become “Wir liefern am Freitag” even though the result is smoother and less faithful.

**Proposed compact changes.**

- Check semantic invariants after polishing: who acts, what action, amount, date, condition, negation, degree of certainty, source of authority and actual commitment.
- Preserve modal meaning and conditional wording whenever it carries uncertainty, permission, scope or obligation. Simplify its syntax only when meaning survives.
- Keep official names and shared technical terms consistent. Explain an unfamiliar term when needed; avoid synonym churn that makes one thing look like two.
- For a difficult update, state the concrete effect and available next action. A calm tone should leave material uncertainty or disagreement visible.
- Adapt structure to the actual channel. A Teams message does not need a formal salutation or subject line; the skill's existing channel caveat should stay flexible.

**Limits / counterevidence.** Active voice is useful when the actor is known. An automatic conversion of every passive sentence can fabricate an actor or add blame. A fixed sentence-length maximum can damage nuance. Clear communication can be warm, concise and technically precise without claiming that all German workplaces prefer the same tone.

**Behavioral evaluation candidates.**

1. “We could deliver Friday if tests pass” is revised for clarity. Passing behavior preserves possibility and the condition.
2. “A decision has not yet been made” is changed to active voice with no known decision maker. Passing behavior avoids inventing a person or role.
3. A friendly draft contains two different deadlines for different recipients. Passing behavior keeps them distinguishable.
4. The user asks for a short Teams message to a colleague they address with Du. Passing behavior preserves the relationship and channel rather than adding formal corporate email framing.

## Research-to-skill handoff

These findings should enter the skills selectively. Add only short instructions that prevent plausible errors; put conditional appraisal detail in a reference if it becomes substantial. A source list at repository level is useful for credibility, but copying whole manuals into each skill would make use slower and blur source scope.

Prioritize three changes for the next iteration:

1. **Meaning preservation during rewriting:** explicit attention to modality, conditions, negation and authority. This helps communication, minutes and decision memos.
2. **Measurement provenance:** reporting dates, completion basis and cash-versus-capacity classification. This helps business cases and project status.
3. **Decision scope:** preserve supplied mandates, consultation status and separate a proposal from the eventual authorization. This helps every artifact.

The next validation should compare realistic skill-assisted outputs against outputs from the same model without the skills, using the same raw material and task. Score decisions and unsupported additions, not whether headings match. Have a reviewer judge the outputs without the condition labels where practical. Keep a few cases held out from prompt refinement, and retain failures as evidence. Structural validators can verify the package, but source grounding and examples alone cannot establish behavioral performance.

The [official PM² artifact inventory](https://pm2.europa.eu/pm2-artefacts_en) confirms that business cases, stakeholder matrices, communication plans, status reports, meeting minutes and decision/issue/risk/change logs are recognizable workflow artifacts. This is supporting evidence for the portfolio's coherence, not a claim that PM² validates these implementations or that its downloadable templates were inspected in this pass.

## Access limitations and excluded evidence

- The federal BMI and CIO pages and some ITZBund/PDF links returned access errors. The actual V-Modell XT Bund 2.4 PDF was obtained through a link from WEIT e.V.'s primary release announcement; its content was inspected. Older federal HTML was inspected as corroboration but was not used as the sole current-edition authority.
- PM² v3.1 downloads could not be retrieved with the research tool. Only the verified official artifact inventory supports claims here.
- DIN publications behind paid access were not inspected, and no conformity claim is made.
- Search snippets, commercial consultancy articles, legal provisions unrelated to the workflow, and social-media interpretations were excluded from substantive conclusions.
- No real corporate deck, transcript or confidential company template was used. All proposed evaluation inputs are synthetic. Real-world validation remains a separate step.

No shipped files, external messages or public releases were changed by this research pass.
