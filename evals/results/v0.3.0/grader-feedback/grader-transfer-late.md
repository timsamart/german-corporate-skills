# Independent transfer review: cases 08–14

Review type: **Independent model review; not human validation**.

All seven requested outputs were present and reviewed. Seven `new_skill/grading.json` files have been saved. The review used only each case's frozen `eval_metadata.json`, its `new_skill/outputs/output.md`, and the raw input named in the metadata under `transfer-private`. Assertions, raw inputs and outputs were not changed. These are synthetic fixtures, so these results do not establish performance on real customer or workplace material.

The actual result is **37 of 38 assertions passed (97.37%)**, including **21 of 22 critical assertions (95.45%)**. Six of seven cases pass every assertion. All seven outputs satisfy their word limits. Every compound assertion was assessed as one binary result, requiring all its parts; no partial-credit scoring was used.

| Case | Assertions passed / total | Critical passed / total | Word count | Limit | Fully passed |
| --- | ---: | ---: | ---: | ---: | --- |
| 08 — v03-gv-02 | 5 / 5 | 2 / 2 | 56 | 120 | Yes |
| 09 — v03-ps-01 | 6 / 6 | 4 / 4 | 250 | 300 | Yes |
| 10 — v03-ps-02 | 5 / 5 | 3 / 3 | 30 | 120 | Yes |
| 11 — v03-ep-01 | 6 / 6 | 4 / 4 | 232 | 300 | Yes |
| 12 — v03-ep-02 | 5 / 5 | 3 / 3 | 56 | 120 | Yes |
| 13 — v03-sk-01 | 5 / 6 | 2 / 3 | 201 | 250 | No |
| 14 — v03-sk-02 | 5 / 5 | 3 / 3 | 47 | 120 | Yes |
| **Total** | **37 / 38** | **21 / 22** | **872** | — | **6 / 7** |

Word counts were independently calculated from the entire output file: split on Unicode whitespace (`\s+`) and count each resulting token containing at least one Unicode letter or number (`\p{L}` or `\p{N}`). This includes headings, labels, table text and task IDs, while excluding punctuation-only or Markdown-only tokens. It is not a prose-only count or a model estimate.

Independent arithmetic agrees with the outputs: case 08's 5 + 10 + 5 minutes equal 20. Case 09 needs 8 − 2 = 6 extra person-days; two testers for three days also equal six. Six times 1,200 euros equals 7,200 euros net; minus the 2,000 euros remaining budget leaves 5,200 euros, which exceeds the sponsor's 5,000-euro additional-funding authority by 200 euros. Case 11's 12,000-euro offer exceeds Nora's exclusive 10,000-euro threshold by 2,000 euros. Case 13's 50,000-euro integration plus 30,000-euro annual license equals 80,000 euros for the first year. No arithmetic assertion failed.

The only failure is case 13's third assertion. Its frozen text requires the estimate to be identified as **“noch nicht freigegebene Schätzung”**. The source explicitly supplies that status. The output says **“aktuelle, unverbindliche Kostenschätzung”**, that a binding offer does not yet exist, and that a final price is not agreed. These accurately communicate noncommitment, but do not state that the estimate itself is still unapproved. The amount, net basis, first-year limitation, integration/license breakdown and exclusions are all correct. Because all parts of the original compound criterion are required, omission of the approval status fails the whole assertion. This is **omission**, not a fabricated approval, an invented price or an unauthorized binding commitment.

That failure is also a criterion concern. An estimate can be approved for communication while remaining nonbinding; nonbinding and unapproved are not interchangeable meanings. However, the prompt asks for a customer reply without unnecessary internal detail. The frozen criterion genuinely requires unapproved status, so this review preserves it, but future evaluation design should clarify whether that internal status is essential to the customer-facing answer or whether a clear statement that no binding quote/final price exists is sufficient. The criterion was not rewritten or relaxed for this run.

Other potential ambiguities were judged semantically. In case 09, the internal decision time of 15 October at 10:00 is expressly proposed to allow ordering before the supplied 12:00 deadline. It is a supported recommendation, not an invented agreed commitment. In case 13, the guided demonstration on 1 December is already authorized as bindingly possible by the raw input; its offer is not an unsupported promise. The promised 21 November update concerns the **status** of the binding offer, not a guarantee that an approved offer will be delivered that day.

Cases 11 and 12 add a draft/check label, and case 11 repeats missing-year and synthetic-source metadata. These reduce concision and make the artifact less natural for workplace use. They do not, by themselves, introduce an approver, approval task, deadline or a formal protocol acceptance procedure. The frozen criteria forbid a new approval process, not the word “Entwurf”; those assertions therefore pass. If future criteria intend to prohibit even draft/check labels, that requirement should be explicit.

The shorter cases received no credit for extra length. Case 10 is exactly two grammatical sentences and case 12 exactly three Markdown bullets. Case 08's timing detail restates the supplied format, rather than creating new session direction. Case 14's building-work explanation is supplied by the source, not invented. No case was found to fabricate approval, resource authorization, task commitments or a confirmed release date.
