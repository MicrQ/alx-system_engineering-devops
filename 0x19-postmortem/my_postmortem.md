<img src="https://github.com/MicrQ/alx-system_engineering-devops/blob/master/0x19-postmortem/images/2.jpeg">

#### Summary:
- Our server outage lasted for approximately 2 hours, from 8:00 PM to 10:00 PM EAT (East Africa Time). During this period, users experienced slow response times or were unable to access our web application. The root cause was identified as a memory leak in one of our server processes, resulting in high CPU usage and eventual server failure.

#### Timeline (in EAT):
- <b>8:00 PM</b> - Monitoring systems detected abnormal CPU usage spikes, triggering an alert to the on-call engineer.<br>
- <b>8:15 PM</b> - The engineer commenced investigations, uncovering excessive memory consumption by one of the server processes.<br>
- <b>8:30 PM</b> - Recognizing the severity, the issue was promptly escalated to the senior engineering team.<br>
- <b>8:45 PM</b> - Collaborative efforts identified a recently deployed code change as the source of a memory leak.<br>
- <b>9:00 PM</b> - We initiated a rollback of the problematic code change and restarted the server to mitigate the issue.<br>
- <b>9:30 PM</b> - Monitoring confirmed that the server's memory usage had stabilized, and the web application's performance improved.<br>
- <b>10:00 PM</b> - We concluded that the server was fully functional, and the issue had been successfully resolved.<br>

#### Root Cause and Resolution:
- The memory leak, caused by a bug in the deployed code change, led to gradual memory consumption, affecting CPU performance and ultimately causing the server to fail.<br>

- To rectify this, we implemented a rollback of the code change, freeing up memory resources. Additionally, we applied a temporary solution by optimizing the server's memory allocation to prevent similar issues from causing future outages.

#### Corrective and Preventative Measures:
To prevent recurrence, we propose the following improvements:<br>

- Enhancing server monitoring and alerting systems to promptly detect and notify of abnormal memory usage.<br>
- Instituting a rigorous code review process to identify potential memory leaks or similar issues before deployment.<br>
- Implementing robust error handling and logging practices, particularly for memory-related issues.<br>
- Conducting a comprehensive post-incident review to extract lessons learned and identify further areas for improvement.<br>

#### Relevant tasks to address the issue:

- Update server software and optimize memory allocation to enhance stability.
- Set up monitoring for server memory usage with automated alerts to promptly detect anomalies.<br>
- Modify the code review process to include memory leak checks as a standard procedure.<br>
- Enhance error handling and logging, prioritizing memory-related issues, to facilitate quicker issue identification and resolution.<br>
- Schedule a post-incident review within a week to ensure effective learning and implementation of improvements.
