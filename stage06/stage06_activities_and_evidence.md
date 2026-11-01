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

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

[response]

## L Stage 6 formative questions

1. What is version control?

[response]

2. Why is a feature branch useful?

[response]

3. What makes a commit a good engineering commit?

[response]

4. What is a pull request?

[response]

5. What is the purpose of code review?

[response]

6. What does a Git diff show?

[response]

7. What is a Definition of Done?

[response]

8. What is the appropriate role of GitHub Copilot in pull-request review?

[response]

9. Why should individual contribution not be judged only by commit count?

[response]

10. What is the Stage 6 engineering rule?

[response]

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
