import pandas as pd

############################# Question 1 ######################################

def higher_salary_emp():

    """
    This method returns a list contained the give the name of employees,
    whose salaries are greater than their immediate manager’s

    :param: None
    :return: list

    """

    employee = pd.read_excel('Employee_sample.xlsx')
    df1 = employee.merge(right=employee, left_on='manager_id', right_on='id')
    df2 = df1[df1['Salary_x'] > df1['Salary_y']]
    list_name = list(df2['Name_x'])

    return list_name

def avg_salary_of_non_manager():

    """
    This method returns the average salary of employees who do not manage anyone

    :param: None
    :return: float

    """

    employee = pd.read_excel('Employee_sample.xlsx')
    df1 = employee.merge(right=employee, left_on='manager_id', right_on='id')
    cond = employee['id'].isin(df1['id_y'])
    employee.drop(employee[cond].index, inplace=True)

    avg_salary = employee['Salary'].mean()


    return avg_salary

############################# Question 2 ######################################

# v = 'Kata'

def exists(v):

    try:
        v = v
    except NameError:
        print("well, it WASN'T defined after all!")
    else:
        print("sure, it was defined.")

############################# Question 3 ######################################

def PascalTriangle(n):
   if n>= 1:
       trow = [1]
       y = [0]
       for x in range(n):
          print(trow)
          trow=[left+right for left,right in zip(trow+y, y+trow)]
   else:
       print('n must be greater than 0')
   return

