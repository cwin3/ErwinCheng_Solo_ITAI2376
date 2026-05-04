# ErwinCheng_Solo_ITAI2376

# Smart Car Buying Assistant

## Objective

The objective of this project is to design and develop an AI-powered car buying assistant that helps users find the best vehicle options based on their preferences. The system filters and analyzes car listings, highlights good deals, and flags potentially risky listings to support smarter decision-making. This project also demonstrates how AI concepts can be applied to a real-world problem in a simple and practical way.

---

## Features
- 10,000 realistic car listings
- VIN, dealer, fraud detection
- Filtering + sorting
- Favorites + comparison
- AI assistant (Ollama)

## Run

python generated_dataset.py
ollama run llama3
streamlit run app.py


## Deep Learning Connection

This project is designed to simulate how AI systems help people make better decisions when buying a car.

Even though the deployed version uses a simplified AI response for stability, the structure of the system is inspired by real deep learning models, especially Transformer-based models like ChatGPT.

---

How to choose Agent Framework.pdf
PDF
ITAI_2376_Midterm_Final_Project_Specs.pdf
PDF
OVERVIEW

Your midterm is a design document — a blueprint for the AI agent you will build for the final. You are not building anything yet. You are planning, researching, and showing me that you understand how the deep learning concepts we have covered connect to real-world AI agent applications.

This blueprint becomes the foundation for your Final Project (due May 3).


CHOOSE YOUR PATH

• Option A — Single AI Agent: Plan one agent that uses deep learning to perceive, reason, and act on a real-world task.


Declare which option you are choosing and explain why.


WHAT TO INCLUDE IN YOUR BLUEPRINT (3–6 pages)

1. Problem Statement — What real-world problem does your agent solve? Who benefits?
2. Option Choice — Which option (A ) and why.
3. Agent Architecture — A diagram showing inputs, reasoning, actions, and tools. Label everything.
4. Deep Learning Connection — Identify at least 2 course modules (CNNs, RNNs, Transformers, VAEs, GANs, etc.) and explain how they fit into your agent.
5. Agent Framework — Which framework you plan to use (LangChain, CrewAI, AutoGen, smolagents, or other) and why.
6. Tools & Data — What tools, APIs, and data sources will your agent need?
7. Build Plan — A week-by-week timeline from midterm to final due date.
8. Anticipated Challenges — What could go wrong and how will you handle it?


RUBRIC (100 points)

• Problem Statement & Use Case — 10 pts
• Option Choice & Justification — 5 pts
• Agent Architecture & Diagram — 30 pts
• Deep Learning Connection (2+ modules) — 25 pts
• Agent Framework & Tools/Data — 15 pts
• Build Plan & Challenges — 10 pts
• Professional Quality & File Naming — 5 pts Should be an agent non existing yet
make it related to a steam bun manufacturing company
topic about car buying consolidating all listing available online from various sellers
Convert this into a clean Word document with formatting
Create a professional diagram image instead of ASCII
Pasted text(3).txt
Document
Full working LangChain code (agent + tools)
Clean GitHub README (already formatted)
Your REFLECTION.md (easy points)
Better architecture diagram (submission-ready)
Demo script (so you sound confident) Build the actual Python agent code next
Improve your Word document (make it longer + more professional)
Create your GitHub repo files (README, structure, etc.)
help push to github
help creating the app on a platform
make UI better
 add these: Car images 🖼️
Real API listings
“Good Deal Score” UI
Sorting (Best / Cheapest / Newest)
Chat-style interface
Real APIs (RapidAPI Cars / Autotrader scraping)
Save favorites ❤️
Compare cars side-by-side
Login system
Deploy to public URL
Clean your UI to look like CarMax / Tesla site
consolidate and arrange all upgrades into the correct arrangement and give me the final code per file
 review github code File "/mount/src/erwincheng_solo_itai2376/app.py", line 2, in <module>
    from src.agent import agent
File "/mount/src/erwincheng_solo_itai2376/src/agent.py", line 1, in <module>
    from langchain.agents import initialize_agent, Tool error
ImportError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/erwincheng_solo_itai2376/app.py", line 2, in <module>
    from src.agent import agent
File "/mount/src/erwincheng_solo_itai2376/src/agent.py", line 1, in <module>
    from langchain.agents import initialize_agent
https://github.com/cwin3/ErwinCheng_Solo_ITAI2376/tree/main check what is wrong with my codes wont work with streamlit
how to get OPENAI_API_KEY
switch agent to local LLM
build everything with ollama locally and run through streamlit
what are other alternative with ollama to run with streamlit
where does the app get the database?
Auto.dev and MarketCheck use these api for data source
generate real data file with 100000 us cars base online current data
archive.zip
Zip Archive
use this as data set build the app with this dataset
finalize code using the dataset provided
file have schema.json what does this mean?
generate 10k data set for project use similar to real dataset online
make it more realistic like real live dataset online
VIN numbers
Dealer names
Real image URLs
Price anomalies (great deals / bad deals)
Fraud listings
add advanced realism“connect dataset to filtering UI”
👉 “final project polish”
give me final codes for github
https://github.com/cwin3/ErwinCheng_Solo_ITAI2376/tree/main check for errors and what to remove
Error running app. If you need help, try the Streamlit docs and forums.
renamed to generated_dataset.py
https://github.com/cwin3/ErwinCheng_Solo_ITAI2376
what should my github contain?
list me all the final codes 
where is my generated cars.csv 
not on github
did you create me a cars.csv file?
generate a downloadable cars.csv 
where car  i run option 1
run on vs code
run on google colab
where do I do step 5
update all files for github 
[04:57:59] ❗️ installer returned a non-zero exit code

[04:57:59] ❗️ Error during processing dependencies! Please fix the error and push an update, or try restarting the app. streamlit error
make cloud safe  version
streamlit stop not running the app while installing
Pasted text(5).txt
Document
add right photo for each car brand and model
add multiple images per car (gallery)
add real dealer logos
make UI look like CarMax/Tesla
Tesla-style UI
give me updated full codes and documentations
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 542, in _run_script
    exec(code, module.__dict__)
File "/mount/src/erwincheng_solo_itai2376/app.py", line 23, in <module>
    cars_data = load_data()
                ^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/caching/cache_utils.py", line 210, in wrapper
    return cached_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/caching/cache_utils.py", line 239, in __call__
    return self._get_or_create_cached_value(args, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/caching/cache_utils.py", line 266, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/caching/cache_utils.py", line 322, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/mount/src/erwincheng_solo_itai2376/src/tools.py", line 14, in load_data
    df["images"] = df["images"].apply(ast.literal_eval)
                   ~~^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/pandas/core/frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc
    raise KeyError(key) from err
generate full code with fall back
no clear cache and deploy option
add drop down choices for car brands and model
show me updated full code wit changes
TypeError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 542, in _run_script
    exec(code, module.__dict__)
File "/mount/src/erwincheng_solo_itai2376/app.py", line 74, in <module>
    st.image(c["images"][0], use_container_width=True)
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/metrics_util.py", line 397, in wrapped_func
    result = non_optional_func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
give me full updated code for the changes done
TypeError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 542, in _run_script
    exec(code, module.__dict__)
File "/mount/src/erwincheng_solo_itai2376/app.py", line 78, in <module>
    st.image(image[0], use_container_width=True)
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/metrics_util.py", line 397, in wrapped_func
    result = non_optional_func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
update app.py codes
image = c.get("images")

# FINAL SAFE CHECK
if isinstance(image, list) and len(image) > 0 and isinstance(image[0], str) and image[0].startswith("http"):
    st.image(image[0], use_container_width=True)
else:
    st.image("https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg", use_container_width=True) where to add this
write full code and which file it goes to
add generate botton
search botton
TypeError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 542, in _run_script
    exec(code, module.__dict__)
File "/mount/src/erwincheng_solo_itai2376/app.py", line 86, in <module>
    st.image(image[0], use_container_width=True)
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/metrics_util.py", line 397, in wrapped_func
    result = non_optional_func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
get me updated app.py with new changes
remove generate new listing botton
TypeError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 542, in _run_script
    exec(code, module.__dict__)
File "/mount/src/erwincheng_solo_itai2376/app.py", line 109, in <module>
    st.image(get_safe_image(c), use_container_width=True)
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/metrics_util.py", line 397, in wrapped_func
    result = non_optional_func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
go back to generic car photo
show me the updated codes
final codes
TypeError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 542, in _run_script
    exec(code, module.__dict__)
File "/mount/src/erwincheng_solo_itai2376/app.py", line 93, in <module>
    st.image(
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/metrics_util.py", line 397, in wrapped_func
    result = non_optional_func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
where do I get the files
where do I generate image files
give me updated codes with online image 
use car brand logo as image
update the codes with latest change request
how to create the demo
Demo Inside the Repository

Your demo must be accessible from the repo. Choose one of these three approaches.

The preferred approach is to upload the demo video file directly to the repo in a folder called demo. GitHub supports video files up to 100 MB. If your video is larger, compress it or use one of the other options.

A second approach is to upload the video to YouTube as unlisted, or to Loom or Google Drive, and place the link in your README.

A third approach, if your agent runs in a notebook or has a simple text interface, is to include a recorded screen capture or an animated GIF showing it working.

The demo must show your agent handling at least 3 different real world scenarios and must be 3 to 5 minutes long.
ollama not working
how much it cost to use open ai
Pasted text(6).txt
Document
did my work satisfy the grading rubics
upgrade your Deep Learning explanation (easy boost) write your perfect reflection
relax and humanized tone
write an objective 
use openai for more complex queries and ollama for basic once
integrate this cleanly into your current app
update reflection
deep learning connection update

---

### Big Picture

Overall, this project shows how AI concepts like:
- decision-making
- feature evaluation
- anomaly detection
- and language-based guidance

can be applied to a real-world problem like buying a car.

Even though the AI is simplified, the structure reflects how real AI systems are designed.


Final Project Structure
ErwinCheng_Solo_ITAI2376/
│
├── app.py
├── generated_dataset.py
├── requirements.txt
├── README.md
├── REFLECTION.md
│
├── data/
│   └── cars.csv   (optional, auto-generated if missing)
│
├── src/
│   ├── tools.py
│   └── ollama_agent.py
