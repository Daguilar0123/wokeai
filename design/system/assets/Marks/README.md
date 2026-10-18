# Marks

The source files use `currentColor` so the mark takes the ink of whatever it sits on. Because stored images render through `<img>` and cannot inherit color, this group holds explicit-ink copies:

- `a-roots-ink.svg` — the wokeai mark in `ink` (#141414), for light surfaces.
- `a-roots-paper.svg` — the wokeai mark in dark-theme `ink` (#f2efe8), for dark surfaces and for setting on `accent`.
- `b-heard-ink.svg`, `b-heard-paper.svg` — the podcast mark, same two inks.
- `a-roots.svg`, `b-heard.svg` — the `currentColor` sources, for inlining in HTML where color should inherit.

Geometry is fixed: Roots is grass above a ground line with a git-graph root system (main branch, two branches, nodes, no merge); Heard is three arcs of sound arriving at a listening dot. Refine stroke weight if a size demands it; never redraw, never add an eye, rays, fist, chains, or any likeness.
