# Kenyan Premier League & EPL Mindshare Analysis

## Executive Summary
This project analyzes the search interest and mindshare gap between the English Premier League (EPL) and domestic football competitions (such as the FKF Premier League) in Kenya. 

Using automated remote data extraction (`pytrends`), statistical computing (`pandas`), and visual analytics (`Tableau`), this analysis quantifies search volume disparities, matchday volatility, and the impact of broadcast scheduling.

---

## Key Findings
* **Search Interest Dominance:** Popular EPL terms lead domestic search interest by a ratio exceeding **10:1**.
* **Event Volatility:** EPL search behavior displays high volatility ($\sigma \approx 18.4$) tied directly to weekend matchday cycles, whereas local leagues display lower baseline search persistence.
* **Core Drivers:** Premier League dominance is structurally sustained by broadcast timing alignment (UTC+3), localized sports betting products, and historical player representation.

---

## Project Structure
* `eplvslocal.py` – Data collection script using PyTrends to pull Kenya-specific Google search volume.
* `analyze_trends.py` – Python script using Pandas to compute statistical summaries (mean, spikes, standard deviation).
* `tableau_kenya_trends_tall.csv` – Transformed long-format dataset optimized for Tableau visualization.

---

## Technologies Used
* **Languages:** Python 3.x, SQL, Markdown
* **Libraries:** Pandas, PyTrends
* **Visualization:** Tableau Public
