## Fantasy Football Trade Value Calculator

Welcome to the **Fantasy Football Trade Value Calculator** – a tool dedicated to fantasy football enthusiasts that aims to evaluate and compare the trade value of players based on projected fantasy points.

### Project Structure:
- `ff_scraper.py`: Contains functions and logic to scrape and process player data.
- `ff_gui.py`: Houses the GUI implementation for the tool using `tkinter`.
- `team_fantasy_points.csv`: A CSV file storing player names along with their respective projected fantasy points.
- `README.md`: An informative guide about the tool and how to use it.

### Key Features:

1. **Data Acquisition and Integration**:
    - Player data is sourced and processed from DST's URL, but for the ease of usage and direct integration, the information is then converted into a `team_fantasy_points.csv`.
    - Columns in the CSV are appropriately named as `Player` and `PlayerValue` to ensure straightforward referencing within the codebase.

![ff_photo5](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/0a979ecd-25b5-4ecc-b675-ba259fa36a32)


2. **User-friendly GUI**:
    - The application boasts an intuitive GUI built with the `tkinter` library.
    - Users are presented with two distinct list boxes, "Team A" and "Team B", where multiple players can be selected to represent the trade.
    - Efficient player searching is enabled with search bars above each list box.
    - The "Evaluate" button, once clicked, computes the total fantasy points for the selected players and provides an evaluative message on the trade's value.
    - For restarting trade evaluations, a "Clear Selections" button is available.
    - Users have access to the "Trade History" button to review past evaluations, complete with a graphical representation using `matplotlib` for insightful analysis
  
![ff_photo](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/628f3b56-87a6-4705-973f-f0ea0907b220)

![ff_photo2](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/04705db5-83b7-4702-a746-ecfc29ef3173)

![ff_photo_4](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/b4d8c4df-f3cc-4e3d-b430-53654ebfb96c)


3. **Analytical Depth**:
    - The tool goes beyond mere value representation; it provides context. Users get a message describing the nature of the trade – whether it's lopsided, balanced, or beneficial for a particular team.
    - Trade history features list previous trade evaluations with their respective values, facilitating a track of trading decisions over time.
    - The graphical representation of the trade history provides a visual snapshot of trade value distributions over sessions.

![ff_photo3](https://github.com/bennettnottingham/Fantasy-Football-Trade-Calculator/assets/65934399/b0b75bb4-19a5-470d-ac1d-4580b1401b89)

5. **Branding & Aesthetics**:
    - The application window features a thematic icon, giving the tool a unique identity and a professional touch.

### How to Use:

1. Run the `ff_gui.py` script.
2. From the GUI, select players you're considering for a trade from "Team A" and "Team B".
3. Click on "Evaluate" to get an evaluation of the trade.
4. You can view past evaluations by clicking on "Trade History".

### Requirements:
Make sure you have `tkinter` and `matplotlib` libraries installed. If not, they can be installed via pip:

```bash
pip install tk matplotlib
```

### Conclusion:
The **Fantasy Football Trade Value Calculator** is a culmination of scraping, data analysis, and GUI implementation to create a seamless user experience for evaluating player trades in fantasy football. Whether you're a newbie or a seasoned player, this tool is bound to be a valuable addition to your fantasy toolkit.
