# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Group 7 Thursday 2:30pm
- Members, GitHub usernames and cohorts: u3309151 MBLL02, u3313159 Rubai21321
- Repository URL: https://github.com/MbLL02/4483_Assignment_3.git
- Starting SHA: 64e3fcd

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Implement patient lookup by ID (PatientService.find_patient)
- Context: The application coordinates registered patients within an active session. Staff need to retrieve existing registered patients by ID without creating duplicate objects.
- Requirement: Return the actual registered Patient object stored in SmartCareDataStore given a valid patient ID.
- Acceptance criteria: Return the identical stored Patient reference for an existing valid ID. Strip/trim leading and trailing whitespace from the ID input.Ensure ID lookup remains strictly case-sensitive. Raise ValueError if the ID is blank, empty, or non-string. Raise LookupError if the ID is valid format but not found in the store.
- Scope: Confined to PatientService.find_patient in smartcare/services.py and unit tests in tests/test_services.py. Does not modify domain.py, data_store.py, or console/menu logic.
- Definition of Done: Method implemented, passes 100% of unit tests covering positive/negative/boundary cases, passes full regression test suite, human review and Copilot review completed, merged to main via PR.
- Owner: MBLL02
- Actual issue link: 

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: Implement guarded appointment cancellation (AppointmentService.cancel_appointment)
- Context: Scheduled appointments may need cancellation while preserving complete clinical audit history and record retrievability.
- Requirement: Cancel a scheduled appointment by transitioning its state using the domain method while retaining the appointment object in the data store.
- Acceptance criteria: Retrieve the existing appointment and transition status from SCHEDULED to CANCELLED via appointment.cancel(). Return the exact same appointment object reference. Retain the appointment in SmartCareDataStore (verifiable via find_appointment and list_appointments). Raise LookupError if the appointment ID does not exist. Raise ValueError for blank/invalid ID. Raise ValueError without mutating object state if the appointment is already CANCELLED or COMPLETED.
- Scope: Confined to AppointmentService.cancel_appointment in smartcare/services.py and unit tests in tests/test_services.py. Does not delete data from data_store.py.
- Definition of Done: Implemented without mutating rejected states or deleting records; passes unit and regression tests; approved via peer PR review; merged to main.
- Owner: Rubai21321
- Actual issue link: 

## B Commit quality

| Original example                               | Strong or Weak | Reason     |
|------------------------------------------------|----------------|------------|
| changes                                        | Weak       | Vague, non-descriptive, provides no context on what files or behaviors changed. |
| final version                                  | Weak       | Meaningless in version control; fails to describe engineering intent or atomic functionality. |
| Add patient search by ID                       | Strong       | Clear imperative statement describing the exact feature and behavior introduced. |
| fix stuff                                      | Weak       | Ambiguous, does not state what bug was fixed or how it was verified. |
| Prevent cancellation of completed appointments | Strong       | Specific, intent-driven description of a business invariant and boundary enforcement. |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: The PR mixes appointment cancellation logic with unrelated refactoring (renaming patient fields, restructures, new dependencies). This introduces merge conflicts, muddies the Git history, and makes isolated code review nearly impossible.
- Responsibility and architecture concerns: Renaming patient fields breaks established public domain contracts without an approved requirement change. Adding external dependencies introduces maintenance bloat when the project strictly requires standard Python library utilities.
- Testing and review concerns: Tests for cancellation might pass while regressions in patient workflows go unnoticed. Diff noise hides genuine flaws in cancellation edge cases
- Changes to remove or separate, with reasons: Strip all patient field renames, external package additions, and broad file formatting. Keep only AppointmentService.cancel_appointment and its corresponding test file changes.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: Copilot provides no proof that tests actually ran, does not verify object identity (is), does not check retained history (FR-07), and does not confirm that invalid transitions preserve state without mutation.
- Follow-up review question 1: Did you verify that the returned appointment is the identical memory reference (is) rather than a cloned object?
- Follow-up review question 2: How does the implementation guarantee that the appointment remains retrievable in SmartCareDataStore after cancellation (FR-07)?
- Follow-up review question 3: Does attempting to cancel a COMPLETED appointment raise ValueError while leaving status completely unchanged?
- Follow-up review question 4: Are whitespace-padded and empty/blank IDs explicitly verified with boundary tests?
- Follow-up review question 5: What specific tests ensure that absent IDs raise LookupError rather than silently returning None?
- Additional questions if useful: 

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | feature/<issue-id>-<short-description> (e.g., feature/fr02-patient-search) |
| Commit message convention | Imperative mood present tense: <Action> <component>: <description>  |
| PR size | Focused atomic changes limited to one feature/issue and its tests (under 100 lines changed) |
| Another-member review requirement | Mandatory review and sign-off by the other teammate; self-merging is strictly prohibited |
| Merge rule | Squash and merge or regular merge commit after all tests pass and approvals are granted |
| Significant Copilot disclosure rule | Document prompt, generated diff, human verification checks, and Accept/Modify/Reject decision in Section H |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement                          | Owner      | Acceptance criteria or precise link | Status     |
|------------|--------------------------------------|------------|-------------------------------------|------------|
| 1          | FR-02 Patient Search                 | MBLL02 | PatientService.find_patient returns stored instance, handles trimming, raises ValueError/LookupError  | Closed ||
| 2          | FR-06 & FR-07 Cancellation           | RUBAI21321 | AppointmentService.cancel_appointment transitions status, retains history, rejects invalid states  | Closed |
| 3          | Supporting FR-03 Practitioner Search | MBLL02 | PractitionerService.find_practitioner returns stored instance, trimmed, handles exceptions | Closed |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [https://github.com/MbLL02/4483_Assignment_3/pull/1]  Complete team agreement and issue activities in Stage 6 record
- Linked issue and requirement: Closes #1 (FR-02 Patient Search) and #3 (Supporting FR-03 Practitioner Search)
- Feature branch: feature/team-agreement
- Changed behaviour: Updated stage06/stage06_activities_and_evidence.md with verified repository details, starting SHA, issue specifications (FR-02, FR-06/07), commit quality classifications, over-scoped PR analysis, Copilot challenge criteria, team workflow agreements, and formative conceptual responses. No application code was altered.
- Meaningful commits: 64e3fcd — Complete team agreement and issue activities in Stage 6 record
- Test command, directory and observed result: Ran python -m pytest from project/; observed 8 passed (unchanged scaffold suite baseline confirmed)
- Another-member reviewer: Rubai21321
- Human observations recorded before Copilot: Inspected markdown formatting, verified table layouts, confirmed starting commit hash (64e3fcd), and ensured acceptance criteria explicitly cover error handling, trimming, and object identity rules
- Requirement, responsibilities, test assertions and unrelated-scope checks: Confirmed changes are strictly isolated to stage06/stage06_activities_and_evidence.md. Verified no stray files, personal credentials, or unnecessary external packages were added. Checked that the agreed team workflow defines peer-review gates, atomic commit standards, and clear Copilot disclosure policies.
- Key feedback: Reviewer confirmed all required sections (A through F, and L) were complete and requested merging to establish the shared base before starting feature branches
- Author response/change and verification: Accepted feedback; no code modifications required; pushed final documentation adjustments
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: Merged into main; merge commit SHA 64e3fcd
- Significant Copilot assistance: None (human-drafted documentation and team policy).
- Linked issue closure: No functional issues closed yet, backlog tracking active.
- Each member updated main: MBLL02: Pulled main on local machine, confirmed merge SHA 64e3fcd. Rubai21321: Pulled main on local machine, confirmed merge SHA.
- Integrated verification after merge: Command: python -m pytest, Working directory: project/, Observed result: 8 passed, Code SHA: 64e3fcd

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: Rubai21321 reviewing PR #1 (feature/team-agreement)
- Prompt/purpose and relevant issue/diff: Executed the required Part H review prompt in Copilot Chat using the diff of stage06/stage06_activities_and_evidence.md.
- Summary of output: Copilot flagged that the diff contained only evidence/documentation lines and lacked implementation or test code for FR-02/FR-03, warning that tests could not be verified from the documentation alone.
- Human check against actual code, requirements and tests: Verified that PR #1 was intentionally scoped exclusively to the team agreement and issue definitions (no application code was expected in this PR), confirming Copilot's observation was accurate regarding the absence of Python code
- Decision — Accept / Modify / Reject: Modify
- Reason: Copilot correctly identified that no code or test changes were present, but its warning assumed PR #1 should have contained code; human judgment clarified that PR #1 was deliberately a documentation/agreement PR before code implementation starts.
- Verification/evidence: Confirmed main.py and python -m pytest run locally with 8 passing scaffold tests, preserving the baseline

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: The PR diff only contains edits to stage06/stage06_activities_and_evidence.md. The document properly answers team metadata, issue specifications, workflow policies, and formative questions. No Python code or test files were changed, and the baseline 8 tests remain passing.
- Overlap: Both identified that the diff lacks application source code (smartcare/services.py) and test suites (tests/test_services.py).
- What did the human reviewer notice that Copilot did not: PR #1 is intentionally a non-code setup PR meant solely to establish the group workflow agreement and backlog before writing code
- What did Copilot identify that the human reviewer initially missed: Copilot flagged that approving a PR tagged with search acceptance criteria without attached automated tests creates a governance/evidence gap against Definition of Done standards.
- Unsupported or incorrect Copilot suggestion: Copilot's prompt inference that the PR might be incomplete was contextually incorrect because this branch was solely dedicated to documentation setup, but its caution was technically sound.
- Human judgement accepted, modified or rejected, and why: Modified: Accepted Copilot's observation that code is absent, but clarified that implementation belongs in subsequent dedicated feature branches (feature/lookup-services), keeping PR #1 atomic.
- Which evidence justified merge approval: Clean git diff with no unintended files, caches, or secrets committed. Complete responses in Sections A–F and L.

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: MBLL02
- Implementation: Authored feature/team-agreement setup branch and stage record draft. Implemented PatientService.find_patient and PractitionerService.find_practitioner in smartcare/services.py. Enforced input trimming, case sensitivity, and distinction between ValueError and LookupError.
- Testing: Created project/tests/test_services.py. Wrote unit tests verifying exact object identity (is), trimmed lookup, case sensitivity, missing ID rejection, and blank string validation.
- Review: Conducted line-by-line human diff review on PR #2 (AppointmentService.cancel_appointment). Verified that cancellation does not delete records and that completed appointments cannot be cancelled.
- Issue refinement: Created and specified GitHub Issue #1 (FR-02) and Issue #3 (supporting FR-03) with observable acceptance criteria
- Design and responsibility discussion: Clarified architectural boundary between SmartCareDataStore (returns None for missing keys) and PatientService (raises LookupError).
- Debugging or integration: Verified local baseline runs (python -m pytest with 8 passes). Tested merged main branch locally to confirm 14 total passing tests after integration. 
- Documentation or team support: Completed initial Sections A–F, K, and L in stage06/stage06_activities_and_evidence.md. Coordinated repository setup and tracked starting commit SHA (64e3fcd).

- Member: Rubai21321
- Implementation: Implemented AppointmentService.cancel_appointment in smartcare/services.py. Delegated state transition directly to Appointment.cancel() without direct property mutation or record deletion.
- Testing: Added cancellation test cases in project/tests/test_services.py. Tested successful cancellation status transition, same object return, retained history retrievability (FR-07), and exception handling for invalid/repeated transitions.
- Review: Conducted human review on PR #1 (feature/team-agreement) and PR #2 (feature/lookup-services). Executed mandatory GitHub Copilot comparison prompt for PR diffs and recorded comparative findings in Sections H and I.
- Issue refinement: Authored GitHub Issue #2 (FR-06 and FR-07) detailing cancellation contracts and retained history criteria.
- Design and responsibility discussion: Ensured appointment state invariants stay encapsulated within the Appointment domain class rather than in the service.
- Debugging or integration: Pulled updated main after each PR merge and verified local test suite execution. Verified that repeated cancellation attempts leave object state intact without partial mutation.
- Documentation or team support: Completed Section H (Copilot collaboration log) and Section I (human vs. AI review critique). Coordinated PR review approvals on GitHub.

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

A large number of commits does not necessarily mean a person has contributed effectively because commit frequency does not indicate anything about architectural quality, correctness, or value provided to the project. Many large numbers of commits are caused by unnecessary tasks such as fixing small typos, changing format, sending partially functional intermediate builds, or creating many separate commits for what should be a single piece of work. In addition, there is no way for the commit history to account for very important contributions that help projects succeed but do not involve coding, such as setting clear acceptance criteria, building positive and boundary tests, having architectural discussions, and line-by-line diffs. Overall, a person who writes fewer but well-thought out commits with proper testing and review makes much greater contribution to meeting the Definition of Done than a person with many unnecessary commits.

## L Stage 6 formative questions

1. What is version control?

Version control is a process that allows tracking all changes made to a program's source code over time, providing a history of its development through its revisions. Version control helps in collaborating with other programmers since different versions of the code will not be overwritten by others' changes. Moreover, version control provides a capability to view diffs, ensures accountability, and helps rollback to a known good version.

2. Why is a feature branch useful?

The use of a feature branch ensures that any development done will not interfere with the code in the main branch as well as any untested or problematic code. Moreover, a feature branch helps in establishing a clear diff which makes the review process easier.

3. What makes a commit a good engineering commit?

The commit in question should be atomic in its nature. This means that it reflects a particular change in the code which makes the repository function. The commit should contain only necessary files and not combine any unrelated actions like refactoring, dependencies or formatting with the main feature implementation. Lastly, the commit should have a clear imperative message which describes what has been done and why.

4. What is a pull request?

The pull request is a tool used to propose integration of a feature branch into a target integration branch, usually the main one. Pull request gives a separate collaborative workspace for team members to check diff, test code and discuss any design decisions. Thus, in the engineering process, pull requests represent a quality gate to check whether code has been reviewed by peers.

5. What is the purpose of code review?

Code review aims at validating whether the proposed code meets the acceptance criteria, doesn't break any architectural boundaries, and takes care of edge cases.

6. What does a Git diff show?

The output of a Git diff is the comparison line by line between two statuses, for example between two commits, two branches, or between a staged index and a working tree. The diff uses minuses for marking removed lines and pluses for added lines in order to show precise changes at the level of characters. Code reviewers depend on a diff in order to estimate changes' influence.

7. What is a Definition of Done?

A Definition of Done is a list of standards that should be achieved for an issue or a feature in order to consider it done. The definition of done requires not only coding of a feature but also unit testing, verification by automation, documenting, and review by peers. It guarantees that all increments that are being merged are ready for production and comply with system requirements.

8. What is the appropriate role of GitHub Copilot in pull-request review?

GitHub Copilot is an advisory assistant to point out any possible omissions, errors of syntax, edge cases, and lack of tests in a pull request diff. It is supposed to help and not replace the critical thinking of people; thus, human code reviewers should manually examine code and test results. It should be verified explicitly, declared openly, and accepted or rejected after considering.

9. Why should individual contribution not be judged only by commit count?

Commits counting refers to the frequency of code saves without regard to the technical complexity and business value of the deliverable code. Commits are easily manipulated via superficial edits, fixing typos repeatedly or splitting one logically cohesive action into several very small commits. Evaluation of work via commits does not account for critical tasks of an engineer, such as refining issues, discussions of the architecture, creating effective tests, and peer review.

10. What is the Stage 6 engineering rule?

Stage 6 engineering guideline assumes that the team should work on requirements using specific issues, create feature branches for working on particular features and verify all changes via automated testing. Unreviewed code should never be pushed to main and self-merging is not allowed. Every pull request should pass independent review by a colleague and receive evaluation via Copilot review.

## M Completion and handover

- Starting SHA: 64e3fcd
- Final Stage 6 code SHA: 64e3fcd
- Test command: python -m pytest -v
- Working directory: project/
- Observed result: 14 passed (8 scaffold starter tests + 6 newly added service tests)
- PR and another-member reviewer: PR https://github.com/MbLL02/4483_Assignment_3/pull/1 Reviewer Rubai21321.
- Unresolved issue or none: None
- Stage 7 handover status: ready for tutor checkpoint
- Final submitted SHA if later than tested SHA: Final submitted SHA records this evidence document update commit; it differs from the tested code SHA only by documentation additions in stage06/stage06_activities_and_evidence.md with no application code changes.

- [x] Three Stage 6 service targets completed and checked.
- [x] Original supplied tests retained and passing.
- [x] At least two focused issues link requirements and acceptance criteria.
- [x] Feature work reviewed by another member using the actual diff.
- [x] Human-first review and required Copilot comparison recorded.
- [x] Feedback resolved and approval recorded before merge.
- [x] Everyone pulled main and integrated checks passed.
- [x] Required activities, quiz responses and contribution notes completed.
- [x] Only synthetic data included; confidential peer material kept out.
- [x] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
