import pytest
from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService


def test_find_patient_success_and_identity():
    store = SmartCareDataStore()
    service = PatientService(store)
    registered = service.register_patient("P1", "Jane Doe")

    result = service.find_patient("P1")
    assert result is registered
    assert result.patient_id == "P1"
    assert result.name == "Jane Doe"


def test_find_patient_trims_whitespace():
    store = SmartCareDataStore()
    service = PatientService(store)
    registered = service.register_patient("P1", "Jane Doe")

    result = service.find_patient("   P1   ")
    assert result is registered


def test_find_patient_case_sensitive():
    store = SmartCareDataStore()
    service = PatientService(store)
    service.register_patient("P1", "Jane Doe")

    with pytest.raises(LookupError):
        service.find_patient("p1")


def test_find_patient_not_found_raises_lookup_error():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(LookupError):
        service.find_patient("NONEXISTENT")


def test_find_patient_invalid_blank_id_raises_value_error():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(ValueError):
        service.find_patient("")

    with pytest.raises(ValueError):
        service.find_patient("    ")


def test_find_practitioner_success_and_identity():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    registered = service.register_practitioner("DR1", "Dr. Smith", "Cardiology")

    result = service.find_practitioner("DR1")
    assert result is registered
    assert result.practitioner_id == "DR1"
    assert result.name == "Dr. Smith"
    assert result.specialty == "Cardiology"


def test_find_practitioner_trims_whitespace():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    registered = service.register_practitioner("DR1", "Dr. Smith", "Cardiology")

    result = service.find_practitioner("  DR1  ")
    assert result is registered


def test_find_practitioner_case_sensitive():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    service.register_practitioner("DR1", "Dr. Smith", "Cardiology")

    with pytest.raises(LookupError):
        service.find_practitioner("dr1")


def test_find_practitioner_not_found_raises_lookup_error():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(LookupError):
        service.find_practitioner("DR999")


def test_find_practitioner_invalid_blank_id_raises_value_error():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(ValueError):
        service.find_practitioner("")

    with pytest.raises(ValueError):
        service.find_practitioner("   ")