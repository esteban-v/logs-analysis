# Logs Analysis
This is a reporting tool for a news database built with skills learned on Part 3 of the Full Stack Web Developer program.

## Dependencies
* Python 3, [download here](https://www.python.org/downloads/)
* VirtualBox 5.1, [download here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* Vagrant, [download here](https://www.vagrantup.com/downloads.html)
* Virtual Machine configuration files, fork and clone https://github.com/udacity/fullstack-nanodegree-vm
 
## Getting Started
After downloading and installing all dependencies, from your terminal navigate to the `vagrant` folder inside the cloned (https://github.com/udacity/fullstack-nanodegree-vm) file structure.  Run the command `vagrant up`, after this command has finished executing, run `vagrant ssh` to log in to the Virtual Machine. Download the data necessary for this reporting tool [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip and place the file `newsdata.sql` into the `vagrant` directory, which is shared with your virtual machine. Back to your terminal cd into the `vagrant` directory where you just placed `newsdata.sql`, using the command `cd /vagrant` and then run `psql -d news -f newsdata.sql`. Place `logs_analysis.py` inside the same `vagrant` directory.

## Common Usage
After following all previous steps, it's required to create a view inside the news database to run this reporting tool. Access the news database by running `psql news`, then run the following command to create a view named most_viewed: `create view most_viewed as select articles.title, count(*) as visits from articles join log on '/article/'||articles.slug = log.path group by articles.title order by visits desc;`.  Exit the news database by running `\q`.  Finally, inside the `vagrant` directory where `logs_analysis.py` was placed, run `python logs_analysis.py`.

License
----

MIT
