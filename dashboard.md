<div align="center">

# 📊 Chirag Lohar — Coding Dashboard

<sub>A live, self-updating snapshot of my LeetCode grind + GitHub activity.</sub>

[![GitHub](https://img.shields.io/badge/GitHub-chiraaglohar-181717?style=flat-square&logo=github)](https://github.com/chiraaglohar)
[![LeetCode](https://img.shields.io/badge/LeetCode-Chiraaglohar-FFA116?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/u/Chiraaglohar/)
[![Last Updated](https://img.shields.io/github/last-commit/chiraaglohar/Leetcode?label=last%20updated&style=flat-square)](https://github.com/chiraaglohar/Leetcode/commits/main)

</div>

---

## 📌 Table of Contents
- [Overview](#-overview)
- [LeetCode Stats](#-leetcode-stats)
- [Topic-wise Breakdown](#-topic-wise-breakdown)
- [GitHub Activity](#-github-activity)
- [How this stays up to date](#-how-this-stays-up-to-date)

---

## 🖼️ Overview

<div align="center">
<img src="dashboard.svg" alt="Coding dashboard" width="100%" />
</div>

The image above is generated fresh every day — it combines my **LeetCode
submission activity** and **GitHub commit activity** into one heatmap, plus a
difficulty breakdown and topic-wise bar chart. Everything below is the same
data, laid out as plain markdown for anyone who wants the numbers without
loading an image (screen readers, low-bandwidth, quick skim, etc).

---

## 🧠 LeetCode Stats

| Metric | Live Badge |
|---|---|
| **Total Solved** | ![Solved](https://img.shields.io/badge/dynamic/json?url=https://alfa-leetcode-api.onrender.com/Chiraaglohar/solved&query=%24.solvedProblem&label=Solved&style=flat-square&color=4F46E5) |
| **Easy** | ![Easy](https://img.shields.io/badge/dynamic/json?url=https://alfa-leetcode-api.onrender.com/Chiraaglohar/solved&query=%24.easySolved&label=Easy&style=flat-square&color=22C55E) |
| **Medium** | ![Medium](https://img.shields.io/badge/dynamic/json?url=https://alfa-leetcode-api.onrender.com/Chiraaglohar/solved&query=%24.mediumSolved&label=Medium&style=flat-square&color=F59E0B) |
| **Hard** | ![Hard](https://img.shields.io/badge/dynamic/json?url=https://alfa-leetcode-api.onrender.com/Chiraaglohar/solved&query=%24.hardSolved&label=Hard&style=flat-square&color=EF4444) |


<img src="https://leetcard.jacoblin.cool/chiraaglohar?theme=dark&font=RocknRoll%20One&ext=heatmap" />



---

## 🗂️ Topic-wise Breakdown

Pulled from LeetCode's `tagProblemCounts` (same source as the bar chart
above). Refreshed by the same script that draws `dashboard.svg`:

| Topic | Problems Solved |
|---|---|
| Database | 19 |
| HashMap and Set | 2 |
| Arrays | 2 |
| Math | 2 |
| Sliding Window | 1 |
| Linked List | 1 |
| Recursion | 1 |

<sub>These rows are placeholders from the last generator run — see <a href="#-how-this-stays-up-to-date">below</a> to regenerate them with your latest numbers.</sub>

---

## 🐙 GitHub Activity

| Metric | Value |
|---|---|
| **Repo** | [chiraaglohar/Leetcode](https://github.com/chiraaglohar/Leetcode) |
| **Sync method** | [LeetHub v2](https://github.com/arunbhardwaj/LeetHub-2.0) — auto-commits on every accepted submission |
| **Public repos** | ![Repos](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/users/chiraaglohar&query=%24.public_repos&label=Public%20Repos&style=flat-square&color=0EA5E9) |
| **Followers** | ![Followers](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/users/chiraaglohar&query=%24.followers&label=Followers&style=flat-square&color=0EA5E9) |

---

## 🔄 How this stays up to date

```
scripts/generate_dashboard.py          → fetches LeetCode + GitHub data, draws dashboard.svg
.github/workflows/update-dashboard.yml → runs the script daily + on every push, commits the result
dashboard.md                           → this file — embeds the SVG, plus the tables above
```

To manually refresh everything:

```bash
python3 scripts/generate_dashboard.py --leetcode Chiraaglohar --github chiraaglohar
```

Full setup steps are in `DASHBOARD_SETUP.md`.

<div align="center">
<sub>🕐 Last manually refreshed: <!-- DATE --></sub>
</div>
