# National Archives' Hackatown Project - Viva Documentos
![Screenshot 2024-04-08 151719](https://github.com/miguelthemigs/files-project/assets/93150152/1fc45169-fcff-4b84-af0d-4bc7b615ef11)

## Overview
This project presents an interactive web application, developed in Django, designed for the National Archives' Hackatown (made in less than 2 days), aiming to engage the community in the collaborative description of public records. Users can contribute by describing titles, dates, detailed descriptions, and tags for randomly presented documents. The more descriptions they provide, the more points the user earns and can collect badges. It was designed and programmed to be responsive and compatible with all devices it runs on, whether tablets, computers, or cell phones.
![image](https://github.com/miguelthemigs/files-project/assets/93150152/6c3277cd-cc77-4b02-bcf2-c60f901da3a2)

## Features
- **Collaborative Description**: Users can insert descriptions for titles, dates, detailed descriptions, and tags. Each contribution is voted on by the community, and descriptions with the highest number of votes would go for analysis, to be formalized.
  ### Titles, descriptions, or dates (example with title):
  ![image](https://github.com/miguelthemigs/files-project/assets/93150152/a6069d88-b59f-4896-86b3-721c06072030)
  ### Tags
  - We can agree with tags written by other users:
  ![image](https://github.com/miguelthemigs/files-project/assets/93150152/e4d30768-c6a4-4251-8afe-7ca0682c3457)
  - Or we write our own tags:
  ![image](https://github.com/miguelthemigs/files-project/assets/93150152/507e4ecb-5554-4145-96e9-680c20948953)
  - The controlled vocabulary (standard words provided by the Archive) has not been implemented, but it is simple to do and of great value to the National Archives, as it follows the standard of tags, just put specific tags.
    
- **Random Selection of Documents**: After completing a description, a new document is randomly presented to the user, maintaining engagement and variety.
- **Scoring System**: Contributors receive points for each element they describe. Additional points are awarded when a suggested word is highly voted.
  
- **Recognition Badges**: To encourage continuous participation, users earn badges upon reaching different score levels, which are displayed on the profile page.
  ![image](https://github.com/miguelthemigs/files-project/assets/93150152/cebc6c6c-fbd9-4bfe-b3d5-4de9247796bb)

- **Analytical Dashboard**: A dashboard for administrators and advanced users that shows the most voted words in their respective documents, to facilitate analysis by the National Archive.
 ![image](https://github.com/miguelthemigs/files-project/assets/93150152/0b9e3223-2375-4a12-b18d-aaea23b1089c)
