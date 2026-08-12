currency={
    "india":"rupees",
    "portugal":"euro",
    "USA":"Dollar",
    "UAE":"Dirham"
}

print(currency["india"])

print("The currency of Japan is",currency.get("Japan","NOT FOUNd"))
print("The currency of USA is",currency.get("USA","NOT FOUNd"))