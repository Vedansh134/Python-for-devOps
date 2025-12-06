# def calculate_shipping_cost(destination, weight_kg, is_expedited):
#     """
#     Calculates shipping cost using nested conditions based on 
#     destination (domestic/international), weight, and shipping speed.
#     """
#     base_cost = 0.0
#     expedited_fee = 10.0

#     print(f"Calculating shipping for {weight_kg}kg package to {destination}...")

#     # OUTER CONDITION: Check the destination
#     if destination == "domestic":
#         # First level of nesting
#         print("Destination: Domestic.")
        
#         # INNER CONDITION 1: Check weight for domestic shipping
#         if weight_kg <= 5:
#             base_cost = 5.00
#         elif weight_kg <= 20:
#             base_cost = 10.00
#         else:
#             base_cost = 25.00
            
#         # INNER CONDITION 2 (Nested within 'domestic' block): Check expedited status
#         if is_expedited:
#             total_cost = base_cost + expedited_fee
#             print(f"Expedited shipping selected (+${expedited_fee:.2f} fee).")
#         else:
#             total_cost = base_cost
            
#     elif destination == "international":
#         # Another path for the outer condition (international)
#         print("Destination: International.")

#         # INNER CONDITION 1: Check weight for international shipping
#         if weight_kg <= 2:
#             base_cost = 15.00
#         else:
#             # Another level of nesting within the 'international' weight check
#             # Heavier international packages require extra checks/fees
#             base_cost = 50.00
#             print("Heavy international package identified.")
            
#             # Very deep nesting for specific heavy international handling
#             if destination == "international" and weight_kg > 50:
#                  print("Requires special freight handling fee of $100.")
#                  base_cost += 100.00 # Add extra heavy freight fee

#         # INNER CONDITION 2 (Nested within 'international' block): Check expedited status
#         if is_expedited:
#             total_cost = base_cost + (expedited_fee * 2) # International expedited costs more
#             print(f"Expedited shipping selected (+${expedited_fee * 2:.2f} fee).")
#         else:
#             total_cost = base_cost

#     else:
#         # Outer else condition handles invalid destinations
#         print("Error: Invalid destination specified.")
#         return "N/A"

#     print(f"Base Cost: ${base_cost:.2f}")
#     print(f"Total Cost: ${total_cost:.2f}")
#     return total_cost

# # --- Example Usage ---
# print("--- Scenario 1: Domestic, Medium Weight, Standard Shipping ---")
# calculate_shipping_cost("domestic", 15, False)

# print("\n--- Scenario 2: International, Light Weight, Expedited Shipping ---")
# calculate_shipping_cost("international", 1, True)

# print("\n--- Scenario 3: International, Very Heavy Weight, Standard Shipping ---")
# calculate_shipping_cost("international", 60, False)
