---

title: 🔶 Sketch Design to Code Agent - Dev Diary

date: 2026-01-14

slug: 2026-01-14-sketch-design-to-code-agent-dev-diary

tags: [dev-diary, ai]

image: 

image_alt: 

---



This blog post documents creating a custom AI agent for use with the Sketch MCP server. The agent’s purpose is to transform Sketch designs into production-ready HTML and CSS.

I developed the agent using VS Code and Copilot. I used the Claude Sonnet 4.5 model in Copilot to create the agent and iteratively refine it.

## Fri, 2 Jan 2026

- Created custom Copilot agent
- Enforces strict design fidelity with real data
- Implemented BEM methodology for class naming
- Sketch API data extraction
- BEM methodology CSS generation
- MCP server integration
- Respect null values principle

## Tue, 6 Jan 2026

- ﻿Improved Sketch Design to Code agent capabilities
- Fixed font weight extraction for accurate CSS
- ﻿﻿Correctly extracted text colors from layers
- ﻿﻿Included accurate line-height and letter-spacing values
- Verified fixes against actual Sketch layers

## Sat, 10 Jan 2026

- Enhanced agent for color extraction from Sketch symbols
- Added extractExpandedLayers function
- Integrated guide on color extraction
- Correctly applied symbol colours
- Verified badge rendered in green (#41d646)

## Tue, 13 Jan 2026

- ﻿﻿Enhanced gradient fill extraction
- ﻿﻿Added inner shadows support
- ﻿﻿Category-preserving CSS mappings
- Tested on round liquid glass button
- Ensured perfect fidelity


## Wed, 14 Jan 2026

- Added guidance for simplifying gradient borders
- Ensured vendor prefixes for maximum browser compatibility
- ﻿﻿Emphasised visual fidelity over technical accuracy

---

## Next Steps

- Test with additional components (inputs, cards, modals)
- Build design tokens extraction from Sketch color/text styles
- Extend to support responsive breakpoints and layout modes
- Create component library generator from Sketch symbols







