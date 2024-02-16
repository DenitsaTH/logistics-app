# Logistics App

Logistics app is a console application that handles the planning of a logistics business based in Australia.
It lets the user log packages, create delivery routes and operate with a total of 40 trucks.

Running the program displays the following menu:

\*_\*_\*_\* MENU \*_\*_\*_\*
TO VIEW THE MENU, TYPE [0]
CREATE A ROUTE, TYPE [1]
TO ASSIGN A TRUCK TO ROUTE, TYPE [2]
TO CREATE A PACKAGE, TYPE [3]
TO ASSIGN A PACKAGE TO ROUTE, TYPE [4]\n' \
TO BULK ASSIGN, TYPE [5]
TO SEARCH FOR A PACKAGE BY ID, TYPE [6]
TO VIEW INFORMATION FOR ALL PENDING PACKAGES, TYPE [7]
TO VIEW INFORMATION FOR ALL ROUTES, TYPE [8]
TO EXIT THE PROGRAM, TYPE [Exit]
\*_\*_\*_\* MENU \*_\*_\*_\*

1. Creating routes:
    To create a route, type [1]. Then, you'll be prompted to type **at least** 2 stops. You can choose from a list of predefined stops. Input the stops with the following codes (upper or lower):

        SYD for Sydney
        MEL for Melbourn
        ADL for Adelaide
        ASP for Alice Springs
        BRI for Brisbane
        DAR for Darwin
        PER for Perth

    Default departure time is tomorrow, 6 am. Type [0] for keeping the default, or a number of days ahead to create a route for another day.
    The route is created and displayed on the console with departure time for first stop, arrival time for the rest of the stops, as well as delivery weight for each stop.

2. Assigning trucks to routes:
    To assign a truck to a route, type [2]. Then, you'll be prompted to provide the ID of the route you would like to assign a truck to.
    The system searches for an available truck for the designated time slot and assigns it to the route, if found.
    A message will be displayed whether a truck was found.

3. Creating packages:
    To create a package, type [3]. Then, you'll be asked to provide the following information (on a single line, separated by spaces):

        start location - the location where the package is being sent from. It has to be a correct stop (refer to 1).
        end location - the location that the package will be sent to. Again, it has to be a correct stop.
        package weight - has to be a number (in kg).
        customer's first name - has to be at least 2 characters long (upper or lower)
        customer's last name - has to be at least 2 characters long (upper or lower)
        customer's email - has to contain both '@' and '.'

    The package is created and information about the package is displayed on the console.

4. To assign a package to route, type [4]. Then, you'll be prompted to provide the ID of the package you want to assign to a route.
    The system searches for a suitable route and assigns the package, if found. A message will be displayed whether the package was assigned.

5. To bulk assign, type [5]. Then, provide the name of the warehouse where you would like the to do the bulk assign. It has to be a correct warehouse (refer to 1).
    The system checks the backlog of the warehouse. If there are less than 5 pending packages (not assigned to a route), it will display a message that there is no backlog.
    If the packages are more than 5, it will attempt to create a custom route for these packages, find a suitable truck for it and load _as many_ packages as possible. Then, it will display a message for each package - whether it is successfully assigned or not.

6. To search for a particular package by ID, type [6] and then input the ID of the package. The system will display information about the package - if it exists.

7. To view information for all _pending_ packages, type [7]. The system will display the information.

8. To view information for routes, type [8]. Then, you'll be prompted to type _all_ to display all routes, or _in progress_ to display only the routes currently in progress.

You can go back to the main menu at any time by typing 'back'.
When you are in the main menu, you can type [0] to display the menu again.

You can exit the program **only** from the main menu by typing 'exit'.
