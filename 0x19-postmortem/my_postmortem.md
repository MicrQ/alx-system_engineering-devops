<img src="#">

#### Summary:
- Our server outage lasted for approximately 2 hours, from 8:00 PM to 10:00 PM EAT (East Africa Time). During this period, users experienced slow response times or were unable to access our web application. The root cause was identified as a memory leak in one of our server processes, resulting in high CPU usage and eventual server failure.

#### Timeline (in EAT):
- ** 8:00 PM ** - Monitoring systems detected abnormal CPU usage spikes, triggering an alert to the on-call engineer.<br>
- ** 8:15 PM ** - The engineer commenced investigations, uncovering excessive memory consumption by one of the server processes.<br>
- ** 8:30 PM ** - Recognizing the severity, the issue was promptly escalated to the senior engineering team.<br>
- ** 8:45 PM ** - Collaborative efforts identified a recently deployed code change as the source of a memory leak.<br>
- ** 9:00 PM ** - We initiated a rollback of the problematic code change and restarted the server to mitigate the issue.<br>
- ** 9:30 PM ** - Monitoring confirmed that the server's memory usage had stabilized, and the web application's performance improved.<br>
- ** 10:00 PM ** - We concluded that the server was fully functional, and the issue had been successfully resolved.<br>

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
