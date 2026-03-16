# Software Testing Project Documentation

**Name:** Portik Lukacs-Krisztian  

---

## 1. The Description of the Selected Unit Testing Suite 

### Motivations 
For this project, the primary focus is unit testing, during which a small piece of code is tested and evaluated to see whether it is fit for use. The testing suite selected for this project is `pytest`. 

This framework was chosen because:
* It is one of the most widely used open-source Python 3 testing frameworks.
* It allows for creating compact and simple test suites.
* It supports unit testing, functional testing, and API testing.
* It is highly extensible by using plugins.
* It has a very large active community.

### Installation 
The testing environment was set up using a virtual environment[: 23]. The exact commands used in the terminal were:

1. Create the virtual environment: `python3 -m venv pytest-env` 
2. Activate the virtual environment: `source pytest-env/bin/activate`  (or `.\pytest-env\Scripts\activate` on Windows).
3. Install pytest: `pip3 install pytest` 

---

## 2. The Description of the Unit Test Repository 

### How is data structured in your repository? 
The repository is structured to separate the application code from the unit tests. 
The application codebase provides an oversimplified employee management software consisting of the `Employee` class, the `Relations Manager` class, and the `EmployeeManager` class. 

Our test files are kept separate and follow the `pytest` naming convention:
* `test_relations_manager.py`: Contains tests for the team and leadership logic.
* `test_employee_manager.py`: Contains tests for salary calculations and email notifications.

---

## 3. The Description of Each Developed Unit Test 

### Employee Relations Manager Tests 

**Test 1: Team Leader John Doe**
* **Input:** Fetch the employee named John Doe.
* **Expected Output:** Check if there is a team leader called John Doe whose birthdate is 31.01.1970.

**Code:**
```python
def test_john_doe_leader_and_birthdate(rm):
    john = get_employee_by_name(rm, "John", "Doe")
    
    assert john is not None
    assert rm.is_leader(john) is True
    assert john.birth_date == datetime.date(1970, 1, 31)
```

`vv_proj/relations_manager_testpy::test_john_doe_leader_and_birthdate`
<span style="color: green;">**PASSED**[58%]</span>

**Test 2: John Doe's Team Members**
* **Input:** Fetch the team members for John Doe.
* **Expected Output:** Check if John Doe's team members are Myrta Torkelson and Jettie Lynch.

**Code**
```python
def test_john_doe_team_members(rm):
    john = get_employee_by_name(rm, "John", "Doe")
    myrta = get_employee_by_name(rm, "Myrta", "Torkelson")
    jettie = get_employee_by_name(rm, "Jettie", "Lynch")
    
    team_member_ids = rm.get_team_members(john)
    
    assert myrta.id in team_member_ids
    assert jettie.id in team_member_ids

```
`vv_proj/relations_manager_test.py::test_john_doe_team_members` <span style="color: green;">**PASSED**[66%]</span>