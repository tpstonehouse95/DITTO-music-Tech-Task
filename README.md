# How to Run

## 1. Setup Virtual Environment

```bash
python -m venv .venv
```

## 2. Activate Virtual Environment

**Mac/Linux:**
```bash
source .venv/bin/activate
```

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
.\.venv\Scripts\Activate.ps1
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

## 3. Run the Tests

- **Standard headless run:** `pytest`
- **Visual run (headed):** `pytest --headed`

---

# Assumptions

- **Environmental constraints:** Black-box testing without a CAPTCHA bypass key or backend API access.
- **Component standardization:** Email and password validation use shared front-end components. The Signup page was prioritized as it exercises the full set of rules (length, complexity, format).
- **Browser compatibility:** Chromium was chosen as the primary target browser for this task.

---

# Approach & Trade-offs

- **Negative testing:** Focus on resilience—Sign Up disabled and specific error banners when requirements (e.g. password length) are not met.
- **Page Object Model (POM):** Strict POM so UI locators live in page objects; CSS changes require updates in one place.
- **User-centric locators:** Prefer `get_by_role` and `get_by_text` over XPath/CSS for stability under HTML refactors.
- **Test data isolation:** UserFactory for unique, dynamic data to avoid test interdependence.
- **Test data strategy:** Each run creates a unique user in production; in staging, API cleanup or DB rollback would keep the environment clean.
- **Dependency injection:** Page objects created in `conftest.py` fixtures to keep tests DRY and maintainable.

---

# Further Enhancements

- **CI/CD:** Run the suite in CI (e.g. on every PR) and publish HTML reports.
- **API testing:** Backend checks to confirm user records are created.
- **Accessibility:** Integrate axe-core for signup flow accessibility (e.g. screen readers, keyboard navigation).
