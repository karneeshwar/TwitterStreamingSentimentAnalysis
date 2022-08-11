Step 1: Install Docker desktop application

Step 2: Unzip Q1.zip

Step 3: Open support.py and enter the bear token in the space provided for variable bearer_token

Step 4: Set Q1 as current directory

Step 5: Run the following command
	
	docker compose up -d

Step 6: Wait for at least 5 to 10 mins so that docker sets up everything
	Then go to the elastic host by entering the following link in browser

	http://localhost:5601/

Step 7: Navigate,

	Menu -> Stack Management -> Index Management

	The set index "sentiment" should appear in the indices list 
	If it appears, the setup is complete and the data can be visualized

Step 8: Goto Discover under Analytics, create a data view with the index "sentiment" and set @timestamp as sorting

Step 9: Goto Dashboard under Analytics, create visualization and view the data in variety of visualization tools

Note: The docker compose file has been created to incorporate all the necessary technologies required for this assignment. Base image from PySpark and added Kafka, Elasticsearch, Kibana and Logstash.