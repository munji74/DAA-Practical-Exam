from collections import defaultdict, deque

class SocialNetworkGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, user1, user2):
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)

    def get_friends(self, user):
        return self.graph[user]

def find_mutual_friends(graph, user1, user2):
    #  a set to keep track of visited users
    visited = set()

    # a queue for BFS
    queue = deque()

    # append(enqueue) the starting user, mark it as visited
    queue.append(user1)
    visited.add(user1)

    # BFS to find user2
    while queue:
        current_user = queue.popleft()

        #if the current user is user2, if yes, return mutual friends
        if current_user == user2:
            return get_mutual_friends(graph, user1, user2)

        # Enqueue unvisited neighbors
        for neighbor in graph.get_friends(current_user):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    # If no user2, an empty list is returned(no mutual friends)
    return []

def get_mutual_friends(graph, user1, user2):
    # a list to store mutual friends
    mutual_friends = []

    #friends of both users
    friends_user1 = set(graph.get_friends(user1))
    friends_user2 = set(graph.get_friends(user2))

    #intersection two sets for get mutual friends
    mutual_friends = list(friends_user1.intersection(friends_user2))

    return mutual_friends



social_network = SocialNetworkGraph()
social_network.add_edge("Alala", "James")
social_network.add_edge("Alala", "Nina")
social_network.add_edge("James", "Ian")
social_network.add_edge("Nina", "David" )
social_network.add_edge("David", "Amos")

user1 = "Alala"
user2 = "David"

#print mutual friends
mutual_friends = find_mutual_friends(social_network, user1, user2)
print(f"Mutual friends between {user1} and {user2}: {mutual_friends}")
