print("🧾✨ Bill Split Calculator ✨🧾")

from datetime import datetime
from barcode import Code128
from barcode.writer import ImageWriter

# Input section
bill_amount = float(input("💰 Enter bill amount: $"))
tip_percentage = float(input("💡 Enter tip percentage: "))
people = int(input("🧑‍🤝‍🧑 Enter number of people: "))

# Calculations
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / people

# Generate a unique bill ID
bill_id = f"BILL-{datetime.now().strftime('%Y%m%d%H%M%S')}"

# Show results on screen with emojis
print("\n🎉 --- Results --- 🎉")
print(f"🆔 Bill ID: {bill_id}")
print(f"💵 Total (including tip): ${total_amount:.2f}")
print(f"🙋 Each person pays: ${amount_per_person:.2f}")

# Save results to a text file
with open("bill.txt", "w", encoding="utf-8") as file:
    file.write("🧾✨ Bill Split Calculator ✨🧾\n\n")
    file.write(f"🆔 Bill ID: {bill_id}\n")
    file.write(f"💰 Bill amount: ${bill_amount:.2f}\n")
    file.write(f"💡 Tip percentage: {tip_percentage}%\n")
    file.write(f"💵 Total (including tip): ${total_amount:.2f}\n")
    file.write(f"🙋 Each person pays: ${amount_per_person:.2f}\n")

# Generate and save a barcode image for the bill ID
barcode_file = Code128(bill_id, writer=ImageWriter()).save("bill_barcode")
print(f"✅ Bill saved to bill.txt and barcode saved to {barcode_file}.png")

input("Press Enter To Leave")