PROBLEM DESCRIPTION
With the vast amount of video content on YouTube, it has become increasingly difficult for viewers to differentiate between accurate information and misinformation. While platforms like X (formerly Twitter) and Instagram have started integrating fact-checking tools for posts and images, YouTube doesn’t have a system available for the viewers to view. As a result, viewers may unknowingly consume misleading, biased, or incorrect information. This gap in verification poses risks for general viewers, educators, researchers, and advertisers who rely on YouTube for credible content. Thus, this project aims to create a fact-checking tool that adds a layer of credibility to a video.  

API/MODULES
The APIs I’ll be using for this project include:

YouTube Transcript API - To retrieve video metadata and transcripts from YouTube.
Overview and Documentation: Google Developers
API Reference: Google Developers

Google Fact Check Tools API (Later on, for this project, I simply stopped at the claim extraction part)
- To cross-reference claims from the video transcript with verified fact-checks. This API connects to verified fact-checking resources, providing claim verification information.
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

P3 VERSION:
For this project checkpoint, I decided to stop at the claim extraction part, using only two APIs. I will be working on this project further to incorporate the Google Fact Check API.