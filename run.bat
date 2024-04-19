pytest -v -s -m "smoke" -n=2 --html=./Reports/report_chrome.html testCases/ --browser chrome
rem pytest -v -s -m "smoke" -n=2 --html=./Reports/report_firefox.html testCases/ --browser firefox
rem pytest -v -s -m "smoke" -n=2 --html=./Reports/report_edge.html testCases/ --browser edge

rem pytest -v -s -m "smoke or regression" -n=2 --html=./Reports/report_chrome.html testCases/ --browser chrome
rem pytest -v -s -m "smoke or regression" -n=2 --html=./Reports/report_firefox.html testCases/ --browser firefox
rem pytest -v -s -m "smoke or regression" -n=2 --html=./Reports/report_edge.html testCases/ --browser edge