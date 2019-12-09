
class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, path):
        self.children[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self, hanlder=None):
        self.root = RouteTrieNode(hanlder)

    def insert(self, paths, handler):

        current_node = self.root
        for path in paths:

            if path not in current_node.children:
                current_node.insert(path)
            current_node = current_node.children[path]

        current_node.handler = handler


    def find(self, paths):

        current_node = self.root

        for path in paths:

            if path in current_node.children:
                current_node = current_node.children[path]
            elif path not in current_node.children:
                return False

        if current_node.handler:

            return current_node.handler

class Router:
    def __init__(self):
        self.routes = RouteTrie("Root Handler")

    def add_handler(self, path, handler):
        self.routes.insert(self.split_path(path), handler)



    def lookup(self, path):
        handler = self.routes.find(self.split_path(path))

        if handler:
            return handler
        else:
            return 404, "Not Found"


    def split_path(self, path):
        return list(filter(None, path.split("/")))


# create the router and add a route
router = Router() # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
