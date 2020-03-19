from util import Queue
import random
import math

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # loop over a range of 0 to numUsers
        for i in range(0, num_users):
            # add user to the graph
            self.add_user(f"User {i}")

        # Create friendships
         # make a list of possible friendships
        possible_friends = []

        # avoid duplicates ensuring that the first number is smaller than the second

        # loop over userID in users
        for user_id in self.users:
            
            # loop over friend id in a range from user id + 1 to the lastID +1
            for friend_id in range(user_id + 1, self.last_id + 1):

                # append the tuple of (user id , friend id) to the possible friendships list
                possible_friends.append((user_id, friend_id))

        # shuffle the possible friendships using the random.suffle method
        random.shuffle(possible_friends)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            
            # set the friendship to possible friends at i
            friendship = possible_friends[i]
            
            # add friendship of friendship[0] and friendship[1]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # TODO
        # create a queue
        queue = Queue()
        # enqueue the user id as a list
        queue.enqueue([user_id])

        # while queue is not empty
        while queue.size() > 0:
            # dequeue to path variable
            path = queue.dequeue()
            # set new user id to the last item in path
            new_user_id = path[-1]

            # check if the new user id is not in the visited structure
            if new_user_id not in visited:
                # set the new user ids path in visited
                visited[new_user_id] = path

                # loop over each friend id in the friendships at the index of new user id
                for friend_id in self.friendships[new_user_id]:
                    # check that the friend id is not in visited
                    if friend_id not in visited:
                        # create a copy of the path
                        new_path = list(path)
                        # append the friend id to the copy of the path
                        new_path.append(friend_id)
                        # enqueue the copy of the path
                        queue.enqueue(new_path)

        # return the visited data structure
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
