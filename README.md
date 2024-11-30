Apartment Rental Management System


Description

This Apartment Rental Management System is a Python program designed to help manage apartment rentals. It allows users to rent, update, view, and end the rental of apartments, while also keeping track of payments and rental information. The system supports apartments numbered 1 to 30 and provides options for full or down payments. All apartment details, including rental dates and payment statuses, are saved to a file for future use, ensuring data persistence even after the program ends.


Features

Rent an Apartment: Tenants can choose an available apartment, enter their personal information, select an apartment type (studio, 1-bedroom, or 2-bedroom), and decide on the rental duration. They can also make full or down payments.

Update Rental Information: The system allows users to update tenant information or rental details like the rent date.

End Rent: The program allows tenants to end their rental term, making the apartment available again for other tenants.

View Apartments: Users can view both rented and available apartments along with tenant and payment details.

Data Persistence: All apartment rental information is stored in a JSON file (apartments_data.json) and can be reloaded when the program restarts.


Usage

The program will prompt you with a menu. You can choose from the following options:

[1] Rent Apartment: Rent a new apartment.

[2] Update Rental Information: Modify existing rental details.

[3] End Rent: End an existing rental.

[4] View All Apartments: View rented and available apartments.

[5] Exit: Exit the program and save the data.
