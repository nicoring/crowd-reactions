# crowd-reactions
Google Analytics for the real world! Get demographics and sentiment of people in front of your ads at public places.

This project is a result of a night of coding at [OxfordHack](http://www.oxfordhack.com/), also take a look at our submission at [DevPost](https://devpost.com/software/crowd-reactions)!

## Inspiration
We are bringing the capabilities of services like Google Analytics into the real world!
Allowing businesses to explore how people interact with billboards, posters and ads has tremendous value. 
And with our application, we can give the insights that people need to better target their audience in the physical world. 

## What it does
We are using the Microsoft Cognitive Services to analyze video footages of people around things like billboards, posters or other kinds of advertisements. 
Using this footages, we can analyze facial features and determine how people react to whatever they are looking at. 
So we also can determine demographics such as age, gender and other characteristics to give insights into how the target audience looks like.

## How we built it
Video footages are processed with the Microsoft Cognitive Services APIs.

First, we process the video file to find the different faces through the video.
Then we generate frames for every point in the video where faces are recognized. 

These images are then slightly enhanced and go through further processing by the Faces API and Emotion API. 
This data is then aggregated using react.js and highchart to provide clear characteristics about the audience reactions and demographics. We could even tell you how many people wear glasses.

## Challenges we ran into
Since we currently don't have a system with cameras attached to advertisements in places such as the London Underground, we don't have these footages to analyze. Therefore, we used timelaps videos of public places as a replacement. The charts shown in the images are based on this footage: https://www.youtube.com/watch?v=ZpHRp-WgQ0w.

## Accomplishments that we're proud of
Even though we did not have much experience in the area of video processing, we accomplished fairly good results and were able to work with video footage without further problems.

The tool-chain that we built to generate the final data has grown very quickly and has several intermediate steps. With this established tool-chain, it is easy to process further videos.

## What we learned
We learned how to process video footage with the Microsoft Cognitive Services and how to use external libraries to generate images for specific frames in a video. We were astonished how fast we could achieve good results using the Microsoft Cognitive Services without training a dedicated model for this task.

## What's next for crowd-reactions
Currently we can track faces in the video of people in front of ads, but we can't say whether they look on their phone, at the ad or somewhere else. As a next step we want to build a custom face recognition model that also computes for each face the probability that this person ist actually looking at the ad. Furthermore, our current platform can process complete video files. This can be extended with an endpoint, which consumes video streams in real time.  
