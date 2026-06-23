from datetime import datetime

bill_no = 1
customer_count = 0
grand_total = 0

while True:
    print("\n" + "=" * 50)
    print("SALES BILLING SYSTEM")
    print("Bill No:", bill_no)
    print("=" * 50)

    # Customer Name Validation
        name = input("Enter Customer Name: ").strip()
        if name:
            break
        print("Customer name cannot be empty!")

    total = 0
    items = []

    while True:
        item_name = input("Enter Item Name: ").strip()

        if not item_name:
            print("Item name cannot be empty!")
            continue

        # Amount Validation
        while True:
            try:
                amount = float(input("Enter Amount: "))
                if amount > 0:
                    break
                print("Amount must be greater than 0!")
            except ValueError:
                print("Please enter a valid amount!")

        # Quantity Validation
        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                if quantity > 0:
                    break
                print("Quantity must be greater than 0!")
            except ValueError:
                print("Please enter a valid quantity!")

        item_total = amount * quantity
        total += item_total

        items.append([item_name, amount, quantity, item_total])

        repeat = input(
            "Do you want to add more items? (yes/no): "
        ).lower()

        if repeat == "no":
            break

    gst = total * 0.18
    discount = total * 0.10
    final_amount = total + gst - discount

    current_time = datetime.now()

    print("\n" + "=" * 50)
    print("BILL RECEIPT")
    print("=" * 50)
    print("Bill No :", bill_no)
    print("Customer :", name)
    print(
        "Date & Time :",
        current_time.strftime("%d-%m-%Y %H:%M:%S")
    )

    print("\nItems Purchased")
    print("-" * 50)
    print(
        f"{'Item':15} {'Price':10} {'Qty':5} {'Total':10}"
    )
    print("-" * 50)

    for item in items:
        print(
            f"{item[0]:15} {item[1]:10.2f} "
            f"{item[2]:5} {item[3]:10.2f}"
        )

    print("-" * 50)
    print(f"Sub Total    : {total:.2f}")
    print(f"GST (18%)    : {gst:.2f}")
    print(f"Discount(10%): {discount:.2f}")
    print(f"Final Amount : {final_amount:.2f}")
    print("=" * 50)
    print("***** Happy Shopping *****")

    # Save All Bills Summary
    with open("sales.txt", "a") as f:
        f.write(
            f"Bill No: {bill_no}, "
            f"Customer: {name}, "
            f"Final Amount: {final_amount:.2f}\n"
        )

    # Save Individual Bill
    file_name = f"Bill_{bill_no}.txt"

    with open(file_name, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("BILL RECEIPT\n")
        f.write("=" * 50 + "\n")
        f.write(f"Bill No: {bill_no}\n")
        f.write(f"Customer: {name}\n")
        f.write(
            f"Date & Time: "
            f"{current_time.strftime('%d-%m-%Y %H:%M:%S')}\n\n"
        )

        f.write("Items Purchased\n")
        f.write("-" * 50 + "\n")

        for item in items:
            f.write(
                f"{item[0]} | "
                f"Price: {item[1]} | "
                f"Qty: {item[2]} | "
                f"Total: {item[3]}\n"
            )

        f.write("-" * 50 + "\n")
        f.write(f"Sub Total: {total:.2f}\n")
        f.write(f"GST: {gst:.2f}\n")
        f.write(f"Discount: {discount:.2f}\n")
        f.write(f"Final Amount: {final_amount:.2f}\n")

    grand_total += final_amount
    customer_count += 1
    bill_no += 1

    repeat1 = input(
        "\nDo you want to go to next customer? (yes/no): "
    ).lower()

    if repeat1 == "no":
        print("\n" + "=" * 50)
        print("DAY SUMMARY")
        print("=" * 50)
        print("Total Customers :", customer_count)
        print(f"Grand Total Sale : {grand_total:.2f}")
        print("=" * 50)
        print("Thank You!")
        break