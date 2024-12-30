import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime, time


def run_google_search(search_term):
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.maximize_window()

    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    time.sleep(1)

    suggestions_box = driver.find_element(By.CSS_SELECTOR, "ul.G43f7e")
    suggestion_elements = suggestions_box.find_elements(By.TAG_NAME, "li")
    suggestions = []
    for element in suggestion_elements:
        try:
            suggestion_text = element.get_attribute("data-entityname")
            if suggestion_text:
                suggestion_text = suggestion_text.replace("<b>", "").replace("</b>", "")
                suggestions.append(suggestion_text)
        except:
            continue

    max_min = []

    if suggestions:
        longest_suggestion = max(suggestions, key=len)
        shortest_suggestion = min(suggestions, key=len)
        max_min.insert(0, longest_suggestion)
        max_min.insert(1, shortest_suggestion)

    driver.close()
    return max_min

def modify_cv():
    workbook = openpyxl.load_workbook("D:/Programming/Projects/Google_Short_Long_Keywords/SeleniumTest/Excel.xlsx")
    today = datetime.date.today()
    day_name = today.strftime("%A")

    sheet = workbook[day_name]

    print("Extracting CSV data")

    for row in range(3, 13):
        cell_value = sheet[f'C{row}'].value
        max_min = run_google_search(cell_value)
        print(max_min[0])
        sheet[f'D{row}'] = max_min[0]
        sheet[f'E{row}'] = max_min[1]

    workbook.save("D:/Programming/Projects/Google_Short_Long_Keywords/SeleniumTest/Excel.xlsx")
    print("CSV modified!")
    return None



if __name__ == "__main__":
    modify_cv()
    print("Program ran successfully");
