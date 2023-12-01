## Tools
https://robertheaton.com/enf/  
The website by Robert Heaton discusses the use of Electrical Network Frequency (ENF) matching as a forensic technique to date audio recordings by analyzing the electrical hum present in the recordings. The article explains that ENF matching relies on the variations in the frequency of the mains hum, which is a faint background noise caused by the electrical grid. The method involves extracting the ENF values from a target recording, comparing them to a reference database of ENF values obtained from the electrical grid, and finding the best match to estimate the recording's timestamp. The article provides technical details on how this process works, including downsampling the recording, filtering out frequencies, and using Short-time Fourier Transforms (STFT) to calculate the ENF values. It also discusses potential challenges, such as the absence of mains hum in some recordings and the need for recordings to be at least 10 minutes long for accurate dating. Overall, the article explores the intriguing concept of using electrical grid frequency as a timestamp for audio recordings.

https://github.com/robert/enf-matching/
GitHub repository called "enf-matching" by Robert Heaton. This repository contains example code for the ENF (Electrical Network Frequency) matching technique discussed in Robert Heaton's blog post titled "How to date a recording using background electrical noise."
The code in this repository can be used to predict when a target recording was taken by comparing its background electrical noise to a reference recording. It requires Python 3, Virtualenv (or a similar virtual environment tool), and Curl (for downloading sample files).

https://github.com/bellingcat/open-questions/issues/16

## Databases
### Powergrid
https://osf.io/m43tg/
The Open Access Power-Grid Frequency Database is a repository created on June 15, 2020, and last updated on February 14, 2023. It provides an open database containing power-grid frequency recordings from various sources, including Transmission System Operators (TSOs), independent measurements, and research projects. The data is processed and ready for research use. It is licensed under CC-By Attribution 4.0 International. The repository offers a collection of frequency time series from synchronous areas worldwide and synchronized data from locations in the Continental European grid, making it a valuable resource for research in energy systems and power-grid frequency analysis.

https://power-grid-frequency.org/
The Power-grid frequency database website serves as the front-end for the Open Access Power-Grid Frequency Database, hosted on the Open Science Framework. It offers access to power-grid frequency recordings from around the world. The database contains data from three dimensions: TSO data (publicly available recordings from Transmission Systems Operators), research projects (open-data research project recordings), and independent gatherings (publicly accessible industrial, private, or personal recordings). The data is free for use, but users should check individual dataset licensing for compliance. While TSO and Independent Gatherings data is processed, research project data is linked without processing. The website encourages contributions to promote transparent and clean science and is registered in the re3data.org registry. It is powered by Jekyll & Minimal Mistakes and was created by Leonardo Rydin Gorjão, Benjamin Schäfer, and Galib Hassan in 2021-2022.
https://github.com/LRydin/Power-Grid-Frequency
### Gridradar  
https://gridradar.net/en/wide-area-monitoring-system
Grid Radar provides insights into the power grid's dynamic nature, highlighting how operational changes in power plants, grid element failures, and large consumer shifts impact the grid frequency. Weather phenomena also influence the feed-in and consumption situation, causing load flows to shift unexpectedly. The website emphasizes the capability to measure these fluctuations through frequency and phase angle differences.

- **Continuous Monitoring:** The website details an expanding monitoring system to precisely track load flows.
- **Powerful Analysis System:** Data from the wide-area monitoring system is evaluated in a distributed system, ensuring information availability even during system failures.
- **Free Accounts:** Offer limited access in terms of time series and resolutions. Restrictions include limits on querying time periods, although complete time series can be obtained with periodic requests.
- **Individual API Accounts:** For users needing more extensive access, individual accounts offer enhanced capabilities. Users are encouraged to contact for more details.
- **Supported Methods:** Both POST and GET requests are used, exclusively over HTTPS connections.
- **Rate Limiting:** Accounts have individual limits on request intervals, request periods, data resolution, and other metrics. Exceeding these limits results in error code 429.
- **API Endpoints:** The website lists various endpoints like `/metrics`, `/alerts`, `/query`, etc., each serving different purposes like listing metric names, managing alerts, and querying time series data.
- **General URL Parameters:** Parameters like 'help', 'format', and 'token' modify the endpoint responses.
- **Endpoint-Specific Parameters:** Certain endpoints have additional parameters, e.g., `/help?html` shows an HTML version of the help documentation.
- **Multiple Formats:** The API supports various response formats, including JSON (default), CSV, HTML, and XML, with examples provided for querying these formats
- **Function Specification:** Users can specify functions for downsampling or transforming time series data, with examples provided for different aggregation and selection functions.

In summary, Grid Radar provides a comprehensive platform for monitoring and analyzing power grid dynamics, offering various tools and data access levels to users for tracking and understanding grid frequency variations and load flows.

### National historic frequency data and grid providers
UK:
https://www.nationalgrideso.com/industry-information/balancing-services/frequency-response-services/historic-frequency-data


### Academic papers:

Forensic manipulation analysis:
https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7807225

