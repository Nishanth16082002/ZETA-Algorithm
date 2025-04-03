# ZETA: Zoned Efficient Tour Algorithm

A blazing-fast heuristic for solving the Travelling Salesman Problem (TSP) at extreme scale. Designed by **Pawarit Chantaraket**, ZETA is capable of computing TSP tours for **1 million cities in ~3 seconds** — using only pure Python and no external libraries.

---

## 🚀 What is ZETA?

ZETA (Zoned Efficient Tour Algorithm) is a divide-and-conquer heuristic for TSP. It uses a simple but powerful idea:

1. **Divide** all cities into small zones (e.g. 5–10 cities per zone)
2. **Greedy solve** each zone independently
3. **Merge** the zone tours into a single large tour
4. (Optional) Apply **2-opt optimization** within each zone for better accuracy

---

## ⚡ Key Features

| Feature            | Description                                      |
|--------------------|--------------------------------------------------|
| 💡 Simple Logic     | No external libraries, just Python              |
| 🚀 High Performance | 1M cities in ~3 seconds (ZETA core version)     |
| 🧠 Optional Refinement | Zone-wise 2-opt for better accuracy         |
| 🔁 Deterministic     | Uses seeded random generation                  |

---

## 📦 Included Versions

- `zlh_tsp` — ZETA Core (greedy only)
- `zlh_tsp_2opt` — ZETA + zone-wise 2-opt

---

## 🧪 Example Benchmark (on 1M Cities)

```bash
[ZETA] Runtime: 2.89s | Cost: 38424382.78
[ZETA+2opt] Runtime: 31.22s | Cost: 29734124.55
```

> ✅ ZETA is ideal when you need **speed at extreme scale**
> ✅ ZETA + 2-opt balances **accuracy and performance**

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**Pawarit Chantaraket**  
> “I built ZETA to test whether logic-first thinking can beat brute-force knowledge — turns out it can.”

---

## 📈 Want to contribute?
Feel free to fork, open issues, or propose enhancements. Optimization ideas (3-opt, zone linking, caching) are welcome!

---

## 🔗 Related Keywords
`TSP`, `Heuristic`, `Million Cities`, `Python`, `Divide and Conquer`, `Greedy`, `2-opt`, `Algorithm`, `Open Source`, `Logistics`, `Optimization`
