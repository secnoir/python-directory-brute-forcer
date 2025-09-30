# Simple Python Directory Brute Forcer

This is one of my first Python security scripts. It brute-forces website directories by trying a list of common paths and shows which ones exist (200 OK) or are blocked (403).
I built it to learn how directory brute forcing works under the hood, instead of just using tools like Gobuster or Dirb. It helped me understand HTTP status codes, requests, and how wordlists can reveal hidden parts of a site.

# Improved python directory brute forcer

This is a better version of the directory brute forcer that uses a wordlist file instead of manually typing words and it also uses Multithreading that makes it much faster
If the response is not 404, it prints the URL and status code — those are likely existing resources (200, 301, 403, etc.).
But != 404: catches more signs of existence (403, redirects, etc.), but it’s noisy (false positives like custom 404 pages that return 200). So it could be better.
