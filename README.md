## Fantasy Football Trade Value Calculator

Welcome to the **Fantasy Football Trade Value Calculator** – a tool dedicated to fantasy football enthusiasts that aims to evaluate and compare the trade value of players based on projected fantasy points.

### Project Structure:
- `ff_scraper.py`: Contains functions and logic to scrape and process player data from CBS Sports.
- `ff_gui.py`: Houses the GUI implementation for the tool using `tkinter`.
- `team_fantasy_points.csv`: A CSV file storing DST player names along with their respective projected fantasy points, due to scraping constraints.
- `README.md`: An informative guide about the tool and how to use it.

### Key Features:

1. **Data Acquisition and Integration**:
    - Player data is sourced from CBS Sports, specifically URLs like [CBS Sports QB Projections](https://www.cbssports.com/fantasy/football/stats/QB/2023/season/projections/nonppr/) and others.
    - While data from most positions is scraped directly, DST data posed challenges. As a result, we reference it from the `team_fantasy_points.csv` for integration and usage.
    - Columns in the CSV are `Player` and `PlayerValue` to ensure efficient referencing within the codebase.

![ff_photo5](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/0a979ecd-25b5-4ecc-b675-ba259fa36a32)

2. **User-friendly GUI**:
    - Built using the `tkinter` library, the GUI is intuitive and straightforward.
    - "Team A" and "Team B" list boxes let users select players for a potential trade.
    - Efficient player searching is facilitated with search bars above each list box.
    - Upon clicking the "Evaluate" button, the application computes total fantasy points for the selected players and provides a value-based evaluation of the trade.
    - The "Clear Selections" button allows for starting over, and with the "Trade History" button, users can review their past evaluations, which also showcases a graphical representation using `matplotlib` for in-depth insights.

![ff_photo](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/628f3b56-87a6-4705-973f-f0ea0907b220)

![ff_photo2](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/04705db5-83b7-4702-a746-ecfc29ef3173)

![ff_photo_4](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/b4d8c4df-f3cc-4e3d-b430-53654ebfb96c)

3. **Analytical Depth**:
    - The tool provides context for each trade evaluation, letting users know if a trade is balanced, skewed, or particularly beneficial for one team.
    - The "Trade History" feature lists previous trade evaluations, giving users a retrospective view of their decisions.
    - Graphical representation of trade evaluations offers users a visual understanding of trade value distributions over time.

![ff_photo3](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/b0b75bb4-19a5-470d-ac1d-4580b1401b89)

5. **Branding & Aesthetics**:
    - The application window showcases a unique icon, lending a professional touch to the tool.

### How to Use:

1. Start by running the `ff_gui.py` script.
2. In the GUI, choose players for a trade under "Team A" and "Team B".
3. Click "Evaluate" to get a breakdown of the trade's value.
4. Past evaluations can be reviewed by clicking on "Trade History".

### Requirements:
Ensure you have `tkinter` and `matplotlib` libraries installed. If not, install them via pip:

```bash
pip install tk matplotlib
```

### Conclusion:
The **Fantasy Football Trade Value Calculator** amalgamates scraping, data processing, and GUI craftsmanship to offer a seamless experience for evaluating fantasy football trades. Whether you're just getting started or have been in the game for a while, this tool promises to be a worthy companion in your fantasy journey.
