# Vulnerable Python Application - Security Testing Demo

This repository contains an intentionally vulnerable Python Flask application used to demonstrate various security testing tools and DevSecOps practices. **WARNING: This application contains serious security vulnerabilities. DO NOT use in production!**

## Security Issues Demonstrated

1. SAST (Static Application Security Testing) Issues:

   - Hardcoded secrets
   - Weak password hashing (MD5)
   - SQL injection vulnerabilities
   - Command injection possibilities
   - Debug mode enabled in production

2. SCA (Software Composition Analysis) Issues:

   - Outdated dependencies
   - Known vulnerable packages
   - Insecure package versions

3. Other Security Issues:
   - Server-Side Template Injection
   - Unsafe deserialization
   - Path traversal vulnerabilities
   - Weak JWT implementation

## Repository Structure

```
vulnerable-python-app/
├── app.py              # Vulnerable Flask application
├── requirements.txt    # Python dependencies
├── .github/
│   └── workflows/
│       └── security-scan.yml  # GitHub Actions security workflow
└── README.md
```

## Security Tools Used

1. SAST Tools:

   - Bandit: `bandit -r .`
   - Pylint: `pylint --recursive=y .`
   - Semgrep: Uses `p/python` and `p/security-audit` rulesets

2. Dependency Scanning:

   - Safety: `safety check`
   - Snyk (requires token): Comprehensive dependency scanning

3. DAST Tools:

   - OWASP ZAP: Dynamic application security testing

4. Secret Scanning:
   - GitLeaks: Scans for exposed secrets

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/vulnerable-python-app.git
cd vulnerable-python-app
```

2. Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Security Scans Locally

1. SAST with Bandit:

```bash
pip install bandit
bandit -r . -f json -o bandit-results.json
```

2. Dependencies check with Safety:

```bash
pip install safety
safety check
```

3. Run Pylint:

```bash
pip install pylint
pylint --recursive=y .
```

## GitHub Actions Workflow

The repository includes a GitHub Actions workflow that automatically runs security scans on push and pull requests. To use it:

1. Add required secrets to your GitHub repository:

   - `SNYK_TOKEN` (if using Snyk)

2. The workflow will run automatically on push/PR to main branch

3. Check the Actions tab in GitHub for scan results

## Warning

This application is intentionally vulnerable and is meant for educational purposes only. It contains serious security issues and should never be deployed in a production environment.

## Contributing

Feel free to suggest improvements or add new security tests by creating a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Resources

- [Python Security Best Practices](https://python-security.readthedocs.io/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Snyk Documentation](https://docs.snyk.io/)
