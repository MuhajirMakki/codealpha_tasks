# Secure Coding Review Report

## 1. Executive Summary
An application security audit was performed on `vulnerable_app.py` using Static Application Security Testing (SAST) via **Bandit** and manual code inspection. Three critical vulnerabilities (SQL Injection, Command Injection, and Hardcoded Secrets) were identified and successfully remediated in `secure_app.py`. The final scan of the secure code reduced all High and Medium risks to zero, leaving only three Low-severity informational alerts that have been manually verified as safe.

## 2. Audit Methodology
* **Target Language:** Python 3.12
* **Tools Used:** Bandit (v1.9.4) for automated static analysis.
* **Manual Inspection:** Code logic review against OWASP Top 10 vulnerabilities.

## 3. Initial Findings & Remediations (`vulnerable_app.py`)

### Finding 1: OS Command Injection (High Severity)
* **CWE:** CWE-78
* **Description:** Bandit flagged `os.system()` taking unfiltered user input (`ip_address`). An attacker appending `; ls -la` executes arbitrary terminal commands on the host server.
* **Remediation:** Replaced `os.system()` with the `subprocess.run()` module, explicitly passing arguments as a list without invoking a shell.

### Finding 2: SQL Injection (Medium Severity)
* **CWE:** CWE-89
* **Description:** Bandit flagged string formatting (`f"SELECT..."`) used to construct SQL queries. An attacker can inject `' OR '1'='1` to bypass authentication or dump the database.
* **Remediation:** Implemented parameterized queries (`?` placeholders). The `sqlite3` library now treats the input strictly as data, not executable code.

### Finding 3: Hardcoded Secrets (Critical Severity)
* **CWE:** CWE-798
* **Description:** Identified via manual inspection (bypassed automated scan). An API key was hardcoded in plain text.
* **Remediation:** Removed the hardcoded string and utilized the `os.getenv()` library to pull the secret securely from the server's environment variables.

## 4. Final Scan Results & Accepted Risks (`secure_app.py`)
A rescan of the remediated `secure_app.py` script yielded **0 High** and **0 Medium** severity issues. Bandit flagged three **Low** severity informational warnings:
* **[B404]** Consider possible security implications associated with the subprocess module.
* **[B607]** Starting a process with a partial executable path (`ping`).
* **[B603]** Subprocess call - check for execution of untrusted input.

**Security Analyst Conclusion:** 
These three Low-severity findings are **False Positives / Accepted Risks**. Because `subprocess.run(["ping", "-c", "1", ip_address], check=True)` passes arguments strictly as a list and does not invoke the shell (`shell=True` is omitted by default), the OS will not evaluate any injected shell operators (such as `;`, `&&`, or `|`). The remediation is effective, and the code is secure.