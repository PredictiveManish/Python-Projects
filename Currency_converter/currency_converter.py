import requests
import streamlit as st

# Base URL and API key
base_url = "https://v6.exchangerate-api.com/v6"  # Correct your API URL if needed
api_key = "6dcc1350c605bb73c8478dfb"

# Display an image
st.image("image.jpeg", width=200)

# Function to fetch supported currencies
def fetching_supported_currency():
    url = f"{base_url}/{api_key}/codes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "supported_codes" in data:
            # Return a list of currency codes
            return [currency[0] for currency in data["supported_codes"]]
        else:
            st.write("Error: 'supported_codes' key not found in the response.")
            return None
    else:
        st.write(f"Error {response.status_code}: {response.text}")
        return None

# Function to convert currency
def currency_convert(amount, from_currency, to_currency):
    url = f"{base_url}/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "conversion_rate" in data and "conversion_result" in data:
            rate = data["conversion_rate"]
            converted_amount = data["conversion_result"]
            return rate, converted_amount
        else:
            st.write("Error: Required keys not found in the response.")
            return None, None
    else:
        st.write(f"Error {response.status_code}: {response.text}")
        return None, None

# Main currency converter app
def currency_converter():
    # Input amount
    amount = st.number_input("Enter an amount to convert:", value=100, step=1)

    # Fetch supported currencies
    supported_currencies = fetching_supported_currency()

    if supported_currencies:
        # Input 'from' currency
        from_currency = st.selectbox("From currency:", supported_currencies, index=19)

        # Input 'to' currencies
        to_currencies = st.multiselect("To currencies:", supported_currencies, default=["USD"])

        # Convert currency and display results
        if st.button("Convert"):
            st.write("Conversion results:")
            for to_currency in to_currencies:
                rate, converted_amount = currency_convert(amount, from_currency, to_currency)
                if rate:
                    st.write(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency} (Rate: 1 {from_currency} = {rate:.4f} {to_currency})")
                else:
                    st.write(f"Conversion failed for {from_currency} to {to_currency}. Please try again.")

# Run the app
if __name__ == "__main__":
    currency_converter()
