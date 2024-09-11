greeceData = []
otherCountriesData = []

# Helper Function to Validate Olympic Year
def isOlympicYear(year):
    # Modern Olympics started in 1896 and occur every 4 years.
    return (year - 1896) % 4 == 0

# Add Record for Greece with Previous 5-Year Records
def addGreeceRecord(data):
    country = "Greece"
    pastYearsData = []

    print("\nEnter details for the past five Olympic years:")
    for i in range(5):
        while True:
            pastYear = int(input(f"Enter Olympic year {i + 1} (e.g., 2016): "))
            if not isOlympicYear(pastYear):
                print(
                    f"Error: The Olympics did not happen in {pastYear}. Please enter a valid Olympic year.\n"
                )
            else:
                break

        weightClass = input(f"Enter the weight class for {pastYear} (e.g., 67kg): ")
        medal = input(
            f"Which medal did {country} win in {pastYear} (gold/silver/bronze/Did not get any medal)? "
        ).lower()

        if medal in ["gold", "silver", "bronze"]:
            pastYearsData.append(
                {"Year": pastYear, "WeightClass": weightClass, "Medal": medal}
            )
        elif medal == "did not get any medal":
            pastYearsData.append(
                {
                    "Year": pastYear,
                    "WeightClass": weightClass,
                    "Medal": "Did not get any medal",
                }
            )
        else:
            print("Invalid input for medal. Please try again.\n")
            return data

    # Add the record with past years data
    data.append({"Country": country, "PastYears": pastYearsData})

    print("Records for Greece added successfully!\n")
    print("-" * 50)  # Line break after record completion
    return data

# Add Record for Other Countries
def addOtherCountriesRecord(data):
    country = input("Enter the country: ")

    pastYearsData = []

    print("\nEnter details for the past five Olympic years:")
    for i in range(5):
        while True:
            pastYear = int(input(f"Enter Olympic year {i + 1} (e.g., 2016): "))
            if not isOlympicYear(pastYear):
                print(
                    f"Error: The Olympics did not happen in {pastYear}. Please enter a valid Olympic year.\n"
                )
            else:
                break

        weightClass = input(f"Enter the weight class for {pastYear} (e.g., 67kg): ")
        medal = input(
            f"Which medal did {country} win in {pastYear} (gold/silver/bronze/Did not get any medal)? "
        ).lower()

        if medal in ["gold", "silver", "bronze"]:
            pastYearsData.append(
                {"Year": pastYear, "WeightClass": weightClass, "Medal": medal}
            )
        elif medal == "did not get any medal":
            pastYearsData.append(
                {
                    "Year": pastYear,
                    "WeightClass": weightClass,
                    "Medal": "Did not get any medal",
                }
            )
        else:
            print("Invalid input for medal. Please try again.\n")
            return data

    # Add the record with past years data
    data.append({"Country": country, "PastYears": pastYearsData})

    print(f"Record for {country} added successfully!\n")
    print("-" * 50)  # Line break after record completion
    return data

# View Gold Medal Winners Across All Records
def viewGoldMedalWinners(data):
    if not data:
        print("No records found.\n")
    else:
        print("Gold Medal Winners Across All Countries:")
        found = False
        for record in data:
            print(f"Country: {record['Country']}")
            for pastRecord in record["PastYears"]:
                if pastRecord['Medal'] == "gold":
                    found = True
                    print(
                        f"  - Year: {pastRecord['Year']}, WeightClass: {pastRecord['WeightClass']}"
                    )
                    print("-" * 50)  # Line break after each gold medal record
        if not found:
            print("  No gold medals won.\n")
        print("=" * 50)  # Line break after each main record
        print()

# View All Records with Line Breaks for Each Year
def viewAllRecords(data, countryName=None):
    if not data:
        print("No records found.\n")
    else:
        if countryName:
            print(f"Records for {countryName}:")
        else:
            print("All Records:")

        for record in data:
            print(f"Country: {record['Country']}")
            print("PastYears:")
            for pastRecord in record["PastYears"]:
                print(
                    f"  - Year: {pastRecord['Year']}, WeightClass: {pastRecord['WeightClass']}, Medal: {pastRecord['Medal']}"
                )
                print("-" * 50)  # Line break after each past year record
            print("=" * 50)  # Line break after each main record
        print()

# Delete Record by Country
def deleteRecord(data, countryName):
    found = False
    for i, record in enumerate(data):
        if record["Country"] == countryName:

            found = True
            print(f"Record for {record['Country']} found and deleted successfully!\n")
            del data[i]
            break

    if not found:
        print(f"No record found for {countryName}.\n")

    return data

# Main Program Loop
def main():
    global greeceData, otherCountriesData

    while True:
        print("Choose an option:")
        print("1. Add Record for Greece")
        print("2. Add Record for Other Countries")
        print("3. View All Records for Greece")
        print("4. View All Records for Other Countries")
        print("5. View All Records")
        print("6. View Gold Medal Winners Across All Countries")
        print("7. Delete Record")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            greeceData = addGreeceRecord(greeceData)
        elif choice == "2":
            otherCountriesData = addOtherCountriesRecord(otherCountriesData)
        elif choice == "3":
            viewAllRecords(greeceData, "Greece")
        elif choice == "4":
            viewAllRecords(otherCountriesData, "Other Countries")
        elif choice == "5":
            allRecords = greeceData + otherCountriesData
            viewAllRecords(allRecords)
        elif choice == "6":
            allRecords = greeceData + otherCountriesData
            viewGoldMedalWinners(allRecords)
        elif choice == "7":
            countryName = input("Enter the name of the country to delete: ")
            if countryName.lower() == "greece":
                greeceData = deleteRecord(greeceData, countryName)
            else:
                otherCountriesData = deleteRecord(otherCountriesData, countryName)
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the Program
if __name__ == "__main__":
    main()
