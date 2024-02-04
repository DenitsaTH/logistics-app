# App Structure

1. main.py creates an instance of LogisticsFacade - the only class which directly interacts with client code.
2. It starts a while loop that reads line by line from the client_code.txt and attempts to execute the command, or catches an Error, if raised.
3. Logistics facade instantiates App Data - the central place for all app data. It also instantiates PackageManager and RouteManager both of which have a reference to the app data instance.
4. PackageManager operates with Packages, while RouteManager operates with Routes.
5. AppData has a list of Routes and a list of pending packages.
6. Each route has a Truck.
7. Each Truck has Packages for delivery.
