# ATM User Interface Project

This project is a simple ATM user interface created using Python. It provides basic functionality for user authentication, account management, and transaction processing.

## Features

- **User Authentication**: Users can log in using their ID and password.
- **View Balance**: Users can check their account balance.
- **Deposit**: Users can deposit money into their account.
- **Withdrawal**: Users can withdraw money from their account.
- **Transaction History**: Users can view their transaction history.

## Files

- **u_menu.py**: User menu module containing functions for user interface and operations.
- **w_menu.py**: Worker menu module containing functions for worker interface and operations.
- **Banking** folder: Contains the user account data file and transaction records.
  - **accounts.txt**: File storing user account information.
  - **transactions.txt**: File storing transaction history.

## Getting Started

1. Clone the repository to your local machine.
2. Ensure Python is installed on your system.
3. Place the `u_menu.py` and `w_menu.py` files in a folder named `Banking` in your Python directory.
4. Run the `1.main.py` file to start the Interface.

## Usage

1. Upon starting the program, users are prompted to log in with their ID and password.(If you are using worker's access commands here is the id and password. Id: `overseas123@bank.in` pass: `greenway1234`)
2. After successful authentication, users can select from various options such as viewing balance, depositing, withdrawing, and viewing transaction history.
3. Workers can access additional functionalities such as creating new accounts, modifying account details, and generating transaction reports.

## Dependencies

- Python 3.x
- No external libraries required.

## Contributors

- [Pulkit Rustagi](https://github.com/Pulkit-exe) - Creator and main contributor

## License

This project is licensed under the [MIT License](LICENSE).
