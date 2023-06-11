0x19. Postmortem

# 0x19. Postmortem

## Concepts
For this project, students are expected to look at this concept:

* [On-call](https://www.youtube.com/watch?v=rp5cVMNmbro)

A service or website you want to monitor
You can monitor thousands of things:

* Is my website returning HTTP 200?
* Is my website loading in less than 500ms?
* Is my webserver daemon up?
* Is there more than 50% free disk space on my server?
…

## Setup
To be on call you need at least 4 components:

* A service or website you want to monitor
* A monitoring tool
* An oncall management system
* A software engineer

## A monitoring tool

You need to configure one or multiple monitoring tool(s) to your on-call system, they are the ones that will actually detect any anomaly and report it to the on-call platform.

## A on-call management system

A lot of home tools can be used for that, you can for example in Nagios define on-call periods and then hook this up to a 3rd party service that can send a text message for you. This is fine when you are alone on-call but become very complicated when you have a team. That’s what a company started in 2009 is doing in the Cloud: PagerDuty. It’s a service that allows you to define on-call teams, escalation policies and services integration.

On-call teams are usually rated on 2 metrics:

* MTA (Medium Time to Acknowledgement): The time between an alert/incident is created and an on-call person acknowledged it (which means that he or she is working toward a solution)
* MTR (Medium Time to Resolution): The time between an alert/incident being created and this same incident/alert being marked as solved
You obviously want these mean times to be as low as possible. MTA basically tells how good engineers are at answering their phone. MTR basically tells how good engineers are at solving issues.



## Background Context

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

* To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
* And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

## Resources
Read or watch:

* [Incident Report, also referred to as a Postmortem](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem)
* [How to run a Postmortem](https://blog.serverdensity.com/how-to-write-a-postmortem/)

# Tasks

## [0. My first postmortem](./Postmortem_Online.pdf)
Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

Requirements:

* Issue Summary (that is often what executives will read) must contain:
        duration of the outage with start and end times (including timezone)
        what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
        what was the root cause
* Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:

        when was the issue detected
        how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
        actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
        misleading investigation/debugging paths that were taken
        which team/individuals was the incident escalated to
        how the incident was resolved
* Root cause and resolution must contain:

        explain in detail what was causing the issue
        explain in detail how the issue was fixed
* Corrective and preventative measures must contain:

        what are the things that can be improved/fixed (broadly speaking)
        a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
* Be brief and straight to the point, between 400 to 600 words

## [1. Make people want to read your postmortem](./Postmortem_Online.pdf)
We are constantly stormed by a quantity of information, it’s tough to get people to read you.

Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
