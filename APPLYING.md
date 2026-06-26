# Auto-apply (local)

The daily bot finds and emails you internships. This tool **applies** to them —
it opens each job's application form in a real browser and fills your details.
It defaults to review-before-submit for every form. Cover letters and auto-submit
are explicit opt-ins because they transmit personal data to third parties.

It runs **on your machine** (not GitHub Actions) so you can watch the browser,
solve any CAPTCHA, and review before anything is submitted.

## How it decides to submit

- **Default:** fill fields, then wait for you to review and press Enter to submit
  (or `s` to skip, `q` to quit).
- **Opt-in auto-submit:** pass `--auto-submit --mode auto_simple_review_hard` to
  auto-submit forms with no remaining required fields and pause on harder forms.

Other modes: `review_all` (always pause), `auto_all` (submit everything — riskiest,
requires `--auto-submit`).

## What you need to provide
1. **Your resume** — drop the PDF in `resumes/` (e.g. `resumes/your_name.pdf`).
2. **Your profile** — `cp config/profile.example.yaml config/profile.yaml` and fill it in.
   Required: `full_name`, `email`, `resume_path`. Strongly recommended: `phone`,
   `school`, `graduation_date`, `linkedin`, `github`, `current_location`, and a
   concrete `summary` (this grounds the cover letter in your real experience).
   Both files are gitignored — your data never leaves your machine.
3. **(Optional) Gemini API key** for cover letters — `GEMINI_API_KEY` in `.env`.
   Pass `--cover-letter` when you want to send profile/job context to Google for
   generated cover letters.

## Setup
```bash
source .venv/bin/activate
pip install -r requirements.txt -r requirements-apply.txt
python -m playwright install chromium     # one-time browser download
```

## Use it
```bash
# SAFEST FIRST RUN: fill forms but never submit — see exactly what it does
python -m src.apply --prepare-only --limit 3

# Real run, visible browser, review before every submit
python -m src.apply

# Optional: auto-submit simple forms after you trust the workflow
python -m src.apply --auto-submit --mode auto_simple_review_hard

# Useful flags
python -m src.apply --company Stripe        # only this company
python -m src.apply --category quant         # only quant roles
python -m src.apply --limit 5                # cap this run
python -m src.apply --mode review_all        # pause on every form
python -m src.apply --cover-letter           # opt into Gemini cover-letter generation
```

It only considers jobs whose ATS it can fill (**Greenhouse, Lever, Ashby**) and
that you haven't already applied to. Every attempt is logged to
`data/applications.json` (status: submitted / reviewed / skipped / failed /
prepared), so re-runs never double-apply.

## Scope & honest expectations
- **Coverage:** Greenhouse / Lever / Ashby today. Workday and custom career sites
  aren't auto-fillable yet — you'll still get those in the email digest to apply by hand.
- **Field filling is best-effort.** Forms vary; the tool fills what it confidently
  recognizes and flags the rest for your review. Verified working on live Greenhouse
  forms (fills name/email/phone/links/school + resume, detects custom questions).
  Expect to tune selectors as you hit new form variants — the review step is the safety net.
- **CAPTCHAs / logins:** solve them yourself in the visible browser, then continue.
- **Cover letters** are AI-drafted (Gemini 2.5 Flash) from your `summary` — **read
  them before submit**; the tool is instructed never to invent experience, but you
  own what goes out.

## Etiquette / ToS
This automates **your own** applications at modest volume. It uses each ATS's normal
public application form — no CAPTCHA-bypass, no bot-detection evasion. Many career
sites' terms restrict automated submission; review-before-submit (the default for
non-trivial forms) keeps a human in the loop. Apply thoughtfully — quality over volume.
