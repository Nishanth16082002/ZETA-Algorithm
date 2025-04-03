# ZETA Algorithm - Core Version (zeta_core.py)
# Created by Pawarit Chantaraket
import math
import random
from time import time

# Generate random cities
def generate_cities(n, seed=42):
    random.seed(seed)
    return {i: (random.randint(0, 1000), random.randint(0, 1000)) for i in range(n)}

# Euclidean distance
def dist(a, b, cities):
    ax, ay = cities[a]
    bx, by = cities[b]
    return math.hypot(ax - bx, ay - by)

# Greedy TSP inside a list of cities
def tsp_greedy(city_list, cities):
    start = city_list[0]
    unvisited = set(city_list)
    path = [start]
    unvisited.remove(start)
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda x: dist(last, x, cities))
        path.append(next_city)
        unvisited.remove(next_city)
    cost = sum(dist(path[i], path[i+1], cities) for i in range(len(path)-1)) + dist(path[-1], path[0], cities)
    return path, cost

# 2-opt optimization
def tsp_2opt(path, cities):
    best = path
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best)):
                if j - i == 1:
                    continue
                new_path = best[:i] + best[i:j][::-1] + best[j:]
                new_cost = calc_cost(new_path, cities)
                current_cost = calc_cost(best, cities)
                if new_cost < current_cost:
                    best = new_path
                    improved = True
        path = best
    return best, calc_cost(best, cities)

# Total tour cost
def calc_cost(path, cities):
    return sum(dist(path[i], path[i+1], cities) for i in range(len(path)-1)) + dist(path[-1], path[0], cities)

# ZETA with zone-wise 2-opt optimization
def zlh_tsp_2opt(cities, zone_size=5):
    city_ids = list(cities.keys())
    zones = [city_ids[i:i+zone_size] for i in range(0, len(city_ids), zone_size)]

    full_path = []
    for zcities in zones:
        path = tsp_greedy(zcities, cities)
        refined_path, _ = tsp_2opt(path, cities)
        full_path.extend(refined_path)

    total_cost = calc_cost(full_path, cities)
    return full_path, total_cost

# Example usage
if __name__ == "__main__":
    n = 1000000
    cities = generate_cities(n)

    print("Running ZETA (core version)...")
    start = time()
    path, cost = zlh_tsp(cities)
    elapsed = time() - start
    print(f"[ZETA] Runtime: {round(elapsed, 4)}s | Cost: {round(cost, 2)}")

    print("\nRunning ZETA + 2-opt (zone-wise)...")
    start = time()
    path2, cost2 = zlh_tsp_2opt(cities)
    elapsed2 = time() - start
    print(f"[ZETA+2opt] Runtime: {round(elapsed2, 4)}s | Cost: {round(cost2, 2)}")

    print(f"\nPaths valid: {len(set(path)) == len(cities)} and {len(set(path2)) == len(cities)}")
