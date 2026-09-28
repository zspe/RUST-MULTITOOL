# Rust-Multitool 🕷️

![RUST-MULTITOOL Banner](https://github.com/zspe/RUST-MULTITOOL/raw/main/rustpic.png)

A Python-based web crawling and reconnaissance tool built for educational cybersecurity, bug bounty recon, and authorized lab environments.

Built by [zed](https://github.com/zedwed11).

---

## What it does

Rust-Multitool is a menu-driven CLI tool with two main features:

**1. Website Crawler**
- Takes a starting URL and a max page count
- Crawls same-domain links breadth-first (ignores `#` fragments and external domains)
- Prints every page it finds as it goes
- Handles failed requests gracefully (files, media, non-HTML content)
- User-agent flagged? Pick from 5 alternate user agents (Chrome Win/Mac, iPad Safari, Googlebot, Android Chrome) and continue

**2. Website Scraper**
- Pulls page metadata: title, meta description
- Counts elements: links, images, forms, inputs, buttons, scripts, stylesheets, headings, paragraphs
- Dumps full heading hierarchy (h1–h6)
- Lists all links with their anchor text
- Lists all images with `src` and `alt`
- Enumerates every form with its action, method, and all input fields (type, name, id)
- Lists all external and inline scripts
- Maps page structure (header, nav, main, section, article, aside, footer)

Plus a help screen and links to my GitHub and Discord.

---

## Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4`
- `colorama`

All dependencies are listed in `requirements.txt`. To install everything at once:

```
pip install -r requirements.txt
```

Or install them manually:

```
pip install requests beautifulsoup4 colorama
```

---

## Usage

```
python RustMtool.py
```

You'll get a menu:

```
1. Crawl Websites
2. Scrape Websites
4. Help/info
5. Github/Discord
```

Pick a number and follow the prompts.

**Crawler example:**
```
URL: |> example.com
Max Pages to crawl? |> 25
```

It will test the site first, then crawl up to 25 same-domain pages, printing each one it finds.

**Scraper example:**
```
URL?: |> example.com
```

It will dump everything it can find about the page — links, forms, scripts, headings, images, structure.

---

## What I built this for

I'm 13 and about 3 months into Python. This started as a way to practice `requests`, `BeautifulSoup`, and building real CLI tools with proper flow control instead of the usual tutorial projects.

The crawler taught me about queues, visited sets, domain scoping, and handling bad responses. The scraper taught me about parsing real HTML and pulling structured data out of messy markup.

If you're learning too, feel free to read the source — it's not perfect, but it works, and every bug in it taught me something. 🐛

---

## Known limitations

- Crawler only follows `<a href>` links — it won't find JS-rendered routes or links inside forms
- Scraper dumps everything to console (no export to file yet)
- User-agent rotation is manual, not automatic
- No `robots.txt` checking yet
- No rate limiting between requests — be respectful with your `max_pages`

---

## Planned

- Save crawl/scrape results to a file (JSON or plain text)
- Respect `robots.txt`
- Add delay/rate-limit option
- Auto-rotate user agents instead of prompting
- Maybe a basic port/header check mode

---

## Disclaimer ⚠️

This tool is for **educational use, bug bounty recon on programs you're enrolled in, and authorized lab environments only**. Crawling or scraping a site you don't own or don't have permission to test may violate that site's terms of service and, in some jurisdictions, the law.

Don't point it at anything you don't have written permission to test. I'm not responsible for what you do with it. 🛡️

---

## Links

- GitHub: [github.com/zedwed11](https://github.com/zedwed11)
- Other projects: [github.com/zedwed11/Aya-Multitool](https://github.com/zedwed11/Aya-Multitool)
- Discord: [discord.gg/FB7d4HwM4Y](https://discord.gg/FB7d4HwM4Y)

---

## License

MIT — do what you want, just keep the disclaimer in mind. 🚀

---

⭐ If this helped you learn something, drop a star on the repo — it means a lot. And if you find a bug, open an issue — I'm still learning and I read every one. 💬

## MADE WITH LOVE BY ZED 💘!1!1!!
