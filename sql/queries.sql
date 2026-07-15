-- 1. Total Applications
SELECT COUNT(*) AS Total_Applications
FROM loan_data;

-- 2. Loan Approval Count
SELECT Loan_Status,
COUNT(*) AS Total
FROM loan_data
GROUP BY Loan_Status;

-- 3. Average Loan Amount
SELECT AVG(LoanAmount) AS Average_Loan
FROM loan_data;

-- 4. Highest Applicant Income
SELECT MAX(ApplicantIncome)
FROM loan_data;

-- 5. Lowest Applicant Income
SELECT MIN(ApplicantIncome)
FROM loan_data;

-- 6. Average Applicant Income
SELECT AVG(ApplicantIncome)
FROM loan_data;

-- 7. Loan Approval by Gender
SELECT Gender,
Loan_Status,
COUNT(*)
FROM loan_data
GROUP BY Gender, Loan_Status;

-- 8. Loan Approval by Education
SELECT Education,
Loan_Status,
COUNT(*)
FROM loan_data
GROUP BY Education, Loan_Status;

-- 9. Loan Approval by Property Area
SELECT Property_Area,
Loan_Status,
COUNT(*)
FROM loan_data
GROUP BY Property_Area, Loan_Status;

-- 10. Top 10 Highest Loan Amounts
SELECT Loan_ID,
LoanAmount
FROM loan_data
ORDER BY LoanAmount DESC
LIMIT 10;