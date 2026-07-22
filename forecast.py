import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
teams = {
    "Toronto Maple Leafs": {"v2022": 1.85, "v2025": 4.30},
    "Florida Panthers": {"v2022": 0.65, "v2025": 1.89},
    "Columbus Blue Jackets": {"v2022": 0.60, "v2025": 1.40},
    "Edmonton Oilers": {"v2022": 1.30, "v2025": 2.76},
}
league_v2022 = 1.01
league_v2025 = 2.20
HIST_YEARS = [2022, 2025]
FORECAST_YEARS = [2026, 2027, 2028, 2029, 2030]

def calculate_cagr(start_value, end_value, num_years):
    return ((end_value/start_value) ** (1/num_years) - 1) * 100

def forecast_multiple_years(start_value, growth_rate_percent, num_years, decay=0):
    value = start_value
    current_rate = growth_rate_percent
    history = []
    for year_number in range(num_years):
        value = value * (1 + current_rate / 100)
        history.append(round(value, 2))
        current_rate = current_rate * (1 - decay / 100)
    return history

league_rate = calculate_cagr(league_v2022, league_v2025, num_years=3)

plt.rcParams["font.family"] = "DejaVu Sans"
COLORS = {
    "Toronto Maple Leafs": "#003E7E", # Leafs blue
    "Florida Panthers": "#C8102E", # Panthers red
    "Columbus Blue Jackets": "#002654", # Blue Jackets navy
    "Edmonton Oilers": "#FF4C00", # Oilers orange
}

fig, ax = plt.subplots(figsize=(10,6.5), facecolor="#FAFAF8")
ax.set_facecolor("#FAFAF8")

for team_name, values in teams.items():
    color = COLORS[team_name]
    forecast = forecast_multiple_years(values["v2025"], league_rate, num_years=5, decay=8)

    hist_x = HIST_YEARS
    hist_y = [values["v2022"], values["v2025"]]
    forecast_x = [HIST_YEARS[-1]] + FORECAST_YEARS
    forecast_y = [values["v2025"]] + forecast

    ax.plot(hist_x, hist_y, color=color, linewidth=2.75, solid_capstyle="round")
    ax.plot(forecast_x, forecast_y, color=color, linewidth=2.75,
        linestyle=(0, (5, 3)), alpha=0.85)
    ax.annotate(f" {team_name}\n ${forecast_y[-1]:.2f}B",
                xy=(forecast_x[-1], forecast_y[-1]),
                va="center", ha="left", fontsize=9.5, color=color, fontweight="bold")

    ax.scatter([HIST_YEARS[-1]], [values["v2025"]], color=color, s=35, zorder=5)

ax.axvline(x=2025, color="#999990", linewidth=1, linestyle=":")
ax.text(2025, ax.get_yline()[1] if False else 0, "", alpha=0)

ax.set_title("NHL Franchise Valuations: History & Forecast",
    fontsize=17, fontweight="bold", color="#1a1a1a", pad=18)
ax.set_ylabel("Franchise Value ($B)", fontsize=11, color="#444")
ax.set_xlabel("Year", fontsize=11, color="#444")

ax.set_xlim(2021.5, 2030.5)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}B"))
ax.grid(axis="y", color="#dddad0", linewidth=0.8, zorder=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.tick_params(left=False)

fig.text(0.01, 0.01,
    f"Forecast uses one shared league-wide growth rate ({league_rate:.1f}%/yr),"
    " derived from the 2022-2025 average NHL valuation, as well as a decay rate (8%/yr).",
    fontsize=8.5, color="#888", ha="left")

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig("nhl_forecast_final.png", dpi=170, facecolor=fig.get_facecolor())
print("Saved nhl_forecast_final.png")

ax.set_title("NHL Franchise Valuations: History & Forecast",
    fontsize=17, fontweight="bold", color="=#1a1a1a", pad=18)
ax.set_ylabel("Franchise Value ($B)", fontsize=11, color="#444")
ax.set_xlabel("Year", fontsize=11, color="#444")

ax.set_xlim(2021.5, 2030.5)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}B"))
ax.grid(axis="y", color="#dddad0", linewidth=0.8, zorder=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.tick_params(left=False)

fig.text(0.01, 0.01,
    f"Forecast uses one shared league-wide growth rate ({league_rate:.1f}%/yr),"
    " derived from the 2022-2025 average NHL valuation, as well as a decay rate (8%/yr).",
    fontsize=8.5, color="#888", ha="left")

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig("nhl_forecast_final.png", dpi=170, facecolor=fig.get_facecolor())
print("Saved nhl_forecast_final.png")
