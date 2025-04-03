# ZETA: Zoned Efficient Tour Algorithm 🚀

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/Pawarit-eng/ZETA-Algorithm.svg?style=social)](https://github.com/Pawarit-eng/ZETA-Algorithm)

A lightning-fast TSP heuristic solving **1 million cities in ~3 seconds** — using pure Python.  
Developed by **Pawarit Chantaraket** as a logic-first approach to practical algorithm design.

---

## 🔥 Features

- ⚡ **Extreme speed**: 1,000,000 cities in ~3 seconds
- 🧠 **Zone-based greedy algorithm** with optional zone-wise 2-opt
- 📦 **Pure Python** with no dependencies
- ✅ Scalable, readable, and hackable for any dev

---

## 🧪 Benchmarks

> ⚠️ **Note:** On local machines (e.g. VSCode), ZETA + 2-opt often runs much faster than in Google Colab.
> Performance may vary depending on VM throttling and CPU environment.

| Version           | Cities | Runtime | Cost  | Notes            |
| ----------------- | ------ | ------- | ----- | ---------------- |
| ZETA Core         | 1M     | ~3 sec  | ~38M+ | Fastest possible |
| ZETA + Zone 2-opt | 1M     | ~30 sec | ~29M+ | Better accuracy  |

---

## 📦 Included Files

| File           | Description                         |
| -------------- | ----------------------------------- |
| `zeta_core.py` | Core version — fastest, greedy only |
| `zeta_2opt.py` | Enhanced version — zone-wise 2-opt  |
| `README.md`    | You're reading it!                  |
| `LICENSE`      | MIT License                         |

---

## 🧠 Why ZETA?

> “I wanted to see if logic-first thinking could beat complexity — turns out it can.”  
> — _Pawarit Chantaraket_

---

## 🤝 Contribute

Pull requests, optimizations, new zone-linking strategies — all welcome!  
You can also fork and build your own version of ZETA with ML, 3-opt, grid partitioning, or CUDA!

---

## 🔗 Tags

`tsp`, `python`, `heuristic`, `optimization`, `algorithm`, `zeta`, `open-source`, `million-nodes`, `graph`, `logistics`

---

## 📜 License

This project is released under the [MIT License](LICENSE).

> 🛡 If you use or modify this algorithm, please credit the original author: **Pawarit Chantaraket**

This project is released under the [MIT License](LICENSE).
