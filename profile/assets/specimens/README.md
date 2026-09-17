# Material notes

The project panes use recorded material; the CV and LinkedIn panes introduce the person and the work sought. Each SVG is self-contained. Source material is kept here so the compositions can be rebuilt without a network request.

## CV and LinkedIn

The top row links to [Emil Nesteruk's CV](https://nesterukemil.cv/) and [LinkedIn profile](https://www.linkedin.com/in/emil-nesteruk-018702374/). These are original typographic compositions in the same type palette as the project pieces. The LinkedIn pane explicitly invites long-term AI engineering work with an established team.

## Benzin v strane

`map-crop.png` is an unedited browser capture of [benzinavstrane.net](https://benzinavstrane.net/) on **17 September 2026 at 12:16 UTC**: Kaliningrad, centre 54.7104 / 20.5108, zoom 12, a 400 × 250 viewport at 2× resolution. Map controls were hidden for the capture. The original station colours, markers and map labels were retained. Orange means a reported queue; grey means no data. This is a record of what the site displayed, not a fresh fuel-availability report.

`map-state.json` records the view, visible stations, colour meanings and loaded tiles. Basemap © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), available under the Open Database License. Attribution is also printed on the SVG.

## Hyprchan

`sit_sleeping.png` is the original, unmodified [Hyprchan sprite atlas](https://github.com/AscenderTeam/Hyprchan/blob/d4d4085519faebafe09ad62c89ad700693948958/public/assets/sprites/sit_sleeping.png): 16 frames, each 122 × 234 pixels. The desktop composition is staged; it is not a screenshot of a running session. The annotation `sit.sleeping` is the real [animation ID](https://github.com/AscenderTeam/Hyprchan/blob/d4d4085519faebafe09ad62c89ad700693948958/src/hyprchan/animations/sleeping_sit.py).

The SVG clips the original atlas and advances through its frames. With reduced motion enabled, it shows the first frame.

## login.final.FINAL.v2

An authentication document for the [actual login experiment](https://waromiv.github.io/login-page-final-FINAL-v2/): its potato and “Step 1 of ∞” become the material. The amended FINAL and the single field are a new composition, not a screenshot. The input is part of the image; clicking opens the project.

## Stonkfly

`stonkfly-trace.json` contains 118 recorded observations from the public paper dashboard, run `mexc-fee-sol-paper-x86-20260917`, **17 September 2026, 10:16:04–13:11:07 UTC**. Only the fields needed to identify and reproduce the record are retained.

The plotted value is observed SOL-USDC paper-account equity, in USDC, sampled **before that tick's execution**. It is not an after-fill return series. The horizontal axis is elapsed time, and the vertical axis fits the recorded values. A 56.4-minute interval without observations is left blank, rather than connected by an invented line. There are 75 HOLD decisions, 39 BUY decisions and four SELL decisions in this sample; 17 executions were filled and 26 were vetoed. This short record is not evidence of profitability.

The generated SVG filename includes the date and final tick so GitHub's image cache cannot substitute an older snapshot. The recorded snapshot ends at 13:11 UTC; clicking the piece opens the current dashboard.

The fly is a small original drawing; the plotted line is recorded data. Experiment built on [nftechie/stonkfly](https://github.com/nftechie/stonkfly). The image links to the [hosted paper dashboard](http://109.123.255.162:8766/).

## Rebuild

From the repository root:

```sh
python profile/assets/build_specimens.py
```

Open `profile/badges-preview.html` to view the six pieces together. The SVGs share a 640 × 400 canvas and a serif/monospace type palette. The map and trace are static; the sprite and input caret use restrained CSS animation with reduced-motion support. All pieces remain complete when animation is disabled.
