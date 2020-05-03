##borgr

IT'S LIVE! Try it for yourself!

borgr.space (if your browser complains about that URL go here instead!)

Domain.com Best Domain Submission: borgr.space

Inspiration
Close your eyes and imagine you're on a road trip with your best buddies. Someone's stomach grumbles, you need to find somewhere to eat. It's been a long day and you don't want to argue but how will you pick where to go? That's the problem I'm trying to solve. Introducing borgr, my new project that sends you to the nearest burger restaurant with one click.

What it does
Using borgr is simple: go to borgr.space and hit the button and it'll redirect you to a google maps page for the nearest burger restaurant to your location.

This works by using a pair of Radar.io's APIs. First it uses the IP Geocoding API to get your coordinates from your IP address, then uses the Place Search API to find the nearest burger restaurant to you from those coordinates. Then, it'll do some borgr magic and generate a well formatted google maps search link with it'll then redirect you to, which lets you easily get the directions from.

In addition, my UiPath implementation means that whenever someone uses the website, I get an email saying where the borgr button led them to in an effort to create a borgr map in the future to show where in the world people have been wanting burgers and using borgr.

How I built it
A python3 flask server I deployed on Heroku with gunicorn hosts the site which uses HTML on the frontend. The backend heavily utilizes radar.io's IP Geocoding and Place Search APIs. I also used UiPath's StudioX to send myself the Outlook emails.

Challenges I ran into
-Learning to use Heroku

-Fighting with HTML to make the site legible

-My wifi network thinking I was in NJ and giving my devices IPs accordingly. These IPs were nowhere near any burger places :(

-Learning to use StudioX

Accomplishments that we're proud of
-This was the first hackathon I did by myself!

What's next for borgr
-Get a prettier frontend, I'm a backend guy with little to no graphic design/fancy framework knowledge

-Taking data from automated UiPath emails and doing some data visualization on them to create maps of where people are using borgr
