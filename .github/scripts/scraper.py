import re
from datetime import datetime

# ✏️ UPDATED FROM THM PROFILE SCREENSHOT & RECENT SOC ROOM COMPLETIONS
USERNAME = "ayomiolutoye"
POINTS = 49          # Tickets/Points
STREAK = 141         # Updated: 141 day streak
RANK = "[0xA] WIZARD"
RANK_POSITION = 59991  # Updated: Rank 59,991
TOP_PERCENT = "3%"

COMPLETED_ROOMS = [
    {"title": "How Websites Work", "url": "https://tryhackme.com/room/howwebsiteswork"},
    {"title": "Putting it all together", "url": "https://tryhackme.com/room/puttingitalltogether"},
    {"title": "DNS in Detail", "url": "https://tryhackme.com/room/dnsindetail"},
    {"title": "HTTP in Detail", "url": "https://tryhackme.com/room/httpindetail"},
    {"title": "What is Networking?", "url": "https://tryhackme.com/room/whatisnetworking"},
    {"title": "Intro to LAN", "url": "https://tryhackme.com/room/introtolan"},
    {"title": "OSI Model", "url": "https://tryhackme.com/room/osimodelzi"},
    {"title": "Packets & Frames", "url": "https://tryhackme.com/room/packetsframes"},
    {"title": "Extending Your Network", "url": "https://tryhackme.com/room/extendingyournetwork"},
    {"title": "Careers in Cyber", "url": "https://tryhackme.com/room/careersincyber"},
    {"title": "Virtualisation Basics", "url": "https://tryhackme.com/room/virtualisationbasics"},
    {"title": "Client-Server Basics", "url": "https://tryhackme.com/room/clientserverbasics"},
    {"title": "Inside a Computer System", "url": "https://tryhackme.com/room/insideacomputersystem"},
    {"title": "Offensive Security Intro", "url": "https://tryhackme.com/room/offensivesecurityintro"},
    {"title": "Computer Types", "url": "https://tryhackme.com/room/computertypes"},
    {"title": "Defensive Security Intro", "url": "https://tryhackme.com/room/defensivesecurityintro"},
    {"title": "Linux Fundamentals Part 1", "url": "https://tryhackme.com/room/linuxfundamentalspart1"},
    {"title": "Operating System Security", "url": "https://tryhackme.com/room/operatingsystemsecurity"},
    {"title": "Operating Systems: Introduction", "url": "https://tryhackme.com/room/operatingsystemsintroduction"},
    {"title": "Linux CLI Basics", "url": "https://tryhackme.com/room/linuxclibasics"},
    {"title": "Data Representation", "url": "https://tryhackme.com/room/datarepresentation"},
    {"title": "Data Encoding", "url": "https://tryhackme.com/room/dataencoding"},
    {"title": "JavaScript: Simple Demo", "url": "https://tryhackme.com/room/javascriptsimpledemo"},
    {"title": "Python: Simple Demo", "url": "https://tryhackme.com/room/pythonsimpledemo"},
    {"title": "Windows Basics", "url": "https://tryhackme.com/room/windowsbasics"},
    {"title": "Cloud Computing Fundamentals", "url": "https://tryhackme.com/room/cloudcomputingfundamentals"},
    {"title": "Windows CLI Basics", "url": "https://tryhackme.com/room/windowsclibasics"},
    {"title": "The CIA Triad", "url": "https://tryhackme.com/room/theciatriad"},
    {"title": "Database SQL Basics", "url": "https://tryhackme.com/room/databasesqlbasics"},
    {"title": "Cryptography Concepts", "url": "https://tryhackme.com/room/cryptographyconcepts"},
    {"title": "Become a Hacker", "url": "https://tryhackme.com/room/becomeahacker"},
    {"title": "Become a Defender", "url": "https://tryhackme.com/room/becomeadefender"},
    {"title": "Linux Fundamentals Part 2", "url": "https://tryhackme.com/room/linuxfundamentalspart2"},
    {"title": "Linux Fundamentals Part 3", "url": "https://tryhackme.com/room/linuxfundamentalspart3"},
    {"title": "Windows Fundamentals 1", "url": "https://tryhackme.com/room/windowsfundamentals1xbx"},
    {"title": "Windows Fundamentals 2", "url": "https://tryhackme.com/room/windowsfundamentals2x0x"},
    {"title": "Windows Fundamentals 3", "url": "https://tryhackme.com/room/windowsfundamentals3xzx"},
    {"title": "Wireshark: The Basics", "url": "https://tryhackme.com/room/wiresharkthebasics"},
    {"title": "Active Directory Basics", "url": "https://tryhackme.com/room/winadbasics"},
    {"title": "Windows Command Line", "url": "https://tryhackme.com/room/windowscommandline"},
    {"title": "Networking Concepts", "url": "https://tryhackme.com/room/networkingconcepts"},
    {"title": "Tcpdump: The Basics", "url": "https://tryhackme.com/room/tcpdump"},
    {"title": "Networking Essentials", "url": "https://tryhackme.com/room/networkingessentials"},
    {"title": "Networking Core Protocols", "url": "https://tryhackme.com/room/networkingcoreprotocols"},
    {"title": "Networking Secure Protocols", "url": "https://tryhackme.com/room/networkingsecureprotocols"},
    {"title": "Windows PowerShell", "url": "https://tryhackme.com/room/windowspowershell"},
    {"title": "Linux Shells", "url": "https://tryhackme.com/room/linuxshells"},
    {"title": "Search Skills", "url": "https://tryhackme.com/room/searchskills"},
    {"title": "Blue", "url": "https://tryhackme.com/room/blue"},
    {"title": "Hydra", "url": "https://tryhackme.com/room/hydra"},
    {"title": "John the Ripper: The Basics", "url": "https://tryhackme.com/room/johntheripperbasics"},
    {"title": "Metasploit: Exploitation", "url": "https://tryhackme.com/room/metasploitexploitation"},
    {"title": "Metasploit: Introduction", "url": "https://tryhackme.com/room/metasploitintro"},
    {"title": "Metasploit: Meterpreter", "url": "https://tryhackme.com/room/meterpreter"},
    {"title": "Burp Suite: The Basics", "url": "https://tryhackme.com/room/burpsuitebasics"},
    {"title": "Moniker Link (CVE-2024-21413)", "url": "https://tryhackme.com/room/monikerlink"},
    {"title": "Nmap: The Basics", "url": "https://tryhackme.com/room/nmap"},
    {"title": "Public Key Cryptography Basics", "url": "https://tryhackme.com/room/publickeycrypto"},
    {"title": "Cryptography Basics", "url": "https://tryhackme.com/room/cryptographybasics"},
    {"title": "Hashing Basics", "url": "https://tryhackme.com/room/hashingbasics"},
    {"title": "Gobuster: The Basics", "url": "https://tryhackme.com/room/gobusterthebasics"},
    {"title": "JavaScript Essentials", "url": "https://tryhackme.com/room/javascriptessentials"},
    {"title": "Web Application Basics", "url": "https://tryhackme.com/room/webapplicationbasics"},
    {"title": "SQL Fundamentals", "url": "https://tryhackme.com/room/sqlfundamentals"},
    {"title": "Junior Security Analyst Intro", "url": "https://tryhackme.com/room/jrsecanalystintrouxo"},
    {"title": "Snort", "url": "https://tryhackme.com/room/snort"},
    {"title": "Snort Challenge - The Basics", "url": "https://tryhackme.com/room/snortchallenges1"},
    {"title": "Introduction to SIEM", "url": "https://tryhackme.com/room/introtosiem"},
    {"title": "Splunk: The Basics", "url": "https://tryhackme.com/room/splunk101"},
    {"title": "Incident Response Fundamentals", "url": "https://tryhackme.com/room/incidentresponsefundamentals"},
    {"title": "Logs Fundamentals", "url": "https://tryhackme.com/room/logsfundamentals"},
    {"title": "SOC Fundamentals", "url": "https://tryhackme.com/room/socfundamentals"},
    {"title": "Digital Forensics Fundamentals", "url": "https://tryhackme.com/room/digitalforensicsfundamentals"},
    {"title": "Firewall Fundamentals", "url": "https://tryhackme.com/room/firewallfundamentals"},
    {"title": "IDS Fundamentals", "url": "https://tryhackme.com/room/idsfundamentals"},
    {"title": "Vulnerability Scanner Overview", "url": "https://tryhackme.com/room/vulnerabilityscanneroverview"},
    {"title": "CyberChef: The Basics", "url": "https://tryhackme.com/room/cyberchefbasics"},
    {"title": "CAPA: The Basics", "url": "https://tryhackme.com/room/capathebasics"},
    {"title": "SQLMap: The Basics", "url": "https://tryhackme.com/room/sqlmapthebasics"},
    {"title": "Shells Overview", "url": "https://tryhackme.com/room/shellsoverview"},
    {"title": "Carnage", "url": "https://tryhackme.com/room/carnage"},
    {"title": "Security Principles", "url": "https://tryhackme.com/room/securityprinciples"},
    {"title": "FlareVM: Arsenal of Tools", "url": "https://tryhackme.com/room/flarevmarsenal"},
    {"title": "REMnux: Getting Started", "url": "https://tryhackme.com/room/remnuxgettingstarted"},
    {"title": "Training Impact on Teams", "url": "https://tryhackme.com/room/trainingimpactonteams"},
    {"title": "SOC L1 Alert Triage", "url": "https://tryhackme.com/room/socl1alerttriage"},
    {"title": "SOC L1 Alert Reporting", "url": "https://tryhackme.com/room/socl1alertreporting"},
    {"title": "Humans as Attack Vectors", "url": "https://tryhackme.com/room/humansasattackvectors"},
    {"title": "Systems as Attack Vectors", "url": "https://tryhackme.com/room/systemsasattackvectors"},
    {"title": "SOC Role in Blue Team", "url": "https://tryhackme.com/room/socroleinblueteam"},
    {"title": "OWASP Top 10 2025: IAAA Failures", "url": "https://tryhackme.com/room/owasptop102025iaaafailures"},
    {"title": "OWASP Top 10 2025: Application Design Flaws", "url": "https://tryhackme.com/room/owasptop102025applicationdesignflaws"},
    {"title": "OWASP Top 10 2025: Insecure Data Handling", "url": "https://tryhackme.com/room/owasptop102025insecuredatahandling"},
    {"title": "SOC Workbooks", "url": "https://tryhackme.com/room/socworkbooks"},
    {"title": "SOC Metrics and Objectives", "url": "https://tryhackme.com/room/socmetricsandobjectives"},
    {"title": "Introduction to EDR", "url": "https://tryhackme.com/room/introductiontoedr"},
    {"title": "Elastic Stack: The Basics", "url": "https://tryhackme.com/room/elasticstackthebasics"},
    {"title": "Introduction to SOAR", "url": "https://tryhackme.com/room/introductiontosoar"},
    {"title": "Pyramid Of Pain", "url": "https://tryhackme.com/room/pyramidofpain"},
]

BADGES = [
    "🎯 First Four — Completing four rooms in your first week",
    "🔥 3 Day Streak — Achieving a 3 day hacking streak",
    "🌐 Networking Nerd — Completing the Network Fundamentals module",
    "🔥 7 Day Streak — Achieving a 7 day hacking streak",
    "🕸️ Webbed — Understands how the world wide web works",
    "💻 World Wide Web — Completing the How The Web Works module",
    "🐧 cat linux.txt — Being competent in Linux",
    "🔥 30 Day Streak — Hacking for 30 days solid",
    "📦 Session Held — Completing 4 weekly missions in a row (Rare: 1.9%)",
    "🥇 Platinum League — Platinum League 1st place (Epic: 0.9%)",
    "🛡️ Metasploitable — Contains the knowledge to use Metasploit (Rare: 9.6%)",
    "🪟 Blue — Hacking into Windows via EternalBlue",
    "🗡️ Sword Apprentice — Completing the SQLMap room",
    "🔥 90 Day Streak — Hacking for 90 days in a row",
    "🔬 Network Hog — Sniffed out malicious traffic in the network",
    "📱 First Mobile Quiz — Completing your first quiz or recap on the mobile app (Rare: 2.4%)",
    "🛡️ Shield Apprentice — Completing the FlareVM room",
    "🎓 Cyber Ready — Understanding impact of training on teams",
    "🔥 100 Day Streak — Hacking for 100 days in a row",
    "🛡️ First Step into SOC — Explored emerging threats and SOC response",
    "📚 SOC Apprentice — Explored how a SOC team operates from inside (Rare: 1.8%)",
    "🔍 First alert closed — Closing your first alert (Rare: 2.6%)",
    "🕹️ First scenario completed — Completing your first scenario (Rare: 2.1%)",
    "🎯 100% true positive rate — Achieving 100% true positive rate in a scenario (Rare: 1.7%)",
    "🛡️ Defensive Toolsmith — Mastered essential SOC tools for detection",
]

SKILLS = [
    "Networking", "Linux", "Windows", "Active Directory",
    "Web Application Security", "Cryptography", "SQL",
    "Nmap", "Metasploit", "Wireshark", "Tcpdump",
    "PowerShell", "Python", "JavaScript", "Cloud Computing",
    "Offensive Security", "Defensive Security", "Digital Forensics",
    "Incident Response", "Splunk", "SIEM", "Firewalls", "IDS/IPS", "Snort",
    "Vulnerability Assessment", "OpenVAS", "Nessus", "CyberChef",
    "YARA", "Malware Analysis", "CAPA", "Static Analysis",
    "REMnux", "Volatility3", "Memory Forensics", "oledump.py",
    "OLE/Document Analysis", "Network Traffic Simulation (INetSim)",
    "Malware Triage Tooling (FlareVM)", "Security Principles",
    "OWASP Top 10", "Insecure Data Handling", "Application Design Flaws",
    "IAAA Failures", "SSTI", "Secure Deserialization", "Insecure Design",
    "Human Attack Vectors", "System Attack Vectors", "SOC Operations",
    "Alert Triage", "SOC Workflows", "Alert Reporting", "Alert Escalation", 
    "SOC Crisis Communication", "Five Ws Reporting", "Asset Lookup",
    "Identity Lookup", "Network Diagrams", "SOC Workbooks",
    "SOC Metrics & Objectives", "MTTD / MTTR / MTTA Optimization", "SLA Management",
    "Endpoint Detection & Response (EDR)", "Behavioral Analysis", "Host Isolation & Containment",
    "Elasticsearch", "Kibana", "KQL (Kibana Query Language)", "Log Management & Analytics",
    "SOAR (Security Orchestration, Automation, and Response)", "Security Automation", "Playbook Execution",
    "Pyramid of Pain", "Threat Intelligence", "TTP Mapping", "Adversary Disruption", "Indicator Analysis"
]


def build_readme_section():
    rooms_md = "\n".join(
        [f"- [{r['title']}]({r['url']})" for r in COMPLETED_ROOMS]
    )
    badges_md = "\n".join([f"- {b}" for b in BADGES]) or "_Visit your profile → Badges tab to see all badges!_"
    skills_md = ", ".join(SKILLS)
    last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    section = f"""<!-- THM-STATS:START -->
## 🛡️ TryHackMe Progress

| Stat | Value |
|------|-------|
| 👤 Username | [{USERNAME}](https://tryhackme.com/p/{USERNAME}) |
| 🏆 Rank | {RANK} (#{RANK_POSITION} — Top {TOP_PERCENT}) |
| 💰 Points | {POINTS} |
| 🔥 Current Streak | {STREAK} days |
| ✅ Rooms Completed | {len(COMPLETED_ROOMS)} |
| 🎖️ Badges Earned | {len(BADGES)} |

### 🧠 Skills Gained
{skills_md}

### 🎖️ Badges
{badges_md}

### 📚 Completed Rooms ({len(COMPLETED_ROOMS)})
{rooms_md}

> _Last updated: {last_updated}_
<!-- THM-STATS:END -->"""

    return section


def update_readme(section, readme_path="README.md"):
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = "# My CyberSecurity Journey\n\n"

    pattern = r"<!-- THM-STATS:START -->.*?<!-- THM-STATS:END -->"
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, section, content, flags=re.DOTALL)
    else:
        content += f"\n\n{section}\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README.md updated successfully.")


if __name__ == "__main__":
    section = build_readme_section()
    update_readme(section)
