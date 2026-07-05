from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

#res = tavily_search("Best hotels in india")
#print(res)

#res = search_flights("Plan a 7 days Nepal trip from India")
#print(res)

use_input = input("Enter travel request:")
response = run_travel_agent(
    user_input=use_input,
    thread_id="test_user"
)

print("\nFinal Response:\n")
print(response["answer"])