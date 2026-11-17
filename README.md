# Stav Fisher Gross — portfolio and CV

Static site. No build step, no framework, no dependencies. It deploys to GitHub Pages as is.

The design lives in the Figma file "Portfolio 26" and is built here from it.

## Text comes from Figma

Figma is the source for every word on the site. To bring Figma's text over after an edit there:

1. `env\Scripts\python tools\figma_text_sync.py prepare` writes `private/figma-sync/figma_check.js`.
2. Run that code with the Figma tool (use_figma) on "Portfolio 26". It returns, per page, the lines
   that are new in Figma and the numbers of site lines Figma no longer has.
3. `env\Scripts\python tools\figma_text_sync.py show <page> <n> ...` prints those site lines.
4. Change the text where it lives: `index.html`, `about.html`, `cv.html`, `work/index.html`, or for the
   password-protected parts `private/home-work.html`, `private/cases/<slug>.html` and `CASES` in
   `tools/lock_cases.py`. Then run `tools/lock_cases.py`, and reprint the CV PDF if the CV changed.

The nav, the footer and the password form always show up as small differences, because Figma splits
them into separate text boxes. Which frame belongs to which page is listed in the script.

The CV PDF is the CV page printed. After changing `cv.html`, run the local server and print it
again (Microsoft Edge, which is on every Windows machine):

```
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --no-pdf-header-footer --print-to-pdf="%CD%\assets\stav-fisher-gross-cv.pdf" http://localhost:8321/cv.html
```

## Editing the project list or a case study

The project list and every case study are password protected (one password opens all of them),
because this repo is public and a form in front of plain HTML protects nothing. A visitor signs in
once, and the rest opens without asking again for that browser session.

Edit the plaintext, then rebuild:

- the project list: `private/home-work.html`, with the card screens in `private/assets/cards/`
- a case study: `private/cases/<slug>.html`, with its images in `private/assets/<slug>/`

```
env\Scripts\python tools\lock_cases.py
```

A new case study also needs an entry in `CASES` at the top of `tools/lock_cases.py` and a password
under its slug in `private/passwords.json`. An entry with `listed=False` is built but left out of
the "Next case study" links.

Lose `private/` and the published pages can still be decrypted with the passwords, but nothing else
can recover them.

## Deployment

The repo is named `stav-fg.github.io`, so GitHub Pages publishes the default branch at that address.
There is no workflow to configure.

## Layout

Committed, because it is the published website:

```
index.html              the landing page
about.html              about me and the timeline
cv.html                 single column; printed, it is assets/stav-fisher-gross-cv.pdf
work/                   My work (index.html) and one file per case study, encrypted (built, do not edit by hand)
css/site.css            the whole design system, tokenised on :root
js/unlock.js            decrypts a case study in the browser once the password is right
assets/                 web-sized imagery; assets/site/ holds the public images, assets/locked/ the encrypted screens
tools/                  the build and sync scripts
```

Local only, never committed, because a GitHub Pages repo is public:

```
source-material/        every input
private/                plaintext project list and case studies, their images, the passwords and the working notes
```
