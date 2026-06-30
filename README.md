This is my second task of Code alpha internship in cyber security domain.
About the Task
--------------
Task Name: Secure Coding Review

Objective
---------
The objective of this task is to review an application's source code, identify security vulnerabilities, and recommend secure coding practices to make the application safer.
Application Chosen

Programming Language: Python
Application: Login Authentication System

What I Did
----------
*Created a simple Python login application.
*Reviewed the code manually to identify security vulnerabilities.
*Found common security issues.
*Suggested secure coding practices.
*Improved the code by implementing security measures.

Vulnerabilities Found
---------------------
1. Hardcoded Credentials
Issue: Username and password are written directly in the code.

Risk: Anyone who accesses the source code can see the credentials.

Solution: Store credentials securely using a database or environment variables, and store passwords as hashes.

2. Plain Text Password
Issue: Passwords are stored or compared directly.

Risk: If the code is exposed, attackers can read the password.

Solution: Use SHA-256 or bcrypt to hash passwords before storing or comparing them.

3. Unlimited Login Attempts
Issue: Users can try unlimited passwords.

Risk: Makes brute-force attacks possible.

Solution: Limit login attempts to 3 and lock the account after repeated failures.

4. No Input Validation
Issue: User input is accepted without validation.

Risk: May lead to security problems in larger applications.

Solution: Validate and sanitize all user inputs.

Security Improvements Implemented
---------------------------------
*Used the hashlib module to hash passwords with SHA-256.
*Limited login attempts to three.
*Compared hashed passwords instead of plain-text passwords.
*Displayed generic error messages instead of revealing sensitive information.
