from stopcov_parser import CovidParser

cv_parser = CovidParser()
cv_parser.parse()
text = f"total cases: {cv_parser.totalCases} (In last 24 hours {cv_parser.lastCases});\ntotal Recovered: {cv_parser.totalRecovered} (In last 24 hours {cv_parser.lastRecovered});\ntotal deaths: {cv_parser.totalDeaths} (In last 24 hours {cv_parser.lastDeaths});\nTested in last 24 hours: {cv_parser.lastTests}, with Antigen tests: {cv_parser.antigenTests}, with PCR tests: {cv_parser.pcrTests};\nPositive cases: (per day - {cv_parser.positiveCasesPerDay}, per 7 days - {cv_parser.positiveCasesPerWeek}, per 14 days - {cv_parser.positiveCasesPerTwoWeeks});\nVaccined: (total - {cv_parser.totalVaccined}, last day - {cv_parser.lastVaccined});\nquarantined: {cv_parser.quarantine};\nHospitalized: {cv_parser.hospitalize};\nIn Clinic hotels: {cv_parser.clinicHotels}"
print(text)
