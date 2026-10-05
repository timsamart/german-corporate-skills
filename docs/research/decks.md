# Research dossier: presentation review and committee preparation

> Historical research snapshot before revision and evaluation. Proposed changes and tests below are not completed results. The quality report records current implementation and executed checks.

Research date and access date for every source below: **2026-10-05**. Audience: managers, project leads and consultants working in German. Scope: evidence and proposed improvements for `praesentations-review` and `gremienvorbereitung`. This is research and an implementation handoff; no shipped skill was changed in this pass.

## What the existing skills already do well

The presentation skill reviews purpose before format, covers all accessible slides and relevant notes, identifies source and calculation errors, distinguishes evidence from suggestions, and requires rendered slides for visual judgments. It allows descriptive titles and treats an information or training deck differently from a decision deck. Its synthetic example makes a defensible distinction between capacity value and realized financial savings.

The committee skill distinguishes information, discussion and decision; uses the actual mandate; preserves uncertainty in oral answers; and never treats silence as approval. Its example makes a limited test request conditional on missing effort and responsibility information.

The largest research and evaluation gap is visual and delivery context: the examples are text based, and the repository explicitly says visual PPTX/PDF cases and independent model comparisons remain open. A second gap is explicit evidence traceability for the communication conventions.

## Source ledger

### D1 — IBCS current release boundary

**First-party standard association; version announcement, not an experiment.** Published/released 2026-06-11. [IBCS Standards Version 2.0](https://www.ibcs.com/ibcs-version-2-0/).

The association says version 2.0 was released on 11 June 2026, separates Notation and Composition, and aligns its Notation part with ISO 24896. This confirms that version 1.x rule identifiers must not automatically be called current requirements.

**Limit:** The fetched announcement does not expose the complete substantive version 2.0 rules. Alignment is the association's statement; it is not a compliance assessment of this repository. Do not claim IBCS certification or full conformance from this research.

**Use:** Put standards-specific detailed checks in a conditional reference, with edition, verified clause, applicability and source. Apply the user's actual corporate reporting conventions first.

### D2 — IBCS legacy content and a title counterexample

**First-party editorial standard/convention.** Publication date not stated on this page; heading identifies **version 1.1**, while other page elements advertise version 2.0. [IBCS retained standards page](https://www.ibcs.com/standards/page/4/), especially UN 2.1, UN 2.2 and CH 1.1.

The retained text separates a descriptive content title from a message containing an interpretation or conclusion. It also generally favors zero value axes with an indexed-data exception. These are concrete conventions from this legacy text, not universal psychological laws.

**Limit/contradiction:** The page has inconsistent version metadata and embedded user comments. A comment is not a ratified rule. Do not present UN 2.2 as an independently verified version 2.0 clause. This source is valuable as a documented counterexample to “every title must itself be a takeaway assertion.”

**Use:** Preserve the existing skill's permission for topic titles, and consider whether the message can be carried elsewhere. Do not copy a whole standard into the skill.

### D3 — ISO 24896:2026 status and scope

**First-party international standard metadata.** Edition 1, publication 2026-06; lifecycle shows publication 2026-06-11. [ISO 24896:2026 — Notation for business reporting](https://www.iso.org/standard/88366.html).

The public abstract describes consistent visual notation for business reports, presentations and dashboards, including recurring visual aspects and content labels, applicable across organizational types and locations.

**Limit:** The abstract verifies existence and scope, not every requirement in the paid/full standard. ISO publication does not itself establish a legal obligation for every German corporate deck. A claim about a specific clause requires that clause and its applicability.

**Use:** Avoid outdated statements that this is merely an ISO work item. Keep general deck review separate from a requested standards conformance review.

### D4 — Assertion–evidence audience learning experiment

**Original empirical research; author institution's publication record and abstract.** Garner, Alley, Sawarynski, Wolfe and Zappe, 2011, ASEE proceedings. [Assertion-evidence slides appear to lead to better comprehension and recall of more complex concepts](https://pure.psu.edu/en/publications/assertion-evidence-slides-appear-to-lead-to-better-comprehension--2/).

Two student groups, 55 and 56 participants, heard the same recorded explanation about MRI, roughly six minutes long. One saw topic/subtopic slides and the other assertion–evidence slides. The abstract reports higher scores on complex-concept comprehension and retention for the latter, with some differences statistically significant.

**Limit:** Student learning from a short technical explanation is not a German management-decision study. The tested treatment combines sentence assertions and visual evidence; it does not isolate title wording alone. Full methods and effect sizes were not verified here.

**Use:** Offer an evidence-supported message with relevant visual support as an option for explanatory live talks; do not prescribe it for every page or claim a board-performance benefit.

### D5 — Headline study and treatment confounding

**Original empirical research; indexed extract of author-hosted original paper.** Alley, Schreiber, Ramsdell and Muffo, *Technical Communication*, 53(2), May 2006. [How the Design of Headlines in Presentation Slides Affects Audience Retention](https://www.writing.engr.psu.edu/ae_headlines.pdf).

The paper describes four sections of a large geoscience course, the same instructor and teaching content, with mostly phrase headlines versus sentence headlines. It reports that other transformations included typography and replacing bullets with visual evidence, although the headline change was principal for the studied slides.

**Limit:** The original PDF extract was retrievable in search; opening the complete PDF failed. No numerical effect size is asserted here. The comparison is not a pure randomized title-only manipulation. D4 and D5 share researchers and are not two independent research programs.

**Use:** Research claims in README or launch copy should say that some studies support assertion–evidence slide design in technical education, with scope and combined-treatment limitations.

### D6 — Graphical perception replication

**Original empirical research; full original paper inspected.** Heer and Bostock, CHI 2010. [Crowdsourcing Graphical Perception](https://hci.stanford.edu/publications/2010/crowd-perception/heer-chi2010.pdf), particularly printed pages 3–4, Experiments 1A/1B. [Author institution record](https://hci.stanford.edu/publications/paper.php?id=142).

The researchers replicated spatial-encoding comparisons and extended them to area judgments. Position encoding outperformed length in the tested proportional judgment task. Area and angle were less accurate than position; the expected advantage of length over angle was not supported. Thus a neat universal ranking overstates the result.

**Limit:** Estimating the relative values of two marked objects is narrower than reading a full business chart, recognizing a pattern, discussing options or deciding. The study does not test an LLM's ability to inspect slides.

**Use:** For close numerical comparisons, consider aligned positions or lengths and visible scales. Specify the audience's task before recommending a chart replacement; avoid rules such as “pie charts always fail.”

### D7 — Why perceptual precision is insufficient

**Author-authored research perspective/argument, not a new controlled efficacy experiment.** Bertini, Correll and Franconeri; submitted 2020-08-25, inspected version 3 dated 2021-02-12. [Why Shouldn't All Charts Be Scatter Plots?](https://arxiv.org/html/2008.11310v3).

The authors challenge extending accuracy for two-value comparisons into a universal chart-quality rule. They discuss whole-dataset patterns, semantics, educational goals and memory as additional design concerns, using alternative depictions of Minard's map and other examples.

**Limit:** Their preferred examples and broader argument do not experimentally prove that one alternative is best for a particular corporate audience. The paper challenges overgeneralization; it does not justify distorted data.

**Use:** Review whether the chosen visual supports the task—precise comparison, trend, distribution, relationships, geography or explanation—before scoring aesthetics or declaring a chart family unacceptable.

### D8 — Narrative as a design choice

**Original descriptive design research; case analysis, not an efficacy experiment.** Segel and Heer, IEEE TVCG/InfoVis 2010, DOI 10.1109/TVCG.2010.179. [Author lab record](https://idl.uw.edu/papers/narrative); [original paper](https://vis.stanford.edu/files/2010-Narrative-InfoVis.pdf).

The authors characterize narrative visualization through the balance between author-directed narrative flow and reader exploration. Their framework covers different genres rather than one compulsory narrative structure.

**Limit:** The work concerns data narratives and many journalism examples. A typology cannot establish that management decks should always reveal a recommendation first or adopt a particular dramatic storyline.

**Use:** Ask whether the material presents an established recommendation, explains a mechanism, or opens an investigation. Preserve genuine ambiguity in exploratory discussion instead of fabricating a conclusion.

### D9 — Concrete chart-integrity conventions

**First-party official-statistics practitioner guidance; ONS house style.** Page is undated. [ONS service manual: Axes and gridlines](https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines).

ONS distinguishes bars/areas, which encode values through extent from the axis and should start at zero, from line charts/scatterplots, where a cropped axis can show a narrow range. It recommends consistent scales for comparable charts, clear labeling and relevant context.

**Limit/contradiction:** These are ONS production conventions, not German law. Their non-zero line-chart allowance is broader than the retained IBCS CH 1.1 exception in D2. Do not collapse both sources into an “all axes must start at zero” instruction.

**Use:** In a rendered-slide review, inspect chart type, scale, labels, baseline and the comparison actually implied. A 98–100% quality-rate line chart can legitimately use a disclosed narrow range; a 98–100% bar chart visually claiming a large size difference needs a different assessment.

### D10 — Accessibility without invented compliance claims

**First-party standard and informative application guidance.** [WCAG 2.2 Recommendation](https://www.w3.org/TR/2024/REC-WCAG22-20241212/), 2024-12-12, SC 1.4.1 and 1.4.3; [WCAG2ICT Group Note](https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/), 2025-12-11.

WCAG covers conveying meaning through more than color and specifies text contrast thresholds, with exceptions. WCAG2ICT explains applying WCAG to non-web documents and software; the note explicitly does not set normative requirements.

**Limit:** A rendered-slide screenshot can reveal color-only distinctions and apparent legibility problems, but does not establish complete document accessibility, reading order, alternative text or compliance. Technical conformance criteria and statutory obligations are separate questions.

**Use:** When relevant to the audience, check whether color-coded states also have labels or shapes. Report only checks actually performed; require measurements for a numeric contrast claim and document structure inspection for an accessibility assessment.

### D11 — German board-information context

**First-party governance code and its own explanation of status.** DCGK adopted 2022-04-28, announced 2022-06-27; official site still identifies this as current on the access date. [Section D, principles 13 and 16](https://www.dcgk.de/de/kodex/aktuelle-fassung/d-arbeitsweise-des-aufsichtsrats.html); [code status and scope](https://www.dcgk.de/de/kodex.html).

The code connects governance with open discussion and confidentiality, and identifies regular, timely, comprehensive supervisory-board information, including material deviations from plans and their reasons. Its explanatory page distinguishes statutory provisions, recommendations and suggestions and explains comply-or-explain.

**Limit:** Its stated context is German listed-company governance. It is not a blanket checklist binding all steering groups, project leads or consultants. The source supports checking material information and mandate; it does not prescribe a slide template.

**Use:** For an actual supervisory-board task, locate the organization's governing process. For ordinary steering meetings, use timely material information as a transferable practice and label that transfer.

### D12 — Committee preparation and constructive challenge

**First-party regulator governance guidance; explicitly non-prescriptive.** FRC, published 2024-01-29; last updated 2026-06-03. [Corporate Governance Code Guidance](https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/corporate-governance-code-guidance/), paragraphs 27–32, 66 and 78.

The guidance associates good board decisions with timely quality information, clear expectations, sufficient debate, tested assumptions and constructive challenge. It asks boards to consider how significant proposals were developed and challenged, and allows proportionate safeguards.

**Limit:** This is UK board guidance, not a German requirement or a causal effect estimate. It does not require a devil's advocate for every decision or a fixed allocation of meeting minutes.

**Use:** Prepare the material objection most likely to change the recommendation; identify what evidence would answer it. For a significant decision, preserve discussion time and show the strongest unresolved objection in the briefing. Transfer is a proposed practice, conditional on mandate and available time.

## Proposed changes for the next skill iteration

These are author proposals grounded in the source limits above, not claims that every source directly prescribes this workflow.

1. **Add delivery context to intake.** Determine live presentation, pre-read, reference pack or mixed use when it changes the review. A spoken explanation may use visual evidence with detail in notes; a pack read alone needs enough context to be interpretable. Do not penalize document density without this context.
2. **Make rendered-chart checks operational.** Add a short conditional reference covering value encodings, meaningful baseline, comparison scales, units, periods, actual/plan/forecast distinctions, source freshness, missing data, and visible uncertainty. Keep detailed chart rules out of the short entrypoint.
3. **Preserve title flexibility explicitly.** Judge whether the slide's intended meaning is discoverable and warranted. A supported sentence message is useful on many explanatory slides; a descriptive title, comparison question or navigational title can fit other purposes. This extends the existing sound wording rather than replacing it.
4. **Avoid a mandatory storyline template.** Review logical support for conclusions and fair options. For an exploratory workshop, a useful output may be a question, conflicting evidence and the investigation required. Story coherence must not resolve uncertainty by rhetoric.
5. **Separate oral answer from supporting material.** In committee preparation, provide the short answer plus where its evidence sits in the pack. A good sounding answer must not upgrade an assumption or selective pilot into a verified operational fact.
6. **Test the strongest relevant objection.** Ask what missing evidence would reverse or narrow the request. Select objections from the actual case, preserve unresolved ones in the briefing, and reserve appropriate discussion time. Mandate, internal deadlines and authority come from the supplied organization context.
7. **Add transparent source attribution.** A concise `references/grundlagen.md` per affected skill can identify empirical findings, chosen review conventions and conditional standards. The skill remains self-contained; references carry provenance and limits without needing live browsing for every ordinary review.

## Suggested evaluation cases before claiming improvement

| Proposed case | Observable success | Failure to catch |
| --- | --- | --- |
| Live talk versus pre-read using the same material | Explains which missing context matters for each delivery format | Demands identical density and notes rules for both |
| Exploratory options workshop with unresolved evidence | Preserves the question and fair comparison; identifies next evidence | Fabricates a winning option or forces takeaway titles |
| IBCS-style page with descriptive title plus separate message | Recognizes the visible message and respects supplied style | Calls title itself defective solely because it is descriptive |
| Narrow-range line chart and truncated bar chart | Distinguishes value encodings and consequences using rendered charts | Applies an indiscriminate zero-baseline rule |
| Red/green status without text labels | Flags color-only meaning and gives a concrete fix | Claims full accessibility certification from the image |
| Actual/forecast chart with forecast styled like measurement | Finds the provenance ambiguity and repairs the label/style | Repeats forecast as an observed result |
| Committee request with a serious unresolved objection | Gives an honest short answer, source pointer and next evidence step | Scripts rhetorical deflection or implies prior agreement |
| Information-only agenda item | Prepares useful understanding questions and oral framing | Invents a resolution or budget request |

Use fresh runs with only raw inputs, the tested skill and available tools. Compare the existing version with the revision on the same cases. Grade evidence fidelity and task fit, with human judgment for communication quality; do not equate the presence of headings with success. Visual cases require actual slide renders. No model improvement is demonstrated by this dossier itself.

## Retrieval and interpretation notes

- Only primary papers, author institutions, official standards organizations and first-party governance guidance support the recommendations. Search snippets were used to locate sources; D5 records its limited retrieval status.
- The Cleveland–McGill 1984 PDF cover was accessible at [University of Washington](https://faculty.washington.edu/aragon/classes/hcde511/s12/readings/cleveland84.pdf), but complete text/screenshot inspection failed. It is a bibliographic lead, not the substantive basis of a new claim here; D6 supplies the inspected original replication.
- No source found here establishes that these practices are uniquely German or superior because of national character. “German” in the repository can credibly describe language and supplied business context.
- No expert endorsement, legal certification, IBCS certification or independent skill benchmark follows from citing this dossier.
