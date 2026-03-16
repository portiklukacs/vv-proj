import pytest
import datetime
from unittest.mock import patch, MagicMock

from employee import Employee
from employee_manager import EmployeeManager 

@patch('employee_manager.datetime')
def test_regular_employee_salary(mock_datetime):
    mock_datetime.date.today.return_value = datetime.date(2018, 1, 1)
    
    mock_rm = MagicMock()
    mock_rm.is_leader.return_value = False
    
    em = EmployeeManager(mock_rm)
    
    emp = Employee(id=99, first_name="Regular", last_name="Guy", 
                   birth_date=datetime.date(1970, 1, 1), 
                   hire_date=datetime.date(1998, 10, 10), 
                   base_salary=1000)
   
    salary = em.calculate_salary(emp)
    assert salary == 3000

@patch('employee_manager.datetime')
def test_team_leader_salary(mock_datetime):
    mock_datetime.date.today.return_value = datetime.date(2018, 1, 1)
    
    mock_rm = MagicMock()
    mock_rm.is_leader.return_value = True
    mock_rm.get_team_members.return_value = [101, 102, 103]
    
    em = EmployeeManager(mock_rm)
    
    leader = Employee(id=100, first_name="Leader", last_name="Lady", 
                      birth_date=datetime.date(1980, 1, 1), 
                      hire_date=datetime.date(2008, 10, 10), 
                      base_salary=2000)
    
    salary = em.calculate_salary(leader)
    assert salary == 3600

@patch('employee_manager.datetime')
def test_salary_email_notification(mock_datetime, capsys):
    mock_datetime.date.today.return_value = datetime.date(2018, 1, 1)
    
    mock_rm = MagicMock()
    mock_rm.is_leader.return_value = True
    mock_rm.get_team_members.return_value = [101, 102, 103]
    
    em = EmployeeManager(mock_rm)
    leader = Employee(id=100, first_name="Leader", last_name="Lady", 
                      birth_date=datetime.date(1980, 1, 1), 
                      hire_date=datetime.date(2008, 10, 10), 
                      base_salary=2000)
   
    em.calculate_salary_and_send_email(leader)
    
    captured = capsys.readouterr()
   
    expected_message = "Leader Lady your salary: 3600 has been transferred to you."
    assert expected_message in captured.out