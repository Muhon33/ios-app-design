# ios-app-design

A Claude skill for designing polished, native-feeling iPhone app screens as HTML mockups that follow Apple's Human Interface Guidelines for iOS 26 (Liquid Glass).

It also critiques and improves existing iOS screens or screenshots against the HIG.

## Install

Clone into your Claude skills folder:

```bash
git clone https://github.com/Muhon33/ios-app-design ~/.claude/skills/ios-app-design
```

Then ask Claude something like "design a settings screen for my fitness app".

## Contents

- `SKILL.md`: the skill instructions
- `taste.md`, `anti-patterns.md`: design guidance
- `assets/`: the iOS CSS kit and HTML template
- `references/`: design tokens, components, screen patterns and HIG notes
- `examples/`: reference screenshots and notes
- `scripts/screenshot.py`: renders mockups to images
- `evals/`: test cases for checking the skill's output
