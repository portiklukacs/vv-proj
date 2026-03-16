import pytest
import datetime
from employee import Employee
from relations_manager import RelationsManager  

@pytest.fixture
def rm():
    """Sets up the RelationsManager before each test."""
    return RelationsManager()

def get_employee_by_name(rm, first_name, last_name):
    """Helper function to find an employee by name since the class doesn't have one."""
    for emp in rm.get_all_employees():
        if emp.first_name == first_name and emp.last_name == last_name:
            return emp
    return None

def test_john_doe_leader_and_birthdate(rm):
    john = get_employee_by_name(rm, "John", "Doe")
    
    assert john is not None
    assert rm.is_leader(john) is True
    assert john.birth_date == datetime.date(1970, 1, 31)

def test_john_doe_team_members(rm):
    john = get_employee_by_name(rm, "John", "Doe")
    myrta = get_employee_by_name(rm, "Myrta", "Torkelson")
    jettie = get_employee_by_name(rm, "Jettie", "Lynch")
    
    team_member_ids = rm.get_team_members(john)
    
    assert myrta.id in team_member_ids
    assert jettie.id in team_member_ids

def test_tomas_andre_not_in_johns_team(rm):
    john = get_employee_by_name(rm, "John", "Doe")
    tomas = get_employee_by_name(rm, "Tomas", "Andre")
    
    team_member_ids = rm.get_team_members(john)
    
    assert tomas.id not in team_member_ids

def test_gretchen_walford_salary(rm):
    gretchen = get_employee_by_name(rm, "Gretchen", "Watford") 
    
    assert gretchen is not None
    assert gretchen.base_salary == 4000

def test_tomas_andre_not_leader_and_retrieval_behavior(rm):
    tomas = get_employee_by_name(rm, "Tomas", "Andre")
    assert rm.is_leader(tomas) is False

    team_members = rm.get_team_members(tomas)
    assert team_members is None

def test_jude_overcash_not_in_database(rm):
    jude = get_employee_by_name(rm, "Jude", "Overcash")
    
    assert jude is None