import streamlit as st
import pandas as pd

st.title("🛒 Shopping Bill with Table Input")

# Number of items to add (you can make this dynamic too)
num_items = st.number_input("How many items do you want to enter?", min_value=1, max_value=20, value=3)

st.markdown("### Enter Product Details")

# Initialize an empty list to store item rows
items = []

for i in range(num_items):
    st.markdown(f"#### Item {i+1}")
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    
    with col1:
        product = st.text_input(f"Product Name {i+1}", key=f"name_{i}")
    with col2:
        mrp = st.number_input(f"MRP (₹) {i+1}", min_value=0.0, format="%.2f", key=f"mrp_{i}")
    with col3:
        rate = st.number_input(f"Rate (₹) {i+1}", min_value=0.0, format="%.2f", key=f"rate_{i}")
    with col4:
        quantity = st.number_input(f"Quantity {i+1}", min_value=0.0, format="%.2f", key=f"qty_{i}")
    
    amount = rate * quantity
    items.append({
        "S.No": i+1,
        "Product": product,
        "MRP": mrp,
        "Rate": rate,
        "Quantity": quantity,
        "Amount": amount
    })

tax_percent = st.number_input("Tax Percentage (%)", min_value=0.0, max_value=100.0, format="%.2f")

if st.button("Generate Bill"):
    df = pd.DataFrame(items)
    subtotal = df["Amount"].sum()
    tax = (subtotal * tax_percent) / 100
    total = subtotal + tax

    st.markdown("## 🧾 Bill Summary")
    st.dataframe(df.style.format({"MRP": "₹{:.2f}", "Rate": "₹{:.2f}", "Amount": "₹{:.2f}"}), use_container_width=True)
    st.write(f"**Subtotal:** ₹{subtotal:.2f}")
    st.write(f"**Tax ({tax_percent}%):** ₹{tax:.2f}")
    st.success(f"**Total Amount (including tax): ₹{total:.2f}**")
