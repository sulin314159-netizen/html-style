# html-style

**Ten visual styles for HTML pages and 16:9 decks — one token set, two media.**

`html-style` is an Agent Skill that turns a single source of content into a polished web page or a presentation deck. Each style is a calibrated set of design tokens extracted from real sites and real deck tools, not generic "make it pretty" instructions.

Most AI-generated pages look the same: three identical cards, a purple gradient, emoji icons, and a wall of centered text. This skill exists to prevent that. It gives the model a small, opinionated design system per style, a checklist of failure modes, and two starter skeletons, so output stays consistent instead of drifting every run.

---

## Styles

| # | Style | Identifier | Best for |
|---|-------|------------|----------|
| 01 | Paper Minimal | `moneyai` | Product pages, docs, long reads |
| 02 | Editorial Pop | `muse` | Editorial, young brands, one-screen stories |
| 03 | Tech Blue | `deepseek` | Developer tools, AI products, docs |
| 04 | Black Stage | `openai` | Launches, bold dark pages |
| 05 | Gradient Dream | `gradient` | SaaS, campaigns, Chinese-market landing pages |
| 06 | Warm Paper | `echo` | Memoirs, memorials, storytelling |
| 07 | Ink & Paper | `frontend-slides` | Long-form editorial pages, narrative decks |
| 08 | Soft Gradient | `htmlppt-pitch` | Pitch decks, business reviews |
| 09 | Free Canvas | `open-slide` | Portfolios, design talks, strong personal style |
| 10 | Academy Warm | `goodpage` | Education, courses, knowledge products |

Every style ships with:

- exact color tokens, type scale, spacing and radius
- layout rules for **web** and **deck** separately
- a text-density budget (some styles are deliberately sparse)
- a list of anti-patterns

---

## Install

Clone the repository somewhere, then place the folder in your agent's skills directory.

```bash
git clone https://github.com/sulin314159-netizen/html-style.git
```

**DeepSeek Harness**

```bash
cp -r html-style ~/.dsh/skills/html-style
```

Windows: `C:\Users\<you>\.dsh\skills\html-style`

**Claude Code / other Agent Skills runtimes**

```bash
cp -r html-style ~/.claude/skills/html-style
```

Restart the session if the runtime indexes skills at startup.

---

## Usage

Ask naturally. The skill picks a style, or proposes two or three when the content does not imply one.

```
Make a landing page for a local-first note-taking app in Paper Minimal.
Turn this outline into a 10-slide deck using Soft Gradient.
This page looks generic — restyle it with Tech Blue and keep the copy.
Build a one-screen announcement in Editorial Pop.
```

Web pages are normal documents: they scroll, and each section is at least one viewport tall.

Decks are fixed 16:9 canvases:

- `←` `→` `↑` `↓` `Space` `PageUp` `PageDown` to navigate
- mouse wheel pages when content fits; scrolls content first when it does not
- page number bottom-right, `?slide=N` and `#/N` deep links
- one idea per slide, no scrollbars

---

## How it works

Progressive disclosure, in three layers:

1. `SKILL.md` — required entry point. Trigger metadata, workflow, hard rules.
2. `references/` — loaded only when needed: style selection, quality checklist, deck spec, and ten style cards.
3. `assets/` and `scripts/` — copied or executed, never read wholesale.

The model reads one style card, not all ten. That keeps context small and output focused.

---

## Repository layout

```
html-style/
├── SKILL.md
├── references/
│   ├── choosing.md          # which style for which content
│   ├── quality.md           # pre-delivery checklist + real failure cases
│   ├── deck.md              # canvas, keys, wheel, page numbers, notes
│   └── styles/
│       ├── moneyai.md
│       ├── muse.md
│       ├── deepseek.md
│       ├── openai.md
│       ├── gradient.md
│       ├── echo.md
│       ├── frontend-slides.md
│       ├── htmlppt-pitch.md
│       ├── open-slide.md
│       └── goodpage.md
├── assets/
│   ├── starter.html         # responsive page skeleton
│   └── deck-starter.html    # 16:9 deck skeleton with navigation
├── scripts/
│   └── check.py             # static checks
└── README.md
```

---

## Quality bar

These rules are non-negotiable inside the skill:

- **One accent color.** Gradients only where the style card allows them.
- **No decorative Unicode.** No emoji, no `❦ ☙ ✳` as icons. Use inline SVG or CSS shapes.
- **No accidental drop caps in Chinese.** Emphasis goes on a whole phrase, not a random character.
- **Lining numerals for data.** Old-style figures make `1` read as `I`; data uses tabular lining digits.
- **No half-empty sections.** A web section is at least `100svh`; dead space under one third.
- **Decks fit the screen.** One idea per slide, large type, no shrinking text to avoid a page break.
- **No invented facts.** Illustrative numbers are labeled as such.

The full checklist, including the failure cases that produced these rules, lives in `references/quality.md`.

---

## Checker

`scripts/check.py` catches the machine-detectable mistakes:

```bash
python -B scripts/check.py page.html deck.html
```

It reports missing charset/lang/title, external assets, emoji or dingbats, and warns when a file uses an unusually large number of colors.

`-B` keeps Python from writing `__pycache__` into the skill directory.

---

## Language note

The skill instructions and style cards are currently written in Chinese, the author's working language. The README is English. A complete English translation of `SKILL.md` and `references/` is welcome as a contribution.

---

## Contributing

Issues and pull requests are welcome:

- new styles with tokens taken from real products
- corrections to contrast, typography, or responsive behavior
- English translations of the skill instructions
- additional starter skeletons (pricing page, portfolio detail, event page)

Please keep style cards factual: tokens, layout, density, anti-patterns. No invented metrics.

---

## License

MIT — see [LICENSE](LICENSE).
