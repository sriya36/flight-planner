# flight-planner
Route optimization system 

# ✈️ Flight Planner – Python Project

A flight route optimization system that finds the best travel paths based on customer needs – minimum connections, cheapest fare, or earliest arrival.

## 🚀 Features
- **Minimize Flights & Arrive Earliest**: Uses a BFS-based traversal to find routes with the fewest hops and earliest arrival.
- **Cheapest Route Finder**: Implements Dijkstra's algorithm to minimize fare.
- **Cheapest Among Fewest Flights**: Hybrid logic combining BFS and cost analysis.

## 🧰 Tech Stack
- Python
- Custom Graph Algorithms
- Priority Queue (heapq)
- Time-stamped data modeling

## 📊 Inputs
Each flight is modeled with:
- `flight_id`, `start_city`, `departure_time`, `end_city`, `arrival_time`, `fare`

## 🧠 Key Learnings
- Applied graph theory to real-world travel scenarios
- Designed time-efficient algorithms for decision-making
- Worked with structured data and route-building logic

## 📎 Example
```python
planner = Planner(flight_list)
route = planner.least_flights_cheapest_route(1, 6, 0, 1500)
for flight in route:
    print(f"{flight.flight_no}: {flight.start_city} -> {flight.end_city} | ₹{flight.fare}")
