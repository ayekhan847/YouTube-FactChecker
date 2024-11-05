PROBLEM DESCRIPTION
With the vast amount of video content on YouTube, it has become increasingly difficult for viewers to differentiate between accurate information and misinformation. While platforms like X (formerly Twitter) and Instagram have started integrating fact-checking tools for posts and images, YouTube doesn’t have a system available for the viewers to view. As a result, viewers may unknowingly consume misleading, biased, or incorrect information. This gap in verification poses risks for general viewers, educators, researchers, and advertisers who rely on YouTube for credible content. Thus, this project aims to create a fact-checking tool that adds a layer of credibility to a video.  

API/MODULES
The APIs I’ll be using for this project include:

YouTube Data API - To retrieve video metadata and transcripts from YouTube.
Overview and Documentation: Google Developers
API Reference: Google Developers

Google Fact Check Tools API - To cross-reference claims from the video transcript with verified fact-checks. This API connects to verified fact-checking resources, providing claim verification information.
Overview and Documentation: API Overview
API Explorer: Try the API

Google Cloud Natural Language API - To parse the video transcript and extract factual claims (entities and assertions) that require verification. 
Overview and Documentation: Google Cloud
API Reference: Google Cloud


OUTPUT DESCRIPTION
Clearly describes the planned output format for the project, and why that is an appropriate choice for the imagined user

The output description for this project will be a web-based prototype that includes a sidebar along the YouTube video. It will use the API data from You-Tube do real-time verification for video content. Once the program has analyzed the transcript of the video, it will extract the factual claims, check this against external databases, and then display the results. 
This is appropriate for the user because this output will simulate the experience of what a live fact-checking tool will offer. It’s going to be a separate sidebar, that way it doesn’t disrupt the actual content-viewing experience of the video.

Sidebar Panel Features:
Overall Credibility Indicator:
There will be an overall credibility score at the top of the sidebar that will be the result of all the claim statuses. Labels such as “Mostly Accurate” or “Mixed Claims” will be displayed.
Claims Overview: 
List the claims extracted from the transcript. Each claim includes a summary and timestamp (that will be clickable to the correct section of the video).
Verification Status: 
Will have these icons that display the verification:
Verified ✅: The claim is confirmed as accurate.
Disputed ⚠️: The claim is false or misleading.
Unverified ❓: No verification data is available.
Detailed Fact-Check Information:
If you click on a specific claim, it will give you a detailed view of that claim within the sidebar. This will have the chosen claim and the fact-checking source.

PROJECT PLAN
Week 1: Setting up the Project Workspace and YouTube Data API Integration (by 11/10)
1.	Project Setup:
o	Set up Flask or Django as the backend framework to handle API calls and data processing.
o	Create the basic project structure with folders for templates (HTML files), static files (CSS/JavaScript), and routes (Python scripts).
2.	YouTube Video Embedding and API Integration:
o	Embed a YouTube video player in the main page layout using HTML.
o	Set up API access to the YouTube Data API and write a function to receive the video captions. 
o	Test the function by retrieving and displaying captions from a sample YouTube video.
At this point: A web page with an embedded YouTube video and a sidebar that displays captions from the YouTube Data API.
Week 2: Use the Google Cloud Natural Language API to Identify Factual Claims for Verification. (by 11/17)
1.	Set Up and Integrate Google Cloud Natural Language API:
o	Set up access to the Natural Language API and add the API key to the backend.
o	Write a function in Python to send the transcript data to the Natural Language API for processing.
2.	Extract and Process Claims:
o	Process the API response to identify key factual claims, such as names, dates, and other entities.
o	Store each extracted claim along with its timestamp in a structured format for easy display.
3.	Display Claims in Sidebar:
o	Use Flask or Django templates (Jinja2) to dynamically render each claim in the sidebar.
o	Each claim should display its summary and timestamp.
At this point: Sidebar with a list of extracted claims from the transcript, each with a summary and timestamp.

Week 3: Fact-Checking Integration with Google Fact Check Tools API (by 11/24)
1.	Set Up and Integrate Google Fact Check Tools API:
o	Register and configure the Fact Check Tools API.
o	Write a function in Python that sends each extracted claim to the API and retrieves verification results.
2.	Process and Display Verification Results:
o	Process the fact-check response to determine the verification status for each claim (e.g., “verified,” “disputed,” or “unverified”).
o	Add the source of each verification result and a link to the full article if available.
3.	Update Sidebar to Show Verification Status:
o	Modify the sidebar to include an icon next to each claim (✅ for verified, ⚠️ for disputed, ❓ for unverified).
o	Use Flask/Django templates to display the verification status dynamically alongside each claim.
At this point: Sidebar with real-time verification statuses for each extracted claim, sourced from the Google Fact Check Tools API.

Week 4: Finalize UI, Add Interactivity, Testing, and Prepare Presentation (by 12/01)
1.	Add Overall Credibility Indicator:
o	Write a function to calculate an overall credibility score based on the verification statuses of all claims.
o	Display this score as a badge at the top of the sidebar.
o	
2.	Enhance Sidebar Interactivity:
o	Use JavaScript to make each timestamp clickable, allowing users to jump to the specific part of the video where the claim appears.
o	Add expand/collapse functionality so users can click on a claim to view additional details (such as the source of the fact-check).
3.	Styling and Final Testing:
o	Style the sidebar with CSS for a clean, user-friendly look.
o	Perform end-to-end testing with different videos to ensure smooth data flow, accurate claim extraction, and correct verification display.
4.	Prepare for Presentation:
o	Capture screenshots or record a video walkthrough showing the key features, including claim extraction, verification, and interactivity.
At this point: Have a functional prototype with a dynamic, interactive sidebar that displays real-time fact-checking information, ready for presentation.

Stretch Points:
If I have time, I might want to incorporate:
1.	Google Cloud Speech-to-Text API for videos that don’t have a transcript available. This would broaden this tool's functionality.
2.	Add a user feedback section that will allow users to collect user data on how they are interacting with the information given to them.
3.	Create a visual timeline that would go underneath the video that goes along with the claims in the video (hard to code this though). 
