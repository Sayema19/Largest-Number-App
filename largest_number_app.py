import streamlit as st

def find_largest_number(num1, num2, num3):
    """
    Function to find the largest among three numbers.
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    st.title("Find the Largest Number")

    # Input fields for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Button to trigger the calculation
    if st.button("Find Largest Number"):
        # Call the function to find the largest number
        result = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
