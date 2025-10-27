# Repository Guidelines

## Project Structure & Module Organization
- Static quiz engine lives in `quiz-template.html`, which bundles the HTML, CSS, and JavaScript for flashcards, quizzes, and progress tracking.
- `index-launcher.html` is the entry point; whenever you add a new dataset, update its card list so the launcher mirrors available content.
- Content JSON files (e.g., `ciencias-u1-content.json`, `example-historia.json`, `ingles.json`) sit at the repo root. Start from `template-empty.json` and cross-check fields with `content-schema.json`.
- Reference docs (`README.md`, `QUICK-START.md`, `WORKFLOW.md`, deployment guides) describe authoring workflows—update them alongside UX changes.

## Build, Test, and Development Commands
- `python3 -m http.server 8000` — Serve the repository locally to avoid CORS when fetching JSON; open `http://localhost:8000/index-launcher.html`.
- `open index-launcher.html` (macOS) or `xdg-open index-launcher.html` — Quick smoke test of the launcher UI after minor HTML tweaks.
- `open 'quiz-template.html?content=meu-quiz.json'` — Launch a specific dataset while iterating on questions.
- `cp template-empty.json novo-conteudo.json` — Scaffold a fresh quiz payload before editing.

## Coding Style & Naming Conventions
- Keep two-space indentation across HTML, CSS, and inline JS as already established in `quiz-template.html`; strip trailing spaces before committing.
- Use descriptive camelCase for functions and variables (`loadContent`, `initializeQuiz`), reserving UPPER_SNAKE for global state (`CARDS`, `CONTENT_KEY`).
- JSON keys stay lowerCamelCase (`metadata`, `trueFalse`), with distractor maps keyed by stringified numeric IDs (`"1"`, `"2"`). Match naming patterns like `*-content.json` for new files.
- Extend styling through existing CSS custom properties at the top of each HTML file instead of introducing unreferenced colors.

## Testing Guidelines
- Manual QA: start the local server, open `index-launcher.html`, load each affected quiz, and cycle through Cartões, Teste Rápido, and Verdadeiro/Falso modes.
- Monitor the browser console for fetch or parsing errors; confirm the loading screen hides, progress UI updates, and no buttons remain disabled.
- Validate new JSON against `content-schema.json` (e.g., `npx ajv validate -s content-schema.json -d novo-conteudo.json`) or a comparable schema tool before pushing.
- Ensure `localStorage` keys keep the `QUIZ_<unit>_<version>` pattern, and verify export/import still succeeds after metadata changes.

## Commit & Pull Request Guidelines
- Follow the imperative style visible in history (`Add`, `Remove`, `Adjust`), keep subjects under 72 characters, and scope commits to a single theme (engine logic vs. content).
- Detail impacted quizzes or UI sections in commit bodies when necessary, and note any documentation updates triggered by UI changes.
- Pull requests should link to issues/tasks, enumerate manual test steps (launcher + targeted dataset), and include screenshots or GIFs for visual tweaks.
- When introducing new datasets, paste the `metadata` block in the PR description and flag any unconventional distractor rules reviewers must verify.

## Content Authoring Tips
- Add new JSON files to the launcher immediately so users discover them; align card copy with existing tone and badge labels.
- Keep distractors plausible, language-consistent, and grounded in common misconceptions—mirror phrasing from `ciencias-u1-content.json` for cohesion.
