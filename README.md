This program is a simple currency converter that enables users to enter an amount in one currency and convert it into another currency using current exchange rates from the "exchangerate.host" API.
Program functionality:
Input starting currency (source currency) – the program prompts the user to enter the currency code (e.g., USD, EUR).
Input the amount for conversion – the user inputs the amount they wish to convert.
Input target currency – the program prompts the user to enter the currency code into which they want to convert the amount.
Get conversion rate – the program uses an API call to get the conversion rate between the source and target currencies.
Calculate the converted amount – using the conversion rate, the program calculates how much the amount is in the target currency.
Display the result – the program displays to the user how much the entered amount is converted into the target currency.
The program uses:
urllib.request: Library for sending HTTP requests and downloading URLs.
json: Library for decoding JSON data received from the API.
sys: Library that provides access to some variables and functions interacting with the Python interpreter.
This program uses the "exchangerate.host" API to get current exchange rates. The API does not require an API key, which simplifies usage. The program is straightforward to use and provides quick results for currency conversion.
