# Django

This is a Github repositpry for task related to Creating a Django model named SmallClient. 

A table is created with the following fields:
- name: String, required
- website: String
- point_of_contact: String(email), required
- profile_picture: Image, required
- goal: Choice(CPA, Impressions, Downloads, Installs, Purchase), required
- due_date: DateTime, required
- date_joined: DateTime, auto 

Separate view for adding/register a new client and viewing the list of small clients is made. 
Github authentication is also added as a backend authentication 
