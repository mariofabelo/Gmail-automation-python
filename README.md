## Gmail Automation for Gyms

A simple Python script to send an HTML email to a list of gyms loaded from a CSV file. It supports a safe "test mode" that prints emails to the console without sending.

### Features
- **Test mode**: Preview recipients, subject, and HTML body without sending
- **CSV-driven**: Reads `Gym` name and `Contact Email` columns
- **Gmail SMTP**: Uses Gmail with an App Password for secure sending

### Prerequisites
- **Python**: 3.8+
- **Pip**: to install dependencies
- **Gmail account** with 2‑Step Verification and an **App Password** for SMTP

### Installation
```bash
# (Optional) create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependency
pip install python-dotenv
```

### Configuration
1. Create a `.env` file in the project root with your Gmail credentials (App Password recommended):
```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_char_app_password
```
2. Prepare a CSV with at least these headers:
```csv
Gym,Contact Email
Acme Fitness,team@acmefitness.com
```
3. Update the CSV path in `send_emails_gyms.py` (near the bottom of the file) to point to your CSV. The script currently references an absolute path under `Downloads`.

### Usage
1. Open `send_emails_gyms.py` and set the mode:
   - `TEST_MODE = True` to preview output only (default)
   - `TEST_MODE = False` to actually send emails
2. Optionally customize `subject` and `body_template` (HTML allowed). The placeholder `{gym_name}` will be interpolated from the CSV.
3. Run the script:
```bash
python send_emails_gyms.py
```

### Notes and Tips
- **Gmail SMTP**: The script uses `smtp.gmail.com:465` with SSL.
- **App Password**: Required if your account has 2FA (recommended). Generate one under Google Account → Security → App passwords.
- **Rate limits**: Gmail has sending limits. The script sleeps 2 seconds between rows; consider increasing for large lists.
- **Encoding**: CSV is read with `utf-8-sig`. Keep header names exact: `Gym` and `Contact Email`.

### Troubleshooting
- Login/auth errors: Ensure you are using an App Password and that `.env` variables are loaded.
- Emails not sending, but no error: Check `TEST_MODE` is set to `False`.
- CSV rows skipped: Ensure both `Gym` and `Contact Email` columns are present and non-empty.

### Security
- Do not commit your `.env` file.
- Use an App Password instead of your main Gmail password.


