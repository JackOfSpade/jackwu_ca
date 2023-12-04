#
The website: www.JackWu.ca

**Reset JackWu.ca**

Prerequisite: make sure files .env, service_account_key.json, config.ini is created at system root.

**Reset:**

Note: && means previous command must be success, ; means previous command doesn't have to be success.

Remove all containers + images:

docker-compose down; cd && rm -r -f jackwu_ca; rm -r -f jackwu_ca_maintenance; docker stop $(docker ps -aq); docker rm $(docker ps -aq) -f; docker rmi $(docker images -q) -f; docker system prune -f; docker volume prune -f; docker network prune -f; sudo service docker restart 

Remove all containers + specific images:

docker-compose down; cd && rm -r -f jackwu_ca; rm -r -f jackwu_ca_maintenance; docker stop $(docker ps -aq); docker rm $(docker ps -aq) -f; docker rmi $(docker images "jackwu_ca_web_service") -f; docker rmi $(docker images "jackwu_ca_nginx") -f; docker system prune -f; docker volume prune -f; docker network prune -f; sudo service docker restart

Target (choose one):

	Master:
 
	&& git clone https://github.com/JackOfSpade/jackwu_ca

	Branch:
 
	&& git clone --single-branch --branch branch_name https://github.com/JackOfSpade/jackwu_ca

	Maintenance: 
 
	&& git clone https://github.com/JackOfSpade/jackwu_ca_maintenance 

Copy env + keys:

&& cp jackwu_ca_keys_and_settings/.env jackwu_ca && cp jackwu_ca_keys_and_settings/service_account_key.json jackwu_ca && cp jackwu_ca_keys_and_settings/config.ini jackwu_ca/weather && cp -r jackwu_ca_keys_and_settings/.aws jackwu_ca && cp jackwu_ca_keys_and_settings/SSL/jackwu.key jackwu_ca &&  cp jackwu_ca_keys_and_settings/SSL/www_jackwu_ca.crt jackwu_ca && cp jackwu_ca_keys_and_settings/SSL/bundle.crt  jackwu_ca && cd jackwu_ca && docker-compose up


**Combined with above (remove specific images):**

docker-compose down; cd && rm -r -f jackwu_ca; rm -r -f jackwu_ca_maintenance; docker stop $(docker ps -aq); docker rm $(docker ps -aq) -f; docker rmi $(docker images "jackwu_ca_web_service") -f; docker rmi $(docker images "jackwu_ca_nginx") -f; docker system prune -f; docker volume prune -f; docker network prune -f; sudo service docker restart && git clone https://github.com/JackOfSpade/jackwu_ca && cp jackwu_ca_keys_and_settings/.env jackwu_ca && cp jackwu_ca_keys_and_settings/service_account_key.json jackwu_ca && cp jackwu_ca_keys_and_settings/config.ini jackwu_ca/weather && cp -r jackwu_ca_keys_and_settings/.aws jackwu_ca && cp jackwu_ca_keys_and_settings/SSL/jackwu.key jackwu_ca &&  cp jackwu_ca_keys_and_settings/SSL/www_jackwu_ca.crt jackwu_ca && cp jackwu_ca_keys_and_settings/SSL/bundle.crt  jackwu_ca && cd jackwu_ca && docker-compose up




**To update certificate:**

	Just edit the file texts in jackwu_ca_keys_and_settings/SSL and then rerun command above.
 
	DO NOT generate new .csr, use the existing one in the file.
 
	vi file_name to open file in text.
 
	:1,$d to delete all lines.
 
	Shift-z twice to save.
