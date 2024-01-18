import pandas as pd



# SF Salaries Exercise

# Read Salaries.csv as a dataframe called sal
file_example = "resources/Salaries.csv"
sal = pd.read_csv(file_example)

# Check the head of the DataFrame
print(sal.head())
print("\n")

# Use the .info() method to find out how many entries there are
sal.info()

# What is the average BasePay ?
print(sal['BasePay'].mean())

# What is the highest amount of OvertimePay in the dataset ?
print(sal['OvertimePay'].max())

# What is the job title of JOSEPH DRISCOLL ?
# Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a
# lowercase Joseph Driscoll)
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

# How much does JOSEPH DRISCOLL make (including benefits)?
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

# What is the name of highest paid person (including benefits)?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])
# alternative = print(sal.loc[sal['TotalPayBenefits'].idxmax()])

# What is the name of lowest paid person (including benefits)?
# Do you notice something strange about how much he or she is paid?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['TotalPayBenefits'])

# What was the average (mean) BasePay of all employees per year? (2011-2014)?
print(sal.groupby('Year').mean()['BasePay'])

# How many unique job titles are there?
print(sal['JobTitle'].nunique())

# What are the top 5 most common jobs?
print(sal['JobTitle'].value_counts().head())

# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one
# occurence in 2013?)
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

# How many people have the word Chief in their job title? (This is pretty tricky)
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

# Bonus: Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len', 'TotalPayBenefits']].corr())
