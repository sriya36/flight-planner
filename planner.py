from flight import Flight


class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.flights = flights
        
        last_city_number= max(max(flight.start_city, flight.end_city) for flight in flights)
        self.last_city_number = last_city_number
        self.adj_list = [[] for _ in range(last_city_number+1)]
        for flight in flights:
            self.adj_list[flight.start_city].append(flight)
        
        pass

    





    
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        





    
       
        best_path = [(None, None, float('inf'), float('inf'), None) for _ in range(self.last_city_number+1)]
        best_path[start_city] = (None, start_city, 0, t1, None)
        
        sequence = Queue()
        sequence.enqueue((start_city, 0, t1))
        

        while not sequence.is_empty():
            curr_city, no_of_flights, curr_time = sequence.dequeue()
            
            
            

            if curr_city == end_city:
                break

            for flight in self.adj_list[curr_city]:
                updated_no = no_of_flights + 1
                next_city = flight.end_city
                new_arrival_time = flight.arrival_time
                

                if (flight.departure_time >= max(20 + curr_time, t1) or (flight.start_city == start_city and flight.departure_time >=t1)) and flight.departure_time>=t1 and flight.arrival_time<=t2:
                    if updated_no < best_path[next_city][2] or (updated_no == best_path[next_city][2] and new_arrival_time < best_path[next_city][3]):
                        best_path[next_city] = (flight, next_city, updated_no, new_arrival_time, curr_city)
                    sequence.enqueue((next_city, updated_no, new_arrival_time))

        path = []
        curr_city = end_city
        while curr_city != start_city:
            if best_path[curr_city][0] is None:
                return []
            path.append(best_path[curr_city][0])
            curr_city = best_path[curr_city][4]
        path.reverse()
        return path

                    

        
        


        

        
            

        

        
        


        pass    
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        
            
                
            
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying:
        The route is a cheapest route
        """
        class Cheapest_HeapNode(HeapNode):
            def __init__(self, total_cost, current_time, curr_city, path, visited, arrival_time):
                super().__init__(total_cost, current_time, curr_city)
                self.path = path
                self.visited = visited.copy()
                self.arrival_time = arrival_time
                
            def compare(self, a):
                if self.total_cost != a.total_cost:
                    return self.total_cost < a.total_cost
                return self.arrival_time < a.arrival_time
        
        start_node = Cheapest_HeapNode(0, t1, start_city, [], [False] * (self.last_city_number+1), t1)
        heap = Heap([start_node])
        
        best_path = None
        best_cost = float('inf')
        best_arrival_time = float('inf')
        
        while heap.top() is not None:
            current = heap.extract()
            curr_city = current.curr_city
            
            if current.visited[curr_city]:
                continue
                
            current.visited[curr_city] = True
            
            if curr_city == end_city:
                if (current.total_cost < best_cost or (current.total_cost == best_cost and current.arrival_time < best_arrival_time)):
                    best_cost = current.total_cost
                    best_arrival_time = current.arrival_time
                    best_path = current.path
                continue
            
            
            valid_flights = []
            for flight in self.adj_list[curr_city]:
                
                if flight.departure_time >= current.current_time and flight.arrival_time <= t2:
                    
                    future_flights_exist = False
                    if flight.end_city == end_city:
                        future_flights_exist = True
                    else:
                        for next_flight in self.adj_list[flight.end_city]:
                            if (next_flight.departure_time >= flight.arrival_time + 20 and next_flight.arrival_time <= t2 and not current.visited[next_flight.end_city]):
                                future_flights_exist = True
                                break
                    
                    if future_flights_exist:
                        valid_flights.append(flight)
            
           
            for flight in valid_flights:
                new_cost = current.total_cost + flight.fare
                if new_cost <= best_cost:
                    new_path = current.path + [flight]
                    new_node = Cheapest_HeapNode(
                        new_cost,
                        flight.arrival_time + 20,
                        flight.end_city,
                        new_path,
                        current.visited,
                        flight.arrival_time
                    )
                    heap.insert(new_node)
        
        
        if best_path is None:
            return []
        return best_path
    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        





    
       
        
        class least_cheapest_HeapNode(HeapNode):
            def __init__(self, total_cost, current_time, curr_city, num_flights, path, visited):
                super().__init__(total_cost, current_time, curr_city)
                self.num_flights = num_flights
                self.path = path
                self.visited = visited.copy()
                
            def compare(self, a):
                if self.num_flights != a.num_flights:
                    return self.num_flights < a.num_flights
                return self.total_cost < a.total_cost
        
        init_node = least_cheapest_HeapNode(0, t1, start_city, 0, [], [False] * (self.last_city_number+1))
        heap = Heap([init_node])
        
        best_path = None
        best_flights = float('inf')
        best_cost = float('inf')
        
        while heap.top() is not None:
            current = heap.extract()
            curr_city = current.curr_city
            
            if current.visited[curr_city]:
                continue
                
            current.visited[curr_city] = True
            
            if curr_city == end_city:
                if (current.num_flights < best_flights or(current.num_flights == best_flights and current.total_cost < best_cost)):
                    best_flights = current.num_flights
                    best_cost = current.total_cost
                    best_path = current.path
                continue
            
            valid_flights = []
            for flight in self.adj_list[curr_city]:
                if flight.departure_time >= current.current_time and flight.arrival_time <= t2:
                    future_flights_exist = False
                    if flight.end_city == end_city:
                        future_flights_exist = True
                    else:
                        for next_flight in self.adj_list[flight.end_city]:
                            if (next_flight.departure_time >= flight.arrival_time + 20 and 
                                next_flight.arrival_time <= t2 and 
                                not current.visited[next_flight.end_city]):
                                future_flights_exist = True
                                break
                    
                    if future_flights_exist:
                        valid_flights.append(flight)
            
            for flight in valid_flights:
                if current.num_flights + 1 <= best_flights:
                    new_cost = current.total_cost + flight.fare
                    new_path = current.path + [flight]
                    new_node = least_cheapest_HeapNode(
                        new_cost,
                        flight.arrival_time + 20,
                        flight.end_city,
                        current.num_flights + 1,
                        new_path,
                        current.visited
                    )
                    heap.insert(new_node)
        
        if best_path is None:
            return []
        return best_path

    



class HeapNode:
    def __init__(self, total_cost, current_time, curr_city):
        self.total_cost = total_cost
        self.current_time = current_time
        self.curr_city = curr_city
        
    
    def compare(self, a):
        if self.total_cost < a.total_cost:
            return True
        return False
    
class Heap:
    def __init__(self,init_array):
        
        
       
        
        self.heap = init_array
        self.heapify()

    def heapify(self):
        n = len(self.heap)
        for i in range(n//2, -1, -1):
            self.heapify_down(i)

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract(self):
        if len(self.heap) > 1:
            self.swap(0, len(self.heap) - 1)
            top = self.heap.pop()
            self.heapify_down(0)
        elif self.heap:
            top = self.heap.pop()
        else:
            return None
        return top

    def top(self):
        if self.heap:
            return self.heap[0]
        return None

    def heapify_down(self, index):

        left = 2 * index + 1
        right = 2 * index + 2
        min = index
        if left < len(self.heap) and self.heap[left].total_cost< self.heap[min].total_cost:
            min = left
        if right < len(self.heap) and self.heap[right].total_cost<self.heap[min].total_cost:
            min = right
        if min != index:
            self.swap(index, min)
            self.heapify_down(min)

    def heapify_up(self, index):

        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index].total_cost <self.heap[parent].total_cost:
            self.swap(index, parent)
            self.heapify_up(parent)

    def swap(self, i, j):
        temp=self.heap[i]
        self.heap[i]=self.heap[j]
        self.heap[j]=temp

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None 
        self.rear = None   
        self.size = 0      

    def is_empty(self):
       
        return self.size == 0

    def enqueue(self, data):
        
        new_node = Node(data)
        if self.rear is None:
            
            self.front = self.rear = new_node
        else:
            
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        
        
        dequeued_data = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_data

    

  
