# TEKI Project Hub

[![Live Demo](https://img.shields.io/badge/Live_Site-tekiproject.com-00a896?style=flat-square)](http://tekiproject.com/)
[![Built With](https://img.shields.io/badge/Stack-HTML5_|_CSS3_|_JS-orange?style=flat-square)]()

A custom-engineered, minimalist portfolio and digital sandbox designed to host, document, and showcase technical projects, live software demos, and technical walkthroughs.

---

## Overview

**TEKI** serves as a centralized technical showcase and interactive workbench. Built entirely from scratch without the overhead of heavy content management systems (CMS) or pre-built site templates, this platform emphasizes clean architecture, custom CSS tokenization, fluid micro-interactions, and responsive UI design.

---

## Key Features

* **Zero-Framework Architecture:** Developed using vanilla web standards (HTML5, modular CSS3, ES6+ JavaScript) to maximize performance and maintain full control over the rendering lifecycle.
* **Minimalist, Content-First UI/UX:** Styled with a geometric visual language, utilizing a neutral core palette complemented by high-contrast teal accents for readability and structured visual hierarchy.
* **Curated Typography System:** Structured across three dedicated typefaces—`Fraunces` for high-impact display titles, `Public Sans` for body copy, and `IBM Plex Mono` for technical labels and navigation tokens.
* **Fluid Keyframe Animations & Micro-Interactions:** Includes staggered entrance animations (`rise`, `rise-mark`), logo hover rotations, expanding link underlines, and an interactive backdrop-blur navbar (`navbar--scrolled`).
* **Accessibility & Motion Preferences:** Built-in `:focus-visible` accessibility rings and explicit `@media (prefers-reduced-motion: reduce)` overrides to disable animations for users with motion sensitivity.
* **Adaptive Multi-Breakpoint Layout:** Two-tier responsive layout (`900px` grid collapse and `720px` mobile navigation drawer transition) built with CSS Grid and Flexbox.
* **Modular Project Architecture:** Scalable view structure featuring tabbed project routing to accommodate technical documentation, embedded media, and interactive demos.

---

## Tech Stack

| Category | Technology | Implementation Details |
| :--- | :--- | :--- |
| **Markup & Semantics** | HTML5 | Semantic landmarks, accessible document structure, smooth scrolling |
| **Styling & Layout** | CSS3 (Grid / Flexbox) | Custom design tokens (`:root`), cubic-bezier transitions, fluid `clamp()` sizing, keyframe animations |
| **Logic & Scripting** | JavaScript (ES6+) | Scroll observers for dynamic navbar blur and mobile hamburger drawer toggling |
| **Planned Integrations** | Python | Backend services, API routing, and embedded tooling |

---

## Roadmap

- [ ] Integrate a Python-based backend service (FastAPI/Flask) for dynamic API endpoints.
- [ ] Add interactive in-browser terminal or live code sandboxes for featured software.
- [ ] Implement automated CI/CD deployment workflows.

---

## Quick Start (Local Setup)

Clone the repository and open the entry point in any browser:

```bash
git clone [https://github.com/twill320/TEKI.git
cd TEKI
open home.html
