

# Restaurant Order Management

This Python program allows restaurant staff to manage a menu, place customer orders, undo placed orders, and process orders. It uses a **menu list** to store available items and a **deque** (double-ended queue) to manage placed orders.

## Features

1. **Add Menu Items:** Add food or drink items to the restaurant menu.
2. **Remove Menu Items:** Remove specific items from the menu.
3. **Place Orders:** Customers can place orders from the available menu items.
4. **Undo Orders:** The last placed order can be undone.
5. **Process Orders:** Orders can be processed in the sequence they were placed (First-In, First-Out).

## How to Use

1. **Add Menu Items:** Enter the number of items you'd like to add and specify each item.
2. **Remove Menu Items:** If you wish to remove menu items, enter the number and name of the items to remove.
3. **Place Orders:** Place orders based on the current menu. If an ordered item is not on the menu, the program will notify you.
4. **Undo Orders:** Undo the most recently placed orders.
5. **Process Orders:** Process the orders, starting from the first one placed.

## Example Commands

- **Add a menu item:** `addMenuItem("rice")`
- **Add a menu item:** `addMenuItem("chips")`
- **Remove a menu item:** `removeMenuItem("chips")`
- **Place an order:** `placeOrder("rice")`
- **Undo an order:** `undoOrder()`
- **Process an order:** `processOrder()`
