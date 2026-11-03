# Stage 7 Testing and Verification Record

Group/tutorial: Group 7 Thursday 2:30pm  Members: u3309151 MBLL02, u3313159 Rubai21321
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities
An AI assistant helped draft the section A and section N answers. We checked each one against our code and the handout before keeping it.

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | Register "P001" / "Alex Test"; it is returned and stored | Register a second patient with ID "P001"; ValueError raised | `data_store.find_patient("P001") is patient` and, after the duplicate attempt, the original name is unchanged |
| FR-05 Prevent practitioner conflict | Book the same practitioner at a different time, or a different practitioner at the same time; both succeed | Book the same practitioner at the same time as an existing SCHEDULED appointment; ValueError raised | `pytest.raises(ValueError)` and `len(data_store.list_appointments())` unchanged; the rejected ID is not stored |
| FR-06 Cancel appointment | Cancel a SCHEDULED appointment | Cancel it again, or cancel a COMPLETED appointment; ValueError raised | `appointment.status is AppointmentStatus.CANCELLED` after success; status unchanged after the failed attempt |
| FR-07 Retain cancelled history | After cancelling, look the appointment up again | Cancel an unknown ID; LookupError raised and no record created | `appointment_service.find_appointment("A1") is appointment` and its status is CANCELLED (not deleted or replaced) |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: Weak/unclear  Why: It can never fail, so it checks no behaviour at all. It only proves the test function ran.

`assert appointment is not None`
Judgement: Weak/unclear  Why: It only proves something was returned. It does not check the right object, its ID, status, participants or that it was stored.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: Strong for stated behaviour  Why: It checks the required FR-06 outcome directly. Limit: on its own it does not prove the record was retained (FR-07) or that the same object was returned.

`assert len(results) > 0`
Judgement: Weak/unclear  Why: It passes with wrong or extra results. It does not check which records were returned, how many were expected or their order.

`assert data_store.find_appointment('A1') is appointment`
Judgement: Strong for stated behaviour  Why: An identity check proves the exact stored object is retained and retrievable, not a copy or replacement. Limit: it says nothing about status unless paired with a status assertion.

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract:

| Input / state | Expected result | Supporting contract |
|---|---|---|
| Patient ID `""` | ValueError, nothing stored | `required_text`: IDs must be non-blank |
| Patient ID `"   "` (whitespace only) | ValueError, nothing stored | `required_text` trims, then rejects blank |
| Patient ID `" P001 "` | Stored/found as `"P001"` | IDs are trimmed |
| Lookup `"p001"` when `"P001"` exists | LookupError | IDs are case-sensitive |
| Name `"   "` | ValueError from Patient/Practitioner construction | Names must be non-blank after trimming |
| Same practitioner, same minute as a SCHEDULED appointment | ValueError, appointment count unchanged | FR-05 conflict rule |
| Same practitioner, one minute later | Booking succeeds | Conflict is exact date/time only |
| Different practitioner, same time | Booking succeeds | Conflict is per practitioner |
| Same practitioner/time as a CANCELLED appointment | Booking succeeds | Only SCHEDULED appointments conflict |
| Cancel an already CANCELLED appointment | ValueError, status stays CANCELLED | FR-06: only SCHEDULED may be cancelled |
| Cancel a COMPLETED appointment | ValueError, status stays COMPLETED | FR-06 guard in `Appointment.cancel` |
| Cancel blank ID / unknown ID | ValueError / LookupError | Stage 6 cancellation contract |

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | Asserts only `is not None`; passes even if the wrong patient or a copy is returned | Registering a patient returns the stored object: `find_patient("P001") is patient` and the name matches |
| 2 | Asserts only `is not None`; does not check status or retention | Cancelling a SCHEDULED appointment sets status to CANCELLED and `find_appointment(id) is appointment` |
| 3 | `assert True` can never fail, so it verifies nothing | Booking a conflicting slot raises ValueError and the appointment count is unchanged |
| 4 | Assumes SMS notifications exist; this is an invented requirement not in the baseline | Reject. Replace with a real criterion, e.g. cancelling a COMPLETED appointment raises ValueError and status is unchanged |
| 5 | Also tests invented SMS behaviour, likely needing mocks of something that does not exist | Reject. Replace with e.g. an unknown appointment ID raises LookupError and no record is created |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
Coverage only shows which lines ran during the tests, not whether the tests checked the right results. A test with `assert True` or `is not None` can execute every line and still pass when the behaviour is wrong. Coverage also cannot reveal missing requirements, untested boundary values or rules that were never implemented, because code that does not exist cannot be uncovered.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
Are we building the product right? It checks the software against its specification, requirements and acceptance criteria.

2. What question does validation answer?
Are we building the right product? It checks that the software meets the users' real needs and intended purpose.

3. What is a unit test?
A small automated test that checks one unit of behaviour, such as one method or class, in isolation with a clear expected result.

4. What is a pytest fixture?
A reusable setup function marked with `@pytest.fixture` that provides test data or objects (such as a fresh SmartCareDataStore) to any test that names it as a parameter, keeping tests independent.

5. What is parametrisation in pytest?
Using `@pytest.mark.parametrize` to run the same test with several input/expected-output pairs, such as several blank or whitespace IDs, without duplicating code.

6. What is regression testing?
Re-running the full existing test suite after a change to confirm that previously working behaviour has not been broken.

7. What does code coverage tell us, and what does it not prove?
It shows which lines or branches were executed by the tests. It does not prove the assertions are meaningful, that requirements are complete or that the software is correct.

8. What makes an assertion weak?
It can pass when the behaviour is wrong, for example `assert True`, `is not None` or `len(x) > 0`, because it does not check the specific required outcome.

9. What is the appropriate role of GitHub Copilot as a test assistant?
A suggestion tool for test ideas and drafts. Humans design the test categories first, then check every suggestion traces to a real requirement, uses strong assertions and does not invent rules, and run it before accepting. Copilot does not decide that tests are correct or that they passed.

10. What is the Stage 7 engineering rule?
Every test has to trace back to a real requirement or contract, be able to fail properly, and be run and recorded honestly during the full regression testing.

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]