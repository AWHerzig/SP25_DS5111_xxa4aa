**Crontab commands I used:**

`31 9 * * 1-5 cd /home/ubuntu/SP25_DS5111_xxa4aa && . env/bin/activate && make gainers SRC=yahoo`

`30 12 * * 1-5 cd /home/ubuntu/SP25_DS5111_xxa4aa && . env/bin/activate && make gainers SRC=yahoo`

`1 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_xxa4aa && . env/bin/activate && make gainers SRC=yahoo`

`31 9 * * 1-5 cd /home/ubuntu/SP25_DS5111_xxa4aa && . env/bin/activate && make gainers SRC=wsj`

`30 12 * * 1-5 cd /home/ubuntu/SP25_DS5111_xxa4aa && . env/bin/activate && make gainers SRC=wsj`

`1 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_xxa4aa && . env/bin/activate && make gainers SRC=wsj`

At each time, I navigate to the proper directory, activate the enviornment, and use the makejob. 

**Location of Files:**

I have had some jobs but 15+ output csv's can be found in the `sample_data/` subdirectory.
