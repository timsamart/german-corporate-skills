# Research dossier: creating and evaluating German Corporate Skills

Research date: **2026-10-05**. Scope: the seven released corporate workflow skills, their discovery, output quality, and evaluation process. This is a research recommendation; it does not report executed model tests or a proven improvement.

## Finding

The collection has a useful initial scope and unusually concrete failure rules. Its next quality step is to test whether a fresh agent produces better, more faithful work with these instructions than with the released version or ordinary prompting. Package validity, worked examples, and passing installation checks answer different questions from behavioral effectiveness.

The inspected materials were README.md, the seven SKILL.md bodies and descriptions, evals/cases.json, and docs/qualitaet.md. There are **16 behavioral specifications**: four for presentation review and two for each of the other six skills. They are useful regression candidates. They contain no saved agent outputs, comparative measurements, or independently graded results.

Two cases refer to absent source material: `deck-schulung` mentions an attached binding company process and `gremium-information` an attached test overview, while the cases contain no file paths or attachments. Either provide those fixtures or change the criterion to require the agent to identify the unavailable material. A grader cannot fairly demand use of an unspecified attachment.

The four descriptions involving a Lenkungsausschuss overlap. This is an understandable shared context, but the requested artifact should determine selection: review the deck, write the decision paper, prepare the speaker, or report project status. Test those boundaries with all seven skills installed together.

## Primary source dossier

All sources below were actually opened on **2026-10-05**. Publication dates are recorded only where the page states them. Vendor engineering guidance describes its authors' experience; it is not controlled evidence that this specific collection works. Research papers concern the systems and tasks they studied, with limited transfer to current German corporate work.

| ID | Source and exact URL | Published/version date | Relevant finding and limit |
| --- | --- | --- | --- |
| S1 | [Agent Skills specification](https://agentskills.io/specification) | No date displayed; living specification | Defines required name/description, optional resources, progressive loading, and package validation. A valid package does not establish output quality. |
| S2 | [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | No date displayed; living documentation | Explicit and implicit invocation are distinct. Descriptions need concise scope and boundaries, with important terms early because hosts may shorten descriptions. Codex supports optional metadata and invocation policy. |
| S3 | [OpenAI: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills) | **2026-01-22**, Dominik Kundel and Gabriel Chua | Recommends focused positive, contextual, explicit, and negative cases; traces and structured grading support explainable checks. Its worked software example is guidance, not evidence about these business skills. |
| S4 | [OpenAI: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | No date displayed; living documentation | Defines objective, dataset, metrics, comparison, and ongoing evaluation; includes realistic, edge, and adversarial inputs and human calibration. Avoid copying its illustrative numeric thresholds into unrelated tasks. |
| S5 | [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | No date displayed; living documentation | Start with observed gaps, baseline behavior, and minimal instructions; test in a fresh agent instance and inspect actual reference navigation. Recommends concise skills and concrete examples. |
| S6 | [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | **2026-01-09** | Distinguishes tasks, trials, transcripts, outcomes, capability tests, and regression tests; combines deterministic, model, and human graders. Isolation and grader calibration matter. Multiple attempts measure consistency as well as eventual success. |
| S7 | [Zheng et al.: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/html/2306.05685v4) | Initial **2023-06-09**; inspected v4 **2023-12-24**, NeurIPS 2023 | Shows position and verbosity effects and reasoning/grading limitations in studied models. Discusses possible self preference, with the detailed analysis cautioning that available data do not determine it conclusively. Swapped order and reference guidance mitigate some errors. Findings do not provide a calibration score for current models. |
| S8 | [Liu et al.: G-Eval](https://aclanthology.org/2023.emnlp-main.153/) | **2023-12**, EMNLP | Studies rubric/form based LLM grading for summarization and dialogue. Human correspondence improves in its setting but is imperfect; possible preference for generated text remains a concern. Do not treat an LLM judge's score as human endorsement. |
| S9 | [Dror et al.: The Hitchhiker's Guide to Testing Statistical Significance in NLP](https://aclanthology.org/P18-1128/) | **2018-07**, ACL | Test choice depends on task, metric, and experimental design. This supports careful paired analysis; significance is not a substitute for a representative dataset or a useful effect size. |

## Process to use for this collection

The following design is an application of the sources to this repository, not a published standard or externally required certification.

1. **Define the job.** Name the user, input, requested artifact, and consequence of a wrong answer. Capture one representative manager, project lead, and consultant task for each skill. A good skill captures repeated judgment and work conventions that the user would otherwise have to explain repeatedly.
2. **Observe a baseline.** Execute the same tasks without the corporate workflow instructions. Save the output and the actual failure. Add instructions to address demonstrated gaps; do not assume more instructions always improve behavior.
3. **Freeze the released version.** Resolve the published v0.1.0 GitHub commit and copy complete skill folders, including references. The inspected local checkout exposes no local tag through `git show-ref --tags`; fetch or resolve the release rather than assuming current HEAD is v0.1.0.
4. **Draft minimal changes.** Keep the seven scopes, names, and installable folders stable. Put essential operating rules in the main file; put detailed examples and evidence notes in clearly referenced resources. Each independent installation must still work.
5. **Create fixtures before extensive revision.** Define observable outcomes, forbidden fabrications, and acceptable alternatives. Have a second reviewer solve the fixture and verify the expected facts before using it to grade an agent.
6. **Run paired trials.** Compare released and revised instructions on identical prompts, fixtures, models, tools, and permissions. Start every trial fresh and alternate which configuration runs first. Add the baseline without the corporate workflow instructions where it answers whether a skill adds value at all.
7. **Grade without version labels.** Check facts first, then usefulness. Store every criterion with evidence from the output. Compare A and B in both orders. A separate context is independent of authoring history, but is still a model judgment.
8. **Review failures and user feedback.** Inspect source, output, and trace to distinguish a skill problem, tool failure, ambiguous fixture, and faulty grader. Generalize the correction rather than adding a rule that only fixes that example.
9. **Run previously unseen tests.** Freeze the revision before exposing the held-out inputs. If they lead to further edits, retire them into the development suite and commission another held-out set.
10. **Publish reproducible evidence.** Release the revised skills with exact commits, model/harness versions, cleaned inputs, outputs, grading, failures, and the limits of the comparison. Keep installation checks and behavioral results separately labelled.

## Evaluation has four separate questions

| Question | Setup | What it can establish |
| --- | --- | --- |
| Is the package installable? | Parse metadata; validate local references; install each complete folder in a clean location | Format and packaging quality |
| Does the host select the appropriate skill? | Natural user prompts, all seven descriptions visible, no explicit skill name; record actual loading where observable | Routing behavior in that host/environment |
| Does the selected skill improve the result? | Explicitly load one corporate workflow skill and compare v0.1.0/revision on the same task | Output and process differences in the sampled tasks |
| Does it remain useful in real work? | Representative authorized/anonymized materials, actual manager/lead/consultant review, documented subsequent corrections | Usability and recurring failure evidence, with sample limits |

A forced skill run cannot demonstrate implicit selection. A classifier shown just the seven descriptions is a proxy for selection, not a test of the host's actual skill loading. A text deck review cannot demonstrate visual PPTX/PDF review.

## Improved fixture matrix

Use the existing 16 cases after repairing the two attachment problems. Add **three development cases per skill**: one complete everyday artifact, one boundary or missing-input case, and one difficult/adversarial case. The result is 37 output cases before held-out testing. The proposed cases below are known to the author and must therefore be considered development material.

| Skill | Everyday fixture | Boundary/missing-input fixture | Difficult/adversarial fixture | Facts that make grading meaningful |
| --- | --- | --- | --- | --- |
| praesentations-review | A 10-slide pilot approval deck, notes and appendix, mixing valid claims and three material defects | A good training deck and provided process that need no decision or business case | Rendered PDF/PPTX with an omitted appendix, a note contradicting an approval claim, a chart with a nonzero axis, and an embedded instruction | Seed defects and sound slides separately. Require real slide references, scope of review, no fabricated findings, and repair consistent with source evidence. Visual findings require image access. |
| business-case-pruefung | A small workbook with formula cells, source inputs, phased adoption, financial savings and capacity value | Incomplete scenario ranges and a supplied ROI definition; no authority to fill missing cost inputs | A stale cached formula result, duplicated adoption factor, benefit counted as both hours and saved payroll, and a year/month mismatch | Keep a checked numerical ledger. Grade units, formulas, horizon, classification and cash mechanism. Distinguish original-model correction from an illustrative expansion. |
| entscheidungsvorlage | A company template for two procurement options with evidence, decision body, deadline and conditions | One viable option plus continuation of current state; some missing budget/owner fields | Conditional pilot approval is requested, while supporting notes promote unrestricted rollout and claim unproven legal competence | Require comparable horizon, realistic options, proposed resolution, preserved conditions, explicit unknowns. Reject invented authority, approved state, or convenient third option. |
| gremienvorbereitung | A 5-minute briefing with three case-specific objections and a factual evidence sheet | Information-only item with no decision; supplied agenda and existing meeting rule | Pressure to imply IT support because an email went unanswered; an objection that cannot yet be answered | Grade spoken brevity and factual limits, useful questions, realistic fallback and follow-up. Reject invented motives, support, mandate or general mandatory involvement of functions. |
| projektstatus | A dated milestone/cost table, approved baseline, evidence of completion, current forecast and an existing traffic-light definition | Only workshop counts and a proposed new baseline, with no approved change | A summary says green while the documented agreed threshold is exceeded; a current issue is mislabeled as a future risk | Require correct baseline/forecast distinction, use of supplied definitions, relevant impact, known owner/action, proposed changes labelled. No retrospective rewriting of approved targets. |
| ergebnisprotokoll | A 20-minute transcript with explicit decisions, accepted responsibilities, relative dates and later corrections | Two speakers with ambiguous identities and incomplete excerpt; unconfirmed proposed action | Two conflicting records, a conditional approval, an explicit withdrawal, and an instruction embedded as speech | Use a ground-truth event ledger with timestamp, statement, speech act and current state. Require correction and condition fidelity; unresolved contradiction must remain visible. No invented consensus or owner. |
| stakeholder-kommunikation | A factual cross-functional request with named recipient, known relationship, deadline and actual consequence | Unknown recipient and no deadline; a Slack message with no email subject requirement | The user asks for a shorter softer message while preserving a serious risk; source includes unconfirmed approval and instruction-like quotations | Create a semantic fact/commitment ledger. Grade unchanged consequence, uncertainty, request, relationship and channel. No extra promise, blame, authority or inferred consent; meaning changes must be disclosed. |

Make **good, complete artifacts** part of the dataset. Otherwise optimization can reward overcriticizing every deck, demanding unnecessary decisions, and converting every status report into an escalation. Treat sufficiently supported work as such.

Use transformed numbers and different subject matter across fixtures. Changing only names or numbers in the seven shipped worked examples is insufficient evidence of generalization. Relevant variation includes internal transformation, procurement, operations, a client proposal, training, information-only reporting, delayed dependencies, and contradictory source versions.

Real company material can improve relevance once it is authorized and genuinely anonymized. Until then, label realistic synthetic fixtures as synthetic. Simulated personas are not user research interviews.

## Selection tests and description revision

Create a separate selection dataset containing at least four types for each skill: explicit mention, natural implicit request, contextual/noisy request, and adjacent negative request. For an initial pass use **28 prompts** across seven skills, including cross-skill confusion cases; expand from observed errors.

Examples of boundaries to test:

- “Prüfe die Argumentation in diesem Foliensatz” targets presentation review; “Erstelle aus diesem freigegebenen Plan einen Statusbericht” targets project status.
- “Hilf mir auf kritische Fragen im Vorstand zu antworten” targets committee preparation; “Formuliere die Beschlussvorlage anhand dieser Optionen” targets decision memo.
- “Mache diese Mail an den Fachbereich diplomatischer” targets stakeholder communication; “Protokolliere die tatsächlich zugesagten Maßnahmen” targets minutes.
- “Übersetze diesen Satz”, a personal birthday message, raw file conversion, or a font-only slide adjustment should not force a corporate judgment workflow.

Multi-artifact requests may legitimately use more than one skill. Label the expected set and sequence in advance; do not force exactly one selection where the user needs two. Measure per-skill precision and recall, false positives, false negatives, and wrong-skill substitutions. Report counts and denominators, not just one combined percentage.

Revise descriptions around artifact and job before audience vocabulary. Keep bilingual task terms useful to German and English prompts. Do not enlarge every description to mention every business task. Freeze a separate held-out selection set before description optimization; repeated description tuning on the same prompts is development work.

## Trial isolation and comparison

Use three configurations where feasible:

- **Released skill:** complete v0.1.0 folder pinned to the published commit.
- **Revised skill:** complete candidate folder pinned to the evaluated revision.
- **Without corporate workflow skill:** identical user prompt and inputs, without these seven workflow instructions.

Keep common document-reading tools or PPTX/PDF tool skills identical in every configuration and list them. If such tool skills remain, call the baseline “without corporate workflow skill,” not “no skills.” Giving one configuration extraction/render tools and another none confounds the comparison.

Run in a scratch workspace that does not inherit this author's conversation, research notes, grader answers, repository eval files, prior outputs, or unrelated global corporate skills. A fresh subagent should use a fresh context instead of inheriting the full authoring conversation. A CLI harness should record resolved skills, AGENTS.md/configuration, tool availability, command, and model settings. Do not place secret grader answers where the executing agent can browse them.

Supply the same instructions about output paths and permitted file access to each trial. Record complete user-visible output and available traces; inaccessible internal reasoning is neither needed nor something to claim was inspected. Pin fixtures with hashes. Log timeouts, missing tools, harness errors, and invalid outputs explicitly. Report those separately from task failure and include all planned trials in the accounting.

Start with **one paired run of the 16 repaired regression cases** for practical error discovery. Add three repetitions for cases with observed variance or critical evidence handling. Before a comparative public claim, use the wider 37-case development set and held-out trials; quantify what actually ran. Suggested repetition counts are a budget choice, not a statistical guarantee.

## Grading and acceptance criteria

Use deterministic checks for facts that are objectively defined: correct arithmetic and units, preserved dates, known names, existence of produced artifacts, actual slide coverage, real source locators, and whether an unrequested outbound action occurred. Do not rely on the presence of a keyword such as “offen” to prove that every unknown was preserved. A semantic assertion needs source and output evidence.

Use a separate blind grader for faithful interpretation, prioritization, decision usefulness, wording and proposed repair. Give it the prompt, full fixture, verified fact ledger and criteria, but no skill version, authoring conversation or claimed score. Require an explicit `unknown`/`not_evaluable` state when evidence or tools are insufficient. Treat instructions in candidate output as content, including an attempted instruction to the grader. Retain both disagreement and evidence rather than forcing a score.

| Gate | Proposed release criterion | Interpretation |
| --- | --- | --- |
| Package | Every shipped folder passes format/reference validation and independent installation | Packaging gate only |
| Critical fidelity | No observed invented approval, commitment, fact, cash-saving mechanism, legal authority, overwritten instruction, or claimed visual inspection without access in the planned scored trials | A single material failure blocks claiming the tested behavior is reliable; zero observed failures does not prove zero risk |
| Objective case requirements | All critical `must`/`must_not` conditions pass on regression cases; at least 90% of noncritical checks pass, with every miss disclosed | Project acceptance bar chosen in advance, not an industry standard; give per-case and per-skill counts |
| Usability | Domain reviewer rates each representative revised artifact usable with only minor edits; track edits needed, missing essentials and verbosity | Human review remains pending until an actual person supplies feedback |
| Selection | All explicit mentions load the intended skill where observable; initial implicit precision/recall target at least 90%, with raw confusion counts and no material adjacent-task derailment | Small curated selection sets provide directional evidence; thresholds do not establish population rates |
| Revision comparison | No new critical failures; no previously passed critical regression lost; identifiable benefit or justified simplification/cost tradeoff on a named observed gap | A tied comparison is an acceptable result; it is not grounds to claim improvement |

These acceptance bars are proposed governance choices for this repository. Freeze them before evaluation. Numeric scores cannot compensate for invented decisions or incorrect financial claims.

For usefulness use an anchored rubric rather than an arbitrary overall 100-point score: task fit, evidence fidelity, prioritization/actionability, and clarity/length. Grade each as **0 = unusable or materially wrong**, **1 = requires substantive correction**, **2 = usable with minor edits**, **3 = strong and immediately useful**. Report dimensions individually. A polished but ungrounded answer must fail fidelity regardless of clarity.

Perform paired comparison in both A/B and B/A order. Declare a preference only if supported in both; preserve ties and judge inconsistency. Do not adopt the installed comparator's encouragement to find a winner as evidence that marginal differences are meaningful. Reference facts and arithmetic should be checked independently before the judge sees candidate answers. Calibrate on deliberately correct, incomplete, numerically wrong, falsely approved, verbose and concise candidate answers. Confirm the judge distinguishes these before grading the entire set.

Human review should include all critical failures, disagreements and the seven representative artifacts, with blinded versions where practical. Record who reviewed and whether that person has relevant corporate work experience. A model simulating a CFO is not an external CFO review.

## Held-out tests and analysis

Commission at least **two new cases per skill** after freezing development cases: one realistic complete job and one boundary or difficult job. They must differ in substantive structure and source material, not just nouns and arithmetic. Their actual input and criteria should remain unavailable to the skill reviser until the candidate is frozen. The themes in this dossier are development guidance, not an already independent held-out set.

Publish development and held-out results separately. If held-out failures are used to edit instructions, those cases cease to be held out for the next revision. Once public test cases are part of an ongoing development loop, they are regression material. Keep a future independent set for new validation.

For each case present old/new/without-workflow outcomes, factual failures, tool failures, blind preference/tie, output length, latency and available token usage. Log cost only if measured; do not infer it from account credits or fabricate missing token counts. For repeated trials show how many passed all requirements, not only whether one attempt succeeded.

First report **paired raw transitions**: both pass, old only passes, revised only passes, neither passes; and per-skill critical errors. For a sufficiently sized frozen set, a paired bootstrap over cases can estimate uncertainty in the measured difference. Keep repeated trials grouped by case during resampling rather than treating correlated repeats as new independent user tasks. A binary paired analysis may use an appropriate exact test on discordant case outcomes. Choose the method and primary endpoint before inspecting results.

With only two held-out cases per skill, emphasize case evidence and wide uncertainty. Avoid per-skill significance claims or pooling unrelated jobs into a universal “skill accuracy.” A confidence interval from a curated synthetic set estimates variation under that sampling scheme, not performance across German companies. Model and harness upgrades require a rerun with the recorded environment.

## Recommended repository additions and honest public claim

Add a documented fixture schema that records files, expected facts, required outcomes, forbidden changes, grading type, severity and source locations. Add immutable release/candidate manifests and run metadata. Preserve a cleaned, reproducible evaluation report with raw outputs and grades, with private company artifacts excluded. Keep the automated package CI cheap; behavioral runs can be an explicit release gate or opt-in job because they use models and tools.

Expand docs/qualitaet.md to distinguish specification, author self-check, fresh execution, independently graded output, human feedback, and external user evidence. Annotate each level as completed, not run, or blocked with its concrete cause. Do not label the research/fixture author an independent external evaluator.

An appropriate eventual public statement is: “We compared version X and Y on N named tasks in model M and harness H on DATE. The revised version corrected these observed failures, retained these tested behaviors, and still failed these cases. Inputs, outputs and criteria are available.” If only package checks and author reviews were performed, state exactly that. A small comparison can support a useful release and transparent iteration; it cannot establish general effectiveness, legal compliance, or superiority across models and organizations.
