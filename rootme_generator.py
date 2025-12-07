import re
import requests

USERNAME = "Rizou"
URL = f"https://www.root-me.org/{USERNAME}"

html = requests.get(URL, timeout=15).text

# Extract key values from the HTML (Root-Me layout may change)
score     = re.search(r"Score[^0-9]+([0-9]+)", html).group(1)
rank      = re.search(r"Rank[^0-9]+([0-9]+)", html).group(1)
validated = re.search(r"Validated[^0-9]+([0-9]+)", html).group(1)

svg = f"""
<svg width="460" height="160" viewBox="0 0 460 160" xmlns="http://www.w3.org/2000/svg">
<style>
    .title {{ font: bold 20px sans-serif; fill: #fff; }}
    .label {{ font: 14px sans-serif; fill: #ddd; }}
    .value {{ font: bold 14px sans-serif; fill: #fff; }}
</style>

<rect width="460" height="160" rx="15" fill="#24292e"/>

<text x="20" y="35" class="title">🔐 Root-Me Profile</text>

<text x="20" y="70"  class="label">Username:</text>
<text x="150" y="70" class="value">{USERNAME}</text>

<text x="20" y="95"  class="label">Rank:</text>
<text x="150" y="95" class="value">{rank}</text>

<text x="20" y="120" class="label">Score:</text>
<text x="150" y="120" class="value">{score}</text>

<text x="20" y="145" class="label">Challenges validated:</text>
<text x="250" y="145" class="value">{validated}</text>

</svg>
"""

with open("rootme.svg", "w", encoding="utf-8") as f:
    f.write(svg)
